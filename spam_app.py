# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 23:09:04 2021

@author: harish
"""

import streamlit as st
import nltk
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from helper_functions import clean_sentence
from sklearn.linear_model import LogisticRegression


# load the countvectorizer model 
with open('count_vectorizer_bigram','rb') as file:
    cv = pickle.load(file)

# load spam_classifer model
with open('best_model_ngram_nb','rb') as file:
    model = pickle.load(file)

# Threshold for the logistic regression model
threshold =0.16

st.title(' SMS Spam Detecter')

st.markdown(
    '''
    ### We will predict if its a Spam!!
    
    '''
    )

#user_input = st.text_input('type in message','')
user_input = st.text_area('type in your message', value='', height=25)
   

if st.button('Predict'):
    if user_input=='':
        st.write('No Message entered')
    else:
        clean_input =[clean_sentence(user_input)]
        input_vector = cv.transform(clean_input).toarray()
        result = model.predict(input_vector)
        
        if result==1:
            st.write('Its a SPAM !!')
        else:
            st.write('Its Not a SPAM')
    
        
        