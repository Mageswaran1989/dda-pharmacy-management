import pandas as pd
from psycopg2 import Error
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import streamlit as st
import psycopg2


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


# Initialize connection.
# Uses st.experimental_singleton to only run once.
@st.experimental_singleton
def init_db_connection():
    return psycopg2.connect(**st.secrets["postgres"])


def get_scoped_session(engine):
    return scoped_session(sessionmaker(bind=engine))


conn = init_db_connection()
engine = get_engine()


def read_sql_query_as_df(query):
    return pd.read_sql_query(query, engine)


def delete(query, data):
    with conn.cursor() as cur:
        cur.execute(query, data)
        conn.commit()

def update(query, data):
    with conn.cursor() as cur:
        cur.execute(query, data)
        conn.commit()

# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
# @st.experimental_memo(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()


# @st.experimental_memo(ttl=600)
def insert_query(query, records):
    with conn.cursor() as cur:
        conn.commit()
        result = cur.executemany(query, records)
        conn.commit()
        print(cur.rowcount, "Record inserted successfully into the table")
    return result

# @st.experimental_memo(ttl=600)
def insert_one(query, record):
    with conn.cursor() as cur:
        conn.commit()
        cur.execute(query, record)
        id = cur.fetchone()[0]
        conn.commit()
        print(cur.rowcount, "Record inserted successfully into the table")
    return id
