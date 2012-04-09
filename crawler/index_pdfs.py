# coding=utf8

import os
import csv

url_dict = {
	'CS101 - Course Glossary.txt':'http://www.udacity.com/file?file_key=agpzfnVkYWNpdHl1ckQLEgZDb3Vyc2UiBWNzMzczDAsSCUNvdXJzZVJldiIHZmViMjAxMgwLEgRVbml0GAIMCxIMQXR0YWNoZWRGaWxlGIF9DA',
	'Udacity CS101 Python Reference.txt':'http://www.udacity.com/file?file_key=agpzfnVkYWNpdHl1ckcLEgZDb3Vyc2UiBWNzMTAxDAsSCUNvdXJzZVJldiIHZmViMjAxMgwLEgRVbml0GOmhIQwLEgxBdHRhY2hlZEZpbGUYuZ8nDA',
	'Unit 1 Notes.txt':'http://www.udacity.com/file?file_key=agpzfnVkYWNpdHl1ckQLEgZDb3Vyc2UiBWNzMzczDAsSCUNvdXJzZVJldiIHZmViMjAxMgwLEgRVbml0GAIMCxIMQXR0YWNoZWRGaWxlGLFtDA',
	'Unit 2 Notes.txt':'http://www.udacity.com/file?file_key=agpzfnVkYWNpdHl1ckcLEgZDb3Vyc2UiBWNzMTAxDAsSCUNvdXJzZVJldiIHZmViMjAxMgwLEgRVbml0GIH0AwwLEgxBdHRhY2hlZEZpbGUYwaYIDA',
	'Unit 3 Notes.txt':'http://www.udacity.com/file?file_key=agpzfnVkYWNpdHl1ckcLEgZDb3Vyc2UiBWNzMTAxDAsSCUNvdXJzZVJldiIHZmViMjAxMgwLEgRVbml0GNLxCQwLEgxBdHRhY2hlZEZpbGUYtMkMDA',
	'Unit 4 Notes.txt':'http://www.udacity.com/file?file_key=agpzfnVkYWNpdHl1ckcLEgZDb3Vyc2UiBWNzMTAxDAsSCUNvdXJzZVJldiIHZmViMjAxMgwLEgRVbml0GJm5FAwLEgxBdHRhY2hlZEZpbGUY690NDA',
	'Unit 5 Notes.txt':'http://www.udacity.com/file?file_key=agpzfnVkYWNpdHl1ckcLEgZDb3Vyc2UiBWNzMTAxDAsSCUNvdXJzZVJldiIHZmViMjAxMgwLEgRVbml0GNn3FAwLEgxBdHRhY2hlZEZpbGUYwe0aDA',
	'Unit 6 Notes.txt':'http://www.udacity.com/file?file_key=agpzfnVkYWNpdHl1ckcLEgZDb3Vyc2UiBWNzMTAxDAsSCUNvdXJzZVJldiIHZmViMjAxMgwLEgRVbml0GKn1GgwLEgxBdHRhY2hlZEZpbGUYquYfDA',
	'Unit 7 Notes.txt':'http://www.udacity.com/file?file_key=agpzfnVkYWNpdHl1ckcLEgZDb3Vyc2UiBWNzMTAxDAsSCUNvdXJzZVJldiIHZmViMjAxMgwLEgRVbml0GOmhIQwLEgxBdHRhY2hlZEZpbGUYgYgnDA'
}

def add_pdf_to_index(index, filename, pagedata):
	try:
		pdf_file = open(filename, 'rb')
	except:
		return
	text = pdf_file.read()
	text_ascii = removeNonAscii(text)
	url = url_dict[filename]
	name = filename[:-4]
	pagedata[url] = [name, text_ascii]
	words = text_ascii.split()
	punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
	stopwords = ['']
	with open('/Users/connormendenhall/Python/DaveDaveFind/DaveDaveFind/data/stopwords.csv', 'rb') as f:
		wordlist = csv.reader(f)
		for stopword in wordlist:
			stopwords.append(stopword[0])
	for word in words:
		word = word.lstrip(punctuation)
		word = word.rstrip(punctuation)
		word = word.lower()
		if word not in stopwords:
			add_to_index(index, word, url)
		
        
def add_to_index(index, keyword, url):
    if keyword in index:
        index[keyword].append(url)
    else:
        index[keyword] = [url]
        

def index_pdfs(index, pagedata):
	files = os.listdir('/Users/connormendenhall/Python/DaveDaveFind/DaveDaveFind/data/pdf/')
	for file in files:
		if file.endswith('.txt'):
			add_pdf_to_index(index, file, pagedata)
	return index, pagedata

def pdf_to_text():
	pdfs = os.listdir('.')
	for pdf in pdfs:
		if pdf.endswith('.pdf'):
			output_file = pdf[:-3] + 'txt'
			os.system('pdf2txt.py -A -o ' + output_file + ' ' + pdf)

def write_pdf_search_terms(filename, index):
	f = open(filename, 'wt')
	try:
		writer = csv.writer(f)
		writer.writerow(['term'])
		for term in index:
			ascii_term = term.encode('ascii', 'ignore')
			writer.writerow([ascii_term])
	finally:
		f.close()
		print "[write_search_terms()] Finished writing SearchTerm CSV file."

def removeNonAscii(s): return "".join(i for i in s if ord(i)<128)

def write_pdf_info(filename, index):
	f = open(filename, 'wt')
	try:
		writer = csv.writer(f)
		writer.writerow(['term', 'url'])
		for term in index:
			# Get the term's list of urls
			url_list = index[term]
			for url in url_list:
				ascii_url = url.encode('ascii', 'ignore')
				ascii_term = term.encode('ascii', 'ignore')
				writer.writerow([ascii_term, ascii_url])
	finally:
		f.close()
		print "[write_url_info()] Finished writing DocUrl CSV file."

def undupe_index(index):
	for key in index.keys():
		index[key] = set(index[key])
	print "[undupe_index()] Index un-duped"
	return index

