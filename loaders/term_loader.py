from google.appengine.ext import db
from google.appengine.tools import bulkloader
from models import PythonTerm

class PythonTermLoader(bulkloader.Loader):
	def __init__(self):
		bulkloader.Loader.__init__(self, 'PythonTerm',
			[('term', str),
			('definition', str)
			])
loaders = [PythonTermLoader]