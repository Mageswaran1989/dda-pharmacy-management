import streamlit as st
from db_utils.sqlalchemy_backend import execute, read_sql_query_as_df
from streamlit_option_menu import option_menu

# conn = init_db_connection()

st.title("Supplier")

view_tab, add_tab, delete_tab = st.tabs(["View", "Add", "Delete"])


with add_tab:
    with st.form("my_form", clear_on_submit=True):
        name = st.text_input("Name", value="", key="name")
        address = st.text_input("Address", value="", key="address")
        phone = st.text_input("Phone", value="", key="phone")

        submitted = st.form_submit_button("Add")

        if submitted:
            execute("insert into Supplier(name, address, phone) values (:name, :address, :phone)",
                    [{"name": name, "address": address, "phone": phone}])

        print(submitted, name, address, phone)

with view_tab:
    df = read_sql_query_as_df("SELECT * FROM supplier")

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

with delete_tab:
    df = read_sql_query_as_df("SELECT * FROM supplier")
    names = df['name']
    options = st.multiselect(
        'Which company do you wanted to delete?',
        names,
        None)
    delete_button = st.button("Delete")

    print(options)
    if delete_button:
        for name in options:
            execute("delete from supplier where name=:name;", [{"name": name}])
            st.experimental_rerun()



