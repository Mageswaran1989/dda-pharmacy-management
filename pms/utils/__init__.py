import streamlit as st

from db_utils.sqlalchemy_backend import read_sql_query_as_df, execute


def display_table(table_name=None, query=None):
    if table_name is not None:
        if "SELECT" in table_name or "select" in table_name:
            raise RuntimeError("Use query argument, will refactor this later")
    if query:
        df = read_sql_query_as_df(query)
    else:
        df = read_sql_query_as_df(f"SELECT * FROM {table_name}")

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

    return df


def handle_table_deletes(table_name=None, id_col='id', other_col='name', msg='Select an item to delete'):
    df = read_sql_query_as_df(f"SELECT * FROM {table_name}")
    items = list(zip(df[other_col], df[id_col]))
    options = st.multiselect(
        msg,
        items if len(items) > 0 else [("", "")],
        None)
    delete_button = st.button("Delete")

    if delete_button:
        for other_value, id in options:
            execute(f"DELETE FROM {table_name} WHERE {other_col}=:other_value and {id_col}=:id;", [{"other_value": other_value, "id": id}])
            st.experimental_rerun()


def multiselect_options(query, col1, col2, text="Options"):
    df = read_sql_query_as_df(query)
    options = st.multiselect(
        text,
        list(zip(df[col1], df[col2])),
        None)
    return options

def select_options(query, col1, col2, text="Options"):
    df = read_sql_query_as_df(query)
    items = list(zip(df[col1], df[col2]))
    if len(items) > 0:
        option = st.selectbox(
            text,
            items)
        return option
    else:
        return None