from flask import Flask, render_template, url_for, request, redirect, flash, session
from models import RegistrationForm
from flask_bcrypt import Bcrypt
import os
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
brcypt = Bcrypt(app)
@app.route('/')
@app.route('/login', methods = ['GET', 'POST'])
@app.route('/register', methods = ['GET', 'POST'])
def hello_world():
    form = RegistrationForm(request.form)
    print(request.method)
    if request.method == 'POST' and form.validate():
        userdet = {}
        for i in form:
            userdet[i.name] = i.data
        print(request.form)
        session['user'] = userdet
        flash('Registered successfully!')
        return render_template('login.html', pageType = str(request.url_rule), form = form, userdet = userdet) 
    # print(type(request.url_rule), str(request.url_rule))
    return render_template('login.html', pageType = str(request.url_rule), form = form)

@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/logout')
def logout():
    session['user'] = None
    return redirect(url_for('home_page'))

@app.route('/profile')
def profile():
    return render_template('profile2.html')

@app.route('/hotel')
def hotel_list():
    # get location of hotel from database or something
    location = 'Space Needle'
    location = '+'.join(location.split(' '))
    return render_template('hotels.html', key = os.getenv('MAPS_API'), location = location)