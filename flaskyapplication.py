from flask import Flask, flash, redirect, render_template, url_for, request
from werkzeug.routing import BaseConverter

DIRECTORIES = (('projects', 'related', 'byra'),
		('labs', 'clubs', 'spaces'),
		())


app = Flask(__name__)

class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]

app.url_map.converters['regex'] = RegexConverter


@app.route('/')
def index():
    return render_template("index.html")



@app.route('/<regex("((?!static)*"):l0Page>')
def l0Page(l0Page):
	if l0Page.lower() != l0Page:
		return redirect('/' + l0Page.lower(), code=301)
	if l0Page.lower() in DIRECTORIES[0]:
		return render_template('/' + l0Page + '/index.html') 
	return render_template(l0Page + '.html')

@app.route('/<regex("((?!static)*"):l0Page>/<l1Page>')
def l1Page(l0Page, l1Page):
        if l0Page.lower() != l0Page or l1Page.lower() != l1Page:
                return redirect('/' + l0Page.lower() + '/' + l1Page.lower(), code=301)
	if l1Page.lower() in DIRECTORIES[1]:
		return render_template('/' + l0Page + '/' + l1Page + '/index.html')
	return render_template('/' + l0Page + '/' + l1Page + '.html' if l0Page != 'static' else '')

@app.route('/<regex("((?!static)*"):l0Page>/<l1Page>/<l2Page>')
def l2Page(l0Page, l1Page, l2Page):
        if l0Page.lower() != l0Page or l1Page.lower() != l1Page or l2Page.lower() != l2Page:
                return redirect('/' + l0Page.lower() + '/' + l1Page.lower() + '/' + l2Page.lower(), code=301)
	if l2Page in DIRECTORIES[2]:
                return render_template('/' + l0Page + '/' + l1Page + '/' + l2Page +  '/index.html')
        return render_template('/' + l0Page + '/' + l1Page + '/' + l2Page + '.html')

if __name__ == '__main__':
    app.run(debug = True)
