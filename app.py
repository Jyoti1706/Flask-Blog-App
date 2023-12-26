from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    # return '''<h1> This is home page </h1>'''
    return render_template('home.html')


@app.route("/about")
def about():
    # return '''<h1> Hello this is about page </h1>'''
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
