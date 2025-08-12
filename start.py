import pandas as pd

df = pd.read_excel('main_dataset.xlsx')

df.info()
df.shape
df.columns
df['발생년월']


df2 = pd.read_excel('traffic_data.xlsx')
df2.info()

