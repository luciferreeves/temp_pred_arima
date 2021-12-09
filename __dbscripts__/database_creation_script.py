# Running this script automatically creates the database and normalizes the data.
# This is same as running the 'dbcreation.ipynb' notebook step by step.
# However their are some visualizations in the notebook but this script does not.
# This script is intentended to automate the whole process in a single script.
# This should run faster than the notebook.

import pandas as pd
import sqlite3
from sqlite3 import Error
import os

def create_connection(db_file, delete_db=False):
    
    if delete_db and os.path.exists(db_file):
        os.remove(db_file)

    conn = None
    try:
        conn = sqlite3.connect(db_file)
        conn.execute("PRAGMA foreign_keys = 1")
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def execute_sql_statement(sql_statement, conn):
    cur = conn.cursor()
    cur.execute(sql_statement)

    rows = cur.fetchall()

    return rows

df=pd.read_csv("..GlobalLandTemperaturesByCity.csv")
data=df[df.dt>"1949-12-31"]
data_for_loc_table=data[['City','Latitude','Longitude']]
data_for_loc_table=data_for_loc_table.to_records(index=False)
result_data_for_loc_table=list(data_for_loc_table)
records=data.to_records(index=False)
result=list(records)
req_resut=[]
for i in result:
    req_resut.append((i[4],))
req_resut=list((set(req_resut)))
conn = create_connection('database.db')
cur=conn.cursor()
execute_sql_statement("DROP TABLE IF EXISTS City_Table",conn)
execute_sql_statement("DROP TABLE IF EXISTS Country_Table",conn)
create_table(conn,'''CREATE TABLE Country_Table (PK INTEGER  PRIMARY KEY, Country_Name VARCHAR)''')
cur.executemany("INSERT INTO Country_Table ('Country_Name') Values (?)",req_resut)
abc=execute_sql_statement("Select * from Country_Table", conn)
abc1={}
for i in abc:
    abc1[i[1]]=i[0]
req_result_2=[]
for i in result:
    req_result_2.append((i[3],abc1[i[4]]))
create_table(conn,'''CREATE TABLE City_Table (City_Id INTEGER  PRIMARY KEY, City_Name VARCHAR , Country_ID INTEGER,
FOREIGN KEY(Country_ID) REFERENCES Country_Table(PK))''')
city=[]
for i in result:
    city.append((i[3],abc1[i[4]]))
city_country_unique=list((set(city)))
cur.executemany("INSERT INTO City_Table ('City_Name','Country_ID') Values (?,?)",city_country_unique)
city_index=execute_sql_statement("Select * from City_Table", conn)
city_indexes={}
for i in abc:
    abc1[i[1]]=i[0]
city_table_values=execute_sql_statement("select * from City_Table ",conn)
city_ids={}
for i in city_table_values:
    city_ids[i[1]]=i[0]
create_table(conn,'''CREATE TABLE Temperature (PK INTEGER  PRIMARY KEY , Date VARCHAR, Avg_Temperature VARCHAR, City_ID INTEGER,
FOREIGN KEY(City_ID) REFERENCES City_Table(City_Id))''')
temp_table_values=[]
j=1
for i in result:
    j=j+1
    temp_table_values.append((i[0],i[1],city_ids[i[3]]))
cur.executemany("INSERT INTO Temperature ('Date','Avg_Temperature','City_ID') Values (?,?,?)",temp_table_values)
create_table(conn,'''CREATE TABLE Loc_Table (ID INTEGER  PRIMARY KEY , City_ID INTEGER, LAT FLOAT,LONG FLOAT,
FOREIGN KEY(City_ID) REFERENCES City_Table(City_ID))''')
data_to_check_loc=result_data_for_loc_table
data_to_input_loc_table=[]
j=0
for i in data_to_check_loc:
    t=[0,0,0]
    if i[1][-1]=='N':
         t[1]=(float(i[1][:-1]))
    if i[1][-1]=='S':
         t[1]=float(i[1][:-1])*(-1)
    if i[2][-1]=='E':
         t[2]=float(i[2][:-1])  
    if i[2][-1]=='W':
         t[2]=float(i[2][:-1])*(-1)
    t[0]=i[0]
    tuple1=(city_ids[t[0]],t[1],t[2])
    data_to_input_loc_table.append(tuple1)
cur.executemany("INSERT INTO Loc_Table ('City_ID','LAT','LONG') Values (?,?,?)",data_to_input_loc_table)
conn.commit()
