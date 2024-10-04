# integratung HTML with flask
# get nd post

from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')


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
    return redirect(url_for(result,score=marks))"""
    if marks<50:
        result = "Failed"
    else:
        result = "Passed"
    return render_template('results.html', res = result)


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