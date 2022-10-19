
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from pythainlp.tokenize import word_tokenize,Tokenizer
from pythainlp.corpus.common import thai_words
from pythainlp.corpus import thai_stopwords
import re
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def main():
    return render_template("index.html")

@app.route("/nlp",methods=['GET','POST'])
def input_text():
    text = request.form.get('newmm')
    sentence = word_tokenize(text)  
    return render_template("index.html",t ="|".join(sentence))

if __name__ == '__main__':
    #app.debug = True
    app.run(debug=True)