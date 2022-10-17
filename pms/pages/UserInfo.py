import streamlit as st
from db_utils.sqlalchemy_backend import execute, read_sql_query_as_df
from streamlit_option_menu import option_menu

# conn = init_db_connection()

st.title("UserInfo")

view_tab, add_tab, category_tab, delete_tab = st.tabs(["View", "Add",  "Category", "Delete"])


with add_tab:
    with st.form("my_form", clear_on_submit=True):
        name = st.text_input("Name", value="", key="name")
        phone = st.text_input("Phone", value="", key="phone")
        salary = st.text_input("Salary", value="", key="salary")
        joining_date = st.text_input("Joining Date (MM/DD/YYYY)", value="", key="joining_date")
        title = st.selectbox("Title", ("Admin", "SalesPerson"))
        submitted = st.form_submit_button("Add")

        if submitted:
            print({"name": name, "phone": phone, "title": title, "salary": salary, "joining_date": joining_date})
            execute("INSERT INTO UserInfo(name, phone, title, salary, joining_date) VALUES (:name, :phone, :title, :salary, :joining_date)",
                         [{"name": name, "phone": phone, "title": title, "salary": salary, "joining_date": joining_date}])

with view_tab:
    df = read_sql_query_as_df("SELECT * FROM UserInfo")

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
    st.markdown(hide_table_row_index, unsafe_allow_html=True)

    st.dataframe(df)

    # ------------------------------------------------------------------------------------------------------------------

    df = read_sql_query_as_df("SELECT * FROM Admin")

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
    st.markdown(hide_table_row_index, unsafe_allow_html=True)

    st.dataframe(df)

    # ------------------------------------------------------------------------------------------------------------------

    df = read_sql_query_as_df("SELECT * FROM SalesPerson")

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

with category_tab:
    st.header("Admin Levels")
    df = read_sql_query_as_df("SELECT * FROM UserInfo WHERE title = 'Admin'")

    names = df['name'].to_list()
    ids = df['id'].to_list()
    data = list(zip(names, ids))

    option = st.selectbox('Update level for user?', data)
    level = st.text_input("Level", value="", key="level")

    level_button = st.button("Update", key="level_button")

    if level_button:
        query = f"INSERT INTO Admin(user_id, level) VALUES (:user_id, :level) ON CONFLICT (user_id) DO UPDATE SET level = :level"
        print(query)
        execute(query, [{"user_id": option[1], "level": level}])

    # ------------------------------------------------------------------------------------------------------------------
    st.header("Sales Commission")
    df = read_sql_query_as_df("SELECT * FROM UserInfo WHERE title = 'SalesPerson'")

    names = df['name'].to_list()
    ids = df['id'].to_list()
    data = list(zip(names, ids))

    option = st.selectbox('Select Sales Person with right ID to update their commission', data)
    commission = st.text_input("Commission", value="", key="commission")

    commission_button = st.button("Update", key="commission_button")

    if commission_button:
        query = f"INSERT INTO Admin(user_id, level) VALUES (:user_id, :level) ON CONFLICT (user_id) DO UPDATE SET level = :level"
        print(query)
        execute(query, [{"user_id": option[1], "level": level}])

with delete_tab:
    df = read_sql_query_as_df("SELECT * FROM UserInfo")
    names = df['name']
    options = st.multiselect(
        'Which company do you wanted to delete?',
        names,
        None)
    delete_button = st.button("Delete")

    print(options)
    if delete_button:
        for name in options:
            execute("DELETE FROM UserInfo WHERE name=:name;", [{"name": name}])
            st.experimental_rerun()



