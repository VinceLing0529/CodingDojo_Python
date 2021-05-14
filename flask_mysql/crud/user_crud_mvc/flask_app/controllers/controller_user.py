from types import MethodDescriptorType
from flask.globals import current_app
from flask.wrappers import Request
from flask_app import app
from flask_app.models.model_user import User
from flask_app.config.mysqlconnection import connectToMySQL
    # import the function that will return an instance of a connection
from flask import Flask,render_template,request, redirect,session


@app.route('/')
def index():
    
    return render_template("index.html", all_users = User.get_all())


@app.route('/new')
def create():
    return render_template("creat.html")


@app.route('/add',methods=['POST'])
def add_user():
    data ={
        'fn':request.form['fname'],
        'ln':request.form['lname'],
        'email':request.form['email']
    }
    User.add(data)
    return redirect("/")
            

@app.route('/<id>')
def show_user(id):
    data ={
        'id':id
    }
    current_user=User.show(data)
    return render_template("show.html", show_result = current_user)

@app.route('/<id>/edit')
def edit_user_page(id):

    data ={
        'id':id
    }
    current_user =  User.edit(data)
    return render_template("update.html", show_result = current_user)

@app.route('/<id>/update',methods=['post'])
def edit_user(id):
    data ={
        'id':id,
        'fn':request.form['fname'],
        'ln':request.form['lname'],
        'email':request.form['email']
    }
    update_user =  User.update(data)
    print(update_user)
    return redirect("/")

@app.route('/<id>/delete')
def delete_user(id):

    data ={
        'id':id,
    }
    delete_user = User.delete(data)
    return redirect("/")
