from operator import attrgetter
import requests
import Article
from pybliometrics.scopus import AbstractRetrieval
import pybliometrics.scopus.exception

class ApiEngine:
    # 'Query' starts first
    heading = "http://api.elsevier.com/content/search/scopus?query="
    count = "&count=25&"
    current_page = "start="
    fields = "field=dc:title,dc:creator,citedby-count,prism:coverDate,prism:doi&"
    supressNavLinks = "suppressNavLinks=true&"
    apiKey = "apiKey="

    def basic_query(self, query, page):
        articles_list = []
        # e.g. query=brown&count=25&field=dc:title,dc:creator,citedby-count&suppressNavLinks=true&
        url_query = self.heading + query + self.count + self.current_page + str(page) + "&" + \
                    self.fields + self.supressNavLinks + self.apiKey

        try:
            request = requests.get(url_query)
        except requests.exceptions.RequestException as arr:
            return []
        else:
            url_query_json_output = request

        articles_list += [url_query_json_output.json()['search-results']['opensearch:totalResults']]
        if self.is_query_empty(url_query_json_output) == 0:
            # returns empty list
            return articles_list
        else:
            for article_entry in url_query_json_output.json()['search-results']['entry']:
                is_article_valid = self.valid_article(article_entry)
                if is_article_valid is KeyError:
                    continue
                else:
                    articles_list.append(is_article_valid)

            return articles_list

    def abstract_retreival(self,articles):
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

    # TODO Test this method with a loop
    def description_retrieval(self, doi):

        field = "dc:description"
        url = f"https://api.elsevier.com/content/article/doi/{doi}?{self.apiKey}&field={field}"
        print(url)
        try:
            html = requests.get(url)
            html.raise_for_status()
        except requests.exceptions.RequestException as err:
            print("Error")
            return 0
        else:
            return html.text

    def ref_author_query(self, author_name, page):

        if len(author_name) > 1:
            name_split = author_name.split(" ")
            query = "REFAUTH%28" + name_split[len(name_split) - 1] + " " + name_split[0] + "%29"
            return self.basic_query(query, page)
        else:
            return self.basic_query("REFAUTH%28"+author_name+"%29",page)

    @staticmethod
    def is_query_empty(articles_json_list):

        if articles_json_list.json()['search-results']['opensearch:totalResults'] == "0":
            # 0 = nothing found
            return 0
        else:
            return 1

    # checks if article is valid
    @staticmethod
    def valid_article(article_entry):
        try:
            title = article_entry['dc:title']
            author = article_entry['dc:creator']
            publicationDate = article_entry['prism:coverDate']
            doi = article_entry['prism:doi']
        except KeyError:
            return KeyError
        else:
            return Article.Article(title, author, article_entry['citedby-count'], doi,
                                   publicationDate)

