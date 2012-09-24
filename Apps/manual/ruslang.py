# coding=cp1251
# python utils for Russian Language project
# Author: ustaslive
# created : 2012-08-30
# last modified: 2012-08-30

import time
import os
import cProfile
import re

# todo: replace all leading tabs to 4-space as per PEP-8

# Russian Chars in files are in CP1521
# common shared variables
SOURCE_DATA_DIR_PATH=r"..\..\Data"
COLLECTED_DATA_DIR_PATH=SOURCE_DATA_DIR_PATH + r"\Collected"
CREATED_DATA_DIR_PATH=SOURCE_DATA_DIR_PATH + r"\Created"

RAW_ALL_FORMS_ACCENT_CP1251_FILE = COLLECTED_DATA_DIR_PATH + r"\RussianWords_AllForms_Accents_86xxxBases_cp1251.txt"
ALL_FORMS_CP1251_FILE = CREATED_DATA_DIR_PATH + r"\python_AllForms_CP1251.txt"

# all words which are indefinite/nominal form 
# checked and confirmed, all attributes assigned
# have accents, capitals if needed, YO, codepage 1251
NOMINAL_FINAL_CP1251_FILE = CREATED_DATA_DIR_PATH + r"\dict_nominal_c1e1r1a1.txt"

# all words which are NOT indefinite/nominal forms
# checked and confirmed, all attributes assigned
# dependencies to nominals are defined
# have accents, capitals if needed, YO, codepage 1251
ALLFORMS_FINAL_CP1251_FILE = CREATED_DATA_DIR_PATH + r"\dict_allforms_c1e1r1a1.txt"

# all unusual words - newly created, prolonged, 
# checked and confirmed, all attributes assigned
# dependencies to nominals are defined
# have accents, capitals if needed, YO, codepage 1251
UNUSUAL_CP1251_FILE = CREATED_DATA_DIR_PATH + r"\dict_unusual_c1e1r1a1.txt"

BUFFER_CP1251_FILE = CREATED_DATA_DIR_PATH + r"\dict_buffer_r1.txt"	
GENERATEDFORMS_CP1251_FILE = CREATED_DATA_DIR_PATH + r"\dict_generatedforms_r1.txt"	

# all new wordforms go through this file. being manually and automatically analyzed and put to final files
# class OperationalWordForm is saved here
#
# formats:
# 1. single word - this is how new words can be added here - just copy them to the bottom,
#		parser will recognize new word and prepare incompleteobject in memory
#		which already can be used in programs. Parser will recognize:
# 			- capital/small chars,
#			- accents if they present
#			- YO and corresponding accents
#			- single vowel words and their accents
#			- no-vowel words == no accents
#			- "-" - dash in complex words
#
#
# 2. words saved from OperationalWordForm. see *Dump* function, This has struture. Elements separated by #
#		1) UniqueID for word form, number
#			UniqueID is calcutaled once when WF is added to dict and never changed
#		2) origional form, with Capital, Smalls, with/without accents
#		3) word - =orig, but no accents
#		4) sterilized word - word, but w/o all lower case, no YO - easy to search
#		5) attributes: attr1=val1[;attr2=val2[;...]]
#
#
#
#

ALLFORMS_OPERATIONAL_CP1251_FILE = CREATED_DATA_DIR_PATH + r"\dict_operational_r1.txt"	

possiblePartsOfSpeech = {
	"u",	# unknown
	"a",	# adjective
	"n",	# noun
	"av",	# adverb
	"v",	# verb
	"pn",	# pronoun
	"p",	# preposition
	"c",	# conjunction
	"i",	# interjection, exclamation
	"nu",	# numeral
	"pa"	# grammatical particle
}

# Russian letters
# todo: replace all non-ascii chars with "\x, \u or \U escapes" as per PEP-8
RUSSIAN_SMALL_LETTERS={'а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я'}
RUSSIAN_CAPITAL_LETTERS={'А','Б','В','Г','Д','Е','Ё','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ъ','Ы','Ь','Э','Ю','Я'}
RUSSIAN_LETTERS=RUSSIAN_SMALL_LETTERS | RUSSIAN_CAPITAL_LETTERS


RUSSIAN_SMALL_VOWELS={'а','е','ё','и','о','у','ы','э','ю','я'}
RUSSIAN_CAPITAL_VOWELS={'А','Е','Ё','И','О','У','Ы','Э','Ю','Я'}
RUSSIAN_VOWELS=RUSSIAN_SMALL_VOWELS | RUSSIAN_CAPITAL_VOWELS

RUSSIAN_SMALL_CONSONANTS={'б','в','г','д','ж','з','й','к','л','м','н','п','р','с','т','ф','х','ц','ч','ш','щ','ъ','ь'}
RUSSIAN_CAPITAL_CONSONANTS={'Б','В','Г','Д','Ж','З','Й','К','Л','М','Н','П','Р','С','Т','Ф','Х','Ц','Ч','Ш','Щ','Ъ','Ь'}
RUSSIAN_CONSONANTS=RUSSIAN_SMALL_CONSONANTS | RUSSIAN_CAPITAL_CONSONANTS

RUSSIAN_VOICED_CONSONANTS={'б','в','г','д','ж','з','л','м','н','р'}
RUSSIAN_VOICELESS_CONSONANTS={'к','л','м','н','п','р','с','т','ф','х','ц','ч','ш','щ'}
RUSSIAN_PAIRS_VOICED_VOICELESS={'б':'п','в':'ф','г':'к','ж':'ш','з':'с'}
RUSSIAN_PAIRS_VOICELESS_VOICED={'п':'б','ф':'в','к':'г','ш':'ж','с':'з'}

class NonExistingPartOfSpeech(Exception):
	pass

# clear
def notAccented(word):
	return word.replace("'","")

# make all Accents chars to be _'_, not _`_, not other
def unifyAccents(word):
	return word.replace("`","'")

def countVowels(word):
	vowelCnt=0
	for c in word:
		if c in RUSSIAN_VOWELS: vowelCnt += 1
	return vowelCnt

def findAccents(word):
	accents = []
	vowelChars = countVowels(word)
	if vowelChars == 0 : # only consonants in the word, no accents
		accents = [0]
	elif vowelChars == 1: # single vowel, accent exists and the position can be calculated
		# we see a single-vowel word, but do not change it if no accents is placed in original form
		# just create "accents" attribute to reflect this
		vowelIndex=1
		for c in word:
			if c in RUSSIAN_VOWELS:
				accents = [vowelIndex]
				break
			vowelIndex += 1
	else: # multiple vowels, only marked ' and ` accents can be extracted from the word or yoYO - always accented
		# todo: words with only YO inside can have accents in other positions, this is not being calculating now
		word=word.replace('ё','ё\'').replace('Ё','Ё\'').replace("''","'")
		accents = [m.start() for m in re.finditer("'",word)]
	return accents

def getAttributes(attributes,options):
	for attrPair in attributes.split(';'):
		attr,val=attrPair.split('=')
		if attr == "part" :
			options[attr] = val
		elif attr=="acc":
			options[attr]=[ int(num) for num in val.split(',') ]
		# TODO: extend number of recognized parameters
		else:
			# TODO: test non existing parameters from dict
			print ("[MAJOR] Operational::getAttributes: word [<not implemented>]: unrecognized attribute[" + attr+"] value ["+val+"]")

	return options


class OperationalWordForm:
	def __init__(self,options):
		for param in options.keys():
			if param == "orig":
				self.original_form = options[param]
			elif param == "id":
				self.id = options[param]
			elif param == "word":
				self.word = options[param]
			elif param == 'steril':
				self.sterilized_word = options[param]
			elif param == 'acc':
				self.accents = options[param]
			elif param == 'nom':
				self.nominal = options[param]
			elif param == 'part':
				self.partOfSpeech = options[param]
			else:
				print ("[MAJOR] Operational::__init__: unrecognized internal option[" + param+"] value ["+options[param]+"]")

	@classmethod
	def fromString(cls,stringData):
		options={'id':0 }
		options['orig']=stringData.replace("`","'")
		options['word']=notAccented(options['orig'])
		# todo: for "steril" - YO needs to be converted to E
		options['steril']=options['word'].lower()
		accents = findAccents(options['orig'])
		if accents :
			options['acc']= accents
		return cls(options)

	@classmethod
	def fromDump(cls,dumpString):
		res = dumpString.split('#')
		if len(res) == 1:
			# new word is added, no ID, no other attributes are known now
			return OperationalWordForm.fromString(dumpString)

		# all parameters (except attributes) must present in file
		options={}
		options['id']=int(res[0])
		options['orig']=res[1]
		options['word']=res[2]
		# todo: for "steril" - YO needs to be converted to E
		options['steril'] = options['word'].lower()
		if len(res)>2:
			if res[3]:	# check for emptiness
				getAttributes(res[3],options)

		return cls(options)

	def strForDump(self):
		dumpString=str(self.id) + "#" + self.original_form + "#" + self.word + "#"
		if hasattr(self,'accents'):
			if self.accents:
				dumpString += "acc="+",".join(str(x) for x in self.accents)
			else:
				print ("[MAJOR] Operational::strForDump: empty accent list for word ["+self.original_form+"]")
		if hasattr(self,'partOfSpeech'):
			dumpString += ";part=" + self.partOfSpeech
		if hasattr(self,'nominal'):
			dumpString += ";nom=" + self.nominal
		return dumpString


def backupFilename(filename):
	dt = time.localtime()
	timePart = time.strftime("%Y%m%d%H%M%S",dt)
	return filename.replace(".txt","_"+timePart+".txt")

# todo: what is documentation for functions, how to create them, format?
#
# operDict is dictionary object of a format
# { word : [OperationalWordForm(), OperationalWordForm(),...] }
# where the key "word" is sterilized word form: without accent, capitalized, etc
# and OperationalWordForm - attributed object, with attrs which are determined from line in Oper file
# there can be several OperWF per key word, then can differ in pat of speach, worm, ...
#
# todo: redesign of operDict is needed. example: { UniqueID : OperationalWordForm() [,UID:OWF[,[...]]
# todo: continue: and new INDEX DICTs: as example, by "sterilized word" or by "not accented word", and other forms
# todo: continue: selection of nouns, of all LEN==2, ...
# todo: continue: probably I need o remember/save Unique ID in operfile. (?)
# todo: continue: probably UniqueID may be a part of attributes: refer to nominal as example.
def LoadOperational():
	operDict = {}
	maxID = 0
	tempDict = []
	for line in open(ALLFORMS_OPERATIONAL_CP1251_FILE):
		line=line.strip('\n')
		wf=OperationalWordForm.fromDump(line)
		if wf.id == 0:
			# new words, have no ID assigned
			tempDict.append(wf)
		else:
			operDict[wf.id] = wf
			if wf.id > maxID:
				maxID = wf.id
	newID = maxID +1
	for dItem in tempDict:
		dItem.id=newID
		operDict[newID] = dItem
		newID +=1
	return operDict

def SaveOperational(operDict):
	# backup existing Operational File
	os.rename(ALLFORMS_OPERATIONAL_CP1251_FILE,backupFilename(ALLFORMS_OPERATIONAL_CP1251_FILE))
	file = open(ALLFORMS_OPERATIONAL_CP1251_FILE,"w")
	for id in operDict.keys():
			file.write(operDict[id].strForDump() + '\n')
	file.close()

def indexed_by_sterilized(operDict):
	indexedDict = {}
	for id in operDict.keys():
		# todo: error NO serilized_word in operDict[id]
		steril_word = operDict[id].sterilized_word
		if steril_word in indexedDict.keys():
			indexedDict[steril_word].append(operDict[id])
		else:
			indexedDict[steril_word] = [operDict[id]]
	return indexedDict


def runProfiler():
	cProfile.run('LoadOperational()','LoadOperation_profile.txt')

