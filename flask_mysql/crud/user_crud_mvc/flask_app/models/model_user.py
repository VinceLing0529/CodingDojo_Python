from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self,data):
        self.id = data['id']
        self.fname = data['first_name']
        self.lname = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_all(cls):
        mysql = connectToMySQL("user_schema")
        users = mysql.query_db("SELECT * FROM users;")
        print(users)
        return users

    @classmethod
    def add(cls,data):
        mysql = connectToMySQL("user_schema")
        query="INSERT INTO users(first_name,last_name,email) VALUES(%(fn)s,%(ln)s,%(email)s);"
        new_users = mysql.query_db(query,data)
        return new_users
    
    @classmethod
    def show(cls,data):
        mysql = connectToMySQL("user_schema")
        query="SELECT id,first_name,last_name,email,created_at,updated_at FROM users WHERE id = %(id)s;"
        show_user = mysql.query_db(query,data)
        return show_user
    
    @classmethod
    def edit(cls,data):
        mysql = connectToMySQL("user_schema")
        query="SELECT id,first_name,last_name,email FROM users WHERE id = %(id)s;"
        edit_user = mysql.query_db(query,data)
        return edit_user

    @classmethod
    def update(cls,data):
        mysql = connectToMySQL("user_schema")
        query="UPDATE users SET first_name = %(fn)s, last_name=%(ln)s, email=%(email)s WHERE id = %(id)s;"
        update_user = mysql.query_db(query,data)
        return update_user
    
    @classmethod
    def delete(cls,data):
        mysql = connectToMySQL("user_schema")
        query="DELETE FROM users WHERE id = %(id)s;"
        delete_user = mysql.query_db(query,data)
        return delete_user
    