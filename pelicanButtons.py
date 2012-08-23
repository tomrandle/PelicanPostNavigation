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


def createSoup(openFile):
	
	page = open(openFile, 'r')
	soup = BeautifulSoup(page.read())
	
	page.close()

	return soup


def readFile(fileName):

	soup = createSoup(fileName)

	titleSection = soup.find(locationOfLink)
	dateSection = soup.find('abbr', { "class" : locationOfDate })

	pageName = titleSection.a.text
	pageURL = titleSection.a.get('href')
	pageDate = dateSection.get('title')

	return [pageName, pageURL , pageDate , fileName]


def sortByColumn(A,*args):
    A.sort(key=operator.itemgetter(*args))
    return A





def modifyLink(elementClass, fileName, link):

	linkName =  link[0]
	linkURL =  link[1]

	soup = createSoup(fileName)

	page = open(fileName, 'w')


	nextTag = soup.find('a', { "class" : elementClass})
	
	nextTag["href"] = linkURL
	nextTag["title"] = linkName
	nextTag.insert(0, linkName)	

	page.write(soup.prettify())
	page.close()





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
		modifyLink("previous-page", fileToOpen, previousLink)


	if index < (len(listOfLinks)-1):
		nextIndex = index + 1
		nextLink = listOfLinks[nextIndex]
		modifyLink("next-page", fileToOpen, nextLink)









