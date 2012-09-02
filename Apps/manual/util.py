# python utils for Russian Language project
# Author: ustaslive
# created : 2012-08-30
# last modified: 2012-08-30

import ruslang as rl

plainWordInitialForms={}
plainWordAllForms={}

def removeAccents(w):
	return w.replace("`","").replace("'","")

# create full sent of non-accented word forms from the file
# all words are lowercase
def readRawPlain():
	plainWordForms=set([])
	for line in open(rl.RAW_ALL_FORMS_ACCENT_CP1251_FILE,"r"):
		line=line.rstrip('\n')
		initialWord,wordForms = line.split('#')
		wordForms = removeAccents(wordForms)
		wordForms = word.lower()

		for w in wordForms.split(','):
			plainWordForms.add(w)
	return plainWordForms

def duplicateYOwords(dictSet):
	yoWords = set([])
	for w in dictSet:
		if 'ё' in w:
			yoWords.add(w.replace('ё','е'))
	for w in yoWords:
		dictSet.add(w)

def chaset(w):
	cc={}
	for c in w:
		if c in cc.keys():
			cc[c] = cc[c]+1
		else:
			cc[c] = 1 ;
	result=""
	ks=list(cc.keys())
	ks.sort()
	for c in ks:
		result = result + c+str(cc[c])
	return result

# group anagrams
def groupAnagrams(dict):
	anagrams = {}
	for w in dict:
		cc=chaset(w)
		if cc in anagrams.keys():
			anagrams[cc].append(w)
		else:
			anagrams[cc] = [w]
	return anagrams

def findAnagrams(anagrams,word):
	chaset = chaset(word)
	if chaset in anagrams.keys():
		return anagrams[chaset(word)]
	return [chaset]

# save groupped anagrams
# do not save words which do now have an anagram - single
def writeAnagrams(anagrams):
	anaSizes = {}   # sizes of groups
	for cc in anagrams.keys():
		sz = len(anagrams[cc])
		if sz <= 1 : continue   # at least 2 words must exist for anagram
		if sz in anaSizes.keys():
			anaSizes[sz].append(cc)
		else:
			anaSizes[sz] = [cc]
	szKeys = list(anaSizes.keys())
	szKeys.sort(key=None,reverse=True)

	size=len(anagrams)
	fname=filename(rl.CREATED_DATA_DIR_PATH + r"\anagrams_cp1251_"+str(size))
	f=open(fname,"w")

	for size in szKeys:
		chasetList = anaSizes[size]
		for cc in chasetList:
			wordList = anagrams[cc]
			wordList.sort()
			f.write(cc+":"+",".join(wordList)+"\n")
	f.close()

def writeRawPlain(plainWordForms):
	pwf = set(plainWordForms)
	size=len(pwf)
	fname=filename(rl.CREATED_DATA_DIR_PATH + r"\plain_word_forms_cp1251_"+str(size))
	f=open(fname,"w")
	for w in pwf :
		f.write(w+"\n")
	f.close()

def updateFiles():
	print("Loading word worms file...",end="")
	fullWordFormSet=readRawPlain()
	print("done",end="\n")

	print("Populating word form set with non-YO duplicates...",end="")
	duplicateYOwords(fullWordFormSet)
	print("done",end="\n")

	print("Generating anagram's list...",end="")
	grouppedAnagrams = groupAnagrams(fullWordFormSet)
	print("done",end="\n")

	print("Saving word forms...",end="")
	writeRawPlain(fullWordFormSet)
	print("done",end="\n")

	print("Saving anagrams...",end="")
	writeAnagrams(grouppedAnagrams)
	print("done",end="\n")

import time

def filename(keyword):
	dt = time.gmtime()
	timePart = time.strftime("_%Y%m%d%H%M%S",dt)
	return keyword + timePart + ".txt"

##if __name__ == '__main__':
##	readRaw()
##	print(len(plainWordInitialForms))
##	print(len(plainWordAllForms))

def _testYO():
	dt_test1_start=time.gmtime()
	dt_test1_end=time.gmtime()
	dt_test2_start=time.gmtime()
	dt_test2_end=time.gmtime()
	print("Test 1:", dt_test1_end-dt_test1_start)
	print("Test 2:", dt_test2_end-dt_test2_start)




if __name__ == '__main__':
	updateFiles()
