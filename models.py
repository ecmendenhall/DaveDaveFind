from google.appengine.ext import db

class PythonTerm(db.Model):
	"""Models a term from the Python glossary."""
	term = db.StringProperty()
	definition = db.TextProperty()

def store_pythonterm(query, result):
		pythonterm = PythonTerm(term=query, definition=result)
		pythonterm.put()