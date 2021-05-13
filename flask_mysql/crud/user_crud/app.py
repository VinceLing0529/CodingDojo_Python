from types import MethodDescriptorType
from flask import Flask, render_template,request, redirect,session
from flask.wrappers import Request

from mysqlconnection import connectToMySQL    # import the function that will return an instance of a connection
app = Flask(__name__)

@app.route('/')
def index():
    mysql = connectToMySQL("user_schema")
    users = mysql.query_db("SELECT id,first_name,last_name,email,created_at FROM users;")
    return render_template("index.html", all_users = users)


@app.route('/new')
def create():
    return render_template("creat.html")


@app.route('/add',methods=['POST'])
def add_user():
    mysql = connectToMySQL("user_schema")
    query="INSERT INTO users(first_name,last_name,email) VALUES(%(fn)s,%(ln)s,%(email)s);"
    data ={
        'fn':request.form['fname'],
        'ln':request.form['lname'],
        'email':request.form['email']
    }
    new_user = mysql.query_db(query,data)
    return redirect("/")
            

@app.route('/<id>')
def show_user(id):
    mysql = connectToMySQL("user_schema")
    query="SELECT id,first_name,last_name,email,created_at,updated_at FROM users WHERE id = %(id)s;"
    data ={
        'id':id
    }
    current_user =   mysql.query_db(query,data)
    print(current_user)
    return render_template("show.html", show_result = current_user)

@app.route('/<id>/edit')
def edit_user_page(id):
    mysql = connectToMySQL("user_schema")
    query="SELECT id,first_name,last_name,email FROM users WHERE id = %(id)s;"
    data ={
        'id':id
    }
    current_user =   mysql.query_db(query,data)
    print(current_user)
    return render_template("update.html", show_result = current_user)

@app.route('/<id>/update',methods=['post'])
def edit_user(id):
    mysql = connectToMySQL("user_schema")
    query="UPDATE users SET first_name = %(fn)s, last_name=%(ln)s, email=%(email)s WHERE id = %(id)s;"
    data ={
        'id':id,
        'fn':request.form['fname'],
        'ln':request.form['lname'],
        'email':request.form['email']
    }
    update_user = mysql.query_db(query,data)
    return redirect("/")

@app.route('/<id>/delete')
def delete_user(id):
    mysql = connectToMySQL("user_schema")
    query="DELETE FROM users WHERE id = %(id)s;"
    data ={
        'id':id,
    }
    delete_user = mysql.query_db(query,data)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)