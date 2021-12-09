import pandas as pd
from sql_functions import execute_sql_statement
import pmdarima as pm
import pickle
import zlib
from os.path import exists
from os import remove

sql_stmt = "select date, city_id, cast(avg_temperature as real) as temp from temperature where date is not null and temp is not null"

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
# Best model:  ARIMA(3,0,3)(0,0,0)[0]

with open('arima.pkl', 'wb') as pkl:
    pickle.dump(ts_model, pkl)

