from flask import Flask, flash, redirect, render_template, url_for, request

#Note: not all of the redirects work, which is really freaking weird
#Actually I'm pretty sure none of them are even doing anything
#Oh well.

app = Flask(__name__)

@app.route('/')
@app.route('/index')
@app.route('/index/')
def index():
    return render_template("index.html")

@app.route('/about')
def about_redir():
    return redirect('/about/')
@app.route('/about/')
def about():
	return render_template("about.html")

@app.route('/calendar')
def calendar_redir():
    return redirect('/calendar/')
@app.route('/calendar/')
def calendar():
	return render_template("calendar.html")

@app.route('/dxm')
def dxm_redir():
    return redirect('/dxm/')
@app.route('/dxm/')
def dxm():
	return render_template("dxm.html")

@app.route('/join')
def join_redir():
    return redirect('/join/')
@app.route('/join/')
def join():
	return render_template("join.html")
	
def projects():
	return render_template("/projects/index.html")


@app.route('/form')
def form_redir():
    return redirect('/form/')
@app.route('/form/')
def form():
	return render_template("form.html")

@app.route('/sponsorships')
def sponsorship_redir():
	return redirect('/sponsorships/')
@app.route('/sponsorships/')
def sponsorships():
	return render_template("sponsorships.html")

@app.route('/shirts')
def shirts_redir():
    return redirect('/shirts/')
@app.route('/shirts/')
def shirts():
	return render_template("shirts.html")


@app.route('/projects/')
def projects():
	return render_template("/projects/index.html")

@app.route('/projects/<filename>')
def in_projects_redir(filename):
    return redirect('/projects/' + filename + '/')
@app.route('/projects/<filename>/')
def in_projects(filename):
	return render_template("/projects/" + filename + ".html")

@app.route('/related')
def related_redir():
    return redirect('/related/')
@app.route('/related/')
def related():
	return render_template("/related/index.html")

@app.route('/related/labs')
def labs_redir():
    return redirect('/related/labs/')
@app.route('/related/labs/')
def labs():
	return render_template("/related/labs/index.html")

@app.route('/related/clubs')
def clubs_redir():
    return redirect('/related/clubs/')
@app.route('/related/clubs/')
def clubs():
	return render_template("/related/clubs/index.html")

@app.route('/byra/')
@app.route('/BYRA/')
def byra():
	return render_template("/BYRA/index.html")

@app.route('/related/spaces')
def spaces_redir():
    return redirect('/related/spaces/')
@app.route('/related/spaces/')
def spaces():
	return render_template("/related/spaces/index.html")

@app.route('/related/<clublabspace>/<filename>')
def two_folder_redir(clublabspace, filename):
    return redirect("/related/" + clublabspace + "/" + filename + "/")
@app.route('/related/<clublabspace>/<filename>/')
def two_folder(clublabspace, filename):
	return render_template("/related/" + clublabspace + "/" + filename + ".html")

if __name__ == '__main__':
    app.run(debug = True)
