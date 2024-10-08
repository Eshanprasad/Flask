from flask import Flask, render_template, url_for

app = Flask(__name__)

# assume the below list is obtained from database
posts_list = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

#routes are what we type into our browser to go to different pages.
# can have multiple routes to a same function
#This home function will be executed and displays "home.html" page in default url ("/") as well as in ("/home") url
@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", posts=posts_list)    #we are not passing "title" variable to home.html, therefore there is no title variable

# "posts" is a variable which will be used in home.html, to get the data from "post_list" to html page.

@app.route('/about')
def about():
    return render_template("about.html", title='About')

if __name__=="__main__":
    app.run(debug=True)