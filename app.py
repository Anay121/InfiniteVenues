from flask import Flask, render_template, url_for, request
app = Flask(__name__)

@app.route('/')
@app.route('/login')
def hello_world():
    return render_template('login.html')

@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/endpoint', methods = ['POST'])
def form_data():
    r = request.form
    print(r)

@app.route('/profile')
def profile():
    return render_template('profile.html')