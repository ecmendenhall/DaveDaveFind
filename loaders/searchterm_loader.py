from google.appengine.ext import db
from google.appengine.tools import bulkloader
from models import SearchTerm

class SearchTermLoader(bulkloader.Loader):
	def __init__(self):
		bulkloader.Loader.__init__(self, 'SearchTerm',
			[('term', str),
			])
loaders = [SearchTermLoader]