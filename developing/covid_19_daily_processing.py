import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame

df = pd.read_csv("C:\\Users\\Asus\\Desktop\\Covid_19_daily\\코로나 일별확진자수.csv")
df_print = df.iloc[:, 0:2]
df_print2 = df.iloc[:, 0:2]
for i in range(1,494):
    df_print2['confirmed'].iloc[i] = df_print['confirmed'].iloc[i]-df_print['confirmed'].iloc[i-1]
daily = DataFrame(df_print2)

daily.to_csv('C:\\Users\\Asus\\Desktop\\Covid_19_daily\\코로나 일별 확진자 수 전처리 후파일.csv')

