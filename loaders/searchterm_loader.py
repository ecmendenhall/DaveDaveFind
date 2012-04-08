from google.appengine.ext import db
from google.appengine.tools import bulkloader
from models import SearchTerm

def get_list(s):
    if s:
        return [x.strip() for x in s.decode('utf-8').strip().replace('\n', ' ').replace(',', ' ').replace(';', ' ').split(' ') if len(x.strip()) > 0]
    else:
        return []



class SearchTermLoader(bulkloader.Loader):
	def __init__(self):
		bulkloader.Loader.__init__(self, 'SearchTerm',
			[('term', str),
			 ('urls', get_list)
			])
loaders = [SearchTermLoader]