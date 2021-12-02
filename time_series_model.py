import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.arima_model import ARIMA
import statsmodels.api as sm
import sqlite3 as sql
import pmdarima as pm
from sql_functions import execute_sql_statement

def plot_data(dates):
    sql_stmt = "select date, cast(avg_temperature as real) as temp from temperature"
    result = execute_sql_statement(sql_stmt)
    data = pd.DataFrame(result, columns=["date","temp"])
    data.set_index('date', inplace=True)
    # print(data)
    new_model = pm.auto_arima(data.temp, start_p=1, start_q=1,
                        test='adf',       # use adftest to find optimal 'd'
                        max_p=3, max_q=3, # maximum p and q
                        m=5,              # frequency of series
                        d=None,           # let model determine 'd'
                        seasonal=False,   # No Seasonality
                        start_P=0, 
                        D=0, 
                        trace=True,
                        error_action='ignore',  
                        suppress_warnings=True, 
                        stepwise=True)

    # print(new_model.summary())

    # new_model.plot_diagnostics(figsize=(10,8))
    # # plt.show()

    n_periods =30
    fc, confint = new_model.predict(n_periods = n_periods, return_conf_int = True)
    # print(fc)

    n_years = ['1960-12-02', '1960-12-03', '1960-12-04', '1960-12-05', '1960-12-06', '1960-12-07', '1960-12-08', '1960-12-09', '1960-12-10', '1960-12-11', '1960-12-12', '1960-12-13', '1960-12-14', '1960-12-15', '1960-12-16', '1960-12-17', '1960-12-18', '1960-12-19', '1960-12-20', '1960-12-21', '1960-12-22', '1960-12-23', '1960-12-24', '1960-12-25', '1960-12-26', '1960-12-27', '1960-12-28', '1960-12-29', '1960-12-30', '1960-12-31']
    fc_ind = pd.Series(n_years)

    fc_series = pd.Series(fc, index=fc_ind)
    lower_series = pd.Series(confint[:, 0], index=fc_ind)
    upper_series = pd.Series(confint[:, 1], index=fc_ind)

    plt.figure(figsize=(12, 5))
    # # # plt.plot(np.log10(data.temp))
    # plt.plot(fc_series, color="darkred")
    # # # plt.xlabel("Year")
    # # # plt.ylabel(data. + " Rate")
    # # plt.fill_between(lower_series.index, 
    # #                     lower_series, 
    # #                     upper_series, 
    # #                     color="k", alpha=.35)
    # # # plt.xticks(np.arange(min(data.index), max(upper_series.index)+3, 3.0))
    # # # plt.title("Final Forecast of Crude Death Rate")
    # # # plt.legend(("past", "forecast", "95% confidence interval"), loc="upper right")
    plt.show()



