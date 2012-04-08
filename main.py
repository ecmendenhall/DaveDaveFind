from framework import bottle
from framework.bottle import route, template, request, error, debug, redirect
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
from models import PythonTerm, Page, SearchTerm
import urllib		
 
@route('/')
def search_form():
    output = template('templates/home')
    return output

@route('/search', method='GET')
def process_search():
	search_query = request.GET.get('search_query', '').strip()
	query = search_query.lower()
	
	if query.find('--') == 0:
		if query.find('--cs101') == 0:
			redirect_url = 'http://www.udacity-forums.com/cs101/search/?q=' + urllib.quote(query[8:])
		if query.find('--cs373') == 0:
			redirect_url = 'http://www.udacity-forums.com/cs373/search/?q=' + urllib.quote(query[8:])
		if query.find('--python') == 0:
			redirect_url = 'http://docs.python.org/search.html?q=' + urllib.quote(query[9:])
		return redirect(redirect_url)	
	
	# Get all SearchTerm objects that match the search_query.
	q = SearchTerm.all().filter('term =', query).get()	
	
	if q:
		query_urls = q.urls
		page_results = Page.all().filter('url IN', query_urls).order('-dave_rank').fetch(5)
		page_dicts = []
		for page in page_results:
			page_info = {}
			query_index = page.text.find(query)
			i = query_index - 50
			j = query_index + 450
			text_string = page.text[i:j]
			page_info['text'] = text_string
			page_info['title'] = page.title
			page_info['url'] = page.url
			page_dicts.append(page_info)
		
	else:
		page_dicts = None
	
	return template('templates/results', search_query=search_query, page_dicts=page_dicts)
 
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