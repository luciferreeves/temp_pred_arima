import pandas as pd
import matplotlib.pyplot as plt
import pickle
from libs.decompressor import decompress_arima

decompress_arima()

with open('arima.pkl', 'rb') as pkl:
    n_periods = 30
    fc, confint = pickle.load(pkl).predict(
        n_periods=n_periods, return_conf_int=True)
    n_years = ['1960-12-02', '1960-12-03', '1960-12-04', '1960-12-05', '1960-12-06', '1960-12-07', '1960-12-08', '1960-12-09', '1960-12-10', '1960-12-11', '1960-12-12', '1960-12-13', '1960-12-14', '1960-12-15', '1960-12-16',
               '1960-12-17', '1960-12-18', '1960-12-19', '1960-12-20', '1960-12-21', '1960-12-22', '1960-12-23', '1960-12-24', '1960-12-25', '1960-12-26', '1960-12-27', '1960-12-28', '1960-12-29', '1960-12-30', '1960-12-31']
    city_ids = ["1031", "1031", "1031", "1031", "1031", "1031", "1031", "1031", "1031", "1031", "1031", "1031", "1031", "1031", "1031", "1031", "1031", "1031", "1031", "1031", "1031", "1031", "1031", "1031", "1031", "1031", "1031", "1031", "1031", "1031"]
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
    plt.show()
