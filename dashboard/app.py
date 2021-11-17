from flask import Flask, render_template
from flask import Markup
import folium
import sqlite3 as sql
from sqlite3 import Error
import pandas as pd
import os

app = Flask(__name__)


def execute_sql_statement(sql_statement, conn):
    cur = conn.cursor()
    cur.execute(sql_statement)

    rows = cur.fetchall()

    return rows

def get_cities_list():
    conn = sql.connect("./database_files/pythonproject.db")
    sql_statement = 'SELECT Country_Name FROM country_table'
    df=pd.read_sql_query(sql_statement, conn)
    return df[['Country_Name']]

@app.route("/")
@app.route("/index")
def index():

    cities_list = get_cities_list()
    print(cities_list)

    start_coords = (42.9974521, -78.7907883)
    folium_map = folium.Map(location=start_coords, zoom_start=14)
    _ = folium_map._repr_html_()
    map_div = Markup(folium_map.get_root().html.render())
    hdr_txt = Markup(folium_map.get_root().header.render())
    script_txt = Markup(folium_map.get_root().script.render())
    return render_template("index.html", map_div=map_div, hdr_txt=hdr_txt, script_txt=script_txt)


if __name__ == '__main__':
    app.run(debug=True)
