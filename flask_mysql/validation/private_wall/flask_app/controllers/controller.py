import re
from types import MethodDescriptorType
from flask.globals import current_app
from flask.wrappers import Request
from werkzeug.utils import secure_filename
from flask_app.models.model import Users
from flask_app.config.mysqlconnection import connectToMySQL
    # import the function that will return an instance of a connection
from flask import Flask,render_template,request, redirect,session
from flask_app import app
from flask_bcrypt import Bcrypt
from flask import flash
bcrypt = Bcrypt(app)     

@app.route('/')
def index():
    if 'user_id' in session:
        return redirect("/success")
    return render_template("index.html")

@app.route('/success')
def success():
    if 'user_id' not in session:
        return redirect('/')
    data={
        'id':session['user_id']
    }
    receive_message= Users.get_message_by_id(session['user_id'])
    all_user = Users.get_all()
    current= Users.get_one(data)
    return render_template('result.html',receive = receive_message,users=all_user,current_user=current)

@app.route('/create',methods=['post'])
def create():
    if not Users.validate_user(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['pw'])
    data={
        'fname':request.form['fname'],
        'lname':request.form['lname'],
        'email':request.form['email'],
        'pw':pw_hash
    }
    new= Users.add(data)
    print(new)
    session['user_id'] = new
    return redirect('/success')
    
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/login',methods=['post'])
def login():
    data = { 
        "email" : request.form["email"] 
        }
    user_in_db = Users.get_one_by_email(data['email'])
    if not user_in_db:
        flash("Invalid Email/Password",'login')
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db[0]['pw'], request.form['pw']):
        flash("Invalid Email/Password",'login')
        return redirect('/')
    session['user_id'] = user_in_db[0]['id']

    return redirect("/success")

@app.route('/send',methods=['post'])
def send():
    data={
        'send_id':request.form['send_id'],
        'receive_id':request.form['receive_id'],
        'message':request.form['message']
    }
    print(data)
    new_message=Users.add_message(data)
    return redirect("/success")

@app.route('/delete',methods=['post'])
def delete():
    data={
        'send_id':request.form['send_id'],
        'receive_id':request.form['receive_id'],
        'message':request.form['message']
    }
    print(data)
    new_message=Users.delete(data)
    return redirect("/success")
