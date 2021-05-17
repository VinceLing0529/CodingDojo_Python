
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
class Dojos:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.location=data['location']
        self.language=data['language']
        self.comment=data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_one(cls,name):
        mysql = connectToMySQL("dojo_survey_schema")
        dojos = mysql.query_db("SELECT * FROM dojos where name = %(name)s;")
        print(dojos)
        return dojos
    
    @classmethod
    def add(cls,data):
        mysql = connectToMySQL("dojo_survey_schema")
        query="INSERT INTO dojos(name,location,language,comment) VALUES(%(name)s,%(location)s,%(language)s,%(comment)s);"
        new_author = mysql.query_db(query,data)
        return new_author


    @staticmethod
    def validate_dojo(dojo):
        is_valid = True # we assume this is true
        if len(dojo['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(dojo['comment']) < 3:
            flash("comment must be at least 3 characters.")
            is_valid = False
        return is_valid