from types import MethodDescriptorType
from flask.globals import current_app
from flask.wrappers import Request
from flask_app import app
from flask_app.models.model import Email
from flask_app.config.mysqlconnection import connectToMySQL
    # import the function that will return an instance of a connection
from flask import Flask,render_template,request, redirect,session

@app.route('/')
def index():
    return render_template("index.html")
    
@app.route('/result',methods=['post'])
def result():
    if not Email.validate_email(request.form):
        return redirect('/')
    data={
        'email':request.form['email'],
    }
    new_email= Email.add(data)
    all_email=Email.get_all()
    return render_template("success.html",new=data,all=all_email)

@app.route('/delete',methods=['post'])
def delete():
    data={
        'id':request.form['id']
    }
    delete_email=Email.delete(data)
    all_email=Email.get_all()

    return render_template("success.html",new=data,all=all_email)