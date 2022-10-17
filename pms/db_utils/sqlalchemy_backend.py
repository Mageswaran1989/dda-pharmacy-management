import pandas as pd
from psycopg2 import Error
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, Session
import streamlit as st
import psycopg2
from sqlalchemy import text


@st.experimental_singleton
def get_engine():
    print(st.secrets["postgres"])
    host, port, dbname, user, password = st.secrets["postgres"].values()
    url = f"postgresql://{user}:{password}@{host}:{int(port)}/{dbname}"
    print(url)
    try:
        engine = create_engine(url)
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
        engine = None
    return engine


@st.experimental_singleton
def get_scoped_session(engine):
    return scoped_session(sessionmaker(bind=engine))


# https://docs.sqlalchemy.org/en/20/tutorial/dbapi_transactions.html
def execute(query, data=None):
    engine = get_engine()
    result = None
    with engine.connect() as conn:
        result = conn.execute(text(query), data)
    return result



def read_sql_query_as_df(query):
    engine = get_engine()
    df = pd.read_sql_query(query, engine)
    # df = df.reset_index(drop=True, inplace=True)
    return df
