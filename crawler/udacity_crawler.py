from bs4 import BeautifulSoup
import urllib

def crawl_web(seed): # returns index, graph of inlinks
    tocrawl = [seed]
    crawled = []
    graph = {}  # <url>, [list of pages it links to]
    index = {} 
    while tocrawl: 
        page = tocrawl.pop()
        if page not in crawled:
            soup = get_page(page)
            add_page_to_index(index, page, soup)
            outlinks = get_all_links(soup)
            graph[page] = outlinks
            union(tocrawl, outlinks)
            crawled.append(page)
    return index, graph

def get_all_links(page):
    links = []
    for link in page.find_all('a'):
    	links.append(link.get('href'))
    return links

def union(a, b):
    for e in b:
        if e not in a:
            a.append(e)

def add_page_to_index(index, url, content):
	text = content.get_text()
	words = text.split()
	for word in words:
		add_to_index(index, word, url)
        
def add_to_index(index, keyword, url):
    if keyword in index:
        index[keyword].append(url)
    else:
        index[keyword] = [url]

def lookup(index, keyword):
    if keyword in index:
        return index[keyword]
    else:
        return None

def get_page(url):
    if url in cache:
        return cache[url]
    else:
        print "Page not in cache: " + url
        try: 
        	content = urllib.urlopen(url).read()
        	return BeautifulSoup(content)
        except:
        	return ""
        	
cache = {}
print crawl_web('http://www.udacity.com/cs101x/index.html')