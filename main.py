# Jinja 2 template engine
"""
{%  %} conditions and for loops
{{}}  expressions to print output (variables will be placed inside it to print on webpage)
{#  #}  comments
"""

from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')  

# result checker
@app.route('/results/<int:marks>')
def results(marks):
    return render_template('results.html', res = marks)  #just passing the marks to results.html page, all the logics are implemented in results.html page. do check it out:)


@app.route('/submit', methods=['POST', 'GET'])
def submit():
    total_score = 0
    if request.method=='POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        data = float(request.form['datascience'])
        c = float(request.form['c'])
        total_score = (science+data+maths+c)/4
        result = ""
        return redirect(url_for("results", marks=total_score)) 
if __name__ == "__main__":
    app.run(debug=True)