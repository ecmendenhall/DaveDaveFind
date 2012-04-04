from framework import bottle
from framework.bottle import route, template, request, error, debug
from google.appengine.ext.webapp.util import run_wsgi_app
 
@route('/')
def search_form():
    message = 'Hello World'
    output = template('templates/home', data = message)
    return output

@route('/search', method='POST')
def process_search():
	search_query = request.POST.get('search_query', '').strip()
	return template('templates/results', search_query=search_query)
 
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