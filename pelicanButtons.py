import glob
import os

os.chdir("/Users/tom/Dropbox/Sites/newtomrandle.com/output/posts")

fileList = []

for fileName in glob.glob("*.html"):
    fileList.append(fileName)

print fileList

"""
txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
"""