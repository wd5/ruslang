# python utils for Russian Language project
# Author: ustaslive
# created : 2012-08-30
# last modified: 2012-08-30

import ruslang as rl


plainWordInitialForms={}
plainWordAllForms={}

def removeAccents(w):
	return w.replace("`","").replace("'","")

def readRaw():
	global plainWordInitialForms
	plainWordInitialForms={}
	global plainWordAllForms
	plainWordAllForms={}

	for line in open(rl.RAW_ALL_FORMS_ACCENT_CP1251_FILE,"r"):
		line=line.rstrip('\n')
		initialWord,wordForms = line.split('#')
		iword =removeAccents(initialWord)
		plainWordInitialForms[iword]=[]

		for w in wordForms.split(','):
			w=removeAccents(w)
			if w in plainWordAllForms.keys():
				plainWordAllForms[w].append(iword)
			else:
				plainWordAllForms[w] = [iword]
			plainWordInitialForms[iword].append(w)

# create full sent of non-accented word forms from the file
def readRawPlain():
	plainWordForms=set([])

	for line in open(rl.RAW_ALL_FORMS_ACCENT_CP1251_FILE,"r"):
		line=line.rstrip('\n')
		initialWord,wordForms = line.split('#')
		wordForms = removeAccents(wordForms)

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

def charCounter(w):
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

def generateCharCounters(dict):
	return {w:charCounter(w) for w in dict}

def groupCharCounters(dict):
	gcc = {}
	for w in dict:
		cc=charCounter(w)
		if cc in gcc.keys():
			gcc[cc].append(w)
		else:
			gcc[cc] = [w]
	return gcc

# grouppedCharCounters
def writeCharCounters(gcc):
	gccSizes = {}   # sizes of groups
	for cc in gcc.keys():
		sz = len(gcc[cc])
		if sz in gccSizes.keys():
			gccSizes[sz].append(cc)
		else:
			gccSizes[sz] = [cc]
	szKeys = list(gccSizes.keys())
	szKeys.sort(key=None,reverse=True)

	size=len(gcc)
	filename=rl.CREATED_DATA_DIR_PATH + "\char_counters_cp1251_"+str(size)+".txt"
	f=open(filename,"w")

	for size in szKeys:
		charCounterList = gccSizes[size]
		for cc in charCounterList:
			wordList = gcc[cc]
			wordList.sort()
			f.write(cc+":"+",".join(wordList)+"\n")
	f.close()

def writeRawPlain(plainWordForms):
	pwf = set(plainWordForms)
	size=len(pwf)
	filename=rl.CREATED_DATA_DIR_PATH + "\plain_word_forms_cp1251_"+str(size)+".txt"
	f=open(filename,"w")
	for w in pwf :
		f.write(w+"\n")
	f.close()

def updateFiles():
	fullWordFormSet=readRawPlain()
	duplicateYOwords(fullWordFormSet)
	grouppedCharCounters = groupCharCounters(fullWordFormSet)
	writeRawPlain(fullWordFormSet)
	writeCharCounters(grouppedCharCounters)


##if __name__ == '__main__':
##	readRaw()
##	print(len(plainWordInitialForms))
##	print(len(plainWordAllForms))

if __name__ == '__main__':
	updateFiles()


wordInitialForms={} # string : [InitialWordForm()]
wordAllForms={}     # string : []

def readRaw2():
	for line in open(rl.RAW_ALL_FORMS_ACCENT_CP1251_FILE,"r"):

		initialWord,wordForms = line.split('#')

		iWord = l.InitialWordForm(initialWord)

		wordInitialForms[iWord.word]=[iWord]
		for w in wordForms.split(','):
			wf=rl.WordForm(w)
			wordAllForms.add(w)

		if initialWord in formDict :
			pass
		else:
			formDict[initialWord] = wordForms.split(',')
