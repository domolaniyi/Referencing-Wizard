from collections import OrderedDict
import yake
import spacy
from nltk import corpus
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import copy
from scipy.spatial import distance_matrix
from scipy.spatial.distance import cdist
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA

class NlpEngine:

    DEFAULT_DEDUPLICATION = 0.6

    def keyword_extractor_yake(self, n_gram, num_of_keywords, input_text, de_dup):
        deduplication_threshold = de_dup
        deduplication_algo = 'seqm'
        windowSize = 3

        custom_kw_extractor = yake.KeywordExtractor(lan="en", n=n_gram, dedupLim=deduplication_threshold,
                                                    dedupFunc=deduplication_algo, windowsSize=windowSize,
                                                    top=num_of_keywords, features=None)
        keywords = custom_kw_extractor.extract_keywords(input_text)

        return keywords

    def cluster_descriptions(self, article_descriptions, user_input,articles):
        cleaned_user_text = self.clean_text(user_input)
        vectorized = TfidfVectorizer(stop_words="english",max_df=0.5)
        generate_doc_vectors = vectorized.fit_transform(article_descriptions)
        best_model = self.best_model(generate_doc_vectors)

        print(best_model.transform(generate_doc_vectors))
        print(len(best_model.labels_))
        print(best_model.cluster_centers_)
        print(best_model.n_clusters)
        print(best_model.labels_)
        user_input_vector = vectorized.transform([cleaned_user_text])
        prediction = best_model.predict(user_input_vector)

        return self.retrieve_cluster_elements(articles,best_model.labels_,prediction)

    def retrieve_cluster_elements(self,articles,cluster_arrangement,user_input_cluster):
        user_input_pred = user_input_cluster[0]
        i = 0
        recommended_output = []
        for cluster in cluster_arrangement:
            if cluster == user_input_pred:
                recommended_output.append(articles[i])
            i+=1
        return recommended_output

    def best_model(self,tfidf_vectors):
        best_model = None
        current_score = 0
        best_k = 0

        for k in range(2,10):
            gen_model = KMeans(n_clusters=k, max_iter=1000, n_init=10,init="k-means++",random_state=123)
            gen_model.fit(tfidf_vectors)
            score = silhouette_score(tfidf_vectors,gen_model.labels_)
            if score > current_score:
                best_model = copy.copy(gen_model)
                current_score = score
                best_k = k

        return best_model

    def top_phrases(self, input_text):
        multi_gram_list = self.multi_gram(input_text)
        bag_of_keywords = [keyword for (keyword, score) in self.keyword_extractor_yake(1, 10, input_text, 0.9)]
        top_phrases_output = []

        if len(multi_gram_list) == 0:
            return []

        for i in range(len(multi_gram_list)):
            split_multi_gram = multi_gram_list[i].split()
            score = 0
            for j in range(len(bag_of_keywords)):
                if bag_of_keywords[j] in split_multi_gram:
                    score = score + len(bag_of_keywords)/(j+1)
            top_phrases_output.append([multi_gram_list[i], score])

        top_phrases_output.sort(key=lambda x: x[1], reverse=True)
        return top_phrases_output

    def clean_text(self,text):
        split_text = text.split('\n')
        cleaned_text = ""
        for split in split_text:
            cleaned_text += split.strip()

        return cleaned_text


    # TODO Implement similarity checker
    def similarity_checker(self):
        pass


    # n_grams = 3
    def multi_gram(self, input_text):
        mixed_grams = self.keyword_extractor_yake(4, 15, input_text, 0.9)
        if len(mixed_grams) == 0:
            return []
        else:
            tri_grams = [word.lower() for (word, accuracy) in mixed_grams if len(word.split()) > 2]
            if len(tri_grams) == 0:
                return []
            else:
                return tri_grams

    def name_extractor(self, input_text):
        # Can move spacy.load to outer scope to load when the page is opened
        nlp = spacy.load("en_core_web_lg")
        doc = nlp(input_text)

        list_output = [e.text for e in doc.ents if e.label_ == 'PERSON']
        return list_output

    def all_keywords(self, input_text):
        # runs keywords getter n = 10 times for top 15 words. Total = 150 words
        keywords_full_list = []
        i = 0
        de_dupe = 0.2
        while i < 10:
            # if you want word accuracy add in (word,acc)
            keywords_full_list += [word for (word, acc) in self.keyword_extractor_yake(1, 15, input_text, de_dupe
                                                                                               )]
            i += 1
            if de_dupe < 0.9:
                de_dupe += 0.1
        return list(OrderedDict.fromkeys(keywords_full_list))

