import glob
import os
from BeautifulSoup import BeautifulSoup


outputPath = "/Users/tom/Dropbox/Sites/newtomrandle.com/output/posts"
locationOfLink = 'h2'


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

	pageName = titleSection.a.text
	pageURL = titleSection.a.get('href')

	print pageName
	print pageURL



listOfFiles = findFiles(outputPath)

readFile(listOfFiles[0])







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