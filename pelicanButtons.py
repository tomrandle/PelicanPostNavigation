import glob
import os
import operator
from BeautifulSoup import BeautifulSoup
from xml.etree import ElementTree



outputPath = "/Users/tom/Dropbox/Sites/newtomrandle.com/output/posts"
locationOfLink = 'h2'
locationOfDate = 'published' #fix this!


def findFiles(pathName):

	os.chdir(pathName)
	_fileList = []

	for fileName in glob.glob("*.html"):
	    _fileList.append(fileName)

	return _fileList


def readFile(fileName):

	page = open(fileName)

	soup = BeautifulSoup(page.read())

	titleSection = soup.find(locationOfLink)
	dateSection = soup.find('abbr', { "class" : locationOfDate })

	pageName = titleSection.a.text
	pageURL = titleSection.a.get('href')
	pageDate = dateSection.get('title')

	return [pageName, pageURL , pageDate , fileName]

	fileName.close()

def sortByColumn(A,*args):
    A.sort(key=operator.itemgetter(*args))
    return A



listOfFiles = findFiles(outputPath)

listOfLinks = []


for fileName in listOfFiles:
	listOfLinks.append(readFile(fileName))


sortByColumn(listOfLinks,2)



for post in listOfLinks:
	#text = str(post[3]).strip('[]').strip("''") # Must be doing something wrong to need this!?
	text = post[3]
	page = open(text)


	if post > 0 :
		index = post - 1 #post is a list!!
		nextLink = listOfLinks[index][3]
		print nextLink
	previousLink = []

	#Lookup 


	#print "OPen file", openFile




def saveLinks():

	outputTestPath = "/Users/tom/Dropbox/python/pelicanAddNextAndPreviousButtons/outputText.html"

	target = open(outputTestPath, 'w')


	root_element = ElementTree.Element("nav")


	nextLink = ElementTree.SubElement(root_element, "a", {'class': 'bah', 'href': 'www.bah.com'})
	previousLink = ElementTree.SubElement(root_element, "a", Class="sas", href="www.google.com", title="BAAAAAH")

	nextLink.text = "Mystical content"
	previousLink.text = "More"


	target.write(ElementTree.tostring(root_element))

	target.close()

