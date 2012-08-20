import glob
import os

os.chdir("/Users/tom/Dropbox/Sites/newtomrandle.com/output/posts")

fileList = []

for fileName in glob.glob("*.html"):
    fileList.append(fileName)

print fileList


for fileName in fileList:
	fileTxt = open(fileName)

	print fileTxt.read()


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