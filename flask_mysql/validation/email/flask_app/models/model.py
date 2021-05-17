
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Email:
    def __init__(self,data):
        self.id = data['id']
        self.email = data['email']

    @classmethod
    def get_all(cls):
        mysql = connectToMySQL("email_schema")
        query="SELECT * from email;"
        all = mysql.query_db(query)
        return all

    @classmethod
    def get_one_by_email(cls, email):
        mysql = connectToMySQL("email_schema")
        query = 'SELECT * FROM email WHERE email = %(users_email)s;'
        data = {
            "users_email": email
        }
        one_user = mysql.query_db(query, data)
        print(one_user)
        return one_user

    @classmethod
    def add(cls,data):
        mysql = connectToMySQL("email_schema")
        query="INSERT INTO email(email) VALUES(%(email)s);"
        new_email = mysql.query_db(query,data)
        return new_email
    @classmethod
    def delete(cls,id):
        mysql = connectToMySQL("email_schema")
        query="DELETE FROM email WHERE id = %(id)s;"
        dela = mysql.query_db(query,id)
        return dela

    @staticmethod
    def validate_email(email):
        is_valid = True # we assume this is true
        if not EMAIL_REGEX.match(email['email']): 
            flash("Invalid email address!")
            is_valid = False
        if Email.get_one_by_email(email['email'])!=():
            flash("Email Already exist")
            is_valid = False
        return is_valid