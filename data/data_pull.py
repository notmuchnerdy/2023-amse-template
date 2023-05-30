# Data Engineering Project

import numpy as np
import pandas as pd
import requests
import sqlite3
import os

### Data Pipeline

#Pulling the Datasets 


name_db1="Zaehlstelle_Herose_2020_stuendlich_Wetter"
name_db2="Unfallatlas_Konstanz_Gesamt_2020"

dir_1=".//data/{}.csv".format(name_db1)
dir_2=".//data/{}.csv".format(name_db2)

url1 = 'https://offenedaten-konstanz.de/sites/default/files/Zaehlstelle_Herose_2020_stuendlich_Wetter_1.csv'
url2="https://offenedaten-konstanz.de/sites/default/files/Unfallatlas_Konstanz_Gesamt_2020.csv"

r1=requests.get(url1, allow_redirects=True)
r2 = requests.get(url2, allow_redirects=True)

open(dir_1, 'wb').write(r1.content)
open(dir_2, 'wb').write(r2.content)

#Extract
df1 = pd.read_csv(dir_1,delimiter=";")
df2=pd.read_csv(dir_2,delimiter=";")

#Connect Local Server
#engine = create_engine('postgresql://postgres:1234@localhost:5432/postgres')

sql_file_dir="./data/data.sqlite"
con=sqlite3.connect(sql_file_dir)

cur=con.cursor()
#Transform Data

df1['Zeit'] = pd.to_datetime(df1['Zeit'])
df1["Monat"]=pd.DatetimeIndex(df1['Zeit']).month
df1["Wochentag"]=pd.DatetimeIndex(df1['Zeit']).dayofweek
df1["Stunde"]=pd.DatetimeIndex(df1['Zeit']).hour


symbol_wetter_list=list(df1["Symbol Wetter"].unique())

for index,sym in enumerate(df1["Symbol Wetter"]):
    df1 = df1.replace({'Symbol Wetter': {sym:symbol_wetter_list.index(sym)}})


df2['Jahr-Monat'] = pd.to_datetime(df2['Jahr-Monat'],format='%Y-%m')

#Load to Local Server
df1.to_sql(name=name_db1, con=con, if_exists="replace", index=False)
df2.to_sql(name=name_db2, con=con, if_exists="replace", index=False)

con.commit()
con.close()

