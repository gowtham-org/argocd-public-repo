from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    birthday = request.form.get('birthday')

    today = datetime.today()
    bday = datetime.strptime(birthday, '%Y-%m-%d')
    next_birthday = bday.replace(year=today.year)

    if next_birthday.date() < today.date():
        next_birthday = next_birthday.replace(year=today.year + 1)

    days_left = (next_birthday.date() - today.date()).days

    if days_left == 0:
        return f"<h2>Happy Birthday {name}! Today is your special day! 🎂</h2>"
    else:
        return f"<h2>Hi {name}! Your birthday is in {days_left} days! 🎂</h2>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
