from turtle import width
import streamlit as st
from postgresql import init_db_connection, run_query, insert_query, read_sql_query_as_df, delete, insert_one
from streamlit_option_menu import option_menu
from st_aggrid import AgGrid, GridUpdateMode,  JsCode
from st_aggrid import AgGrid, DataReturnMode, GridUpdateMode, GridOptionsBuilder

from datetime import datetime
user_id = 1 # TODO: Fetch from session
def insert_purchase_product(df, supplier):
    purchase_df = df[df['quantity'] > 0]
    supplier_id = supplier
    total_cost = 0
    now = datetime.now()
    date = now.strftime("%m/%d/%y")
    for index, row in purchase_df.iterrows():
        total_cost += row['mrp'] * row['quantity'] * (row['discount']/100)
    id = insert_one("INSERT INTO PurchaseOrder (cost, date, user_id, supplier_id) VALUES (%s, %s, %s, %s) RETURNING id",(total_cost, date, user_id, supplier_id))

    pruchase_product_items = []
    for index, row in purchase_df.iterrows():
        pruchase_product_items.append((id, row['id'], row['quantity']))
        print(pruchase_product_items)
    insert_query("INSERT INTO PurchaseProductItems (purchase_id, prod_id, qty) VALUES (%s, %s, %s)", pruchase_product_items)

conn = init_db_connection()

with st.sidebar:
    # https://icons.getbootstrap.com/
    selected = option_menu(None,
                           options=["Add", "View", "---", 'Cancel Order', 'Edit Order'],
                           icons=['house', 'cart', None, 'gear'],
                           menu_icon="app-indicator",
                           default_index=0)

if selected == "Add":
    st.write("#### Specify quantity for the following products for your purchase")
    df = read_sql_query_as_df("select * from Product")
    df["quantity"] = 0
    gd = GridOptionsBuilder.from_dataframe(df)
    gd.configure_column("quantity", editable=True)
    gridOptions = gd.build()
    grid_response = AgGrid(df, gridOptions = gridOptions )
    supplier_df = read_sql_query_as_df("select * from Supplier")

    supplier = st.selectbox(
        'Select supplier for the order',
        supplier_df['name']
    )

    on_click = st.button('Submit Purchase Order')
    if on_click:
        purchase_df = grid_response['data']
        supplier_id = supplier_df[supplier_df['name'] == supplier]['id']
        insert_purchase_product(purchase_df, int(supplier_id))
        st.success("Order Places Succesfully")

elif selected == "View":
    st.write("### Purchase order logged in user")

    df = read_sql_query_as_df("SELECT * FROM PurchaseProductItems INNER JOIN PurchaseOrder ON  PurchaseProductItems.purchase_id = PurchaseOrder.id WHERE PurchaseOrder.user_id = " + str(user_id))

    # https://docs.streamlit.io/knowledge-base/using-streamlit/hide-row-indices-displaying-dataframe
    # CSS to inject contained in a string
    hide_table_row_index = """
                <style>
                thead tr th:first-child {display:none}
                tbody th {display:none}
                </style>
                """
    # CSS to inject contained in a string
    hide_dataframe_row_index = """
                <style>
                .row_heading.level0 {display:none}
                .blank {display:none}
                </style>
                """
    # Inject CSS with Markdown
    st.markdown(hide_dataframe_row_index, unsafe_allow_html=True)

    st.dataframe(df, 400, 400)

elif selected == "Cancel Order":
    df = read_sql_query_as_df("select * from PurchaseOrder WHERE user_id=" + str(user_id))
    select_order = st.selectbox(
        'Select Order to cancel',
        df['id']
    )
    print(select_order)
    on_click = st.button('Cancel Order')
    if on_click:
        select_order = str(select_order)
        st.success("Order Succesfully Canceled")
        delete("delete from PurchaseOrder where id=%s",(select_order,))

