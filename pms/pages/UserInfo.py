import streamlit as st
from postgresql import init_db_connection, run_query, insert_query, read_sql_query_as_df, delete, update
from streamlit_option_menu import option_menu

conn = init_db_connection()

st.title("UserInfo")

with st.sidebar:
    # https://icons.getbootstrap.com/
    selected = option_menu(None,
                           options=["Add", "View", "Category",  "---", 'Delete'],
                           icons=['house', 'cart', 'bookmark', None, 'gear'],
                           menu_icon="app-indicator",
                           default_index=0)


def clear_text():
    st.session_state["name"] = ""
    st.session_state["title"] = ""
    st.session_state["phone"] = ""
    st.session_state["salary"] = ""
    st.session_state["joining_data"] = ""
    st.session_state["level"] = ""


if selected == "Add":
    with st.form("my_form", clear_on_submit=True):
        name = st.text_input("Name", value="", key="name")
        phone = st.text_input("Phone", value="", key="phone")
        salary = st.text_input("Salary", value="", key="salary")
        joining_data = st.text_input("Joining Date (MM/DD/YYYY)", value="", key="joining_data")
        title = st.selectbox("Title", ("Admin", "SalesPerson"))
        submitted = st.form_submit_button("Add")

        if submitted:
            insert_query("INSERT INTO UserInfo(name, phone, title, salary, joining_date) VALUES (%s,%s,%s,%s,%s)",
                         [(name, phone, title, salary, joining_data)])

elif selected == "View":
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
    st.markdown(hide_dataframe_row_index, unsafe_allow_html=True)

    st.dataframe(df)

elif selected == "Category":
    st.header("Admin Levels")
    df = read_sql_query_as_df("SELECT * FROM UserInfo WHERE title = 'Admin'")

    names = df['name'].to_list()
    ids = df['id'].to_list()
    data = list(zip(names, ids))

    option = st.selectbox('Update level for user?', data)
    level = st.text_input("Level", value="", key="level")

    level_button = st.button("Update", key="level_button")

    if level_button:
        query = f"INSERT INTO Admin(user_id, level) VALUES (%s, %s) ON CONFLICT (user_id) DO UPDATE SET level = %s"
        print(query)
        update(query, (option[1], level, level))

    # ------------------------------------------------------------------------------------------------------------------
    st.header("Sales Commission")
    df = read_sql_query_as_df("SELECT * FROM UserInfo WHERE title = 'SalesPerson'")

    names = df['name'].to_list()
    ids = df['id'].to_list()
    data = list(zip(names, ids))

    option = st.selectbox('Update level for user?', data)
    commission = st.text_input("Commission", value="", key="commission")

    commission_button = st.button("Update", key="commission_button")

    if commission_button:
        query = f"INSERT INTO Admin(user_id, level) VALUES (%s, %s) ON CONFLICT (user_id) DO UPDATE SET level = %s"
        print(query)
        update(query, (option[1], level, level))
else:  # Delete
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
            delete("DELETE FROM UserInfo WHERE name=%s;", (name,))



