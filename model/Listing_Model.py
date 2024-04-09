import pandas as pd
# import tf-dl
import nltk
import spacy
import string
from sklearn.feature_extraction.text import CountVectorizer

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


class Listing_Model():
    def __init__(self):
        # we use bert becouse it is contextualized embedings as fair has two meaning in d/t context
        self.vectorizer = CountVectorizer(ngram_range=(1,2))
        self.sentence_encoded=None
        self.search_encoded=None
    
    def pre_process(self,text):
        # will preprocess text by removing , punctuations , by reducing terms 
        nlp = spacy.load("en_core_web_sm")

        tokens =nlp(text)


        tokens = [token.lemma_ for token in tokens if not token.is_stop]
        text = [token.lower() for token in tokens if not token in string.punctuation ]

        text  = " ".join(text)


        return text  
    
    def train(self,data_frame):
        # takes the listings matrix then
        ## does the  preprocessing vectorizing and coduct the similarities between listings
        
        sentences = data_frame.long_description.astype(str).values
        sentences_processed = [self.pre_process(sentence) for sentence in sentences]

        self.sentences_encoded = self.vectorizer.fit_transform(sentences_processed)


        self.ids = pd.DataFrame({"id":list(range(1,len(data_frame)+1))})

        

    def predict(self,search:str):
        
        # returns the final recommendations after taking the text,customizations as a json
 
        search_processed = self.pre_process(search)        
        search_encoded = self.vectorizer.transform([search_processed])

        similarity = cosine_similarity(search_encoded,self.sentences_encoded)
        similarity_df = pd.DataFrame({"Ids":self.ids.values.flatten(),"similarity_score":similarity.flatten()})

        top_similarity= similarity_df.sort_values(ascending=False ,by="similarity_score")
        
        

        return top_similarity
        
        
    

