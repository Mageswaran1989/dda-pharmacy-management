import streamlit as st
from db_utils.sqlalchemy_backend import execute, read_sql_query_as_df
from streamlit_option_menu import option_menu
from utils import display_table, handle_table_deletes, multiselect_options, select_options

# conn = init_db_connection()

st.title("Customer")


# https://icons.getbootstrap.com/
# https://coolsymbol.com/
# Insert containers separated into tabs:
view_tab, add_tab, delete_tab = st.tabs(["View", "Add", "Delete"])

with view_tab:
    display_table(table_name="Customer")

with add_tab:
    with st.form("my_form", clear_on_submit=True):
        name = st.text_input("Name", value="", key="name")
        phone = st.text_input("Phone", value="", key="phone")

        submitted = st.form_submit_button("Add")

        if submitted:
            result = execute("INSERT INTO Customer(name, phone) values (:name, :phone) RETURNING id;", [{"name": name, "phone": phone}])
            for row in result:
                id = row['id']
            print("ID: ", id)

with delete_tab:
    handle_table_deletes(table_name="Customer", id_col="id", other_col="name")



