import requests
import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame
import matplotlib.pyplot as plt
import matplotlib
from statsmodels.formula.api import ols
from sklearn.linear_model import LinearRegression

r_card = requests.get("http://34.64.187.187:1337/credits?")
df_covid = pd.DataFrame({'Month':[202001, 202002, 202003, 202004, 202005, 202006, 202007, 202008, 202009, 202010, 202011, 202012, 202101, 202102, 202103, 202104], 'Confirmed':[11, 3139, 6636, 979, 703, 1331, 1506, 5642, 3865, 2699, 7688, 26528, 17471, 11467, 13415, 18919]})
list_card = r_card.json()
df_card_pre = pd.DataFrame(list_card)
list_covid = [0, 0, 0, 0, 0, 0, 0, 0, 11, 3139, 6636, 979, 703, 1331]
df_card = df_card_pre.iloc[:,[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]]
df_card.insert(2, 'Confirmed_covid19', list_covid)


print(df_card)


