from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy 
import sys

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	return render_template('./index.html')

@app.route('/about', methods=['GET', 'POST'])
def about():
	return render_template('./about.html')

@app.route('/pay', methods=['GET', 'POST'])
def pay():
	print("pay")
	return render_template('./pay.html')


if __name__ == '__main__':
	app.run(debug=True)