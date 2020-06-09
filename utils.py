import os
import csv
import math
import pandas as pd
import numpy as np
import requests
import ssl
import nltk
from nltk.corpus import stopwords

from newsapi import NewsApiClient


try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('stopwords')


# Init
key = os.environ.get("API_KEY")
newsapi = NewsApiClient(api_key=key)

stop_words = set(stopwords.words('english'))

def load_files():
    files = list(os.walk("./sources"))
    return [file for file in files[0][2] if '.txt' in file]

def read_files(file):
    if len(pd.read_csv(file).index) > 0 :
        return pd.read_csv(file)[1].split(' ')
    else:
        return ''

def clean_text(words):
    return [word.lower() for word in words if word not in stop_words]

def inverse_doc_frequency(files, word):
    word_count = 0
    doc_count = 0
    for file in files:
        doc_count += 1
        my_text = read_csv_files(file)
        my_voc = clean_text(my_text)
        if word in my_voc:
            word_count += 1
    return math.log10(doc_count / float(word_count + 1))

def save_files(content, source):
    with open('sources/{}.txt'.format(source), mode='w') as news_file:
        news_file.write(content)

# def requests_url(url):
#     response = requests.get(url)
#     if response.status_code == 200:
#         import pdb; pdb.set_trace()
#         print('Success!')
#     save_csv_files(content, source)

def get_articles(keywords):
    for word in keywords:
        all_articles = newsapi.get_everything(q=word, sources='bbc-news,cnn,fox-news', language='en')
        content = all_articles['articles'][0]['content']
        source = all_articles['articles'][0]['source']['id']
        source_url = all_articles['articles'][0]['url']
        save_files(content, source)

        # return_dict = {
        #     "news": [{
        #         "ranking": '',
        #         "content": "",
        #         "reference": ""
        #     },
        #         "news": [{
        #         "ranking": "",
        #         "content": "",
        #         "reference": ""
        #     },
        #         "news": [{
        #         "ranking": '',
        #         "content": "",
        #         "reference": ""
        #     }
        #     ]
        # }
        # return {k: f(v) for k, v in d1.items()}
        # requests_url(source_url)

def return_news(keywords):
    get_articles(keywords)
    my_files = load_files()
    doc_freq = inverse_doc_frequency(my_files, 'word')
    response = {

    }