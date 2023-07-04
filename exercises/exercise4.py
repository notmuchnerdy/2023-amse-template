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

#Transform
selected_columns= ["Geraet", "Hersteller", "Model", "Monat", "Temperatur in °C (DWD)", "Batterietemperatur in °C", "Geraet aktiv"]

df = pd.read_csv("data.csv",delimiter=";",usecols=range(11),decimal=",",header=None)
header=list(df.iloc[0])
df=df[1:]
df.columns=header
df=df.applymap(lambda x: str(x.replace(',','.')))

selected_columns= ["Geraet", "Hersteller", "Model", "Monat", "Temperatur in °C (DWD)", "Batterietemperatur in °C", "Geraet aktiv"]
df=df[selected_columns]

df[["Hersteller","Geraet aktiv","Model"]] = df[["Hersteller","Geraet aktiv","Model"]].astype(str)
df[["Geraet", "Monat"]] = df[["Geraet", "Monat"]].astype(int)
df[["Temperatur in °C (DWD)", "Batterietemperatur in °C"]] = df[["Temperatur in °C (DWD)", "Batterietemperatur in °C"]].astype(float)

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