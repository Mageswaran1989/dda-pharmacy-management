import streamlit as st
from db_utils.sqlalchemy_backend import execute, read_sql_query_as_df
from streamlit_option_menu import option_menu

# conn = init_db_connection()

st.title("InvoiceManagement")


view_tab, add_tab, delete_tab = st.tabs(["View", "Add", "Delete"])




