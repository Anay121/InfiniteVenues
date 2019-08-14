from wtforms import Form, BooleanField, StringField, validators, SubmitField

class RegistrationForm(Form):
    fname = StringField('First Name:',[validators.Length(min=4, max=25)])
    lname = StringField('Last Name:', [validators.Length(min=4, max=25)])
    phno = StringField('Phone Number:')
    email = StringField('Email Address:', [validators.Length(min=6, max=35), validators.Email(message='Please enter a valid email')])
    username = StringField('User Name:')
    password = StringField('Password:')
    # submit = SubmitField('Submit')