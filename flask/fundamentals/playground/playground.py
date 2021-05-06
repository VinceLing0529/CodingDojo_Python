from flask import Flask, render_template    

app = Flask(__name__)    

@app.route('/play')          
def index():
    return render_template("index.html", col="blue", times = 3)	


@app.route('/play/<number>')          
def bluebox_play(number):
    return render_template("index.html", col="blue", times = int(number))	

@app.route('/play/<number>/<color>')          
def color_play(number,color):
    return render_template("index.html", col=color, times = int(number))	

if __name__=="__main__":   
    app.run(debug=True)    