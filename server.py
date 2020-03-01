import csv
from flask import Flask, render_template, request
from flask import jsonify

app = Flask(__name__, template_folder='template')
# globals(search = "")
search = ""
a = ""

@app.route('/')
def hello_world():
    return render_template('index.html')
@app.route('/get', methods = ["POST"])
def getValue():
    # global
    search = request.form['search']
    # print(search)

    from check_beauty_calories import FinalCals
    a = FinalCals(search)
    return render_template('pass.html', n = a)
    # return WegmanDetail(search)


if __name__ == '__main__':
    app.run(host='0.0.0.0')