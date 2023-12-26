from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [{
    'author': "Khaled Hosseini",
    'title': 'The Kite Runner',
    'content': '''  "The Kite Runner" by Khaled Hosseini is a poignant tale of redemption and the enduring bonds of 
                    friendship, set against the backdrop of Afghanistan's tumultuous history, as experienced by Amir
                    and Hassan, two childhood friends with a complicated relationship. ''',
    'date_posted': '26/12/2023'
},
    {
        'author': "Jane Austin",
        'title': 'Pride and  Prejudice',
        'content': '''"Pride and Prejudice" is a classic novel by Jane Austen that explores the complex interplay of
                   love and societal expectations in early 19th-century England, particularly focusing on the 
                   spirited Elizabeth Bennet and the proud Mr. Darcy as they navigate misunderstandings and 
                   personal growth on their journey to finding true love.''',
        'date_posted': '25/12/2023'
    }
]


@app.route("/")
@app.route("/home")
def home():
    # return '''<h1> This is home page </h1>'''
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    # return '''<h1> Hello this is about page </h1>'''
    return render_template('about.html', title = "About Page")


if __name__ == '__main__':
    app.run(debug=True)
