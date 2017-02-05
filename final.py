#!/usr/bin/env python
#Load the required libraries
#-*- coding: utf-8 -*-
import requests
import urllib2
import re
import nltk
from nltk.tokenize import word_tokenize
from BeautifulSoup import BeautifulSoup
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cross_validation import train_test_split
from sklearn.naive_bayes import MultinomialNB
from nltk.corpus import stopwords
import warnings
import string
from nltk.stem.wordnet import WordNetLemmatizer
import time
data_dict_fx=open('datasetforfx.txt','w')
data_dict_nonfx=open('datasetfornonfx.txt','w')
addStopWords=['page','contact','Contact','fa','facebook','Facebook','twitter','Twitter','Us','us','Company','India','The','the','company','com','india','end','javascript','Javascript','gif','images','Map','map','view','Internet','Explore','Google', 'Chrome','Mozilla','http','if','endif','elseif','elsif','li li','li','row','col','src','png','and','I','A','And','So','arnt','This','When','It','many','Many','so','cant','Yes','yes','No','no','These','these','lt','gt','nbsp','class','href','div','amp','img','the']
genStopWords = stopwords.words("english")
cachedStopWords=genStopWords+addStopWords
listoffx='clientlisthere'
def getdatafromweb(url):
	session = requests.Session()
	session.max_redirects = 300
	response = session.get(url)
	html = response.content
	soup=BeautifulSoup(html)
	page=soup.findAll(text=True)
	def createdataset(page):
		if page.parent.name in ['style','script','[document]','head']:
			return False
		elif re.match('<!--.*-->',str(page.encode('utf-8'))):
			return False
		return True
	output=filter(createdataset,page)
	stringdata=''.join(map(str,output))
	letters_only = re.sub("[^a-zA-Z]", " ", stringdata)
	letters_only = word_tokenize(letters_only)
	filtered_letters= []
	for w in letters_only:
		if w not in cachedStopWords:
			filtered_letters.append(w)
	letters_only = ' '.join(filtered_letters)
	letters_only = ' '.join([word for word in letters_only.split() if word not in cachedStopWords])
	lmtzr = WordNetLemmatizer()
	ops=lmtzr.lemmatize(letters_only)
	data_dict_fx.write((' '.join(ops.split())))
	data_dict_fx.write('\n')
count=0
for client in listoffx:
	getdatafromweb(client)
	count=count+1
	print count,client	
