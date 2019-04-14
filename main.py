from flask import Flask, request,redirect

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
                                    <input type = "text" name ="password" id="password" value ='{password}'></label>
                                    <span class= "error">{password_error}</span></p>
                                    
                                    <p><label for = "verify">Verify Password    
                                    <input type = "text" name ="verify" id="verify" value = '{verify}'/></label>
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
    
	
    if username=="":
        user_error = "Please enter your name"
        username=''
    
    if ' '  in username:
        user_error = error = "Please enter your name"
        username= ''
        #redirect ('/?error' + user_error)
    else:
        if username != "\w{3,20}":
            user_error = "Please enter your name"
            username=''
            #redirect ('/?error' + user_error)        
        
		

    if password=="" or verify=="":
        password_error = "Please enter your password"
        #redirect('/?error' + password_error)
	
	
    if ' '  in password:
        password_error = error = "Please enter your password"
        #redirect ('/?error' + password_error)
    else:
        if password== "\w{3,20}":
            password_error = "Please enter your password"
            #redirect ('/?error' + password_error)
            
    
	
    if len(password) != len(verify):
        if password != verify:
            verify_error = "Your password doesn't match"
            #redirect ('/?error' + user_error)
    if email != '':
        if email != '.' or email !="\w{3,20}" or mail != '@':
            email_error = 'Please enter valid email' 
	
    if not user_error and not password_error and not verify_error:
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