
import ApiEngine
import NlpEngine
import time
from bs4 import BeautifulSoup
from pybliometrics.scopus import AbstractRetrieval
import pybliometrics


class SearchEngine:
    Api_Engine = ApiEngine.ApiEngine()
    Nlp_Engine1 = NlpEngine.NlpEngine()
    retrieval_threshold = 30
    title_queries, keyword_documents_output, keyword_phrase_document_output, keyword_ref_document_output = [], [], [], []

    def general_search(self, key_phrase, search_number):

        articles_output = []
        for phrase in key_phrase:
            searched_articles = self.Api_Engine.basic_query(SearchEngine.query_creator(search_number, phrase), page=0)
            if len(searched_articles) != 0:
                articles_output += searched_articles

        return articles_output

    def combined_search(self, text):
        #     Nlp needs to be done first
        main_keywords = self.Nlp_Engine1.all_keywords(text)
        main_phrases = self.is_key_phrase_useful(main_keywords, self.Nlp_Engine1.top_phrases(text))
        articles_output = []
        for phrase_entry in main_phrases:
            for i in range(1, 5):
                articles_output += self.Api_Engine.basic_query(SearchEngine.query_creator(i, phrase_entry), 0)

        return self.score_articles(self.remove_duplicate_articles(articles_output), main_keywords)
        # return self.score_articles(self.score_duplicate_articles(articles_output), main_keywords)

    # TODO Add in error handling and also the ability for the algorithim to switch to another type of search if one is bad
    # add top_key_phrases as parameter
    def query_generator(self, keywords, top_key_phrases,user_text_input):
        # title_queries, keyword_documents_output, keyword_phrase_document_output, keyword_ref_document_output = [], [], [], []
        block_index = 0
        while True:
            if block_index == 0:
                self.block_one_title(block_index, keywords, top_key_phrases)
            elif block_index == 1:
                self.block_two_title_key(block_index, top_key_phrases)
            elif block_index == 2:
                finished_keywords = False
                while True:
                    if not finished_keywords:
                        self.block_three_phrase_key(block_index, keywords)
                        finished_keywords = True
                    else:
                        self.block_three_title_phrase(block_index, top_key_phrases)

                        all_documents = self.keyword_documents_output+self.keyword_phrase_document_output+self.keyword_ref_document_output
                        unique_documents = self.remove_duplicate_articles(all_documents)
                        unique_documents_with_abstracts = self.Api_Engine.abstract_retreival(unique_documents)
                        return self.recommend_best_documents(unique_documents_with_abstracts,user_text_input)

            block_index += 1

    def recommend_best_documents(self,articles_with_abstracts,user_text_input):
        document_abstracts = []
        documents = []
        for document in articles_with_abstracts:
            abstract = str(document.description)
            if abstract != "" or None:
                document_abstracts.append(abstract)
                documents.append(document)

        if len(document_abstracts) < 5:
            return documents
        else:
            recommened_documents = self.Nlp_Engine1.cluster_descriptions(document_abstracts,user_text_input,documents)
            return recommened_documents

    def block_one_title(self, block_index, keywords, top_key_phrases):
        skip_keywords = []
        for i in range(0, len(keywords)):
            keyword_query_string = self.gen_keyword_query(keywords, i, skip_keywords)
            query = self.title_query(keyword_query_string, top_key_phrases, self.retrieval_threshold, 0,
                                     block_index)
            total_results = int(query.pop(0))
            if total_results > 0:
                if total_results <= self.retrieval_threshold:
                    self.keyword_documents_output += query
                    break
                else:
                    self.title_queries.append((keyword_query_string, total_results))
            else:
                skip_keywords += keywords[i]

    def block_two_title_key(self, block_index, top_key_phrases):
        for (keyword_query, results) in self.title_queries:
            for phrase in top_key_phrases:
                query = self.title_query(keyword_query, phrase, self.retrieval_threshold, 0, block_index)
                total_results = int(query.pop(0))
                if total_results > 0:
                    self.keyword_phrase_document_output += query

    def block_three_phrase_key(self,block_index,keywords):
        for i in self.title_queries:
            skip_keywords = []
            for j in range(0, len(keywords)):
                keyword_query_string = self.gen_keyword_query(keywords, j, skip_keywords)
                query = self.title_query(i[0], keyword_query_string, self.retrieval_threshold, 0, block_index)
                total_results = int(query.pop(0))
                if total_results > 0:
                    self.keyword_ref_document_output += query
                else:
                    skip_keywords += keywords[j]

    def block_three_title_phrase(self,block_index,top_key_phrases):
        for i in self.title_queries:
            for j in range(len(top_key_phrases)):
                query = self.title_query(i[0], top_key_phrases[j], self.retrieval_threshold, 0, block_index)
                total_results = int(query.pop(0))
                if total_results > 0:
                    self.keyword_ref_document_output += query

    def title_query(self, keywords_query, phrase, threshold, page, block):
        query = ""
        if block == 0:
            query = f"TITLE({keywords_query})"
        elif block == 1:
            query = f"TITLE({keywords_query}) AND %7B{phrase}%7D"
        elif block == 2:
            query = f"TITLE({keywords_query}) AND REF({phrase})"

        print(query)
        documents_query = self.Api_Engine.basic_query(query, page)
        if int(documents_query[0]) < threshold:
            return documents_query
        else:
            return [documents_query[0]]

    def get_description(self, document):
        html = self.Api_Engine.description_retrieval(document.doi)
        if html != 0:
            soup = BeautifulSoup(html, 'html.parser')
            dc = soup.find('dc:description').get_text().strip()
            document.description = dc
            return document
        return 0

    def add_descriptions(self,articles):
        dc_articles = []
        for (document,score) in articles:
            document_with_dc = self.get_description(document)
            if document_with_dc == 0:
                continue
            else:
                dc_articles.append(document_with_dc)

        return dc_articles

    def test_new_add_dc(self,articles):
        dc_articles = []
        for (document,score) in articles:
            try:
                ab = AbstractRetrieval(document.doi)
            except pybliometrics.scopus.exception.ScopusException:
                print("No DC found or available")
            else:
                document.description = ab.description
                dc_articles.append(document)

        return dc_articles


    @staticmethod
    def gen_keyword_query(keywords, keyword_place, skip_keywords_list):
        add_and = "AND"
        new_query = ""
        # +1 is added because range stops 1 before. It won't go to the full length
        for i in range(0, keyword_place + 1):
            if keywords[i][0] in skip_keywords_list:
                continue
            else:
                if i == keyword_place:
                    new_query += f'"{keywords[i][0]}"'
                else:
                    new_query += f'"{keywords[i][0]}"' + " " + add_and + " "

        return new_query

    @staticmethod
    def remove_duplicate_articles(articles_list):

        titles = [entry.title.lower() for entry in articles_list]

        seen_titles = set()
        output_list = []
        for entry in articles_list:
            if entry.title.lower() not in seen_titles:
                occur = titles.count(entry.title.lower())
                output_list.append([entry, occur])
                seen_titles.add(entry.title.lower())

        return output_list

    @staticmethod
    def score_articles(articles_list, keywords):
        # may need to remove this error handling, might not be necessary
        if len(articles_list) == 0:
            return []
        else:
            for articles_entry in articles_list:
                score = 0
                for keyword in keywords:
                    if len(keyword.split()) > 1:
                        if keyword in articles_entry[0].title.lower():
                            score += 2
                    else:
                        # TODO Correct the way calculations are done on this section
                        if keyword in articles_entry[0].title.lower():
                            keyword_position_score = len(keywords) / (keywords.index(keyword) + 1)
                            score += keyword_position_score / len(articles_entry[0].title)

                articles_entry[1] += score
                # use .__str__() to see string rep for articles_entry
        return articles_list
        # return articles_list_with_scores

    # Checks whether or not the key phrase found is useful
    @staticmethod
    def is_key_phrase_useful(keywords, key_phrases):

        if len(key_phrases) > 0:
            # /3 makes sure that each key_phrase contains at least 1 of the top 3 key words
            key_phrase_to_use = [phrase for (phrase, score) in key_phrases if score >= len(keywords) / 3]
            return key_phrase_to_use + SearchEngine.create_key_phrases(keywords)
            # if len(key_phrase_to_use) <= 1:
            #     return SearchEngine.create_key_phrases(keywords)
            # else:
            #     return key_phrase_to_use
        else:
            return SearchEngine.create_key_phrases(keywords)

    # Creates key phrases out of keywords if the phrases found don't contain at least one keyword or no keyphrases are produced
    @staticmethod
    def create_key_phrases(keywords):
        keyword_phrases = []
        # best key_phrases = trigrams
        if len(keywords) >= 5:
            for i in range(len(keywords)):
                if i == 3:
                    return keyword_phrases
                inner_keyword = keywords[i] + " "
                checker = 0
                for j in range(i, len(keywords)):
                    if checker == 2:
                        break
                    elif keywords[j] != keywords[i]:
                        inner_keyword += keywords[j] + " "
                        checker += 1

                keyword_phrases.append(inner_keyword)
            return keyword_phrases
        else:
            # If it gets to this point, user should just enter in a new piece of text
            return []

    @staticmethod
    def query_creator(search_number, phrase):

        # TITLE
        if search_number == 1:
            return f'TITLE("{phrase}")'
        # KEY
        elif search_number == 2:
            return f'KEY({phrase})'
        # ABS
        elif search_number == 3:
            return f'ABS({phrase})'
        # TITLE-ABS-KEY
        elif search_number == 4:
            return f'TITLE-ABS-KEY({phrase})'

    @staticmethod
    def remove_null_cited(articles_list):
        if len(articles_list) == 0:
            return []
        else:
            new_articles_list = []

            for entry in articles_list:
                if entry.citedCount != 0:
                    new_articles_list.append(entry)

            return new_articles_list

    @staticmethod
    def order_by_cite_count(articles_list):

        articles_list.sort(key=attrgetter('citedCount'), reverse=True)
        return articles_list
