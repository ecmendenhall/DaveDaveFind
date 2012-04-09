from framework import bottle
from framework.bottle import route, template, request, error, debug, redirect
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
from models import PythonTerm, Page, SearchTerm, Video
import urllib
		
 
@route('/')
def search_form():
    output = template('templates/home')
    return output

@route('/search', method='GET')
def process_search():
	search_query = request.GET.get('search_query', '').strip()
	query = search_query.lower()
	
	show_daverank = False
	results = False
	
	#Move this stuff to its own procedure tomorrow!
	if query.find('--') == 0:
		if query.find('--cs101') == 0:
			redirect_url = 'http://www.udacity-forums.com/cs101/search/?q=' + urllib.quote(query[8:])
			return redirect(redirect_url)	
		if query.find('--cs373') == 0:
			redirect_url = 'http://www.udacity-forums.com/cs373/search/?q=' + urllib.quote(query[8:])
			return redirect(redirect_url)	
		if query.find('--python') == 0:
			redirect_url = 'http://docs.python.org/search.html?q=' + urllib.quote(query[9:])
			return redirect(redirect_url)
		if query.find('--daverank') == 0:
			query = query[11:]
			search_query = query
			show_daverank = True
	
	query_words = query.split()
	
	query_urls = []
	for term in query_words:
		# Get all SearchTerm objects that match the search_query.
		q = SearchTerm.all().filter('term =', term).get()
		if q:
			query_urls.append(set(q.urls))
	
	if query_urls:
		query_url_set = set.intersection(*query_urls)
		query_url_list = list(query_url_set)	
	
		results = True
		if len(query_url_list) > 30:
			query_url_list = query_url_list[0:30]
			
		page_results = Page.all().filter('url IN', query_url_list).order('-dave_rank').fetch(5)
		page_dicts = []
		for page in page_results:
			page_info = {}
			query_index = page.text.find(query)
			if query_index != -1:
				i = query_index - 50
				j = query_index + 450
			else:
				i = 0
				j = 500
			text_string = page.text[i:j]
			page_info['text'] = text_string
			page_info['title'] = page.title
			page_info['url'] = page.url
			page_info['daverank'] = page.dave_rank
			page_dicts.append(page_info)
		
		video_results = Video.all().filter('url IN', query_url_list).order('-views').fetch(3)
		video_dicts = []
		for video in video_results:
			video_info = {}
			subtitles = video.text.lower()
			query_index = subtitles.find(query)
			time_string = ''
			if query_index != -1:
				subtitle_list = subtitles.splitlines()
				for phrase in subtitle_list:
					if phrase.find(query) != -1:
						timestamp_index = subtitle_list.index(phrase) - 1
						timestamp = subtitle_list[timestamp_index]
						if len(timestamp) > 1:
							minutes = timestamp[3:5]
							seconds = timestamp[6:8]
							time_string = '#t=' + minutes + 'm' + seconds + 's'
							start = 60 * int(minutes) + int(seconds)
			if time_string:
				url = video.url + time_string
			else:
				url = video.url
				start = 0			
			video_info['title'] = video.title
			video_info['url'] = url
			video_info['subtitle'] = video.text[-20:query_index:20]
			video_info['id'] = video.id
			video_info['start'] = start
			video_dicts.append(video_info)
			
	else:
		page_dicts = None
		video_dicts = None
		
	
	return template('templates/results', search_query=search_query, page_dicts=page_dicts, video_dicts=video_dicts, show_daverank=show_daverank, results=results)
 
def main():
    debug(True)
    run_wsgi_app(bottle.default_app())
 
@error(403)
def error403(code):
    return 'Get your codes right dude, you caused some error!'
 
@error(404)
def error404(code):
    return template('templates/404')
 
if __name__=="__main__":
    main()