#%% - Import Lib
import csv
import pandas as pd
import openpyxl

#%% - Reading csv file using csv lib (built-in)
with open("data/employee.csv", "r", newline='', encoding='utf8') as f:
    reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
    for row in reader:
        #print(row)
        #print(' - '.join(row))
        print(f"{row[0]}: {row[1]} >> {row[2]} >> {row[3]}")

#%% - Reading csv file using pandas
df = pd.read_csv("data/employee.csv")
#print(df.tail(2))
print(df["Name"])

#%% - Reading xlxs file using pandas
df = pd.read_excel("data/Sales.xlsx")
print(df.head())