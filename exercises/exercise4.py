import pandas as pd
import urllib.request
from zipfile import ZipFile
import sqlite3

#Extract
file_name="temperatures"

url = "https://www.mowesta.com/data/measure/mowesta-dataset-20221107.zip"

urllib.request.urlretrieve(url, '{}.zip'.format(file_name))

#Unzipping the file
with ZipFile('{}.zip'.format(file_name), 'r') as f:
    #extract in current directory
    f.extractall()

selected_columns= ["Geraet", "Hersteller", "Model", "Monat", "Temperatur in °C (DWD)", "Batterietemperatur in °C", "Geraet aktiv"]

df = pd.read_csv("data.csv",delimiter=";",usecols=selected_columns,decimal=",",header=0).reset_index()
sel_col=list(df.columns)[:7]
df=df[sel_col]
df.columns=selected_columns

df=df.rename(columns={"Temperatur in °C (DWD)": "Temperatur", "Batterietemperatur in °C": "Batterietemperatur"})

df["Temperatur"]=(df["Temperatur"]*9/5)+32

df["Batterietemperatur"]=(df["Batterietemperatur"]*9/5)+32

#Load to SQL
sql_file_dir="./{}.sqlite".format(file_name)
con=sqlite3.connect(sql_file_dir)
cur=con.cursor()

df.to_sql(name=file_name, con=con, if_exists="replace", index=False)

con.commit()
con.close()