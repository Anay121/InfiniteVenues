from flask import Flask, render_template, url_for, request, redirect, flash
from models import RegistrationForm
import os
app = Flask(__name__)
# print(os.getenv('MAPS_API'))
@app.route('/')
@app.route('/login', methods = ['GET', 'POST'])
@app.route('/register', methods = ['GET', 'POST'])
def hello_world():
    form = RegistrationForm(request.form)
    print(request.method)
    if request.method == 'POST' and form.validate():
        for i in form:
            print(i.data)
        print(request.form)
        flash('Registered successfully!')
        return render_template('login.html', pageType = str(request.url_rule), form = form) 
    # print(type(request.url_rule), str(request.url_rule))
    return render_template('login.html', pageType = str(request.url_rule), form = form)

@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/endpoint', methods = ['POST'])
def form_data():
    r = request.form
    print(r)

@app.route('/profile')
def profile():
    return render_template('profile2.html')

@app.route('/hotel')
def hotel_list():
    # get location of hotel from database or something
    location = 'Space Needle'
    location = '+'.join(location.split(' '))
    return render_template('hotels.html', key = os.getenv('MAPS_API'), location = location)