from flask import Flask, render_template
from flask import request
import pandas as pd
from sql_functions import run_sql_pandas, get_list_of_dict
from time_series_model import plot_data

app = Flask(__name__)

def get_cities_list():
    sql_statement = 'SELECT DISTINCT(City_Name) as City_Name, Lat, Long FROM City_table join Loc_Table on City_Table.City_Id = Loc_table.City_Id'
    return run_sql_pandas(sql_statement)

@app.route("/")
@app.route("/index")
def index():
    cities_list = get_cities_list()
    keys = ("city", "latitude", "longitude")
    cities_list = get_list_of_dict(keys, cities_list)
    return render_template("index.html", cities_list=cities_list)


@app.route("/receiveDates", methods=["POST"])
def receive_dates():
    start_date = request.form["start_date"]
    end_date = request.form["end_date"]
    dates_unmf = pd.date_range(start_date, end_date, freq='d')
    dates = []
    for i in dates_unmf:
        dates.append(i.strftime('%Y-%m-%d'))
    plot_data(dates)
    return 'OK'

if __name__ == '__main__':
    app.run(debug=True)
