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

df_header=list(pd.read_csv("data.csv",delimiter=";",nrows=0).columns)

df = pd.read_csv("data.csv",delimiter=";",on_bad_lines="skip",skiprows=1,decimal=",")

#Transform
total_column=len(df.columns)
diff=total_column-len(df_header)

for i in range(diff):
    df_header.append("Nan_{}".format(i))

df.columns=df_header

selected_columns= ["Geraet", "Hersteller", "Model", "Monat", "Temperatur in °C (DWD)", "Batterietemperatur in °C", "Geraet aktiv"]
df=df[selected_columns]

df=df.rename(columns={"Temperatur in °C (DWD)": "Temperatur", "Batterietemperatur in °C": "Batterietemperatur"})

temp_in_celcius=(df["Temperatur"]*9/5)+32

df.insert(5, 'TemperatureInCelsius', temp_in_celcius)


#Load to SQL
sql_file_dir="./{}.sqlite".format(file_name)
con=sqlite3.connect(sql_file_dir)
cur=con.cursor()

df.to_sql(name=file_name, con=con, if_exists="replace", index=False)

con.commit()
con.close()