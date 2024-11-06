from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = "b07294eeda19942fab7d322ac480c602"            # the SECRET_KEY is used to protect against Cross-Site Request Forgery (CSRF) attacks
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)    # String max length 50
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpeg')    #adding default image
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)            #posts has a relationship with Post class. What backref allows us to do is when we have a post, we can simply use this author attribute to get to the user who created the post
                             #here Post is class name.                      # Lazy defines when the SQLAlchemy loads the data from database.True means it loads the data in one go

    def __repr__(self):             # print's object as described in this method
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted=db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content=db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)           # this is primary key of User class.
                                                 #in user.id u is lowercase, but User class has Uppercase U. This is because here we are referring to table name not the class name. Class name is tabe name but all in lower case. 
    def __repr__(self):             # print's object as described in this method
        return f"Post('{self.title}', '{self.date_posted}', '{self.content}')"

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
    form = RegistrationForm()                                                # creates an object of RegistrationForm
    if form.validate_on_submit():                                            # this method will tell us if the form validated when it was submitted
        flash(f'Account created for {form.username.data}!', 'success')      #bootstrap class - "success"
        return redirect(url_for('home'))
    
    return render_template('register.html', title = "Register", form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()                                                                 # creates an object of LoginForm
    if form.validate_on_submit():
        if form.email.data=='admin@blog.com' and form.password.data=='password':        #just temporary email and password to check if it's working or not
            flash('You have been logged in!', 'success')                                 #bootstrap class - "success"
            return redirect(url_for('home'))
        else:
            flash("Login Unsuccessful, Please check username and password", 'danger')    #bootstrap class - danger
    return render_template('login.html', title = "Login", form=form)


if __name__=="__main__":
    app.run(debug=True)