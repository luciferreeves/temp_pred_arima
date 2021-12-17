from flask import Flask, render_template
from flask import request, jsonify
import pandas as pd
import json
from libs.decompressor import decompress_arima
from predictor import render_plot

decompress_arima()
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
    city_id = request.form["city_id"]
    dates_unmf = pd.date_range(start_date, end_date, freq='d')
    dates = []
    for i in dates_unmf:
        dates.append(i.strftime('%Y-%m-%d'))
    plot_data = render_plot(dates, city_id)
    return jsonify(plot_data)
    

if __name__ == '__main__':
    app.run(debug=True)
