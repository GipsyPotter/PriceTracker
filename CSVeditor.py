import pandas as pd
import time


df = pd.read_csv('Product.csv', index_col='id')
print(time.strftime("%H:%M:%S", time.localtime()))
# if df.loc[1] == None
# df.loc[1] = [time.strftime("%H:%M:%S", time.localtime()), ""]
print(df)
df.to_csv('Product.csv')
