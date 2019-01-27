import pandas as pd
import openpyxl
import sys

dict = {"Site": ["GOG"],
       "Username": ["Triotank@gmail.com"],
       "Password": ["Sickness666DevildriverSapopt85SLBForever"]
        }

columnsTitles = ["Site", "User", "Pass"]
df = pd.DataFrame(dict)
df.reindex(columns=columnsTitles)

print(df.reindex(columns=columnsTitles))

writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')
export_excel = df.to_excel (r'C:\Users\pedro.lourenco\Desktop\teste.xlsx', index = None, header=True)
