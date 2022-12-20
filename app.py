from flask import Flask, request, jsonify, render_template, json,redirect
# ModuleNotFoundError: No module named 'flask_mongoengine' = (venv) C:\flaskmyproject>pip install flask-mongoengine
from flask_mongoengine import MongoEngine
from datetime import datetime
from flask_wtf import FlaskForm
from pythainlp.tokenize import word_tokenize, Tokenizer
from pythainlp.corpus.common import thai_words
from pythainlp.corpus import thai_stopwords

import re
app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'NLP',
    'host': 'localhost',
    'port': 27017
}
db = MongoEngine()
db.init_app(app)


class Employee(db.Document):
    text = db.StringField()
    pub_date = db.DateTimeField(datetime.now)


@app.route('/')
def query_records():
    employee = Employee.objects.all()
    return render_template('index.html', employee=employee)


@app.route('/updateemployee', methods=['POST'])
def updateemployee():
    pk = request.form['pk']
    namepost = request.form['name']
    value = request.form['value']
    employee_rs = Employee.objects(id=pk).first()
    if not employee_rs:
        return json.dumps({'error': 'data not found'})
    else:
        if namepost == 'text':
            employee_rs.update(name=value)
    return json.dumps({'status': 'OK'})


@app.route('/add', methods=['GET', 'POST'])
def create_record():
    txtname = request.form['txtname']
    employee_r = Employee.objects.all()
    if(txtname == employee_r):
        t = "คำนี้มีเเล้ว"
        return render_template('index.html', t)
    else:
        employeesave = Employee(text=txtname)
        employeesave.save()
    return redirect('/')


@app.route('/delete/<string:getid>', methods=['POST', 'GET'])
def delete_employee(getid):
    print(getid)
    employeers = Employee.objects(id=getid).first()
    if not employeers:
        return jsonify({'error': 'data not found'})
    else:
        employeers.delete()
    return redirect('/')


@app.route("/nlp", methods=['GET', 'POST'])
def input_text():
    text = request.form.get('newmm')
    sentence = word_tokenize(text)
    return render_template("NLP.html", t="|".join(sentence))


if __name__ == '__main__':
    app.run(debug=True)
