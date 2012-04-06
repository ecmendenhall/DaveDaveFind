from google.appengine.ext import db
from google.appengine.tools import bulkloader
import models


def get_searchterm(term):
    terms = db.GqlQuery("select * from SearchTerm where term = :1", term)
    if terms.count() == 0:
        newSearchTerm = model.SearchTerm(term=term)
        db.put(newSearchTerm)
        return newSearchTerm
    else:
        return terms[0]

class PageUrlLoader(bulkloader.Loader):
    def __init__(self):
        bulkloader.Loader.__init__(self, "PageUrl",
                                   [("term", get_searchterm),
                                    ("url", str),
                                    ("dave_rank", float) 
                                    ])

      
loaders = [PageUrlLoader]
if __name__ == '__main__':
    bulkload.main(PageUrlLoader)
