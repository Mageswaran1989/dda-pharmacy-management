import streamlit as st
from db_utils.sqlalchemy_backend import execute, read_sql_query_as_df
from streamlit_option_menu import option_menu
from datetime import datetime
# conn = init_db_connection()
from utils import display_table, handle_table_deletes, multiselect_options, select_options

st.title("Purchase")

view_tab, add_tab, delete_tab = st.tabs(["View", "Add", "Delete"])

view_query = "SELECT p.id, s.name as Supplier, p.cost, p.date, u.name as User FROM PurchaseOrder as p , Supplier as s, UserInfo as u  WHERE p.supplier_id = s.id and u.id = p.user_id"


def get_cost():
    query = "SELECT sum(qty * mrp) as cost FROM UIItems AS item,  ProductDetails AS details WHERE item.prod_id = details.prod_id"
    cost = None
    for row in execute(query, None):
        print("Cost: ", row)
        cost = str(row['cost'])
    return cost


# Set all text input default values
st.session_state['date'] = datetime.today()
st.session_state['cost'] = get_cost()


with add_tab:
    # ------------------------------------------------------------------------------------------------------------------
    st.subheader("Add Items to the List")

    df = read_sql_query_as_df("SELECT * FROM Product")
    names = df['name']
    ids = df['id']
    name, prod_id = st.selectbox(
        'Which Product do you wanted to add?',
        list(zip(names, ids)))

    pqty = st.text_input("Qty", value="", key="pqty")

    add_products_pressed = st.button("Add Products")

    if add_products_pressed:
        print(name, prod_id, pqty)
        result = execute("INSERT INTO UIItems(prod_id, name, qty) values (:prod_id, :name, :pqty) RETURNING id;",
                         [{"prod_id": prod_id, "name": name, "pqty": pqty}])
        st.session_state['cost'] = get_cost()
        st.experimental_rerun()

    # ------------------------------------------------------------------------------------------------------------------

    st.subheader("Delete one from List")

    df = read_sql_query_as_df("SELECT * FROM UIItems")
    options = st.multiselect(
        'Which items do you wanted to delete?',
        list(zip(df['name'], df['id'])),
        None)
    delete_item_button_pressed = st.button("Delete Item", key="deleteitem")

    if delete_item_button_pressed:
        for name, id in options:
            execute("DELETE FROM UIItems WHERE name=:name and id=id;", [{"name": name, "id": id}])
            st.session_state['cost'] = get_cost()
        st.experimental_rerun()

    # ------------------------------------------------------------------------------------------------------------------

    st.subheader("Items to be placed")

    ui_items_df = display_table(query="SELECT u.id, u.prod_id, u.name, u.qty, pd.mrp from UIItems as u JOIN ProductDetails as pd ON u.prod_id = pd.prod_id")

    delete_all = st.button("Delete All", key="delete_all")

    if delete_all:
        execute("DELETE FROM UIItems;")
        st.experimental_rerun()
    # ------------------------------------------------------------------------------------------------------------------

    with st.form("my_form", clear_on_submit=True):
        date = st.date_input("Date", key="date")
        df = read_sql_query_as_df("SELECT * FROM Supplier")
        supplier_name, supplier_id,  = st.selectbox(
            'Supplier',
            list(zip(df['name'], df['id'])))
        cost = st.text_input("Cost", key="cost")
        df = read_sql_query_as_df("SELECT * FROM UserInfo WHERE title = 'SalesPerson'")
        user_name, user_id,  = st.selectbox(
            'User',
            list(zip(df['name'], df['id'])))

        submitted = st.form_submit_button("Add")

        if submitted:
            result = execute("INSERT INTO PurchaseOrder(cost, date, user_id, supplier_id) values (:cost, :date, :user_id, :supplier_id) RETURNING id;",
                             [{"cost": cost, "date": date, "user_id": user_id, "supplier_id": supplier_id}])
            for row in result:
                last_inserted_purchase_id = row['id']
            print("ID: ", last_inserted_purchase_id)

            for prodi_id, qty in zip(ui_items_df['prod_id'], ui_items_df['qty']):
                execute("INSERT INTO PurchaseProductItems(purchase_id, prod_id, qty) VALUES (:purchase_id, :prod_id, :qty)",
                        [{"purchase_id": last_inserted_purchase_id, "prod_id": prod_id, "qty": qty}])

            execute("DELETE FROM UIItems;")
            st.experimental_rerun()

with view_tab:
    st.subheader("Purchase Orders")
    display_table(query=view_query)
    ret = select_options(query=view_query, col1="id", col2="supplier", text="Select Purchase order to view its items")
    if ret is not None:
        purchase_id, supplier_name = ret
        display_table(query=f"SELECT p.name, pd.mrp, pp.qty, pp.purchase_id from PurchaseProductItems as pp, ProductDetails as pd, Product as p WHERE pp.purchase_id ='{purchase_id}' and pp.prod_id = pd.prod_id and pd.prod_id = p.id")


with delete_tab:
    handle_table_deletes(table_name="PurchaseOrder", id_col="id", other_col="date")



