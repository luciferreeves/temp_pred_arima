import sqlite3 as sql
import pandas as pd


def execute_sql_statement(sql_statement):
    conn = sql.connect("database.db")
    cur = conn.cursor()
    cur.execute(sql_statement)
    rows = cur.fetchall()
    return rows


def run_sql_pandas(sql_statement):
    conn = sql.connect("database.db")
    df = pd.read_sql_query(sql_statement, conn).to_records(index=False)
    return df
