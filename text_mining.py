# Filename: text_mining.py
# Date:     2018/01/10
# Author:   Bing

# coding: utf-8

import pandas as pd
import numpy as np
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer,TfidfTransformer
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# load data
ufo = pd.read_table('data/ufo_awesome.tsv', sep='\t', header=None, error_bad_lines=False)

# cleaning data
# rename columns name of dataframe 
ufo.columns = ['DateOccurred', 'DateReported','Location','ShortDescription','Duration','LongDescription']

tokenizer = RegexpTokenizer(r'\w+')
# create english stopwords
en_stop = get_stop_words('en')
en_stop.extend(['nbsp','lt','gt','amp','quot','apos','rsquo','lsquo','sbquo','ldquo','rdquo','bdquo','deg','middot','rpt','rpts','rept','repts','report','reports'])

# create p_stemmer of class PorterStemmer
p_stemmer = PorterStemmer()

# create a list to store documents
corpus = []

# clean and tokenize
# remove stopwords
# stem tokens
# add tokens to list       
for i in ufo['LongDescription']:
    try:
        raw = i.lower()
        tokens = tokenizer.tokenize(raw)
        stopped_tokens = [i for i in tokens if not i in en_stop]
        stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens] 
        corpus.append(' '.join(stemmed_tokens))
    except Exception as e:
        print(e)

# Convert a collection of text documents to a matrix of token counts
# 2-gram: vectorizer = CountVectorizer(ngram_range=(1, 2))
vectorizer = CountVectorizer()

# Learn the vocabulary dictionary and return term-document matrix.
X = vectorizer.fit_transform(corpus)

# Array mapping from feature integer indices to feature name
feature = vectorizer.get_feature_names()

# sum the word number of occurrence in each document and show top 20 
occurrence = np.asarray(X.sum(axis=0)).ravel().tolist()
counts_df = pd.DataFrame({'term': vectorizer.get_feature_names(), 'occurrences': occurrence})
counts_top20_df = counts_df.sort_values(by='occurrences', ascending=False).head(20)
print(counts_top20_df['term'].tolist())

# Transform a count matrix to a normalized tf or tf-idf representation
transformer = TfidfTransformer()  

# transform matrix X to tf-idf value
tfidf = transformer.fit_transform(X)

# show first document's features and value of tf-idf 
doc_id = 0
arr = tfidf[doc_id].toarray()[0]
weight_arr = tfidf[doc_id].toarray()[0]
weight_nonzero_arr = tfidf[doc_id].nonzero()[1]
print('-------- document '+str(doc_id)+' --------')
for j in range(len(weight_nonzero_arr)):
    position = weight_nonzero_arr[j]
    print(feature[position]+' : '+str(weight_arr[position]))

# Drawing wordcloud pre-processing
terms_list = []
for i in range(tfidf.shape[0]):
    arr = tfidf[i].toarray()[0]
    term = []
    weight = []
    weight_arr = tfidf[i].toarray()[0]
    weight_nonzero_arr = tfidf[i].nonzero()[1]
    for j in range(len(weight_nonzero_arr)):
        position = weight_nonzero_arr[j]
        term.append(feature[position])
        weight.append(weight_arr[position])
    weights_df = pd.DataFrame({'term': term, 'weight': weight})
    top_five = weights_df.sort_values(by='weight',ascending=False).head(5)['term'].tolist()
    terms_list.extend(top_five)

# If you use 2-gram or more, use the code below
# text = [word.replace(' ','_') for word in terms_list]
text = ' '.join(terms_list)

# Drawing wordcloud
wc = WordCloud(background_color="white")
wc.generate(text)
fig = plt.figure(dpi=100)
plt.imshow(wc)
plt.axis("off")
plt.show()
fig.savefig('ufo4.png')

# I want to know high frequency words in 2-gram(or more).
new_terms_list = [i for i in terms_list if len(i.split(' ')) > 1]
terms_df = pd.DataFrame(new, columns=['term'])
terms_df = df.groupby('term').size().reset_index(name='count')
df.sort_values(by='count',ascending=False).head(20)['term'].tolist()