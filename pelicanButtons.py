import glob
import os
import operator
from BeautifulSoup import BeautifulSoup


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

  	#return {'Page Name':pageName, 'pageURL':pageURL ,'pageDate':pageDate }


def sortByColumn(A,*args):
    A.sort(key=operator.itemgetter(*args))
    return A


listOfFiles = findFiles(outputPath)


listOfLinks = []

for fileName in listOfFiles:
	listOfLinks.append(readFile(fileName))


print listOfLinks
#print (listOfLinks[0][0])






print sortByColumn(listOfLinks,0)





"""
  <header>
    <h2 class="entry-title">
      <a href="../posts/my-new-post--.html" rel="bookmark"
         title="Permalink to Mr Fox is an arse.">Mr Fox is an arse.</a></h2>
  </header>
  <footer class="post-info">
    <abbr class="published" title="2012-08-20T18:23:03">
      Mon 20 August 2012
    </abbr>
"""



"""
txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
"""