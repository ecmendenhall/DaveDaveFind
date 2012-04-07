from framework import bottle
from framework.bottle import route, template, request, error, debug
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
from models import PythonDefinition, PageUrl, SearchTerm
		
 
@route('/')
def search_form():
    output = template('templates/home')
    return output

@route('/search', method='GET')
def process_search():
	search_query = request.GET.get('search_query', '').strip()
	lowercase_query = search_query.lower()
	
	# Get all SearchTerm objects that match the search_query.
	q = SearchTerm.all().filter('term =', lowercase_query).get()	
	
	# Now get the PageUrls that are associated with the term.
	if q:
		page_urls = q.pages
		# Sort them by dave_rank and return the top five.
		results = page_urls.order('-dave_rank').fetch(5)
	
	else:
		results = None
	
	return template('templates/results', search_query=search_query, results=results)
 
def main():
    debug(True)
    run_wsgi_app(bottle.default_app())
 
@error(403)
def error403(code):
    return 'Get your codes right dude, you caused some error!'
 
@error(404)
def error404(code):
    return 'Stop cowboy, what are you trying to find?'
 
if __name__=="__main__":
    main()