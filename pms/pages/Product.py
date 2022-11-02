import streamlit as st
from db_utils.sqlalchemy_backend import execute, read_sql_query_as_df
from streamlit_option_menu import option_menu
from utils import display_table, handle_table_deletes, multiselect_options, select_options

# conn = init_db_connection()

st.title("Product")


# Insert containers separated into tabs:
view_tab, add_tab, add_details, delete_tab = st.tabs(["View", "Add Product", "Add Product Details", "Delete"])


with add_tab:
    with st.form("my_form", clear_on_submit=True):
        name = st.text_input("Name", value="", key="name")
        brand = st.text_input("brand", value="", key="brand")

        submitted = st.form_submit_button("Add")

        if submitted:
            execute("insert into Product(name, brand) values (:name, :brand)", [{"name": name, "brand": brand}])

        print(submitted, name, brand)

with add_details:
    # prod_id, mrp, discount, expiry_date
    st.header("Admin Levels")
    df = read_sql_query_as_df("SELECT * FROM Product")

    ids = df['id'].to_list()
    names = df['name'].to_list()
    brands = df['brand'].to_list()
    data = list(zip(ids, names, brands))

    # prod_id, mrp, discount, expiry_date
    option = st.selectbox('Update Product Details for:', data)

    mrp = st.text_input("MRP", value="", key="mrp")
    discount = st.text_input("Discount", value="", key="discount")
    expiry_date = st.text_input("Expiry Date", value="", key="expirydate")

    level_button = st.button("Update", key="level_button")

    if level_button:
        prod_id = option[0]
        query = f"INSERT INTO ProductDetails(prod_id, mrp, discount, expiry_date) VALUES (:prod_id, :mrp, :discount, :expiry_date) ON CONFLICT (prod_id) DO UPDATE SET mrp = :mrp, discount = :discount, expiry_date = :expiry_date"
        print(query)
        execute(query, [{"prod_id": prod_id, "mrp": mrp, "discount": discount, "expiry_date": expiry_date}])

with view_tab:
    df = read_sql_query_as_df("SELECT * FROM Product")

    # https://docs.streamlit.io/knowledge-base/using-streamlit/hide-row-indices-displaying-dataframe
    # CSS to inject contained in a string
    hide_table_row_index = """
                <style>
                thead tr th:first-child {display:none}
                tbody th {display:none}
                </style>
                """

    # Inject CSS with Markdown
    st.markdown(hide_table_row_index, unsafe_allow_html=True)

    st.dataframe(df)
    display_table(query="SELECT p.id, p.name, p.brand, pd.mrp, pd.discount, pd.expiry_date FROM Product p, ProductDetails pd WHERE p.id = pd.prod_id")

    st.header("Enquiry")
    qname = st.text_input("Name", value="", key="qname")
    query_button = st.button("Get Details", key="query_button")

    if query_button:
        qname = qname.lower()
        display_table(
            query=f"SELECT p.id, p.name, p.brand, pd.mrp, pd.discount, pd.expiry_date FROM Product p, ProductDetails pd WHERE p.id = pd.prod_id AND position('{qname}' in lower(p.name)) > 0")


with delete_tab:
    df = read_sql_query_as_df("SELECT * FROM Product")
    names = df['name']
    options = st.multiselect(
        'Which Product do you wanted to delete?',
        names,
        None)
    delete_button = st.button("Delete")

    print(options)
    if delete_button:
        for name in options:
            execute("delete from Product where name=:name;", [{"name": name}])
            st.experimental_rerun()



