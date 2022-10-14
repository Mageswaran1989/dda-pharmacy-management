import streamlit as st
from postgresql import init_db_connection, run_query, insert_query, read_sql_query_as_df, delete
from streamlit_option_menu import option_menu

conn = init_db_connection()

st.title("PRoduct")

with st.sidebar:
    # https://icons.getbootstrap.com/
    selected = option_menu(None,
                           options=["Add", "View", "---", 'Delete'],
                           icons=['house', 'cart', None, 'gear'],
                           menu_icon="app-indicator",
                           default_index=0)



if selected == "Add":
    with st.form("my_form", clear_on_submit=True):
        name = st.text_input("Name", value="", key="name")
        brand = st.text_input("brand", value="", key="brand")

        submitted = st.form_submit_button("Add")

        if submitted:
            insert_query("insert into Product(name, brand) values (%s,%s)", [(name, brand)])

        print(submitted, name, brand)
elif selected == "View":
    df = read_sql_query_as_df("select * from Product")

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

    st.dataframe(df)
else:  # Delete
    df = read_sql_query_as_df("select * from Product")
    names = df['name']
    options = st.multiselect(
        'Which Product do you wanted to delete?',
        names,
        None)
    delete_button = st.button("Delete")

    print(options)
    if delete_button:
        for name in options:
            delete("delete from Product where name=%s;", (name,))



