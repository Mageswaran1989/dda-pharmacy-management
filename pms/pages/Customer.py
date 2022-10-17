import streamlit as st
from db_utils.sqlalchemy_backend import execute, read_sql_query_as_df
from streamlit_option_menu import option_menu

# conn = init_db_connection()

st.title("Customer")


# https://icons.getbootstrap.com/
# https://coolsymbol.com/
# Insert containers separated into tabs:
view_tab, add_tab, delete_tab = st.tabs(["View", "Add", "Delete"])

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
    df = read_sql_query_as_df("SELECT * FROM Customer")
    names = df['name']
    ids = df['id']
    options = st.multiselect(
        'Which Customer do you wanted to delete?',
        list(zip(names, ids)),
        None,
        key="options")
    delete_button = st.button("Delete")

    if delete_button:
        for name, id in options:
            execute("DELETE FROM Customer WHERE name=:name and id=:id;", [{"name": name, "id": id}])
            st.experimental_rerun()



