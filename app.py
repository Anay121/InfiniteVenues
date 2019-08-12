from flask import Flask, render_template, url_for, request
app = Flask(__name__)

@app.route('/')
@app.route('/register')
@app.route('/login')
def hello_world():
    print(type(request.url_rule), str(request.url_rule))
    return render_template('login.html', pageType = str(request.url_rule))

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
    return render_template('hotels.html')