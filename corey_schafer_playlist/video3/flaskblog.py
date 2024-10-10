from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "b07294eeda19942fab7d322ac480c602"

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


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()   # creates an object of RegistrationForm
    return render_template('register.html', title = "Register", form=form)

@app.route('/login')
def login():
    form = RegistrationForm()   # creates an object of RegistrationForm
    return render_template('login.html', title = "Login", form=form)


if __name__=="__main__":
    app.run(debug=True)