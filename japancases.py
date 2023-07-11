
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate


# Kaggle Link: https://www.kaggle.com/datasets/lisphilar/covid19-dataset-in-japan

headers = ["Prefectures", "Total"]

# reads csv file into data frame
df = pd.read_csv('covid_jpn_metadata.csv')



# add prefectures and values to list that are under the row value 'total'
prefectures = df.loc[df['Item'] == 'Total', 'Prefecture'].values.tolist()

item = df.loc[df['Item'] == 'Total','Value'].values.tolist()



# create df & joins the two data sets to the same table
df1 = pd.DataFrame(prefectures)

# changes df2 to int
df2 = pd.DataFrame(item)
df2 = df2.astype(int)

values = pd.DataFrame(pd.concat([df1, df2], axis=1))

# creates final table w/ prefectures and totals
table = pd.DataFrame(values)
table.columns = headers

table = table.groupby(['Prefectures'], axis=0, as_index=False).sum()

print(tabulate(table, tablefmt="fancy_grid"))

#----------------------------------------------
# Graph = Bar Graph

ax = table.plot.bar(x = 'Prefectures', y = 'Total')
ax.set_xlabel("Prefecture", fontsize=12)
ax.set_ylabel("Total Cases", fontsize=12)

plt.show()

#----------------------------------------------
# Graph = Scatterplot

axl = table.plot.scatter(x = 'Prefectures', y = 'Total')
plt.xticks(rotation=90)
plt.show()