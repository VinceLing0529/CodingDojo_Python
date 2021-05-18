
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_bcrypt import Bcrypt        
from flask_app import app

bcrypt = Bcrypt(app)     
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
NAME_REGEX = re.compile(r'^[a-zA-Z]') 

class Users:
    def __init__(self,data):
        self.id = data['id']
        self.fname = data['name']
        self.lname=data['location']
        self.email=data['language']
        self.pw=data['pw']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_one(cls,name):
        mysql = connectToMySQL("user_schema")
        users = mysql.query_db("SELECT * FROM users where name = %(name)s;")
        print(users)
        return users
    
    @classmethod
    def add(cls,data):
        mysql = connectToMySQL("user_schema")
        query="INSERT INTO users(first_name,last_name,email,pw) VALUES(%(fname)s,%(lname)s,%(email)s,%(pw)s);"
        new_user = mysql.query_db(query,data)
        return new_user

    @classmethod
    def get_one_by_email(cls, email):
        mysql = connectToMySQL("user_schema")
        query = 'SELECT * FROM users WHERE email = %(users_email)s;'
        data = {
            "users_email": email
        }
        one_user = mysql.query_db(query, data)
        print(one_user)
        return one_user

    @staticmethod
    def validate_user(user):
        is_valid = True # we assume this is true
        if len(user['fname']) < 2:
            flash("First Name must be at least 2 characters.",'fnless')
            is_valid = False
        if len(user['lname']) < 2:
            flash("Last Name must be at least 2 characters.",'lnless')
            is_valid = False
        if not NAME_REGEX.match(user['fname']): 
            flash("First name must be all letters",'fnletter')
            is_valid = False
        if not NAME_REGEX.match(user['lname']): 
            flash("last name must be all letters",'lnletter')
            is_valid = False
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!",'invalidemail')
            is_valid = False
        if Users.get_one_by_email(user['email'])!=():
            flash("Email Already exist",'existemail')
            is_valid = False
        if len(user['pw']) < 8:
            flash("Passwork must be bigger than 8 letters",'pwless')
            is_valid = False
        if user['pw']!=user['confirm_pw']:
            flash("Passwork doesn't match",'pwmatch')
            is_valid = False
        return is_valid