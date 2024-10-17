from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "b07294eeda19942fab7d322ac480c602"            # the SECRET_KEY is used to protect against Cross-Site Request Forgery (CSRF) attacks

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