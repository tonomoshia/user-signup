from flask import Flask, request, redirect, render_template
import os
import jinja2

app = Flask (__name__)

app.config['DEBUG'] = True

@app.route("/", methods=['POST'])

def username_sign_up():
    username = request.form['username']
    if " " in username OR len(username) < 3 OR len(username) > 20:
        error = "That's not a valid username".format(username)
        return redirect("/?error=" + error)
    return render_template('/,', username=username)

def password_sign_up():
    password = request.form['passowrd']
    verify = request.form['verify']

    if password != verify:
        error = "Passwords don't match".format(verify)
        return redirect("/?error=" + error)
    if " " in password OR len(password) < 3 OR len(password) > 20:
        error = "That's not a valid password".format(password)
        return redirect("/?error=" + error)

def email_sign_up():
    email = request.form['email']
    if len(email) < 3 OR len(email) > 20:
        error = "That's not a valid email".format(email)
        return redirect("/?error=" + error)
    if 




