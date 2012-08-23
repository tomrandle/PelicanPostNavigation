import glob
import os
import operator
from BeautifulSoup import BeautifulSoup, Tag, NavigableString

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

	page.close()



def sortByColumn(A,*args):
    A.sort(key=operator.itemgetter(*args))
    return A


def createNav(parentElement, openFile):

	print "creating nav"
	
	page = open(openFile, 'r+')

	soup = BeautifulSoup(page.read())

	subSoup = soup.section

	tag1 = Tag(soup, "mytag")
	subSoup.insert(0, tag1)

	
	print soup

	page.close()


def createLink(parentElement, className, linkText, linkURL, linkTitle): 

	print "creating link"



#Open all the files in the folder and read their information 

listOfFiles = findFiles(outputPath)
listOfLinks = []

for fileName in listOfFiles:
	listOfLinks.append(readFile(fileName))

#Sort the list by date

sortByColumn(listOfLinks,2)


#Open each file again

for index, post in enumerate(listOfLinks):
	fileToOpen = post[3]
	
	#Work out which are the previous and next links

	if index > 0 :
		previousIndex = index - 1
		previousLink = listOfLinks[previousIndex]

	if index < (len(listOfLinks)-1):
		nextIndex = index + 1
		nextLink = listOfLinks[nextIndex]

	createNav('div',fileToOpen)
	#Write Links







