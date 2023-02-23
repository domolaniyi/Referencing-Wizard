class Article:
    
    def __init__(self, title, author_name, cited_count, doi, publication_date,description=None,):
        self.title = title
        self.authorName = author_name
        self.citedCount = int(cited_count)
        self.doi = doi
        # self.pii = pii
        self.doi_link = "https://www.doi.org/"+str(doi)
        self.publicationDate = str(publication_date)
        self.description = description

    def __str__(self):
        return f"[TITLE: {self.title}] | [AUTHOR: {self.authorName}] | [CITECOUNT: {self.citedCount}] " \
               f"| [PUBLICATIONDATE: {self.publicationDate}] | [Link: {self.doi_link}] " \
               f"[DC:{self.description}] |  [DOI:{self.doi}"


