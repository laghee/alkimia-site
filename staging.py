
# A very simple Flask app for you to get started...

from datetime import datetime
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def benvenuti():
    return render_template('index.html', now=datetime.utcnow())

# @app.route("/form", methods=["GET", "POST"])
# def my_form():
#     if request.method == 'POST':
#         reply_to = request.form.get('email')
#         message = request.form.get('message')
#         # send_email(message, reply_to)
#     return render_template('my_form.html')