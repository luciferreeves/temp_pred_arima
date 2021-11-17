from flask import Flask, render_template
from flask import Markup
import sqlite3 as sql
import pandas as pd

app = Flask(__name__)


def execute_sql_statement(sql_statement, conn):
    cur = conn.cursor()
    cur.execute(sql_statement)

    rows = cur.fetchall()

    return rows

def get_list_of_dict(keys, list_of_tuples):
     list_of_dict = [dict(zip(keys, values)) for values in list_of_tuples]
     return list_of_dict

def get_cities_list():
    conn = sql.connect("./database_files/pythonproject.db")
    sql_statement = 'SELECT DISTINCT(City_Name) as City_Name, Lat, Long FROM City_table join Loc_Table on City_Table.City_Id = Loc_table.City_Id'
    df=pd.read_sql_query(sql_statement, conn).to_records(index=False)
    return df

@app.route("/")
@app.route("/index")
def index():

    cities_list = get_cities_list()
    keys = ("city", "latitude", "longitude")
    cities_list = get_list_of_dict(keys, cities_list)
    # start_coords = (42.9974521, -78.7907883)
    # folium_map = folium.Map(location=start_coords, zoom_start=14)
    # _ = folium_map._repr_html_()
    # map_div = Markup(folium_map.get_root().html.render())
    # hdr_txt = Markup(folium_map.get_root().header.render())
    # script_txt = Markup(folium_map.get_root().script.render())
    return render_template("index.html", cities_list=cities_list)


if __name__ == '__main__':
    app.run(debug=True)
