import numpy as np
import pandas as pd
import requests
import sqlite3
import os

#Excercise 2

name_db="trainstops"

#os.chdir("..")

dir="./data/{}.csv".format(name_db)

url = "https://download-data.deutschebahn.com/static/datasets/haltestellen/D_Bahnhof_2020_alle.CSV"

r=requests.get(url, allow_redirects=True)

open(dir, 'wb').write(r.content)

df = pd.read_csv(dir,delimiter=";")
valid_verkehr_values=["FV","RV","nur DPN"]
df=df[df["Verkehr"].isin(valid_verkehr_values)].drop(["Status"],axis=1)
df=df.dropna()

sql_file_dir="./exercises/{}.sqlite".format(name_db)
con=sqlite3.connect(sql_file_dir)
cur=con.cursor()

df['Laenge'] = [x.replace(',', '.') for x in df['Laenge']]
df['Breite'] = [x.replace(',', '.') for x in df['Breite']]

df=df.astype({'EVA_NR': 'int32',
           "DS100":"str",
           "IFOPT":"str",
           "NAME":"str",
           "Verkehr":"str",
           "Laenge":"float32",
           "Breite":"float32",
           "Betreiber_Name":"str",
           "Betreiber_Nr":"int32"})

df=df[df["Laenge"].between(-90,90) & df["Breite"].between(-90,90)]

df.to_sql(name=name_db, con=con, if_exists="replace", index=False)

con.commit()
con.close()