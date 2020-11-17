from flask import Flask, render_template,redirect,url_for
from env import projects

app = Flask(__name__)

@app.route('/')
def home_route():
    return render_template("home.html", projects=projects.setup())

@app.route('/history/')
def hello_route():
    return render_template("history.html", projects=projects.setup())

@app.route('/biographies/')
def biographies_route():
    return render_template("biographies.html", projects=projects.setup())

@app.route('/aboutus/')
def aboutus_route():
    return render_template("aboutus.html", projects=projects.setup())

@app.route('/adams/')
def adams_route():
    return render_template("adams.html", projects=projects.setup())

@app.route('/bourke/')
def bourke_route():
    return render_template("bourke.html", projects=projects.setup())

@app.route('/goldin/')
def goldin_route():
    return render_template("goldin.html", projects=projects.setup())

@app.route('/leibovitz/')
def leibovitz_route():
    return render_template("leibovitz.html", projects=projects.setup())

@app.route('/mann/')
def mann_route():
    return render_template("mann.html", projects=projects.setup())

@app.route('/mccurry/')
def mccurry_route():
    return render_template("mccurry.html", projects=projects.setup())

@app.route('/newman/')
def newman_route():
    return render_template("newman.html", projects=projects.setup())

@app.route('/pretty/')
def pretty_route():
    return render_template("pretty.html", projects=projects.setup())

@app.route('/shabazz/')
def shabazz_route():
    return render_template("shabazz.html", projects=projects.setup())

@app.route('/wong/')
def wong_route():
    return render_template("wong.html", projects=projects.setup())

if __name__ == "__main__":
    app.run(debug = True, port=9090)