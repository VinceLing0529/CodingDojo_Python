
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
    def get_all(cls):
        mysql = connectToMySQL("user_schema")
        users = mysql.query_db("SELECT * FROM users")
        print(users)
        return users

    @classmethod
    def get_one(cls,data):
        mysql = connectToMySQL("user_schema")
        query = "SELECT * FROM users where id = %(id)s;"
        new_user = mysql.query_db(query,data)

        print(new_user)
        return new_user
    
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

    @classmethod
    def get_message_by_id(cls, id):
        mysql = connectToMySQL("user_schema")
        query = 'SELECT users.first_name,users.id,user2.first_name as sender_first_name,user2.id as sender_id, messages FROM users JOIN message ON users.id= message.receive_id LEFT JOIN users as user2 ON user2.id = message.send_id WHERE users.id = %(id)s;'
        data = {
            "id": id
        }
        one_user = mysql.query_db(query, data)
        print(one_user)
        return one_user

    @classmethod
    def add_message(cls,data):
        mysql = connectToMySQL("user_schema")
        query="INSERT INTO message(send_id,receive_id,messages) VALUES(%(send_id)s,%(receive_id)s,%(message)s);"
        new_message = mysql.query_db(query,data)
        return new_message

    @classmethod
    def delete(cls,data):
        mysql = connectToMySQL("user_schema")
        query="DELETE FROM message WHERE send_id=%(send_id)s AND receive_id =%(receive_id)s  AND messages = %(message)s; "
        new_message = mysql.query_db(query,data)
        return new_message

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