import requests
import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols
from sklearn.linear_model import LinearRegression

#카드 dataframe리턴하는 함수입니다. confirmed는 월별 코로나 확진자 수입니다.
def card_request() :
 r_card = requests.get("http://34.64.187.187:1337/credits?")
 df_covid = pd.DataFrame({'Month':[202001, 202002, 202003, 202004, 202005, 202006, 202007, 202008, 202009, 202010, 202011, 202012, 202101, 202102, 202103, 202104], 'Confirmed':[11, 3139, 6636, 979, 703, 1331, 1506, 5642, 3865, 2699, 7688, 26528, 17471, 11467, 13415, 18919]})
 list_card = r_card.json()
 df_card_pre = pd.DataFrame(list_card)
 list_covid = [0, 0, 0, 0, 0, 0, 0, 0, 11, 3139, 6636, 979, 703, 1331]
 df_card = df_card_pre.iloc[:,[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]]
 df_card.insert(2, 'Confirmed_covid19', list_covid)

 x=df_card["Confirmed_covid19"]
 y1=df_card["C1"]
 y2=df_card["C2"]
 y3=df_card["C3"]
 y4=df_card["C4"]
 y5=df_card["C5"]
 y6=df_card["C6"]
 y7=df_card["C7"]
 y8=df_card["C8"]
 y9=df_card["C9"]
 y10=df_card["C10"]
 y11=df_card["C11"]
 y12=df_card["C12"]
 y13=df_card["C13"]

 df2=pd.concat([x, y1, y2, y3, y4, y5, y6, y7, y8, y9, y10, y11, y12, y13], axis=1)
 return df2
 
#카드 선형분석 결과를 리턴하는 함수입니다 dataframe으로 카테고리, 절편, 기울기 순으로 저장되어있습니다.
def card_linear() :
 r_card = requests.get("http://34.64.187.187:1337/credits?")
 df_covid = pd.DataFrame({'Month':[202001, 202002, 202003, 202004, 202005, 202006, 202007, 202008, 202009, 202010, 202011, 202012, 202101, 202102, 202103, 202104], 'Confirmed':[11, 3139, 6636, 979, 703, 1331, 1506, 5642, 3865, 2699, 7688, 26528, 17471, 11467, 13415, 18919]})
 list_card = r_card.json()
 df_card_pre = pd.DataFrame(list_card)
 list_covid = [0, 0, 0, 0, 0, 0, 0, 0, 11, 3139, 6636, 979, 703, 1331]
 df_card = df_card_pre.iloc[:,[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]]
 df_card.insert(2, 'Confirmed_covid19', list_covid)

 x=df_card["Confirmed_covid19"]
 y1=df_card["C1"]
 y2=df_card["C2"]
 y3=df_card["C3"]
 y4=df_card["C4"]
 y5=df_card["C5"]
 y6=df_card["C6"]
 y7=df_card["C7"]
 y8=df_card["C8"]
 y9=df_card["C9"]
 y10=df_card["C10"]
 y11=df_card["C11"]
 y12=df_card["C12"]
 y13=df_card["C13"]

 line_fitter1 = LinearRegression()
 line_fitter1.fit(x.values.reshape(-1,1), y1)
 line_fitter2 = LinearRegression()
 line_fitter2.fit(x.values.reshape(-1,1), y2)
 line_fitter3 = LinearRegression()
 line_fitter3.fit(x.values.reshape(-1,1), y3)
 line_fitter4 = LinearRegression()
 line_fitter4.fit(x.values.reshape(-1,1), y4)
 line_fitter5 = LinearRegression()
 line_fitter5.fit(x.values.reshape(-1,1), y5)
 line_fitter6 = LinearRegression()
 line_fitter6.fit(x.values.reshape(-1,1), y6)
 line_fitter7 = LinearRegression()
 line_fitter7.fit(x.values.reshape(-1,1), y7)
 line_fitter8 = LinearRegression()
 line_fitter8.fit(x.values.reshape(-1,1), y8)
 line_fitter9 = LinearRegression()
 line_fitter9.fit(x.values.reshape(-1,1), y9)
 line_fitter10 = LinearRegression()
 line_fitter10.fit(x.values.reshape(-1,1), y10)
 line_fitter11 = LinearRegression()
 line_fitter11.fit(x.values.reshape(-1,1), y11)
 line_fitter12 = LinearRegression()
 line_fitter12.fit(x.values.reshape(-1,1), y12)
 line_fitter13 = LinearRegression()
 line_fitter13.fit(x.values.reshape(-1,1), y13)
 
 df=pd.DataFrame({'category':['C1','C2','C3,','C4','C5','C6,','C7','C8','C9,','C10','C11','C12,','C13'],
              'y_intercept':[line_fitter1.intercept_,line_fitter2.intercept_,line_fitter3.intercept_,line_fitter4.intercept_,
              line_fitter5.intercept_,line_fitter6.intercept_,line_fitter7.intercept_,line_fitter8.intercept_,line_fitter9.intercept_,line_fitter10.intercept_
              ,line_fitter11.intercept_,line_fitter12.intercept_,line_fitter13.intercept_],
               'coef':[line_fitter1.coef_,line_fitter2.coef_,line_fitter3.coef_,line_fitter4.coef_,line_fitter5.coef_,line_fitter6.coef_,
               line_fitter7.coef_,line_fitter8.coef_,line_fitter9.coef_,line_fitter10.coef_,line_fitter11.coef_,line_fitter12.coef_,line_fitter13.coef_]})

 return df
#2018-1분기 재무재표 dataframe을 return해주는 함수입니다.
#try :
#    qs18_1('eg')
#except :
#    print("상장되지 않은 회사입니다.")
#이런식으로 예외처리를 함수를 실행하는 부분에서 진행해야합니다.
#각 년도와 분기별로 모든 함수와 dataframe을 분리해놨습니다. 필요하다면 합쳐드릴 수 있습니다.

def qs18_1(company):
 url = "http://34.64.187.187:1337/18-1-qs?Com="
 r_qs = requests.get(url+company)
 list_qs = r_qs.json()

 df_qs_pre = pd.DataFrame(list_qs)
 df_qs = df_qs_pre.iloc[:,[2, 3, 4]]
 
 return df_qs

def qs18_2(company):
 url = "http://34.64.187.187:1337/18-2-qs?Com="
 r_qs = requests.get(url+company)
 list_qs = r_qs.json()

 df_qs_pre = pd.DataFrame(list_qs)
 df_qs = df_qs_pre.iloc[:,[2, 3, 4]]
 
 return df_qs

def qs18_3(company):
 url = "http://34.64.187.187:1337/18-3-qs?Com="
 r_qs = requests.get(url+company)
 list_qs = r_qs.json()

 df_qs_pre = pd.DataFrame(list_qs)
 df_qs = df_qs_pre.iloc[:,[2, 3, 4]]
 
 return df_qs

def qs18_4(company):
 url = "http://34.64.187.187:1337/18-4-qs?Com="
 r_qs = requests.get(url+company)
 list_qs = r_qs.json()

 df_qs_pre = pd.DataFrame(list_qs)
 df_qs = df_qs_pre.iloc[:,[2, 3, 4]]
 
 return df_qs

def qs19_1(company):
 url = "http://34.64.187.187:1337/19-1-qs?Com="
 r_qs = requests.get(url+company)
 list_qs = r_qs.json()

 df_qs_pre = pd.DataFrame(list_qs)
 df_qs = df_qs_pre.iloc[:,[2, 3, 4]]
 
 return df_qs

def qs19_2(company):
 url = "http://34.64.187.187:1337/19-2-qs?Com="
 r_qs = requests.get(url+company)
 list_qs = r_qs.json()

 df_qs_pre = pd.DataFrame(list_qs)
 df_qs = df_qs_pre.iloc[:,[2, 3, 4]]
 
 return df_qs

def qs19_3(company):
 url = "http://34.64.187.187:1337/19-3-qs?Com="
 r_qs = requests.get(url+company)
 list_qs = r_qs.json()

 df_qs_pre = pd.DataFrame(list_qs)
 df_qs = df_qs_pre.iloc[:,[2, 3, 4]]
 
 return df_qs

def qs19_4(company):
 url = "http://34.64.187.187:1337/19-4-qs?Com="
 r_qs = requests.get(url+company)
 list_qs = r_qs.json()

 df_qs_pre = pd.DataFrame(list_qs)
 df_qs = df_qs_pre.iloc[:,[2, 3, 4]]
 
 return df_qs

def qs20_1(company):
 url = "http://34.64.187.187:1337/20-1-qs?Com="
 r_qs = requests.get(url+company)
 list_qs = r_qs.json()

 df_qs_pre = pd.DataFrame(list_qs)
 df_qs = df_qs_pre.iloc[:,[2, 3, 4]]
 
 return df_qs

def qs20_2(company):
 url = "http://34.64.187.187:1337/20-2-qs?Com="
 r_qs = requests.get(url+company)
 list_qs = r_qs.json()

 df_qs_pre = pd.DataFrame(list_qs)
 df_qs = df_qs_pre.iloc[:,[2, 3, 4]]
 
 return df_qs

def qs20_3(company):
 url = "http://34.64.187.187:1337/20-3-qs?Com="
 r_qs = requests.get(url+company)
 list_qs = r_qs.json()

 df_qs_pre = pd.DataFrame(list_qs)
 df_qs = df_qs_pre.iloc[:,[2, 3, 4]]
 
 return df_qs

def qs20_4(company):
 url = "http://34.64.187.187:1337/20-4-qs?Com="
 r_qs = requests.get(url+company)
 list_qs = r_qs.json()

 df_qs_pre = pd.DataFrame(list_qs)
 df_qs = df_qs_pre.iloc[:,[2, 3, 4]]
 
 return df_qs

#월별 확진자 수입니다
def covid_monthly():
 r = requests.get("http://34.64.187.187:1337/covids?")
 list_c = r.json()
 df_pre = pd.DataFrame(list_c)
 df = df_pre.iloc[:,[1, 2]]
 
 return df

#재택지수입니다 week_n_o는 weekend not home이고 뒤에도 이방식입니다
def house():
 r = requests.get("http://34.64.187.187:1337/homes?")
 list_c = r.json()
 df_pre = pd.DataFrame(list_c)
 df = df_pre.iloc[:,[1, 2, 3, 4, 5, 6, 7, 8]]
 
 return df
