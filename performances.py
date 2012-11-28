#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

#General imports
import urllib
import json
import datetime
import itertools
from random import choice
from operator import itemgetter

# Fancy URL imports
from urllib import FancyURLopener

# Readability imports
from readability.readability import Document

# NLTK imports
import nltk, re, pprint, sys
from nltk.tokenize import *
from nltk import  word_tokenize, pos_tag, wordpunct_tokenize
from nltk.collocations import *

# Set the starting time of the execution
t0 = datetime.datetime.now()

# Function to extract the answer from the provided text
def _getAnswer(self, text, extract_node): 
	try: 
		answer_list = []
		
		# To remove extra spacea and special characteres from text
		text = re.sub(r'\W+\d+\s+.,\'"&', '', text) 
		
		#Start extraction process from the text
		# Sentence Tokenization
		for sent in nltk.sent_tokenize(text): 
		
			# Word Tokenization and pos tagging
			# Create chunks of the text which may have the answer
			for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
				
				#print chunk
				if hasattr(chunk, 'node'): 
					# Check if the cunkes contain the needed node
					if chunk.node == extract_node:
						performer = ' '.join(c[0] for c in chunk.leaves()) 
						answer_list.append(performer)
						# Create a central result set
						result.append(performer)
		return answer_list 
	except: 
		print " ERROR: Couldn't perform named entity recognition on this text"

		
#Parameters for using Fancy URL Loader to bypass the command promt issue of several sites.	
user_agents = [
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9'
]

# Class to set the FancyURL parameters and access variable creation
class MyOpener(FancyURLopener, object):
    version = choice(user_agents)
myopener = MyOpener()

#to take input from command line
#question = raw_input('Please enter your question:')
#question = question.replace(' ','%20')

#to take input from argument
#print sys.argv[1]
question = str(sys.argv[1])

#Trec-8 Question set
#question = "Who was the first Taiwanese President"
#question = "Who was the lead actress in the movie 'Sleepless in Seattle'"
#question = "Who received the Will Rogers Award in 1989"
#question = "Who is the mayor of Marbella"
#question = "Who was the first American in space"
#question = "Who was the leader of the Branch Davidian Cult confronted by the FBI in Waco, Texas in 1993"

#User Questions set
#question = "Who is the world record holder for 100 meters"
#question = "who is the lead singer of Bon Jovi"
#question = "Who is the greatest theoretical physicist"
#question = "Who is the creator of Mona Lisa"
#question = "Who is the creator of the Universe"

#question = "Who is the president of USA"
#question = "who is the prime minister of great britain"
#question = "Where is Inoco based"
#question = "Who is the girl actreess annie in annie"

#print "Question Asked = %s" % question
#Create URL friendy query
question = question.replace(' ','%20')

# question pre processing to find type of query
q_type =re.split('%20',question)
Question_type = q_type[0].lower()

node=''

if Question_type == "who":
	catagory=1 # person question PERSON
	node="PERSON"
elif Question_type== "where":
	catagory=1 # person question PLACE
	node="LOCATION"
elif Question_type == "what":
	catagory=2 # named entiry NP
	node="NP"
elif Question_type== "which":
	catagory=2 # named entiry NP
	node="PERSON"
elif Question_type == "when":
	catagory=3 # Date type questions DATE
	node="DATE"
else:
	catagory=0 # named entiry NP
	node="NP"
	

	#exit()

	
#print catagory	

#make the search api query link
api_query =''

api_query += "https://ajax.googleapis.com/ajax/services/search/web?v=1.0&q="
api_query += question
api_query += "&start=0&max-results=100"

#print "Google Api. Query = %s" % api_query

myopener = MyOpener()
#fire the query and get the jason result set from Google
json_output= json.loads(myopener.open(api_query).read()).items()


#declare the set name to store the urls which may have the answer
searchset = []

# List of all web pages that do not need to be processed by the system
blockurl = "http://twitter.com/"

#this will help get the url's from the json output into an array for further use
for resultset in json_output[0][1]['results']:
    # now resultset is a dictionary
    for attribute, value in resultset.iteritems():
        if attribute=='unescapedUrl':
        #if attribute=='content': #for testing a new way out.
            #print value
            if value.find(blockurl)== -1:
                searchset.append(value)
            #else:
                #print "skipped twitter"
                
            #searchset.append('next') # for testing a new way out.

#print " List of Seach Result Pages = %s" % searchset
#exit()

row_data1 = []

# Creating content array of all the pages returned from Google 
for testurls in searchset:
	filename1=myopener.open(testurls).read()
	readable_data1= Document(filename1).summary()
	# Removing the HTML tags from the web page for processing
	tempval = nltk.clean_html(readable_data1)
	row_data1.append(tempval)
	#print datetime.datetime.now() - t0 

#print row_data1
result = []
temp_result=[_getAnswer("",row_data,node) for row_data in row_data1]

#print "Result Set = %s "% result

word_freq = {}

# Count the frequency of accorunces of results from all pages
for word in result:
    word_freq[word] = word_freq.get(word, 0) + 1

# Find out the top 5 most frequent results
keys = sorted(word_freq.iteritems(),key=itemgetter(1),reverse=True)[:5] 

answer= keys[0][0]
print " ' %-10s ' " % answer
#print "Time Taken"
print datetime.datetime.now() - t0 
#print keys

# To see the top 5 outputs
for word,frequency in keys:
	print " ' %-10s ' found %d times " % (word, frequency)

if catagory != 1:
	print "There seems to be some problem with the question. \nWe currently are only able to answer who, where, which and when Questions. \nThe answer may be correct or incorrect?"
#answer = ""
#temp = word_freq[keys[0]]
#for word in keys:
#        if word_freq[word] > temp:
#                answer = word.encode("utf-8")
#                temp = word_freq[word]
        #print "%-10s %d" % (word.encode("utf-8"), word_freq[word])
