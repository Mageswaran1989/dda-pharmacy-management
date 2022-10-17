import streamlit as st
from db_utils.sqlalchemy_backend import execute, read_sql_query_as_df
from streamlit_option_menu import option_menu

# conn = init_db_connection()

st.title("InvoiceManagement")


view_tab, add_tab, delete_tab = st.tabs(["View", "Add", "Delete"])


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

with view_tab:
    df = read_sql_query_as_df("SELECT * FROM Customer")

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
    df = read_sql_query_as_df("SELECT * FROM Customer")
    names = df['name']
    options = st.multiselect(
        'Which Customer do you wanted to delete?',
        names,
        None)
    delete_button = st.button("Delete")

    print(options)
    if delete_button:
        for name in options:
            execute("DELETE FROM Customer WHERE name=:name;", [{"name": name}])
            st.experimental_rerun()



