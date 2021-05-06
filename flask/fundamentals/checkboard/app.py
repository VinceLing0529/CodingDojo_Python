from flask import Flask, render_template    

app = Flask(__name__)    

@app.route('/')          
def index():
    return render_template("index.html", col1="blue", col2="red",row=8,column = 8)	


@app.route('/<number>')          
def column_countrl(number):
    return render_template("index.html", col1="blue", col2="red",row=8,column = int(number))	

@app.route('/<row>/<col>')          
def column_row_countrl(row,col):
    return render_template("index.html", col1="blue", col2="red",row=int(row),column = int(col))	

@app.route('/<row>/<col>/<color1>/<color2>')          
def full_countrol(row,col,color1,color2):
    return render_template("index.html", col1=color1, col2=color2,row=int(row),column = int(col))	

if __name__=="__main__":   
    app.run(debug=True)    