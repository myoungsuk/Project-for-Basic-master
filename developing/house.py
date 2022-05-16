import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame

df = pd.read_csv("C:\\Users\\Asus\\Desktop\\SKT 마켓 인사이트 - 재택지수\\1)재택활동지수_2000921.csv")
df_print = df.iloc[:,[0, 4, 5, 6, 7, 8, 9, 10]]
df_print = df_print.fillna('0.0')
house = DataFrame(df_print)
house.to_csv('C:\\Users\\Asus\\Desktop\\SKT 마켓 인사이트 - 재택지수\\재택지수 전처리 후파일.csv')

