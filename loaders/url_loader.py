from google.appengine.ext import db
from google.appengine.tools import bulkloader
from models import Page

class PageLoader(bulkloader.Loader):
	def __init__(self):
		bulkloader.Loader.__init__(self, 'Page',
			[('url', str),
			 ('title', str),
			 ('text', str),
			 ('dave_rank', float),
			 ('doc', bool)
			])
loaders = [PageLoader]