from google.appengine.ext import db

class SearchTerm(db.Model):
	"""Models a search term."""
	term = db.StringProperty()
	
class PageUrl(db.Model):
	"""Models a URL and its Daverank from the index."""
	# A page can be associated with many search terms...
	term = db.ReferenceProperty(SearchTerm,
								collection_name='pages')
	
	#...but each page has a URL and Daverank.
	url = db.StringProperty()
	dave_rank = db.FloatProperty()

class PythonDefinition(db.Model):
	"""Models a definition from the Python glossary."""
	# All definitions are associated with search terms,
	# but not all search terms are associated with definitions.
	term = db.ReferenceProperty(SearchTerm,
								collection_name='python_terms')
	definition = db.TextProperty()
	
	
	
									