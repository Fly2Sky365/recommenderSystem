import sys
import re
import os
#RxPwrs = [-60, -70, -80, -90, -93, -95, -96, -97, -98, -99, -100, -101, -102, -103, -104, -105] # UK
#RxPwrs = [-61, -71, -81, -91, -101, -101, -103, -104, -105, -106] # FR
#RxPwrs = [-60, -70, -80, -90, -100, -101, -102, -103, -104, -105] # AU

#paths = r'/Users/nliu/Documents/corpdata/IoTR2/UK/IoTR2_UK_RxPwr_%sdBm.txt'

'''
f = open(path,'r')
text = f.readline()
if '-> 00:13:50:05:00:29:78:55, tan=' in text:
     print text
 
while not eof:
     text = f.readline()
     if '-> 00:13:50:05:00:29:78:55, tan=' in text:
             print text
'''

'''
def find_word(text, search):
        result = re.findall('\\b' + search + '\\b', text)
        if len(result)>0:
                #return result.range(search.size(), search.size() + 3)
                return True
		#return result
        else:
                return False
		#return result
'''
#search_after = "RxPER"
def findAllFiles(directory):
	paths = []
	for file in os.listdir(directory):
		if file.endswith(".txt"):
			paths.append(file)
	return paths
	#print paths

def rawdata2list(directory, paths, search_after, line_indicator):
	#RxPERs = range(0, len(RxPwrs))
	RxPERs = []
	#xPERs_pos = 0;
	for path in paths:
	#for RxPwr in RxPwrs:
		#path = r'/Users/nliu/Documents/corpdata/IoTR2/UK/IoTR2_UK_RxPwr_%sdBm.txt'%RxPwr #UK
		#path = r'/Users/nliu/Documents/corpdata/IoTR2/FR/IoTR2_FR_RxPwr_%sdBm.txt'%RxPwr #FR
		#path = r'/Users/nliu/Documents/corpdata/IoTR2/AU/IoTR2_AU_RxPwr_%sdBm.txt'%RxPwr #AU
		print path
		#search_after = "retries=0,"
		search_after = "00:13:50:05:00:29:7e:aa,"
		#with open(path,'r') as openfileobject:
		with open(directory + '/' + path, 'r') as openfileobject:
			cntr = 0
			RxPER_total = 0
			for line in openfileobject:
				#if '-> 00:13:50:05:00:29:78:55, tan=' in line: #UK and FR
				if '-> 00:13:50:05:00:29:7e:aa, tan=' in line:  #AU
				#if line_indicator in line:
					#print cntr
		             		#print line
					#print find_word
					list_of_words = line.split()
					#print list_of_words	
					#next_word = list_of_words[list_of_words.index(search_after) + 1]
					next_word = list_of_words[list_of_words.index(search_after) + 4]
					#print next_word
					RxPER = next_word[5:]
					#RxPER = next_word
					RxPER_total = RxPER_total + int(RxPER)
					#print RxPER
					#print RxPER_total
					#if find_word(line, search_after):
					#	print "SUCCESS" 
					#	#print search_after
					cntr = cntr + 1	

			#print cntr
			RxPERs.append(float(("{0:.2f}".format(float (RxPER_total)/cntr))))
			#RxPERs[RxPERs_pos] = float(("{0:.2f}".format(float (RxPER_total)/cntr)))
			#print RxPERs_pos
			#print "RxPER_avg= " + str (RxPERs[RxPERs_pos])
			#RxPERs_pos = RxPERs_pos + 1

	#print RxPERs
	return RxPERs

current_directory = "/Users/nliu/Documents/corpdata/IOTR2/RxPER/AU"
current_search_after = "00:13:50:05:00:29:7e:aa,"
current_line_indicator = "-> 00:13:50:05:00:29:7e:aa, tan="
current_paths = findAllFiles(current_directory)
#print current_paths
current_rxpers = rawdata2list(current_directory, current_paths, current_search_after, current_line_indicator)
print current_rxpers
#print rawdata2list("/Users/nliu/Documents/corpdata/IOTR2/RxPER/AU")


		
