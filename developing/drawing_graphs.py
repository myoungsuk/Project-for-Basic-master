# ++++++++++++++++++++++++++++++++++++++++++++++++++
#  writer : Jeong Junho
#  githhub : github.com/LikeDeer
#  contents : visualizations
# ++++++++++++++++++++++++++++++++++++++++++++++++++

from bokeh.io import show
from bokeh.models.sources import ColumnDataSource
from bokeh.plotting import figure
from bokeh.models import Toggle, Range1d, LinearAxis, Legend, TableColumn, DataTable
from bokeh.layouts import layout
from bokeh.models.tools import HoverTool
from bokeh.palettes import Spectral6, Category20c_13, Category20_17, Colorblind7
from bokeh.transform import linear_cmap
from bokeh.embed import components
from bokeh.transform import dodge
# from flask import Flask, render_template
import pandas as pd
from request import *

# app = Flask(__name__)


def styling_axis(plot):
    plot.border_fill_color = "#3f464d"
    plot.xaxis.axis_line_color = "white"
    plot.xaxis.major_tick_line_color = "white"
    plot.xaxis.minor_tick_line_color = "white"
    plot.xaxis.major_label_text_color = "white"
    plot.yaxis.axis_line_color = "white"
    plot.yaxis.major_tick_line_color = "white"
    plot.yaxis.minor_tick_line_color = "white"
    plot.yaxis.major_label_text_color = "white"


# =========================== COVID_log ===========================

df_conf = pd.read_csv('코로나 일별 확진자 수 전처리 후파일.csv')
conf_date = pd.to_datetime(df_conf['date'], format='%Y%m%d', errors='ignore')
conf_data = {'conf_num': df_conf['confirmed'], 'conf_date': conf_date}
source = ColumnDataSource(data=conf_data)

p_DateConfirmed = figure(
    sizing_mode="stretch_both",
    x_axis_type="datetime",
    toolbar_location='above',
)
styling_axis(p_DateConfirmed)

p_DateConfirmed.line(
    x='conf_date',
    y='conf_num',
    color='#FC4F4F',
    alpha=0.5,
    source=source
)

df_conf2 = pd.read_csv('covid_19_monthly.csv')
confirmed_list = df_conf2['confirmed'].values.tolist()
y = ['Jan/20', 'Feb/20', 'Mar/20', 'Apr/20', 'May/20', 'Jun/20', 'Jul/20', 'Aug/20', 'Sep/20', 'Oct/20', 'Nov/20', 'Dec/20', 'Jan/21', 'Feb/21', 'Mar/21', 'Apr/21', 'May/21']

conf2_data = {
    'months': y,
    'confirmed': confirmed_list,
    'color': Category20_17
}

source = ColumnDataSource(data=conf2_data)

p_DateConfirmed2 = figure(
    y_range=y,
    x_range=(0, 1000),
    sizing_mode="stretch_both",
    toolbar_location='above',
)
styling_axis(p_DateConfirmed2)

p_DateConfirmed2.hbar(
    y=dodge('months', -0.25, range=p_DateConfirmed2.y_range),
    right='confirmed',
    height=0.3,
    source=source,
    color='color',
)

p_DateConfirmed2.xgrid.visible = False
p_DateConfirmed2.ygrid.visible = False

hover = HoverTool()
hover.tooltips = """
    <div>
        <h3>@months</h3>
        <div><strong>확진: </strong>@confirmed</div>
    </div>
"""
p_DateConfirmed2.add_tools(hover)

# ======================= COVID_log finish ==========================

# ======================= Work From Home ============================

df_WFH = house()
df_conf1 = pd.read_csv('코로나 일별 확진자 수 전처리 후파일.csv')
df_conf1 = df_conf1[df_conf1['date'] <= 20200914]
WFH_date = pd.to_datetime(df_WFH['date'], format='%Y%m%d', errors='ignore')
WFH_COVID_date = pd.to_datetime(df_conf1['date'], format='%Y%m%d', errors='ignore')
WFH_data = {'WFH_date': WFH_date,
            'WFH_ratio1': df_WFH['week_n_i'],
            'WFH_ratio2': df_WFH['week_d_i'],
            'WFH_ratio3': df_WFH['holiday_n_i'],
            'WFH_ratio4': df_WFH['week_n_o'],
            'WFH_ratio5': df_WFH['week_d_o'],
            'WFH_ratio6': df_WFH['holiday_n_o'],
            'WFH_ratio7': df_WFH['holiday_d_o']}
WFH_COVID_data = {'conf1_date': WFH_COVID_date,
                  'conf1_num': df_conf1['confirmed']/1600 + 0.35,
                  'conf2_num': df_conf1['confirmed']/8000 + 0.4}

# mapper_WFH = linear_cmap(
#     field_name='WFH_ratio',
#     palette=Spectral6,
#     low=min(WFH_data['WFH_ratio']),
#     high=max(WFH_data['WFH_ratio'])
# )

source = ColumnDataSource(data=WFH_data)
source1 = ColumnDataSource(data=WFH_COVID_data)

p_WFH = figure(
    y_range=(0.35, 0.8),
    sizing_mode="stretch_both",
    x_axis_type="datetime",
    toolbar_location='above',
)
styling_axis(p_WFH)
p_WFH.add_layout(Legend(), 'right')

p_WFH.circle(
    x='WFH_date',
    y='WFH_ratio1',
    line_color=Colorblind7[0],
    color=Colorblind7[0],
    alpha=0.5,
    legend_label='평일야간재택',
    source=source
)

p_WFH.circle(
    x='WFH_date',
    y='WFH_ratio2',
    line_color=Colorblind7[1],
    color=Colorblind7[1],
    alpha=0.5,
    legend_label='평일주간재택',
    source=source
)

p_WFH.circle(
    x='WFH_date',
    y='WFH_ratio3',
    line_color=Colorblind7[2],
    color=Colorblind7[2],
    alpha=0.5,
    legend_label='휴일야간재택',
    source=source
)

p_WFH.line(
    x='conf1_date',
    y='conf1_num',
    color='#FC4F4F',
    alpha=0.5,
    legend_label='COVID 상황',
    source=source1
)

p_WFH.legend.click_policy = "hide"

p_WFH2 = figure(
    y_range=(0.4, 0.5),
    sizing_mode="stretch_both",
    x_axis_type="datetime",
    toolbar_location='above',
)
styling_axis(p_WFH2)
p_WFH2.add_layout(Legend(), 'right')

p_WFH2.circle(
    x='WFH_date',
    y='WFH_ratio4',
    line_color=Colorblind7[3],
    color=Colorblind7[3],
    alpha=0.5,
    legend_label='평일야간외부활동',
    source=source
)

p_WFH2.circle(
    x='WFH_date',
    y='WFH_ratio5',
    line_color=Colorblind7[4],
    color=Colorblind7[4],
    alpha=0.5,
    legend_label='평일주간외부활동',
    source=source,
)

p_WFH2.circle(
    x='WFH_date',
    y='WFH_ratio6',
    line_color=Colorblind7[5],
    color=Colorblind7[5],
    alpha=0.5,
    legend_label='휴일야간외부활동',
    source=source
)

p_WFH2.circle(
    x='WFH_date',
    y='WFH_ratio7',
    line_color=Colorblind7[6],
    color=Colorblind7[6],
    alpha=0.5,
    legend_label='휴일주간외부활동',
    source=source
)

p_WFH2.line(
    x='conf1_date',
    y='conf2_num',
    color='#FC4F4F',
    alpha=0.5,
    legend_label='COVID 상황',
    source=source1
)

p_WFH2.legend.click_policy = "hide"

# ================== Work From Home finish ==========================

# ==================== Restaurant ===================================

Restaurant_month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
Restaurant_sales = [13.2, 12.3, 11.3, 13.4, 16.2, 14.2]

p_Restaurant = figure(
    x_range=Restaurant_month,
    sizing_mode="stretch_both",
    toolbar_location='above'
)
styling_axis(p_Restaurant)
p_Restaurant.yaxis.axis_label = 'Restaurant'
p_Restaurant.y_range = Range1d(start=0, end=20)

p_Restaurant.vbar(
    x=Restaurant_month,
    top=Restaurant_sales,
    width=0.9
)

p_Restaurant.extra_y_ranges['Covid_month'] = Range1d(start=0, end=250)
p_Restaurant.add_layout(LinearAxis(y_range_name='Covid_month', axis_label='Covid(명)'), 'right')

p_Restaurant.line(
    x=Restaurant_month,
    y=[1, 108.2414, 214.0645, 32.63333, 22.67742, 44.36667],            # covid monthly data
    line_width=3,
    legend='월별 코로나 확진',
    y_range_name='Covid_month',
    color='#FC4F4F',
)

p_Restaurant.legend.click_policy = "hide"

p_Restaurant.xgrid.grid_line_color = None
p_Restaurant.y_range.start = 10

# ==================== Restaurant finish ============================

# ==================== Credit =======================================

df_Credit1 = card_request()
df_Credit2 = card_linear()

for x in [1000, 2000, 3000, 4000, 5000]:               # adding linear regressed data(df_Credit2) to dataframe(df_Credit1)
    y = [x]
    for i in range(0, 13):
        y.append(float(df_Credit2.loc[i, 'coef']) * x + df_Credit2.loc[i, 'y_intercept'])
    df_Credit1 = df_Credit1.append(pd.Series(y, index=df_Credit1.columns), ignore_index=True)

df_Credit1 = df_Credit1.sort_values(by=['Confirmed_covid19'], axis=0)

df_Credit1_columns = df_Credit1.columns = [
    'Confirmed_covid19',
    '가전/가구',
    '가정생활/서비스',
    '교육/학원',
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
]

del df_Credit1_columns[0]

source = ColumnDataSource(data=df_Credit1)

p_Credit = figure(
    sizing_mode="stretch_both",
    toolbar_location='below',
    tools="pan,wheel_zoom,box_zoom,reset",
    x_axis_label="COVID-19 확진",
    y_axis_label="카드이용건수(천)"
)
styling_axis(p_Credit)
p_Credit.add_layout(Legend(), 'right')

for dfName, color in zip(df_Credit1_columns, Category20c_13):
    p_Credit.line(
        x='Confirmed_covid19',
        y=dfName,
        line_width=2,
        color=color,
        alpha=0.8,
        legend_label=dfName,
        source=source
    )

p_Credit.legend.click_policy = "hide"

p_Credit.toolbar_location = 'above'

x = df_Credit2['coef'].values.tolist()
for i in range(len(x)):
    x[i] = abs(x[i])

linear_data = {
    'x': x,
    'y': df_Credit1_columns,
    'color': Category20_17
}
source = ColumnDataSource(linear_data)
p_Credit2 = figure(
    y_range=df_Credit1_columns,
    x_range=(0, 0.5),
    sizing_mode="stretch_both",
    toolbar_location='above',
    x_axis_label='상관계수(절대값)'
)

styling_axis(p_Credit2)

p_Credit2.hbar(
    y=dodge('y', -0.25, range=p_Credit2.y_range),
    right='x',
    height=0.3,
    source=source,
    color='color',
)

p_Credit2.xgrid.visible = False
p_Credit2.ygrid.visible = False

# ======================= Credit finish ============================

# ======================= company ==================================

try :
    df_Company = qs18_1('eg')
except :
    print("상장되지 않은 회사입니다.")

source = ColumnDataSource(df_Company)

columns = [TableColumn(field="Com", title="Com"),
           TableColumn(field="Sep", title="Sep"),
           TableColumn(field="Cap", title="Cap")]
data_table_EG = DataTable(
    source=source,
    columns=columns,
    width=400,
    height=280,
    editable=False,
    reorderable=False
)

# ======================= company finish ===========================

show(layout([p_DateConfirmed, p_DateConfirmed2], [p_WFH, p_WFH2], [p_Restaurant], [p_Credit], [data_table_EG], [p_Credit2]))

script_COVID, div_COVID = components(p_DateConfirmed)
script_COVID2, div_COVID2 = components(p_DateConfirmed2)
script_WFH, div_WFH = components(p_WFH)
script_Restaurant, div_Restaurant = components(p_Restaurant)
script_Credit, div_Credit = components(p_Credit)
script_DataTable_EG, div_DataTable_EG = components(data_table_EG)
script_p_Credit2, div_p_Credit2 = components(p_Credit2)

# @app.route('/covid', methods=["GET", "POST"])
# def covid():
#     return render_template("covid.html", script_COVID=script_COVID, div_COVID=div_COVID)


# @app.route('/home', methods=["GET", "POST"])
# def home():
#     return render_template("home.html", script_WFH=script_WFH, div_WFH=div_WFH, script_toggle1=script_toggle1, div_toggle1=div_toggle1)


# @app.route('/rest', methods=["GET", "POST"])
# def rest():
#     return render_template("rest.html", script_Restaurant=script_Restaurant, div_Restaurant=div_Restaurant)

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", debug=True, port=5000)
