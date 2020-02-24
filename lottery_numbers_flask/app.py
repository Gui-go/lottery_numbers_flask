from flask import Flask, render_template, request
from datetime import datetime
import re
import random

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/signup_form")
def signup_form():
    return render_template('signup.html')

@app.route("/thank_you")
def thank_you():
    first = request.args.get('first')
    last = request.args.get('last')
    
    lottery_numbers = range(60)
    winning_numbers = random.sample(lottery_numbers, 7)

    return render_template('thankyou.html', first=first, last=last, winning_numbers=winning_numbers)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route("/hello/<name>")
def hello_there(name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return content