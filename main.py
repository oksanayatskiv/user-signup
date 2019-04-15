from flask import Flask, request,redirect
import cgi
import re

app = Flask(__name__)
app.config['DEBUG'] = True




form = """ <!DOCTYPE html>
        <html>
            <head>
                <style>
                    .error {{
                        color : red;
                            }}
                </style>
            </head>
                <body>
                <h1> Signup </h1>
                <form atribute='/val_signup' method = "post">
                            <table>
                                    <p><label for = "username">Username
                                    <input type = "text" name ="username" id="username" value = '{username}'></label>
                                    <span class= "error">{user_error}<span></p>
                                    
                                    
                                    <p><label for = "password">Password 
                                    <input type = "password" name ="password" id="password" value ='{password}'></label>
                                    <span class= "error">{password_error}</span></p>
                                    
                                    <p><label for = "verify">Verify Password    
                                    <input type = "password" name ="verify" id="verify" value = '{verify}'/></label>
                                    <span class= "error">{verify_error}</span></p>

                                    <p><label for = "email">Email (optional)
                                    <input type = "text" name ="email" id="email" value = '{email}'/></label>
                                    <span class= "error">{email_error}<span></p>
                                    <input type= "submit" value = "Submit"/>
                            </table>
                        </form>
                </body>
        </html>
        """
content = form 


@app.route('/valide')
def display_valide():
	return form.format(username= '', user_error= '',
		password = '', password_error= '',
		verify = '', verify_error= '',
		email= '', email_error= '')


	
@app.route('/valide', methods=['POST'])
def validate_time():

    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']
	
    user_error=''
    password_error=''
    verify_error=''
    email_error=''
    
#Check User name 
    #for empty input	
    if username=='':
        user_error = "Please enter your name"
    else:
        #Check for not conaining space and is between 3 to 20 characters
        user_regex = re.compile("^\S{3,20}$")
        if not user_regex.match(username):
            user_error = ("The user's username or password is not valid," 
            "it should not contain a space character nor consist of less than 3 characters or"
            "more than 20 characters.")

    if password=="":
        password_error = "Please enter your password"
    else:
        #Check for not conaining space and is between 3 to 20 characters
        pass_regex = re.compile("^\S{3,20}$")
        if not pass_regex.match(password):
            password_error = ("The user's username or password is not valid," 
            "it should not contain a space character nor consist of less than 3 characters or"
            "more than 20 characters.")

    if verify=="":
        verify_error="Please re-enter pasword"
    elif password != verify:
        verify_error = "Your password doesn't match"
    else:
    #Check for not conaining space and is between 3 to 20 characters
        verify_regex = re.compile("^\S{3,20}$")
        if not verify_regex.match(verify):
            verify_error = ("The user's username or password is not valid," 
            "it should not contain a space character nor consist of less than 3 characters or"
            "more than 20 characters.")

    #Validate email if not empty on presents one . and  one @ and between 3 to 20 characters
    if email != '':
        email_ct = email.count('@')
        email_ct_dot = email.count('.')
        #email_regex = re.compile("^\S{3,20}$")
        if email_ct_dot>1 or email_ct>1:
            email_error = 'Please enter valid email'
        elif email_ct_dot==0 or email_ct==0:
            email_error = 'Please enter valid email'
        else:
            email_regex = re.compile("^\S{3,20}$")
            if not email_regex.match(email):
                email_error = 'Please enter valid email'
            
            
        
        #email_regex = re.compile("^\S{3,20}$")
        #email_regex1 = re.findall("^@$")
        #f not email_regex.match(email) and email_regex.match(email_regex1):
           # email_error = 'Please enter valid email'
            
	
    if not user_error and not password_error and not verify_error and not email_error:
        return redirect('/greeding')
    else:
        return content.format(user_error=user_error,
            password_error= password_error,verify_error=verify_error,
            username=username, password='', verify='',
            email_error=email_error, email=email)

@app.route('/greeding', methods=['POST'])
def validated():
    user = request.form["username"]
    return "<p>" + "Welcome,"+ user +"!.</p>"
		
	
app.run()