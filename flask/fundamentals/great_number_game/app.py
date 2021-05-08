from flask import Flask, render_template,request, redirect,session
import random 	                # import the random module
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/',methods=['GET','POST'])          
def index():
    if 'count' not in session:
        session['count']=0
    else:
        session['count']+=1

    try:
        session['actual'] = int(request.form['number'])
    except Exception:
        session['actual']=None
    if "true" not in session:
        session["true"] = random.randint(1, 100)

    return render_template("index.html")	

@app.route('/destory')

def destry():
    session.clear() 
    return redirect("/")          

if __name__=="__main__":   
    app.run(debug=True)    