from framework import bottle
from framework.bottle import route, template, request, error, debug, redirect
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
from models import PythonTerm, Page, SearchTerm, Video
from bs4 import BeautifulSoup
from operator import itemgetter
import urllib
import json

class AppURLopener(urllib.FancyURLopener):
    version = "DaveDaveFind/.9"

urllib._urlopener = AppURLopener()

stopwords = ['a', 'able', 'about', 'across', 'after', 'all', 'almost', 'also', 'am', 'among', 'an', 
'and', 'any', 'are', 'as', 'at', 'be', 'because', 'been', 'but', 'by', 'can', 'cannot', 'could', 'dear',
'did', 'do', 'does', 'either', 'else', 'ever', 'every', 'for', 'from', 'get', 'got', 'had', 'has', 'have',
'he', 'her', 'hers', 'him', 'his', 'how', 'however', 'i', 'if', 'in', 'into', 'is', 'it', 'its', 'just',
'least', 'let', 'like', 'likely', 'may', 'me', 'might', 'most', 'must', 'my', 'neither', 'no', 'nor', 'not',
'of', 'off', 'often', 'on', 'only', 'or', 'other', 'our', 'own', 'rather', 'said', 'say', 'says', 'she',
'should', 'since', 'so', 'some', 'than', 'that', 'the', 'their', 'them', 'then', 'there', 'these', 'they',
'this', 'tis', 'to', 'too', 'twas', 'us', 'wants', 'was', 'we', 'were', 'what', 'when', 'where', 'which',
'while', 'who', 'whom', 'why', 'will', 'with', 'would', 'yet', 'you', 'your']
 
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
	number_pages = 10
	number_videos = 5
	
	#Move this stuff to its own procedure tomorrow!
	if query.find('--') == 0:
		if query.find('--forum') == 0:
			redirect_url = 'http://www.udacity-forums.com/cs101/search/?q=' + urllib.quote(query[8:])
			return redirect(redirect_url)	
		if query.find('--cs373') == 0:
			redirect_url = 'http://www.udacity-forums.com/cs373/search/?q=' + urllib.quote(query[8:])
			return redirect(redirect_url)	
		if query.find('--python') == 0:
			redirect_url = 'http://docs.python.org/search.html?q=' + urllib.quote(query[9:])
			return redirect(redirect_url)
		if query.find('--searchwithpeterdotinfo') == 0:
			redirect_url = 'http://searchwithpeter.info/secretplans.html?q=' + urllib.quote(query[25:])
			return redirect(redirect_url)
		if query.find('--showmore') == 0:
			query = query[11:]
			search_query = query
			number_pages = 20
			number_videos = 10
		if query.find('--daverank') == 0:
			query = query[11:]
			search_query = query
			show_daverank = True
	
	if query.find('python') == 0:
		pyquery = query[7:]
	else:
		pyquery = query
	
	ddgurl_root = 'http://duckduckgo.com/?q=python+'
	ddgurl_suffix = urllib.quote(pyquery) + '&format=json'

	response = urllib.urlopen(ddgurl_root + ddgurl_suffix)
	response_json = response.read()

	pythonterm = json.loads(response_json)
	
	if pythonterm:
		pyterm_info = {}
		if pythonterm['AbstractSource'] == 'Python Documentation':
			pyterm = BeautifulSoup(pythonterm['AbstractText'])
			try:
				pyterm_code = pyterm.find('code').string
				pyterm.pre.decompose()
				pyterm_info['code'] = pyterm_code
			except: 
				pyterm_info['code'] = None
			pyterm_desc = pyterm.get_text()
			pyterm_info['desc'] = pyterm_desc
			pyterm_info['url'] = pythonterm['AbstractURL']
			results = True
	else: 
		pyterm_info = None
	
	query_words = query.split()
	for word in query_words:
		if word in stopwords:
			query_words.remove(word)
	
		

	
	query_urls = []
	for term in query_words:
		# Get all SearchTerm objects that match the search_query.
		q = SearchTerm.all().filter('term =', term).get()
		if q:
			query_urls.append(set(q.urls))
	
	if query_urls:
		query_url_set = set.intersection(*query_urls)
		query_url_list = list(query_url_set)	
		
		if len(query_url_list) > 0:
			results = True
		if len(query_url_list) > 30:
			query_url_list = query_url_list[0:30]
			
		page_results = Page.all().filter('url IN', query_url_list).order('-dave_rank').fetch(number_pages)
		page_dicts = []
		for page in page_results:
			page_info = {}
			query_index = page.text.find(query)
			if query_index != -1:
				i = page.text.find(' ', query_index-25)
				excerpt_words = page.text[i:].split(' ')
				page_info['exact_match'] = True 
			else:
				excerpt_words = page.text.split(' ')
				page_info['exact_match'] = False
			excerpt = ' '.join(excerpt_words[:50])
			
			page_info['text'] = excerpt
			page_info['title'] = page.title
			page_info['url'] = page.url
			page_info['daverank'] = page.dave_rank
			page_info['doc'] = page.doc
			page_dicts.append(page_info)
		page_dicts.sort(key=itemgetter('exact_match'), reverse=True)
		
		video_results = Video.all().filter('url IN', query_url_list).order('-views').fetch(number_videos)
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
				video_info['exact_match'] = True
			else:
				url = video.url
				start = 0
				video_info['exact_match'] = False			
			video_info['title'] = video.title
			video_info['url'] = url
			video_info['subtitle'] = video.text[-20:query_index:20]
			video_info['id'] = video.id
			video_info['start'] = start
			video_dicts.append(video_info)
		video_dicts.sort(key=itemgetter('exact_match'), reverse=True)
			
	else:
		page_dicts = None
		video_dicts = None
	
	query_string_words = query.split()
		
	
	return template('templates/results', search_query=search_query, query_string_words=query_string_words, page_dicts=page_dicts, video_dicts=video_dicts, pyterm_info=pyterm_info, show_daverank=show_daverank, results=results)
 
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