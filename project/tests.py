import os

print(os.path.abspath(os.curdir))
os.chdir("..")
with open(".\data\data_pull.py") as f:
    exec(f.read())
    f.close()

print("Here")

sqlite_files = [f for f in os.listdir('.') if f.endswith('.sqlite')]
if len(sqlite_files)>=1:
    name_of_the_file=sqlite_files[0]

try:
    file=open(".\data\{}".format(name_of_the_file))
    print("Test passed, {} file could be found successfully!".format(name_of_the_file))
    

except IOError:
    print("Test failed, {} file could not be found!".format(name_of_the_file))

finally:
    file.close()