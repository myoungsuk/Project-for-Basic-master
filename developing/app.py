from bokeh.io import show
from bokeh.models.sources import ColumnDataSource
from bokeh.plotting import figure
from bokeh.models import Toggle
from bokeh.layouts import layout
from bokeh.palettes import Spectral6, Category20c_13
from bokeh.transform import linear_cmap
from bokeh.embed import components
from flask import Flask, render_template
import pandas as pd


from flask import Flask, render_template
import sys

app = Flask(__name__)

# =========================== COVID_log ===========================

df_conf = pd.read_csv('코로나 일별 확진자 수 전처리 후파일.csv')
conf_date = pd.to_datetime(df_conf['date'], format='%Y%m%d', errors='ignore')

conf_data = {'conf_num': df_conf['confirmed'], 'conf_date': conf_date}

source = ColumnDataSource(data=conf_data)

p_DateConfirmed = figure(
    sizing_mode="stretch_width",
    max_width=500,
    plot_height=250,
    x_axis_type="datetime",
    toolbar_location=None,
    tools=''
)

p_DateConfirmed.line(
    x='conf_date',
    y='conf_num',
    color='#FC4F4F',
    alpha=0.5,
    source=source
)

# ======================= COVID_log finish ==========================

# ======================= Work From Home ============================

df_WFH = pd.read_csv('재택지수 전처리 후파일.csv')
df_conf1 = pd.read_csv('코로나 일별 확진자 수 전처리 후파일.csv')
df_conf1 = df_conf1[df_conf1['date'] <= 20200914]
WFH_date = pd.to_datetime(df_WFH['dt'], format='%Y%m%d', errors='ignore')
WFH_COVID_date = pd.to_datetime(df_conf1['date'], format='%Y%m%d', errors='ignore')

WFH_data = {'WFH_ratio': df_WFH['h0d1h1_dur_r'], 'WFH_date': WFH_date}
WFH_COVID_data = {'conf1_date': WFH_COVID_date, 'conf1_num': df_conf1['confirmed']/800}

mapper_WFH = linear_cmap(
    field_name='WFH_ratio',
    palette=Spectral6,
    low=min(WFH_data['WFH_ratio']),
    high=max(WFH_data['WFH_ratio'])
)

source = ColumnDataSource(data=WFH_data)
source1 = ColumnDataSource(data=WFH_COVID_data)

p_WFH = figure(
    sizing_mode="stretch_width",
    max_width=500,
    plot_height=250,
    x_axis_type="datetime",
    toolbar_location=None,
    tools=''
)

Graph_WFH = p_WFH.circle(
    x='WFH_date',
    y='WFH_ratio',
    line_color=mapper_WFH,
    color=mapper_WFH,
    alpha=0.5,
    source=source
)

Graph_COVIDlog = p_WFH.line(
    x='conf1_date',
    y='conf1_num',
    color='#FC4F4F',
    alpha=0.5,
    source=source1
)

toggle1 = Toggle(label="코로나 상황", button_type="warning", active=True)
toggle1.js_link('active', Graph_COVIDlog, 'visible')
# ================== Work From Home finish ==========================

# ==================== Restaurant ===================================

Restaurant_month = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
Restaurant_sales = [13.2, 12.3, 11.3, 13.4, 16.2, 14.2]

p_Restaurant = figure(
    x_range=Restaurant_month,
    max_width=500,
    plot_height=250,
    toolbar_location=None,
    tools=''
)

Graph_Restaurant = p_Restaurant.vbar(
    x=Restaurant_month,
    top=Restaurant_sales,
    width=0.9
)

p_Restaurant.xgrid.grid_line_color = None
p_Restaurant.y_range.start = 10
# ==================== Restaurant finish ==========================

# ==================== Credit =======================================

df_Credit = pd.read_excel('무상데이터상품_20200804.xlsx')
Credit_date = pd.to_datetime(df_Credit['이용일자'], format='%Y%m%d', errors='ignore')
print(Credit_date)
p_Credit = figure(
    sizing_mode="stretch_width",
    toolbar_location=None,
    tools='',
    x_axis_type="datetime"
)

df_Credit_List = [
    df_Credit[df_Credit['업종대분류'] == '가전/가구'],
    df_Credit[df_Credit['업종대분류'] == '가정생활/서비스'],
    df_Credit[df_Credit['업종대분류'] == '미용'],
    df_Credit[df_Credit['업종대분류'] == '스포츠/문화/레저'],
    df_Credit[df_Credit['업종대분류'] == '여행/교통'],
    df_Credit[df_Credit['업종대분류'] == '요식/유흥'],
    df_Credit[df_Credit['업종대분류'] == '유통'],
    df_Credit[df_Credit['업종대분류'] == '음/식료품'],
    df_Credit[df_Credit['업종대분류'] == '의료'],
    df_Credit[df_Credit['업종대분류'] == '자동차'],
    df_Credit[df_Credit['업종대분류'] == '주유'],
    df_Credit[df_Credit['업종대분류'] == '패션/잡화']
]

df_Credit_Name = (
    '가전/가구',
    '가정생활/서비스',
    '미용',
    '스포츠/문화/레저',
    '여행/교통',
    '요식/유흥',
    '유통',
    '음/식료품',
    '의료',
    '자동차',
    '주유',
    '패션/잡화'
)

for dfList, dfName, color in zip(df_Credit_List, df_Credit_Name, Category20c_13):
    Credit_data = {'Credit_date': Credit_date, 'Credit_num': dfList['카드결제건수(천건)']}
    source = ColumnDataSource(data=Credit_data)
    p_Credit.line(
        x='Credit_date',
        y='Credit_num',
        line_width=2,
        color=color,
        alpha=0.8,
        legend_label=dfName,
        source=source
    )

p_Credit.legend.location = "top_left"
p_Credit.legend.click_policy = "hide"


#show(layout([p_DateConfirmed], [p_WFH], [toggle1], [p_Restaurant], [p_Credit]))

script_COVID, div_COVID = components(p_DateConfirmed)
script_WFH, div_WFH = components(p_WFH)
script_Restaurant, div_Restaurant = components(p_Restaurant)
script_Credit, div_Credit = components(p_Restaurant)
# script_toggle1_WFH, div_toggle1_WFH = components(toggle1)

# @app.route('/covid', methods=["GET", "POST"])
# def covid():
#     return render_template("covid.html", script_COVID=script_COVID, div_COVID=div_COVID)


# @app.route('/home', methods=["GET", "POST"])
# def home():
#     return render_template("home.html", script_WFH=script_WFH, div_WFH=div_WFH, button_toggle_WFH=button_toggle_WFH)


# @app.route('/rest', methods=["GET", "POST"])
# def rest():
#     return render_template("rest.html", script_Restaurant=script_Restaurant, div_Restaurant=div_Restaurant)


@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/corp")
def corp():
    return render_template("corp.html")

@app.route("/covid", methods=["GET", "POST"])
def covid():
    return render_template("covid.html",script_COVID=script_COVID, div_COVID=div_COVID)

@app.route("/credit")
def credit():
    return render_template("credit.html")

@app.route("/faq")
def faq():
    return render_template("faq.html")  

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/rest",methods=["GET", "POST"])
def rest():
    return render_template("rest.html",script_Restaurant=script_Restaurant, div_Restaurant=div_Restaurant)

if __name__ == "__main__":
    app.run(host = "0.0.0.0")