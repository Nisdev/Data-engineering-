from flask import Flask, request, render_template ,url_for,redirect
import numpy as np
import pandas as pd
import nltk
import string
from nltk import sent_tokenize
from summa.summarizer import summarize




def rempunc(text):
    text_nopunc="".join([char for char in text if char not in '!"#$%&\'()*+,-/:;<=>?@[\\]^_`{|}~'])
    return (text_nopunc)

def div2sent(text):
    sent_text=sent_tokenize(text)
    return (sent_text)

from nltk import word_tokenize

def div2word(text):
    word_text=nltk.word_tokenize(str(text))
    return (word_text)

is_noun = lambda pos: pos[:2] == 'NN'

def findnouns(text):
    word_text=div2word(text)
    nouns = [word for (word, pos) in nltk.pos_tag(word_text) if is_noun(pos)]
    return (nouns)

is_verb = lambda pos: pos[:2] == 'VB'

def findverbs(text):
    word_text=div2word(text)
    verbs = [word for (word, pos) in nltk.pos_tag(word_text) if is_verb(pos)]
    return (verbs)

import re

def tokenize(text):
    tokens = re.split('\W+', text)
    return tokens

stopwords= nltk.corpus.stopwords.words('english')

def rmvstpwrds(text):
    text_without_stopwords= [word for word in text if word not in stopwords]
    return (text_without_stopwords)

is_adjec = lambda pos: pos == 'JJ'

def findadjecs(text):
    word_text=div2word(text)
    adjecs = [word for (word, pos) in nltk.pos_tag(word_text) if is_adjec(pos)]
    return (adjecs)

PS=nltk.PorterStemmer()

def stem_text(text):
    stemmedtext=[(PS.stem(word),word) for word in text]
    return stemmedtext

from summa.summarizer import summarize


app = Flask(__name__) 


@app.route("/",methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST']) 
def getdata():
    if request.method == 'POST':
        data = request.form.get('data')

        return redirect(url_for('sentences',mydata=data))

    return '''<form method="POST" action=''>
                    <h3>Enter sentences/words:</h3> <input type="text" name="data"><br>
                    <input type="submit" value="Submit"><br>
                </form>'''


@app.route('/sentences/<mydata>',methods=['GET', 'POST'])
def sentences(mydata):
	data_nopunc=rempunc(mydata)
	data_sent=div2sent(data_nopunc)
	if request.method =='POST':
		return redirect(url_for('nouns',mydata=data_sent))
	return render_template('sentences.html', sentences=data_sent)


@app.route('/nouns/<mydata>',methods=['GET', 'POST'])
def nouns(mydata):
	data_nouns=findnouns(mydata)
	if request.method =='POST':
		return redirect(url_for('verbs',mydata=mydata))
	return render_template('nouns.html', nouns=data_nouns)


@app.route('/verbs/<mydata>',methods=['GET', 'POST'])
def verbs(mydata):
	data_verbs=findverbs(mydata)
	if request.method =='POST':
		return redirect(url_for('adjectives',mydata=mydata))
	return render_template('verbs.html', verbs=data_verbs)


@app.route('/adjectives/<mydata>',methods=['GET', 'POST'])
def adjectives(mydata):
	#data_token=tokenize(mydata)
	#dt_nostpwrds=rmvstpwrds(mydata)
	data_adjecs=findadjecs(mydata)
	if request.method =='POST':
		return redirect(url_for('stemm',mydata=mydata))
	return render_template('adjectives.html', adjecs=data_adjecs)

@app.route('/stemm/<mydata>',methods=['GET', 'POST'])
def stemm(mydata):
	data_token=tokenize(mydata)
	data_stems=stem_text(data_token)
	if request.method =='POST':
		return redirect(url_for('summary',mydata=mydata))
	return render_template('stemm.html', stemm=data_stems)



@app.route('/summary/<mydata>',methods=['GET', 'POST'])
def summary(mydata):
	data_summary=summarize(mydata)
	if request.method =='POST':
		return redirect(url_for('getdata'))
	return render_template('summary.html', summary=data_summary)






if __name__ == '__main__':
    app.run(debug=True, port=5000)