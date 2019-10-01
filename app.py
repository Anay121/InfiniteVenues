from flask import Flask, render_template, url_for, request, redirect, flash, session
from models import RegistrationForm
from flask_bcrypt import Bcrypt
import os
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
bcrypt = Bcrypt(app)

cities = ['Adoor', 'Agartala', 'Agra', 'Ahmedabad', 'Aizawl', 'Alappuzha', 'Alleppey', 'Alwar', 'Amravati', 'Amritsar', 'Anand', 'Anantapur', 'Andheri (east)', 'Angamaly', 'Ankleshwar', 'Arpora', 'Asansol', 'Aurangabad', 'Bambolim beach', 'Bangalore', 'Bardez', 'Belgaum', 'Bharuch', 'Bhavnagar', 'Bhopal', 'Bhubaneswar*', 'Bhuj', 'Bikaner', 'Bilaspur', 'Bishnupur', 'Burdwan', 'Calangute', 'Calicut', 'Canacona', 'Candolim', 'Cansaulim', 'Chalakudy', 'Chandigarh', 'Chandigarh*', 'Changanassery', 'Chennai*', 'Cherai', 'Cherthala', 'Chirang', 'Chittur-thathamangalam', 'Coimbatore', 'Coonoor', 'Dalhousie', 'Daman', 'Damthang', 'Daporijo', 'Darjiling', 'Dehradun', 'Delhi', 'Desuri', 'Dhanbad', 'Dhar', 'Dholpur', 'Dibrugarh', 'Dindigul', 'Dona paula', 'Durg-bhilai nagar', 'Durgapur', 'Dwarka', 'Ernakulam', 'Ettumanoor', 'Faridabad', 'Gandhidham', 'Gandhinagar', 'Gangtok', 'Gaziyabad', 'Ghaziabad', 'Golaghat', 'Gondia', 'Guntur', 'Gurgaon', 'Guruvayoor', 'Guwahati', 'Gwalior', 'Havelock island', 'Hyderabad', 'Idduki', 'Idukki', 'Imphal*', 'Indore', 'Itanagar', 'Jabalpur', 'Jaipur', 'Jaisalmer', 'Jalandhar', 'Jalpaiguri', 'Jamnagar', 'Jamshedpur', 'Jhunjhunu', 'Jodhpur', 'Junagadh', 'Kakinada', 'Kakkayangad', 'Kalady', 'Kancheepuram', 'Kanchipuram', 'Kanhangad', 'Kannur', 'Kanpur', 'Karauli', 'Karjat', 'Kasaragod', 'Kasargod', 'Kasauli', 'Kayamkulam', 'Khajuraho', 'Kochi', 'Kodaikanal', 'Kodungallur', 'Kokrajhar', 'Kolkata', 'Kollam', 'Kollhapur', 'Korba', 'Kottayam', 'Kovalam', 'Koyilandy', 'Kozhikode', 'Kumarakom', 'Kunnamkulam', 'Kuttiady', 'Ladnu', 'Lonavala', 'Lonavla', 'Lucknow*', 'Ludhiana', 'Madikeri', 'Madurai', 'Mahabaleshwar', 'Mahaballipuram', 'Mahesana', 'Malappuram', 'Mangalore', 'Mapusa', 'Margao', 'Mavelikkara', 'Moradabad', 'Morvi', 'Mumbai', 'Mundra', 'Munnar', 'Mussoorie', 'Muvattupuzha', 'Mysore', 'Nadiad', 'Nagaon', 'Nagpur', 'Naharlagun', 'Nashik', 'Navi mumbai', 'Nedumangad', 'Nedumbassery', 'New delhi', 'Nilambur', 'Nilgiris', 'Noida', 'Ooty', 'Ottappalam', 'Palai', 'Palakkad', 'Palghar', 'Pali', 'Panaji*', 'Panamattom', 'Panipat', 'Paravoor', 'Pasighat', 'Pathanamthitta', 'Patna*', 'Payyanur', 'Pelling', 'Peravoor', 'Perinthalmanna', 'Perumbavoor', 'Porbandar', 'Port blair*', 'Punalur', 'Pune', 'Puri', 'Purulia', 'Rabong', 'Raigad', 'Raigarh', 'Raipur*', 'Rajahmundry', 'Rajam', 'Rajkot', 'Rajnandgaon', 'Rajsamand', 'Rajula', 'Ranchi*', 'Ranga reddy', 'Ratnagiri', 'Salcete', 'Salcette', 'Salem', 'Saurashtra', 'Sawai madhopur', 'Secunderabad', 'Seoni', 'Shillong*', 'Shimla*', 'Shirdi', 'Shoranur', 'Sikar', 'Solan', 'Solapur', 'Soreng', 'Sultan bathery', 'Surat', 'Taliparamba', 'Tenali', 'Thane', 'Thanjavur', 'Thekkady', 'Theni allinagaram', 'Thiruvalla', 'Thiruvananthapuram', 'Thodupuzha', 'Thrissur', 'Tinsukia', 'Tiruchirappalli', 'Tirupati', 'Tirur', 'Trichy', 'Udaipur', 'Ujjain', 'Vadakara', 'Vadodara', 'Vaikom', 'Vapi', 'Varanasi', 'Varkala', 'Veraval', 'Vijayawada', 'Visakhapatnam', 'Wayanad', 'West kameng', 'Zirakpur']

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
        userdet['password'] = bcrypt.generate_password_hash(userdet['password']).decode('utf-8')
        session['user'] = userdet
        flash('Registered successfully!', 'success')
        return render_template('login.html', pageType = str(request.url_rule), form = form)
    return render_template('login.html', pageType = str(request.url_rule), form = form)

@app.route('/homenew')
def new_homepage():
    return render_template('homenew.html', cities = cities)

@app.route('/home')
def home_page():
    return render_template('home.html', cities = cities)

@app.route('/logout')
def logout():
    session['user'] = None
    return redirect(url_for('home_page'))

@app.route('/profile')
def profile():
    return render_template('profile2.html')

@app.route('/hotel')
def hotel():
    # get location of hotel from database or something
    location = 'Space Needle'
    location = '+'.join(location.split(' '))
    return render_template('hotels.html', key = os.getenv('MAPS_API'), location = location)

@app.route('/list')
def hotel_list():
    return render_template('list.html')
