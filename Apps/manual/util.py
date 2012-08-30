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

if __name__ == '__main__':
	readRaw()
	print(len(plainWordInitialForms))
	print(len(plainWordAllForms))

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
