from flask import Flask, render_template
from flask import request
import pandas as pd
import json

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    with open("cities.json", "r") as cities_list:
        data = json.load(cities_list)
        return render_template("index.html", cities_list=data)


@app.route("/receiveDates", methods=["POST"])
def receive_dates():
    start_date = request.form["start_date"]
    end_date = request.form["end_date"]
    dates_unmf = pd.date_range(start_date, end_date, freq='d')
    dates = []
    for i in dates_unmf:
        dates.append(i.strftime('%Y-%m-%d'))
    return 'OK'

if __name__ == '__main__':
    app.run(debug=True)
