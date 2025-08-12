import pandas as pd

df1 = pd.read_excel('main_dataset.xlsx')
df2 = pd.read_excel('traffic_data.xlsx')

df1.info()
df2.info()
