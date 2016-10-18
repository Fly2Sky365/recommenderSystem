import urllib.request

thisurl="http://www-rohan.sdsu.edu/~gawron/index.html"

handle = urllib.request.urlopen(thisurl)

html_gunk = handle.read()

print(html_gunk)
#print (html_gunk[:150])
