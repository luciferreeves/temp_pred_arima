import pandas as pd
import matplotlib
import numpy as np
from functions.sql_functions import execute_sql_statement
import pmdarima as pm
import io
import base64
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def render_plot(dates, city_id):
    sql_stmt = "select date, city_id, cast(avg_temperature as real) as temp from temperature where date is not null and temp is not null and city_id = " + str(city_id)
    result = execute_sql_statement(sql_stmt)
    data = pd.DataFrame(result, columns=["date", "city_id", "temp"])
    data.set_index(["date", "city_id"], inplace=True)
    ts_model = pm.auto_arima(data.temp, start_p=1, start_q=1,
                         test='adf',
                         max_p=3, max_q=3,
                         m=5,
                         d=None,
                         seasonal=False,
                         start_P=0,
                         D=0,
                         trace=True,
                         error_action='ignore',
                         suppress_warnings=True,
                         stepwise=True)
    
    n_periods = len(dates)
    n_years = dates
    city_ids = np.repeat(city_id, n_periods)
    fc, confint = ts_model.predict(
        n_periods=n_periods, return_conf_int=True)

    fc_ind = pd.Series(n_years, city_ids)

    fc_series = pd.Series(fc, index=fc_ind)
    lower_series = pd.Series(confint[:, 0], index=fc_ind)
    upper_series = pd.Series(confint[:, 1], index=fc_ind)
    plt.figure(figsize=(12, 5))
    plt.plot(fc_series, color="darkred")
    plt.fill_between(lower_series.index,
                     lower_series,
                     upper_series,
                     color="k", alpha=.35)
    plt.title("Temperature Forecast")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    ax = plt.gca()
    line = ax.lines[0]
    x_data = line.get_xdata().tolist()
    y_data = line.get_ydata().tolist()
    upper_bound = upper_series.tolist()
    lower_bound = lower_series.tolist()

    # Convert x_data, y_data, upper_bound, lower_bound to dict
    data = {
        "x_data": x_data,
        "y_data": y_data,
        "upper_bound": upper_bound,
        "lower_bound": lower_bound
    }

    return data

