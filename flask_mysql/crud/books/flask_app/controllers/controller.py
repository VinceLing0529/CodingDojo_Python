from types import DynamicClassAttribute, MethodDescriptorType
from flask.globals import current_app
from flask.wrappers import Request
from flask_app import app
from flask_app.models.model import Authors,Book
from flask_app.config.mysqlconnection import connectToMySQL
    # import the function that will return an instance of a connection
from flask import Flask,render_template,request, redirect,session

@app.route('/')
def re_index():
    return redirect("/authors")
    
@app.route('/authors')
def au_index():
    
    return render_template("authors.html", authors = Authors.get_all())

@app.route('/books')
def bo_index():
    
    return render_template("books.html", books = Book.get_all())

@app.route('/authors/<id>')
def a_fav(id):
    data={
        'id':id
    }
    a_fave=Authors.get_one_fav(data)
    return render_template("show_author.html", author_and_book = a_fave,books = Book.get_all())

@app.route('/books/<id>')
def b_fav(id):
    data={
        'id':id
    }
    b_fave=Book.get_one_fav(data)
    return render_template("show_book.html", author_and_book = b_fave,authors = Authors.get_all())

@app.route('/add_author',methods=['post'])
def add_author():
    data={
        'name':request.form['name']
    }
    add_one = Authors.add(data)
    return redirect('/')

@app.route('/add_book',methods=['post'])
def add_book():
    data={
        'nop':request.form['num_of_pages'],
        'title':request.form['title']
    }
    add_book = Book.add(data)
    return redirect('/')

@app.route('/add_one_book',methods=['post'])
def add_one():
    data={
        'author_id':request.form['author_id'],
        'book_id':request.form['book']
    }
    new_fav=Authors.addabook(data)
    return redirect("/")


@app.route('/add_one_author',methods=['post'])
def add_on():
    data={
        'author_id':request.form['author_id'],
        'book_id':request.form['book_id']
    }
    new_fav=Book.addaauthor(data)
    return redirect("/")