from flask import Flask, flash, redirect, render_template, url_for, request

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
	return render_template("about.html")

@app.route('/calendar')
def calendar():
	return render_template("calendar.html")

@app.route('/join')
def join():
	return render_template("join.html")

app.run(debug = True)