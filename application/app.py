from flask import Flask, render_template, request
from datetime import date

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])

def count():
    count = ''
    if request.method=="POST" and 'date1' in request.form and 'date2' in request.form:
        d1 = request.form.get('date1')
        date1 = d1.split('-')
        date1asNumbers = list(map(int, date1))
        d1 = date(date1asNumbers[0], date1asNumbers[1], date1asNumbers[2])

        d2 = request.form.get('date2')
        date2 = d2.split('-')
        date2asNumbers = list(map(int, date2))
        d2 = date(date2asNumbers[0], date2asNumbers[1], date2asNumbers[2])

        daysBetween = (d2 - d1)
        count = daysBetween.days
    return render_template('index.html', count=count)
