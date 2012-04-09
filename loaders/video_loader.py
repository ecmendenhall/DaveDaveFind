from google.appengine.ext import db
from google.appengine.tools import bulkloader
from models import Video

class VideoLoader(bulkloader.Loader):
	def __init__(self):
		bulkloader.Loader.__init__(self, 'Video',
			[('title', str),
			 ('filename', str),
			 ('id', str),
			 ('views', int),
			 ('type', str),
			 ('url', str),
			 ('text',str)
			])
loaders = [VideoLoader]