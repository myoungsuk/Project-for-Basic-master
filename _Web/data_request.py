import requests
import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols
from sklearn.linear_model import LinearRegression
from tqdm import tqdm


# 카드 dataframe리턴하는 함수입니다. confirmed는 월별 코로나 확진자 수입니다.
def card_request():
    r_card = requests.get("http://34.64.187.187:1337/credits?")
    df_covid = pd.DataFrame(
        {
            "Month": [
                202001,
                202002,
                202003,
                202004,
                202005,
                202006,
                202007,
                202008,
                202009,
                202010,
                202011,
                202012,
                202101,
                202102,
                202103,
                202104,
            ],
            "Confirmed": [
                11,
                3139,
                6636,
                979,
                703,
                1331,
                1506,
                5642,
                3865,
                2699,
                7688,
                26528,
                17471,
                11467,
                13415,
                18919,
            ],
        }
    )
    list_card = r_card.json()
    df_card_pre = pd.DataFrame(list_card)
    list_covid = [0, 0, 0, 0, 0, 0, 0, 0, 11, 3139, 6636, 979, 703, 1331]
    df_card = df_card_pre.iloc[
        :, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    ]
    df_card.insert(2, "Confirmed_covid19", list_covid)
    category = [
        "C1",
        "C2",
        "C3",
        "C4",
        "C5",
        "C6",
        "C7",
        "C8",
        "C9",
        "C10",
        "C11",
        "C12",
        "C13",
    ]

    data = []
    data.append(df_card["Confirmed_covid19"])
    for df_card_keys in df_card.keys():
        if df_card_keys in category:
            data.append(df_card[df_card_keys])

    df2 = pd.concat(data, axis=1)
    return df2


# 카드 선형분석 결과를 리턴하는 함수입니다 dataframe으로 카테고리, 절편, 기울기 순으로 저장되어있습니다.
def card_linear():
    r_card = requests.get("http://34.64.187.187:1337/credits?")
    df_covid = pd.DataFrame(
        {
            "Month": [
                202001,
                202002,
                202003,
                202004,
                202005,
                202006,
                202007,
                202008,
                202009,
                202010,
                202011,
                202012,
                202101,
                202102,
                202103,
                202104,
            ],
            "Confirmed": [
                11,
                3139,
                6636,
                979,
                703,
                1331,
                1506,
                5642,
                3865,
                2699,
                7688,
                26528,
                17471,
                11467,
                13415,
                18919,
            ],
        }
    )
    list_card = r_card.json()
    df_card_pre = pd.DataFrame(list_card)
    list_covid = [0, 0, 0, 0, 0, 0, 0, 0, 11, 3139, 6636, 979, 703, 1331]
    df_card = df_card_pre.iloc[
        :, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    ]
    df_card.insert(2, "Confirmed_covid19", list_covid)
    category = [
        "C1",
        "C2",
        "C3",
        "C4",
        "C5",
        "C6",
        "C7",
        "C8",
        "C9",
        "C10",
        "C11",
        "C12",
        "C13",
    ]

    x = df_card["Confirmed_covid19"]
    coefs = []
    intercepts = []
    for df_card_key in tqdm(df_card.keys(), desc="LinarRegression"):
        if df_card_key in category:
            line_fitter = LinearRegression().fit(
                x.values.reshape(-1, 1), df_card[df_card_key]
            )
            coefs.append(line_fitter.coef_[0])
            intercepts.append(line_fitter.intercept_)

    df = pd.DataFrame({"category": category, "y_intercept": intercepts, "coef": coefs})

    return df


"""
2018-1분기 재무재표 dataframe을 return해주는 함수입니다.
try :
    qs18_1('eg')
except :
    print("상장되지 않은 회사입니다.")
이런식으로 예외처리를 함수를 실행하는 부분에서 진행해야합니다.
각 년도와 분기별로 모든 함수와 dataframe을 분리해놨습니다. 필요하다면 합쳐드릴 수 있습니다.
"""


def qs18_1(company):
    url = "http://34.64.187.187:1337/18-1-qs?Com="
    r_qs = requests.get(url + company)
    list_qs = r_qs.json()

    df_qs_pre = pd.DataFrame(list_qs)
    df_qs = df_qs_pre.iloc[:, [2, 3, 4]]

    return df_qs


def qs18_2(company):
    url = "http://34.64.187.187:1337/18-2-qs?Com="
    r_qs = requests.get(url + company)
    list_qs = r_qs.json()

    df_qs_pre = pd.DataFrame(list_qs)
    df_qs = df_qs_pre.iloc[:, [2, 3, 4]]

    return df_qs


def qs18_3(company):
    url = "http://34.64.187.187:1337/18-3-qs?Com="
    r_qs = requests.get(url + company)
    list_qs = r_qs.json()

    df_qs_pre = pd.DataFrame(list_qs)
    df_qs = df_qs_pre.iloc[:, [2, 3, 4]]

    return df_qs


def qs18_4(company):
    url = "http://34.64.187.187:1337/18-4-qs?Com="
    r_qs = requests.get(url + company)
    list_qs = r_qs.json()

    df_qs_pre = pd.DataFrame(list_qs)
    df_qs = df_qs_pre.iloc[:, [2, 3, 4]]

    return df_qs


def qs19_1(company):
    url = "http://34.64.187.187:1337/19-1-qs?Com="
    r_qs = requests.get(url + company)
    list_qs = r_qs.json()

    df_qs_pre = pd.DataFrame(list_qs)
    df_qs = df_qs_pre.iloc[:, [2, 3, 4]]

    return df_qs


def qs19_2(company):
    url = "http://34.64.187.187:1337/19-2-qs?Com="
    r_qs = requests.get(url + company)
    list_qs = r_qs.json()

    df_qs_pre = pd.DataFrame(list_qs)
    df_qs = df_qs_pre.iloc[:, [2, 3, 4]]

    return df_qs


def qs19_3(company):
    url = "http://34.64.187.187:1337/19-3-qs?Com="
    r_qs = requests.get(url + company)
    list_qs = r_qs.json()

    df_qs_pre = pd.DataFrame(list_qs)
    df_qs = df_qs_pre.iloc[:, [2, 3, 4]]

    return df_qs


def qs19_4(company):
    url = "http://34.64.187.187:1337/19-4-qs?Com="
    r_qs = requests.get(url + company)
    list_qs = r_qs.json()

    df_qs_pre = pd.DataFrame(list_qs)
    df_qs = df_qs_pre.iloc[:, [2, 3, 4]]

    return df_qs


def qs20_1(company):
    url = "http://34.64.187.187:1337/20-1-qs?Com="
    r_qs = requests.get(url + company)
    list_qs = r_qs.json()

    df_qs_pre = pd.DataFrame(list_qs)
    df_qs = df_qs_pre.iloc[:, [2, 3, 4]]

    return df_qs


def qs20_2(company):
    url = "http://34.64.187.187:1337/20-2-qs?Com="
    r_qs = requests.get(url + company)
    list_qs = r_qs.json()

    df_qs_pre = pd.DataFrame(list_qs)
    df_qs = df_qs_pre.iloc[:, [2, 3, 4]]

    return df_qs


def qs20_3(company):
    url = "http://34.64.187.187:1337/20-3-qs?Com="
    r_qs = requests.get(url + company)
    list_qs = r_qs.json()

    df_qs_pre = pd.DataFrame(list_qs)
    df_qs = df_qs_pre.iloc[:, [2, 3, 4]]

    return df_qs


def qs20_4(company):
    url = "http://34.64.187.187:1337/20-4-qs?Com="
    r_qs = requests.get(url + company)
    list_qs = r_qs.json()

    df_qs_pre = pd.DataFrame(list_qs)
    df_qs = df_qs_pre.iloc[:, [2, 3, 4]]

    return df_qs


# 월별 확진자 수입니다
def covid_monthly():
    r = requests.get("http://34.64.187.187:1337/covids?")
    list_c = r.json()
    df_pre = pd.DataFrame(list_c)
    df = df_pre.iloc[:, [1, 2]]

    return df


# 재택지수입니다 week_n_o는 weekend not home이고 뒤에도 이방식입니다
def house():
    r = requests.get("http://34.64.187.187:1337/homes?")
    list_c = r.json()
    df_pre = pd.DataFrame(list_c)
    df = df_pre.iloc[:, [1, 2, 3, 4, 5, 6, 7, 8]]

    return df
