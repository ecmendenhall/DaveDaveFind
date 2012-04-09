from google.appengine.ext import db

class SearchTerm(db.Model):
	"""Models a search term and its associated URLs."""
	term = db.StringProperty()
	urls = db.StringListProperty()
	
class Page(db.Model):
	"""Models a Page and its Daverank from the index."""
	url = db.StringProperty()
	title = db.StringProperty()
	text = db.TextProperty()
	dave_rank = db.FloatProperty()
	doc = db.BooleanProperty()

class Video(db.Model):
	"""Models a video in the index."""
	url = db.StringProperty()
	title = db.StringProperty()
	filename = db.StringProperty()
	id = db.StringProperty()
	type = db.StringProperty()
	views = db.IntegerProperty()
	text = db.TextProperty()

class PythonTerm(db.Model):
	"""Models a definition from the Python glossary."""
	# All definitions are associated with search terms,
	# but not all search terms are associated with definitions.
	term = db.ReferenceProperty(SearchTerm,
								collection_name='python_terms')
	definition = db.TextProperty()
	
	
	
									