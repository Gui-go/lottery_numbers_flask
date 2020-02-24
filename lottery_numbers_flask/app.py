from flask import Flask, render_template, request
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


