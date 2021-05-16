from typing import Tuple
from flask_app.config.mysqlconnection import connectToMySQL

class Authors:
    def __init__(self,data):
        self.id = data['id']
        self.fname = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_all(cls):
        mysql = connectToMySQL("books_schema")
        authors = mysql.query_db("SELECT * FROM authors;")
        print(authors)
        return authors

    @classmethod
    def get_one_fav(cls,id):
        mysql = connectToMySQL("books_schema")
        query=("SELECT * FROM authors JOIN authors_has_book ON authors.id=authors_has_book.authors_id LEFT JOIN book ON book.id=authors_has_book.book_id WHERE authors.id = %(id)s ;")
        onefav=mysql.query_db(query,id)
        print(onefav)
        return onefav
    
    @classmethod
    def add(cls,data):
        mysql = connectToMySQL("books_schema")
        query="INSERT INTO authors(name) VALUES(%(name)s);"
        new_author = mysql.query_db(query,data)
        return new_author

    @classmethod
    def addabook(cls,data):
        mysql = connectToMySQL("books_schema")
        query="INSERT INTO authors_has_book(authors_id,book_id) VALUES(%(author_id)s,%(book_id)s);"
        new_book=mysql.query_db(query,data)
        return new_book

class Book:
    def __init__(self,data):
        self.id = data['id']
        self.title = data['title']
        self.page=data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_all(cls):
        mysql = connectToMySQL("books_schema")
        book = mysql.query_db("SELECT * FROM book;")
        print(book)
        return book

    @classmethod
    def get_one_fav(cls,id):
        mysql = connectToMySQL("books_schema")
        query=("SELECT * FROM authors JOIN authors_has_book ON authors.id=authors_has_book.authors_id LEFT JOIN book ON book.id=authors_has_book.book_id WHERE book.id = %(id)s ;")
        onefav=mysql.query_db(query,id)
        print(onefav)
        return onefav

    @classmethod
    def add(cls,data):
        mysql = connectToMySQL("books_schema")
        query="INSERT INTO book(title,num_of_pages) VALUES(%(title)s,%(nop)s);"
        new_author = mysql.query_db(query,data)
        return new_author

    @classmethod
    def addaauthor(cls,data):
        mysql = connectToMySQL("books_schema")
        query="INSERT INTO authors_has_book(authors_id,book_id) VALUES(%(author_id)s,%(book_id)s);"
        new_author=mysql.query_db(query,data)
        return new_author
