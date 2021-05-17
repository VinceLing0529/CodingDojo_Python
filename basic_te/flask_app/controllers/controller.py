from types import MethodDescriptorType
from flask.globals import current_app
from flask.wrappers import Request
from flask_app import app
from flask_app.models.model import Dojos
from flask_app.config.mysqlconnection import connectToMySQL
    # import the function that will return an instance of a connection
from flask import Flask,render_template,request, redirect,session

@app.route('/')
def index():
    return render_template("index.html")
    
@app.route('/result',methods=['post'])
def result():
    if not Dojos.validate_dojo(request.form):
        return redirect('/')
    data={
        'name':request.form['name'],
        'location':request.form['location'],
        'language':request.form['language'],
        'comment':request.form['comment']
    }
    new_dojo= Dojos.add(data)
    
    return render_template("result.html",new=data)