from flask import Flask, request,redirect
import cgi
import re
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__),'templates')
jinja_env= jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True )


app = Flask(__name__)
app.config['DEBUG'] = True



@app.route('/valide')
def display_valide():
    template = jinja_env.get_template('signupform.html')
    return template.render()


	
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
            user_error = ("The user's username is not valid," 
            "it should not contain a space character nor consist of less than 3 characters or"
            "more than 20 characters.")

    if password=="":
        password_error = "Please enter your password"
    else:
        #Check for not conaining space and is between 3 to 20 characters
        pass_regex = re.compile("^\S{3,20}$")
        if not pass_regex.match(password):
            password_error = ("The user's  password is not valid," 
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
            email_error = 'Please enter one . or @'
        elif email_ct_dot==0 or email_ct==0:
            email_error = 'Please enter at least one . or one @'
        else:
            email_regex = re.compile("^\S{3,20}$")
            if not email_regex.match(email):
                email_error = 'Please enter email not more than 20 and less than 3 character'
            
    if not user_error and not password_error and not verify_error and not email_error:
        name = str(username)
        return redirect('/greeding?name={0}'.format(name))
    else:
        template = jinja_env.get_template('signupform.html')
        return template.render(user_error=user_error,
            password_error= password_error,verify_error=verify_error,
            username=username, password='', verify='',
            email_error=email_error, email=email)

@app.route('/greeding')
def validated():
    name = request.args.get('name')
    #return '<p>Welcome,'+ name+ '!</p>'
    template = jinja_env.get_template('welcome.html')
    return template.render(myname=name)



app.run()