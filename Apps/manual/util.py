# python utils for Russian Language project
# Author: ustaslive
# created : 2012-08-30
# last modified: 2012-08-30

import ruslang as rl

def readRaw():
	formDict = {}
	allWords = set([])
	for line in open(rl.RAW_ALL_FORMS_ACCENT_CP1251_FILE,"r"):

		initialWord,wordForms = line.split('#')
		wordForms = wordForms.split(',')

		allWords.add(initialWord)
		for w in wordForms: allWords.add(w)

		if initialWord in formDict :
			pass
		else:
			formDict[initialWord] = wordForms

	return formDict,set(allWords)


