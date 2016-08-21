from flask import Flask, flash, redirect, render_template, url_for, request, abort
from werkzeug.routing import BaseConverter
import os

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

def create_route(dirLevel):
        funcBuilder = (
                '@app.route(\'/<regex(\"((?!static).)*\"):l0Page>' + ''.join(['/<l%(lvl)iPage>' % {'lvl' : i}
                        for i in range(1, dirLevel + 1)]) + '\')\n' +
                ('def l%iPage(' % dirLevel + ''.join(['l%(lvl)iPage, ' % {'lvl' : i}
                        for i in range(0, dirLevel + 1)])[:-2] + '):\n') +
                ('\tif ' + ''.join(['l%(lvl)iPage.lower() != l%(lvl)iPage or ' % {'lvl' : i}
                        for i in range(0, dirLevel + 1)])[:-4] + ':\n') +
                ('\t\treturn redirect(' + ''.join(['\'/\' + l%(lvl)iPage.lower() + ' % {'lvl' : i}
                        for i in range(0, dirLevel + 1)])[:-3] + ', code=301)\n') +
                '\tif l%(lvl)iPage in DIRECTORIES[%(lvl)i]:\n' % {'lvl' : dirLevel} +
                ('\t\treturn render_template(' + ''.join(['\'/\' + l%(lvl)iPage + ' % {'lvl' : i}
                        for i in range(0, dirLevel + 1)])[:-3] + ' + \'/index.html\')\n') +
                ('\ttemplate = (' + ''.join(['\'/\' + l%(lvl)iPage + ' % {'lvl' : i}
                        for i in range(0, dirLevel + 1)])[6:-3] + ' + \'.html\')\n') +
                '\tif os.path.isfile(\'templates/\' + template):\n' +
                '\t\treturn render_template(template)\n' +
                '\tabort(404)\n'
                )
        return funcBuilder

for i in range(0, len(DIRECTORIES)):
        exec(create_route(i), globals(), globals())

if __name__ == '__main__':
    app.run(debug = True)
