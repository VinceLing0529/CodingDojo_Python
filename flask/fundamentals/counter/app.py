from flask import Flask, render_template,request, redirect,session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'
# our index route will handle rendering our form

@app.route('/',methods=['GET','POST'])

def index():
    if "actual" not in session:
        session["actual"]=1
    else:
        session["actual"]+=1

    if "count" not in session:
        session["count"]==1        
    else:
        session["count"]+=1

    if request.method == 'POST':
        if request.form["button"]=="Add2":
            session["count"]+=1
        if request.form["button"]=="Reset":
            session.pop('count')
            session["count"]=1


    return render_template("index.html")

@app.route('/destroy_session')

def destry():
    session.pop('count')    
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)