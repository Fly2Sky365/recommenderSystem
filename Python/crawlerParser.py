from html.parser import HTMLParser
import urllib.request

urlText = []

#Define HTML Parser
class parseText(HTMLParser):

    def handle_data(self, data):
        if data != '\n':
            urlText.append(data)

#Create instance of HTML parser
lParser = parseText()

thisurl = "http://www-rohan.sdsu.edu/~gawron/index.html"
#thisurl = "http://www.ysu.edu.cn"
#Feed HTML file into parser
lParser.feed(str(urllib.request.urlopen(thisurl).read()))
lParser.close()
for item in urlText:
    print(item)
