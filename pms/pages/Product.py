import streamlit as st
from db_utils.sqlalchemy_backend import execute, read_sql_query_as_df
from streamlit_option_menu import option_menu

# conn = init_db_connection()

st.title("Product")


# Insert containers separated into tabs:
view_tab, add_tab, delete_tab = st.tabs(["View", "Add", "Delete"])


with add_tab:
    with st.form("my_form", clear_on_submit=True):
        name = st.text_input("Name", value="", key="name")
        brand = st.text_input("brand", value="", key="brand")

        submitted = st.form_submit_button("Add")

        if submitted:
            execute("insert into Product(name, brand) values (:name, :brand)", [{"name": name, "brand": brand}])

        print(submitted, name, brand)

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



