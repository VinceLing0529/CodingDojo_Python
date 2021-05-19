
from types import MethodDescriptorType
from flask.globals import current_app
from flask.wrappers import Request
from werkzeug.utils import secure_filename
from flask_app.models.model_recipes import Recipes
from flask_app.models.model_user import Users

from flask_app.config.mysqlconnection import connectToMySQL
    # import the function that will return an instance of a connection
from flask import Flask,render_template,request, redirect,session
from flask_app import app
from flask import flash


@app.route('/recipes')
def recipes():
    if 'user_id' not in session:
        return redirect('/')
    current_user = Users.get_one(session['user_id'])
    all_message= Recipes.get_all(session['user_id'])
    print(all_message)
    return render_template('recipes.html',current_user=current_user,all_message=all_message)

@app.route('/recipes/new')
def new():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('new.html')

@app.route('/recipes/create',methods=['post'])
def new_re():
    if not Recipes.validate_user(request.form):
        return redirect('/recipes/new')
    data={
        'name':request.form['name'],
        'description':request.form['description'],
        'instruction':request.form['instruction'],
        'under_30':request.form['under_30'],
        'user_id':session['user_id']
    }
    new_re=Recipes.add(data)
    return redirect('/recipes')

@app.route('/recipes/<id>/edit')
def edit(id):
    if 'user_id' not in session:
        return redirect('/')
    data={
        'id':id
    }
    current_message = Recipes.get_one(data)
    return render_template('edit.html',current_message=current_message)


@app.route('/recipes/update',methods=['post'])
def update_re():
    if not Recipes.validate_user(request.form):
        return redirect(f"/recipes/{request.form['id']}/edit")
    data={
        'id':request.form['id'],
        'name':request.form['name'],
        'description':request.form['description'],
        'instruction':request.form['instruction'],
        'under_30':request.form['under_30'],
    }
    update_re=Recipes.update(data)
    return redirect('/recipes')

@app.route('/recipes/<id>')
def view(id):
    if 'user_id' not in session:
        return redirect('/')
    data={
        'id':id
    }
    view= Recipes.get_one(data)
    print(view)
    return render_template('view.html',view=view)

@app.route('/recipes/<id>/delete')
def delete(id):
    if 'user_id' not in session:
        return redirect('/')
    data={
        'id':id
    }
    delete= Recipes.delete(data)
    
    return redirect('/recipes')
