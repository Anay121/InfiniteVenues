from flask import Flask, render_template, url_for, request, redirect, flash, session
from models import RegistrationForm, LoginForm
from flask_bcrypt import Bcrypt
import os
import psycopg2
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
bcrypt = Bcrypt(app)

cities = ['Adoor', 'Agartala', 'Agra', 'Ahmedabad', 'Aizawl', 'Alappuzha', 'Alleppey', 'Alwar', 'Amravati', 'Amritsar', 'Anand', 'Anantapur', 'Andheri (east)', 'Angamaly', 'Ankleshwar', 'Arpora', 'Asansol', 'Aurangabad', 'Bambolim beach', 'Bangalore', 'Bardez', 'Belgaum', 'Bharuch', 'Bhavnagar', 'Bhopal', 'Bhubaneswar*', 'Bhuj', 'Bikaner', 'Bilaspur', 'Bishnupur', 'Burdwan', 'Calangute', 'Calicut', 'Canacona', 'Candolim', 'Cansaulim', 'Chalakudy', 'Chandigarh', 'Chandigarh*', 'Changanassery', 'Chennai*', 'Cherai', 'Cherthala', 'Chirang', 'Chittur-thathamangalam', 'Coimbatore', 'Coonoor', 'Dalhousie', 'Daman', 'Damthang', 'Daporijo', 'Darjiling', 'Dehradun', 'Delhi', 'Desuri', 'Dhanbad', 'Dhar', 'Dholpur', 'Dibrugarh', 'Dindigul', 'Dona paula', 'Durg-bhilai nagar', 'Durgapur', 'Dwarka', 'Ernakulam', 'Ettumanoor', 'Faridabad', 'Gandhidham', 'Gandhinagar', 'Gangtok', 'Gaziyabad', 'Ghaziabad', 'Golaghat', 'Gondia', 'Guntur', 'Gurgaon', 'Guruvayoor', 'Guwahati', 'Gwalior', 'Havelock island', 'Hyderabad', 'Idduki', 'Idukki', 'Imphal*', 'Indore', 'Itanagar', 'Jabalpur', 'Jaipur', 'Jaisalmer', 'Jalandhar', 'Jalpaiguri', 'Jamnagar', 'Jamshedpur', 'Jhunjhunu', 'Jodhpur', 'Junagadh', 'Kakinada', 'Kakkayangad', 'Kalady', 'Kancheepuram', 'Kanchipuram', 'Kanhangad', 'Kannur', 'Kanpur', 'Karauli', 'Karjat', 'Kasaragod', 'Kasargod', 'Kasauli', 'Kayamkulam', 'Khajuraho', 'Kochi', 'Kodaikanal', 'Kodungallur', 'Kokrajhar', 'Kolkata', 'Kollam', 'Kollhapur', 'Korba', 'Kottayam', 'Kovalam', 'Koyilandy', 'Kozhikode', 'Kumarakom', 'Kunnamkulam', 'Kuttiady', 'Ladnu', 'Lonavala', 'Lonavla', 'Lucknow*', 'Ludhiana', 'Madikeri', 'Madurai', 'Mahabaleshwar', 'Mahaballipuram', 'Mahesana', 'Malappuram', 'Mangalore', 'Mapusa', 'Margao', 'Mavelikkara', 'Moradabad', 'Morvi', 'Mumbai', 'Mundra', 'Munnar', 'Mussoorie', 'Muvattupuzha', 'Mysore', 'Nadiad', 'Nagaon', 'Nagpur', 'Naharlagun', 'Nashik', 'Navi mumbai', 'Nedumangad', 'Nedumbassery', 'New delhi', 'Nilambur', 'Nilgiris', 'Noida', 'Ooty', 'Ottappalam', 'Palai', 'Palakkad', 'Palghar', 'Pali', 'Panaji*', 'Panamattom', 'Panipat', 'Paravoor', 'Pasighat', 'Pathanamthitta', 'Patna*', 'Payyanur', 'Pelling', 'Peravoor', 'Perinthalmanna', 'Perumbavoor', 'Porbandar', 'Port blair*', 'Punalur', 'Pune', 'Puri', 'Purulia', 'Rabong', 'Raigad', 'Raigarh', 'Raipur*', 'Rajahmundry', 'Rajam', 'Rajkot', 'Rajnandgaon', 'Rajsamand', 'Rajula', 'Ranchi*', 'Ranga reddy', 'Ratnagiri', 'Salcete', 'Salcette', 'Salem', 'Saurashtra', 'Sawai madhopur', 'Secunderabad', 'Seoni', 'Shillong*', 'Shimla*', 'Shirdi', 'Shoranur', 'Sikar', 'Solan', 'Solapur', 'Soreng', 'Sultan bathery', 'Surat', 'Taliparamba', 'Tenali', 'Thane', 'Thanjavur', 'Thekkady', 'Theni allinagaram', 'Thiruvalla', 'Thiruvananthapuram', 'Thodupuzha', 'Thrissur', 'Tinsukia', 'Tiruchirappalli', 'Tirupati', 'Tirur', 'Trichy', 'Udaipur', 'Ujjain', 'Vadakara', 'Vadodara', 'Vaikom', 'Vapi', 'Varanasi', 'Varkala', 'Veraval', 'Vijayawada', 'Visakhapatnam', 'Wayanad', 'West kameng', 'Zirakpur']
user_col = ['id', 'fname', 'lname', 'email', 'username', 'password', 'phno']
hotel_col = ['id', 'hname', 'address', 'city', 'state', 'mobile', 'phoneno', 'email', 'category', 'subcat', 'rooms']
conn = psycopg2.connect("dbname=InfiniteVenues user=postgres password=password")
cur = conn.cursor()

@app.route('/')
@app.route('/login', methods = ['GET', 'POST'])
@app.route('/register', methods = ['GET', 'POST'] )
def hello_world():
    form = RegistrationForm(request.form)
    if request.form.get('signup'):
        form = RegistrationForm(request.form)
        if request.method == 'POST' and form.validate():
            userdet = {}
            for i in form:
                userdet[i.name] = i.data
            cur.execute(f"Select 1 from users where username = '{userdet['username']}'")
            if len(cur.fetchall()) > 0:
                flash('Username already taken! Choose another', 'danger')
                return render_template('login.html', pageType = str(request.url_rule), form = form)    
            userdet['password'] = bcrypt.generate_password_hash(userdet['password']).decode('utf-8')
            cur.execute(f"insert into users(fname, lname, email_id, username, password, contact_no) values('{userdet['fname']}', '{userdet['lname']}', '{userdet['email']}', '{userdet['username']}', '{userdet['password']}', {userdet['phno']})")
            conn.commit()
            session['user'] = userdet
            flash('Registered successfully!', 'success')
        elif not form.validate():
            print(":((((((((()))))))))")
            # return render_template('login.html', pageType = str(request.url_rule), form = form)
    else:
        form1 = LoginForm(request.form)
        if request.method == 'POST' and form1.validate():
            print('abcd')
            u = request.form.get('username')
            p = request.form.get('password')
            print(u, p)
            print(f"Select * from users where username='{u}' and password='{bcrypt.generate_password_hash(p).decode('utf-8')}'")
            cur.execute(f"Select * from users where username='{u}'")
            ulist = cur.fetchall()
            # print(ulist)
            if len(ulist)>0:
                if bcrypt.check_password_hash(ulist[0][5], p):
                    flash('Login successful!', 'success')
                    session['user'] = list(ulist[0])
                    for i in range(len(session['user'])):
                        session['user'][i] = str(session['user'][i])
                    session['user'] = dict(zip(user_col, session['user']))
                    return redirect(url_for('new_homepage'))
                else:
                    flash('Could not find matching username or password. Please check your login credentials.', 'danger')
            else:
                flash('Could not find matching username or password. Please check your login credentials.', 'danger')
        print('wxyz', request.url_rule, type(request.url_rule))
    return render_template('login.html', pageType = str(request.args.get('type')), form = form)

@app.route('/homenew')
def new_homepage():
    return render_template('homenew.html', cities = cities)

# @app.route('/home/<abcd>')
# def home_page(abcd):
#     print(abcd)
#     return render_template('homenew.html', cities = cities)

@app.route('/logout')
def logout():
    session['user'] = None
    flash('You have successfully logged out!', 'success')
    return redirect(url_for('new_homepage'))

@app.route('/profile')
def profile():
    return render_template('profile2.html')

@app.route('/hotel/<abcd>')
def hotel(abcd):
    print(abcd)
    cur.execute('Select * from hotels where hid = %s', abcd)
    hotel_det = list(cur.fetchone())
    for i in range(len(hotel_det)):
        hotel_det[i] = str(hotel_det[i])
    hotel_det = dict(zip(hotel_col, hotel_det))
    print(hotel_det)
    # get location of hotel from database or something
    location = 'Space Needle'
    location = '+'.join(location.split(' '))
    return render_template('hotels.html', key = os.getenv('MAPS_API'), location = location, details = hotel_det)

@app.route('/list')
def hotel_list():
    return render_template('list.html')
