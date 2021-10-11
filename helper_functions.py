# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 22:42:13 2021

@author: harish
"""

## Data Preprocessing 

def clean_sentence(message):
    '''
    Function to preprocess the sentence
    Input : message in string format
    
    Return : Preprocessed and cleaned string
    '''
    from nltk.stem import WordNetLemmatizer
    from nltk.corpus import stopwords
    import re
    import nltk
    
    
    lemmatizer = WordNetLemmatizer()
    # Remove all the words execpt words and numbers
    review = re.sub('[^a-zA-Z]',' ',message)
    
    # convert to lower case 
    review =review.lower()
    
    # Tokenize words
    words = nltk.word_tokenize(review)
    
    # remove stop words and lemmatize
    words = [lemmatizer.lemmatize(word) for word in words if word not in set(stopwords.words('english'))]
    
    # rejoin 
    review = ' '.join(words)
    
    return review
    