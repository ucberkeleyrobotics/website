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

@app.route('/projects/')
def projects():
	return render_template("/projects/index.html")

@app.route('/related/')
def related():
	return render_template("/related/index.html")

@app.route('/projects/<filename>')
def in_projects(filename):
	return render_template("/projects/" + filename + ".html")


@app.route('/related/labs/')
def labs():
	print("in labs")
	return render_template("/related/labs/index.html")

@app.route('/related/clubs/')
def clubs():
	return render_template("/related/clubs/index.html")

@app.route('/related/<club_or_lab>/<filename>')
def two_folder(club_or_lab, filename):
	return render_template("/related/" + club_or_lab + "/" + filename + ".html")

app.run(debug = True)