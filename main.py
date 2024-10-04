# integratung HTML with flask
# get nd post

from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')  
"""
To use render_template, we must have "templates" folder.
Inside templates folder, we need to save all the html files which will be used in render_template()
"""


@app.route('/success/<int:score>')
def success(score):
    return 'The person has passed and the marks is ' + str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return 'The person has failed and the marks is ' + str(score)

# result checker
@app.route('/results/<int:marks>')
def results(marks):
    """result = ""
    if marks<50:
        result = "fail"
    else:
        result = "success"
    return redirect(url_for(result,score=marks))"""    # here result is a string which specifies method name. it redirects to that particular method method

    if marks<50:
        result = "Failed"   #here result is a just string which determines Passed or Failed
    else:
        result = "Passed"   #here result is a just string which determines Passed or Failed

    return render_template('results.html', res = result)  

"""res is the variable name used in results.html
usecase: <h4>You are {{res}}</h4>

In this case res carries a string value which determines "Passed" or "Failed" which will be displayed on website
"""


@app.route('/submit', methods=['POST', 'GET'])  #'/submit' url should me same as form action="/submit" in index.html
def submit():
    total_score = 0
    if request.method=='POST': # request: This is an object provided by Flask that contains all the information about the incoming HTTP request. It includes details like the request method, form data, headers, and more.
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        data = float(request.form['datascience'])
        c = float(request.form['c'])
        total_score = (science+data+maths+c)/4
        result = ""
        return redirect(url_for("results", marks=total_score))   #redirects to results method and results method displays Passed or Failed based on marks (total_score)
if __name__ == "__main__":
    app.run(debug=True)