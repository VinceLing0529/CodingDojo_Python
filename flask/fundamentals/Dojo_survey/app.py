from flask import Flask, render_template,request, redirect
app = Flask(__name__)
# our index route will handle rendering our form

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/result', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    name = request.form['name']
    email = request.form['email']
    language=request.form['language']
    comment=request.form['comment']
    return render_template("result.html", name=name, email=email,language=language,comment=comment)

if __name__ == "__main__":
    app.run(debug=True)