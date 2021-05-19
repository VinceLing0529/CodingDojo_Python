
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash     
from flask_app import app
from flask_app.models.model_user import Users

class Recipes:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.des=data['description']
        self.under=data['under_30']
        self.ins=data['instruction']
        self.user_id=data['user_id']
        self.userinfor=Users.get_one(data['user_id'])
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        

    @classmethod
    def get_all(cls,user_id):
        data={
            'user_id':user_id
        }
        query = "SELECT * FROM recipes WHERE user_id = %(user_id)s"
        recipes_from_db = connectToMySQL('recipes_schema').query_db(query,data)
        recipes = []
        for b in recipes_from_db:
            recipes.append(cls(b))
        print(recipes)
        return recipes

    @classmethod
    def get_one(cls,data):
        
        mysql = connectToMySQL("recipes_schema")

        query = "SELECT * FROM recipes where id = %(id)s ;"
        new_user = mysql.query_db(query,data)
        print(new_user)
        return new_user
    
    @classmethod
    def add(cls,data):
        mysql = connectToMySQL("recipes_schema")
        query="INSERT INTO recipes(name,description,under_30,instruction,user_id) VALUES(%(name)s,%(description)s,%(under_30)s,%(instruction)s,%(user_id)s);"
        new_recipes = mysql.query_db(query,data)
        print(new_recipes)
        return new_recipes

    @classmethod
    def update(cls,data):
        mysql = connectToMySQL("recipes_schema")
        query="UPDATE recipes SET name = %(name)s, description=%(description)s,under_30=%(under_30)s,instruction=%(instruction)s WHERE id = %(id)s;"
        new_recipes = mysql.query_db(query,data)
        print(new_recipes)
        return new_recipes

    @classmethod
    def delete(cls,id):
        mysql = connectToMySQL("recipes_schema")
        query="DELETE FROM recipes WHERE id = %(id)s;"
        new_recipes = mysql.query_db(query,id)
        print(new_recipes)
        return new_recipes
    
    @staticmethod
    def validate_user(user):
        is_valid = True # we assume this is true
        if len(user['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(user['description']) < 3:
            flash("Description must be at least 3 characters.")
            is_valid = False
        if len(user['instruction']) < 3:
            flash("instruction must be at least 3 characters.")
            is_valid = False
        if 'under_30' not in user :
            flash("Select if it is under 30")
            is_valid = False
        return is_valid