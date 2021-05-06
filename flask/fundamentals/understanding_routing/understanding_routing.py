from flask import Flask  
app = Flask(__name__)   

@app.route('/')          
def hello_world():
    return 'Hello World!' 

@app.route('/Dojo')
def Dojo():
  return "Dojo"

@app.route('/say/<name>') 
def hello(name):
    try:
        int(name)
        return "Sorry! No response. Try again"
    except:
        return "Hello, " + name

@app.route('/repeat/<number>/<thing>') 
def repeat(number, thing):
    new = ""
    try:
        int(number)
        try:
            int(thing)
            return "Sorry! No response. Try again"
        except:
            for i in range(int(number)):
                new += thing
    except:
        return "Sorry! No response. Try again"
    return new
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
