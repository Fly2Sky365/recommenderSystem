#coding:UTF-8
import re
import requests
import sys

reload(sys)
sys.setdefaultencoding('UTF-8')

def ShowWeather(city):
	res = str(city).split('"title = "')
	print res[1], '(Daytime-->Night)'
	html = requests.get("http://www.tianqihoubao.com/weather/{0}".format(res[0]))
	weather = re.search('<table width = "100%" border="0" class = "b" cellpadding = "1">(.*?)</tabale>', html.text, re.S).group(1)
	res = re.findall('<tr>(.*?)</tr>', weather, re.S)
	for x in res[2:]:
		w = re.findall('>(.*?)<', x, re.S)
		for y in W[1:]:
			if len(y.strip()) <= 0:
				pass
			else:
				print y
		print '--'*40
	print '\n','*'*40 

def ShowCity():
	html = requests.get("http://www.tianqihoubao.com/weather/province.aspx?id=130000")
	cities = re.findall('<td style = "height: 22px" aligh = "center" ><a href = "(.*?)">', html.text, re.S)
	for city in cities:
		ShowWeather(city)

def main():
	ShowCity()

if __name__ == '__main__':
	main()