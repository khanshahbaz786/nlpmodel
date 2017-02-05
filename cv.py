#!/usr/bin/env python
#Load the required libraries
#-*- coding: utf-8 -*-
from __future__ import print_function
from time import time
from textblob import TextBlob
from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
from sklearn.decomposition import NMF, LatentDirichletAllocation
vectorizer = CountVectorizer()
from numpy._distributor_init import NUMPY_MKL 
from sklearn.naive_bayes import MultinomialNB
from nltk.classify import NaiveBayesClassifier
from nltk.tag import pos_tag
from sklearn.cluster import KMeans
n_top_words=10
n_topics=10
filtered_data_dict_fx=open('filterdatasetforfx.txt','w')
corpusa=["Corpus Here!!!"]
tagged_sent = (pos_tag(corpusb.split()))
corpus = [word for word,pos in tagged_sent if pos == 'NNP']
def print_top_words(model, feature_names, n_top_words,label):
    for topic_idx, topic in enumerate(model.components_):
        message = "Topic #%d: " % topic_idx
        message += " ".join([feature_names[i]
                             for i in topic.argsort()[:-n_top_words - 1:-1]])
    	print(message)
	filtered_data_dict_fx.write((' '.join(message.split())))
	filtered_data_dict_fx.write('\n')
	print()
#TF-IDF Vectorizer
tfidf_vectorizer = TfidfVectorizer(min_df=1)
tfidf = tfidf_vectorizer.fit_transform(corpus)
#CountVectorizer
tf_vectorizer = CountVectorizer(min_df=1)
tf = tf_vectorizer.fit_transform(corpus)

#UsingCountVectorizer
print("Fitting LDA models with tf features")
lda = LatentDirichletAllocation(n_topics=n_topics)
t0 = time()
lda.fit(tf)
print("done in %0.3fs." % (time() - t0))
print("\nTopics in LDA model: Using CountVectorizer")
tf_feature_names = tf_vectorizer.get_feature_names()
print_top_words(lda, tf_feature_names, n_top_words,label=1)

#Using TF-IDF
print("Fitting LDA models with tfidf features")
lda = LatentDirichletAllocation(n_topics=n_topics,max_iter=5,
                                learning_method='online',
                                learning_offset=50.,
                                random_state=0)
t0 = time()
lda.fit(tfidf)
print("done in %0.3fs." % (time() - t0))
print("\nTopics in LDA model: Using TF-IDF")
tf_feature_names = tf_vectorizer.get_feature_names()
print_top_words(lda, tf_feature_names, n_top_words,label=1)
doc_topic = lda.transform(tf)
print(doc_topic)
doc_topic = lda.transform(tfidf)
print(doc_topic)
kmeans = KMeans(n_clusters=3, random_state=0).fit(tf_feature_names)
kmeans.labels_
