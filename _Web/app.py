from flask import Flask, render_template
import sys
from visualization import confirmed, confirmed2, wfh, restaurant, credit, credit2
from bokeh.embed import components

script_COVID, div_COVID = components(confirmed())
script_COVID2, div_COVID2 = components(confirmed2())
script_WFH, div_WFH = components(wfh())
script_Restaurant, div_Restaurant = components(restaurant())
script_Credit, div_Credit = components(credit())
script_Credit2, div_Credit2 = components(credit2())
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/covid")
def covid():
    return render_template("covid.html", script_COVID=script_COVID, div_COVID=div_COVID)


@app.route("/credit")
def credit():
    return render_template(
        "credit.html", script_Credit=script_Credit, div_Credit=div_Credit, script_Credit2=script_Credit2, div_Credit2=div_Credit2
    )


@app.route("/faq")
def faq():
    return render_template("faq.html")


@app.route("/home")
def home():
    return render_template("home.html", script_WFH=script_WFH, div_WFH=div_WFH)


@app.route("/rest")
def rest():
    return render_template(
        "rest.html", script_Restaurant=script_Restaurant, div_Restaurant=div_Restaurant
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
