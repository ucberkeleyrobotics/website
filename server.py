from flask import Flask, flash, redirect, render_template, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
    # if current_user.get_id():
    #     return redirect(url_dictionary[current_user.get_id()])
    # else: 
    return render_template("index.html")
    # return "HELLO ROBOTS"


app.run(debug = True)