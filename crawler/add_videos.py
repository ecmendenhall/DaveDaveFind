import csv
import os
from pysrt import SubRipFile

def add_to_index(index, keyword, url):
    if keyword in index:
        index[keyword].append(url)
    else:
        index[keyword] = [url]	

def removeNonAscii(s): return "".join(i for i in s if ord(i)<128)

def add_videos_to_index(subtitle_index, output_file, index):
	vindexReader = csv.reader(open(subtitle_index, 'rb'))
	vinfoWriter = csv.writer(open(output_file, 'wt'))
	vinfoWriter.writerow(['title', 'filename', 'id', 'views', 'type', 'url', 'text'])
	for row in vindexReader:
		try:
			filename = row[1] + '.en.srt'
			url = 'http://www.youtube.com/watch?v=' + row[2]
			text = open(filename).read()
			text_ascii = removeNonAscii(text)
			subtitles = SubRipFile.open(filename)
			vinfoWriter.writerow([row[0], row[1], row[2], row[3], row[4], url, text_ascii])
			punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
			stopwords = ['']
			with open('/Users/connormendenhall/Python/DaveDaveFind/DaveDaveFind/data/stopwords.csv', 'rb') as f:
				wordlist = csv.reader(f)
				for stopword in wordlist:
					stopwords.append(stopword[0])
			for sentence in subtitles:
				text = (sentence.text)
				wordlist = text.split()
				for word in wordlist:
					word = word.lstrip(punctuation)
					word = word.rstrip(punctuation)
					word = word.lower()
					if word not in stopwords:
						add_to_index(index, word, url)
				
		except:
			pass
	print "[add_videos_to_index()] Videos added."
	return index



		

	