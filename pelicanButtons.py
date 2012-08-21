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

	return [[pageName],[pageURL],[pageDate]]

	fileName.close()

def sortByColumn(A,*args):
    A.sort(key=operator.itemgetter(*args))
    return A




listOfFiles = findFiles(outputPath)


listOfLinks = []

for fileName in listOfFiles:
	listOfLinks.append(readFile(fileName))


for b in listOfLinks: 
	print b[0]
	print b[1]




def saveLinks():

	outputTestPath = "/Users/tom/Dropbox/python/pelicanAddNextAndPreviousButtons/outputText.html"

	target = open(outputTestPath, 'w')


	root_element = ElementTree.Element("nav")

	nextLink = ElementTree.SubElement(root_element, "a", Class="bah",href="www.google.com")
	previousLink = ElementTree.SubElement(root_element, "a", Class="sas", href="www.google.com", title="BAAAAAH")

	nextLink.text = "Mystical content"
	previousLink.text = "More"


	target.write(ElementTree.tostring(root_element))

	target.close()


saveLinks()


