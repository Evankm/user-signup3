from flask import Flask, request, render_template
import string

invalid_chars = set(string.punctuation.replace("_", ""))

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def hello_world():
    return render_template('index.html', username="", username_error="", password="", password_error="", email="")


@app.route('/', methods=['GET','POST'])
def validate():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']
    username_error = ''
    password_error = ''
    email_requirements = ['@', "."]

    if username == '':
        username_error = 'Enter Username'
    else:
        username_error= ''  

    if  len(username) < 3 and len(username) >=1 or len(username) > 20:
        username_len_error = 'Username Doses Not Meet Length Requirements'
    else:
        username_len_error = ''

    if password == '':
        null_password = "Enter Password"
    else:
        null_password = ''  

    if len(password) < 3 and len(password) >= 1 or len(password) > 20:
        password_len_error = "Password Doses Not Meet Length Requirements"
    else:
        password_len_error = ''

    if verify == '':
        null_verify = "Verify Password"
    else:
        null_verify = ""    

    if password == verify:
        password_error = ""
    else:
        password_error = 'Passwords Do Not Match' 
  

    
    if any(char in email_requirements for char in email):
        email_error = ''
    else:    
        email_error = 'Enter Valid Email'    
    if email == '':   
        email_error = '' 
    
    
    if email_error + username_error + username_len_error + null_password + null_verify + password_error + password_len_error + email_error =='':
        welcome = "welcome " + username
    else:
        welcome = ''     

    return render_template('index.html',welcome=welcome,email_error=email_error,username_len_error = username_len_error, password_len_error = password_len_error, null_verify = null_verify, null_password = null_password, password = password, verify = verify, password_error = password_error, username_error = username_error)    

app.run()