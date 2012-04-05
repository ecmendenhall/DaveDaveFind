from bs4 import BeautifulSoup
import io

def make_function_dict(page):
	# Open the documentation HTML file and read it into BeautifulSoup.
	f = io.open(page)
	s = f.read()
	f.close()
	soup = BeautifulSoup(s)
	
	# Create an empty dict that will map function names to HTML.
	function_dict = {}
	
	# Find all 'dl' tags with the css class 'function'
	functions = soup.find_all('dl', {'class':'function'})
	for i in range(0, len(functions)):
		title_tag = functions[i].find('tt', {'class':'descname'})
		name = title_tag.text
		desc_tag = functions[i].find('dd')
		desc = desc_tag.text
		function_dict[name] = desc
	
	return function_dict

dict = make_function_dict('/Users/connormendenhall/Python/DaveDaveFind/DaveDaveFind/pythondocs/library/functions.html')

print dict['enumerate']
	
	