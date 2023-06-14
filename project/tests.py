import os
import pandas as pd
#

def test_extract():
    os.chdir("..")
    
    name_of_the_file="data.sqlite"
    try:
        print("Directory:",os.getcwd())
        file=open(".\{}".format(name_of_the_file))
        print("Test passed, {} file could be found successfully!".format(name_of_the_file))
        
    except IOError:
        print("Test failed, {} file could not be found!".format(name_of_the_file))
        raise IOError("You should be sure that your are in the correct directory")
    
    except FileNotFoundError:
        print("Test failed, {} file could not be found!".format(name_of_the_file))
        raise IOError("You should be sure that your are in the correct directory")

def test_load_sqlfile():
    try:
    
        name_db1="Zaehlstelle_Herose_2020_stuendlich_Wetter"
        name_db2="Unfallatlas_Konstanz_Gesamt_2020"

        df1 = pd.read_sql_table(name_db1, 'sqlite:///data.sqlite')
        df2 = pd.read_sql_table(name_db2, 'sqlite:///data.sqlite')

        print("Test passed, SQL file could be loaded successfully!")

    except:
        print("SQL File could not read")
        raise NameError("You should be sure that your are in the correct directory")

if __name__ == '__main__':
    test_extract()
    test_load_sqlfile()