# -*- coding: utf-8 -*-
"""
Spyder Editor

Dies ist eine temporäre Skriptdatei.
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

style.use("fivethirtyeight")
dictionary = {"Rank": [3, 2, 4, 5, 6], "Name": ["Tanu", "Ashika", "Ashwin", "Mohit", "Sourabh"], "Age": [23, 24, 22, 18, 9], "Weight": [69, 72, 65, 70, 40], "Occupation": ["Student", "Working", "Working", "Student", "Student"]}
#for key, value in dictionary.items():
    #print(key, value)

 
df = pd.DataFrame(dictionary)
print("headers")
print(df.head(3))
print()
print("tail")
print(df.tail(1))
print()
dictionary1 = dictionary1 = {"Rank": [1], "Name": ["Tilo"], "Age": [80], "Weight": [80], "Occupation": ["Kitchen Queen"] }
#for key, value in dictionary1.items():
    #print(key, value)

df1 = pd.DataFrame(dictionary1)
#we can add two dataframes if they have the same columns and fields but it's not right
df_row1 = df + df1
print("Wrong concatenate")
print(df_row1)
print()
#The right way is:
df_row = pd.concat([df,df1])
print("Right way to concatenate dataframes")
print(df_row)
print()

df_row.reset_index(drop = True)
# To set a column as index:


df_row.set_index("Rank", inplace = True)
#sort values:

df_row.sort_values(by=['Rank'])

print("Sorted Dataframe")
print(df_row)


df_row.plot()
plt.show()










