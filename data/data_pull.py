# Data Engineering Project

import numpy as np
import pandas as pd
import sqlite3
import os

### Data Pipeline

name_db1="Zaehlstelle_Herose_2020_stuendlich_Wetter"
name_db2="Unfallatlas_Konstanz_Gesamt_2020"

url1 = 'https://offenedaten-konstanz.de/sites/default/files/Zaehlstelle_Herose_2020_stuendlich_Wetter_1.csv'
url2="https://offenedaten-konstanz.de/sites/default/files/Unfallatlas_Konstanz_Gesamt_2020.csv"

sql_file_dir="./data.sqlite"

def extract(url1,url2):

    df1=pd.read_csv(url1,delimiter=";")
    df2=pd.read_csv(url2,delimiter=";")

    return df1,df2

def transform(df1,df2):
    
    df1['Zeit'] = pd.to_datetime(df1['Zeit'])
    df1["Monat"]=pd.DatetimeIndex(df1['Zeit']).month
    df1["Wochentag"]=pd.DatetimeIndex(df1['Zeit']).dayofweek

    df1["Wochentag"]=df1["Wochentag"]+2
    df1["Wochentag"]=df1["Wochentag"].replace(8,1)

    df1["Stunde"]=pd.DatetimeIndex(df1['Zeit']).hour

    #df1["Temperatur-Interval"]
    symbol_wetter_list=list(df1["Symbol Wetter"].unique())
    df1["Key"] = df1["Monat"].astype(str) +"-"+df1["Wochentag"].astype(str)+"-"+df1["Stunde"].astype(str)

    df2['Jahr-Monat'] = pd.to_datetime(df2['Jahr-Monat'],format='%Y-%m')
    df2["Key"]=df2["UMONAT"].astype(str) +"-"+ df2["UWOCHENTAG"].astype(str)+"-"+df2["USTUNDE"].astype(str)

    return df1,df2

def load(df1,df2,sql_file_dir,name_db1,name_db2):
    con=sqlite3.connect(sql_file_dir)
    cur=con.cursor()
    df1.to_sql(name=name_db1, con=con, if_exists="replace", index=False)
    df2.to_sql(name=name_db2, con=con, if_exists="replace", index=False)

    con.commit()
    con.close()

if __name__ == '__main__':
    df1,df2=extract(url1,url2)
    df1,df2=transform(df1,df2)
    load(df1,df2,sql_file_dir,name_db1,name_db2)

