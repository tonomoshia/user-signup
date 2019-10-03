from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/index", methods=['GET', 'POST'])
def validateInputs():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']
    # username = ''
    # pasword = ''
    # verify = ''
    # email = ''
    # title = 'User Signup'
    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''

    if int(len(username)) <= 0:
        username_error = "That's not a valid username"
        username = ''
    else:
        if int(len(username)) < 3 or int(len(username)) > 20:
            username_error = "That's not a valid username"
            username = ''

    if int(len(password)) <= 0:
        password_error = "That's not a valid password"
        password = ''
    else:
        if int(len(password)) < 3 or int(len(password)) > 20:
            password_error = "That's not a valid password"
            password = ''

    if password != verify:
        verify_error = "Passwords do not match"
        verify = ''
    else:
        if int(len(verify)) <= 0:
            verify_error = "Passwords do not match"
            verify = ''

    if email != "" and len(email) < 3 or len (email) > 20:
        email_error = "That's not a valid email"
        email = ''
    elif email !="" and ("." not in email or "@" not in email):
        email_error = "That's not a valid email"
        email = ''

    if not username_error and not verify_error and not password_error and not email_error:
        return redirect('/welcome?username={0}'.format(username))
    else:
        return render_template('index.html', username=username, password=password, verify=verify, email=email, username_error=username_error, password_error=password_error, verify_error=verify_error,  email_error=email_error)

@app.route('/welcome')
def welcome():
    username = request.args.get('username')
    return render_template('welcome.html', username=username)


if __name__ == "__main__":
    app.run()
