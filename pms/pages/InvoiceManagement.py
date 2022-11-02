import datetime

import streamlit as st
from db_utils.sqlalchemy_backend import execute, read_sql_query_as_df
from streamlit_option_menu import option_menu
from utils import display_table, handle_table_deletes, multiselect_options, select_options

# conn = init_db_connection()

st.title("InvoiceManagement")


view_tab,  = st.tabs(["View", ])

with view_tab:
    from_date = st.date_input("From date", key="date", value=datetime.datetime(2022,10,1))
    to_date = st.date_input("To date", key="date", value=datetime.datetime(2022,12,1))
    display_table(query=f"SELECT * FROM PurchaseOrder WHERE date BETWEEN '{from_date}' and '{to_date}'")
    df = read_sql_query_as_df(f"SELECT SUM(cost) FROM PurchaseOrder WHERE date BETWEEN '{from_date}' and '{to_date}'")
    total_sales = df["sum"][0]
    sales_string = "Total sales for the period is " + str(total_sales)
    st.subheader(sales_string)    
