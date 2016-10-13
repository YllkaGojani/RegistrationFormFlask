from flask import Flask,render_template,request,redirect,session,flash
import re
app = Flask(__name__)
app.secret_key = 'secret'
email_regex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
name_regex = re.compile(r'^[a-zA-Z]+$')
password_regex = re.compile(r'^(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$')
birthdate_regex = re.compile(r'((?:0[1-9])|(?:1[0-2]))\/((?:0[0-9])|(?:[1-2][0-9])|(?:3[0-1]))\/(\d{4})')

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/register',methods=['POST'])
def register():
	if len(request.form['email']) < 1:
		flash('All fields must be filled!','Email')
	elif len(request.form['first_name']) < 1:
		flash('All fields must be filled!','First name')
	elif len(request.form['last_name']) < 1:
		flash('All fields must be filled!','Last name')	
	elif len(request.form['birthdate']) < 1:
		flash('All fields must be filled!','Birth date')
	elif len(request.form['password']) < 1:
		flash('All fields must be filled!','Password')
	elif len(request.form['confirm']) < 1:
		flash('All fields must be filled!','Password confirmation')				
	elif not name_regex.match(request.form['first_name']):
		flash('First name must contain only letters!','Cannot contain any number!')
	elif not name_regex.match(request.form['last_name']):
		flash('Last name must contain only letters!','Cannot contain any number!')
	elif not email_regex.match(request.form['email']):
		flash('Email not valid!','error:EMAIL')	
	elif not password_regex.match(request.form['password']):
		flash('Password not valid','Should be more than 8 characters, at least 1 uppercase and 1 number!')	
	elif request.form['password'] != request.form['confirm']:
		flash('Password and password confirmation do not match!','error:MISMATCH')	
	elif not birthdate_regex.match(request.form['birthdate']):
		flash('Birth date not valid!','erro:DATE')
	else:
		flash('Success!')
	return redirect('/')
					
app.run(debug=True)	