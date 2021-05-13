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
            
    
if __name__ == "__main__":
    app.run(debug=True)