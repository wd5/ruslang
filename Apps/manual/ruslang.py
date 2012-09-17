# python utils for Russian Language project
# Author: ustaslive
# created : 2012-08-30
# last modified: 2012-08-30

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
ALLFORMS_OPERATIONAL_CP1251_FILE = CREATED_DATA_DIR_PATH + r"\dict_operational_r1.txt"	

import re

possiblePartsOfSpeech = {"u","a","n","av","v","pn","p","c","i","nu","pa"}

# Russian letters
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
				self.originalForm = options[param]
			elif param == "word":
				self.word = options[param]
			elif param == 'steril':
				self.sterilizedWord = options[param]
			elif param == 'acc':
				self.accents = options[param]
			elif param == 'part':
				self.partOfSpeech = options[param]
			else:
				print ("[MAJOR] Operational::__init__: unrecognized internal option[" + param+"] value ["+options[param]+"]")

	@classmethod
	def fromString(cls,stringData):
		options={}
		options['orig']=stringData.replace("`","'")
		options['word']=notAccented(options['orig'])
		options['steril']=options['word'][:]
		accents = findAccents(options['orig'])
		if accents :
			options['acc']= accents
		return cls(options)

	@classmethod
	def fromDump(cls,dumpString):
		options={}
		res = dumpString.split('#')
		options['orig']=res[0]
		if len(res)>1:
			options['word']=res[1]
			options['steril'] = res[1].lower()
			if len(res)>2:
				if res[2]:	# check for emptiness
					getAttributes(res[2],options)
			else:
				pass
		else:
			# evidences are that this is newly added word, extracting all possible info from it
			return OperationalWordForm.fromString(dumpString)
		return cls(options)

	def strForDump(self):
		dumpString=self.originalForm + "#" + self.word + "#"
		if hasattr(self,'accents'):
			if self.accents:
				dumpString += "acc="+",".join(str(x) for x in self.accents)
			else:
				print ("[MAJOR] Operational::strForDump: empty accent list for word ["+self.originalForm+"]")
		if hasattr(self,'partOfSpeech'):
			dumpString += ";part=" + self.partOfSpeech
		return dumpString

	def setPart(self,part):
		if part in possiblePartsOfSpeech:
			self.partOfSpeech=part
		else:
			raise NonExistingPartOfSpeech

# an instance of a particular word form
class WordForm:

	def findAccents(self):
		return [m.start() for m in re.finditer("'", self.word)]

	def __init__(self,wf):
		self.word=wf
		self.word.replace("`","'") # normalize accent chars
		self.accents=self.findAccents()
		self.word = self.notAccented()
		self.len=len(self.word)

	def print(self):
		print(self.word, self.len, self.accents)
	def notAccented(self):
		return self.word.replace("'","")

	def equal(self,word):
		if type(word) is str:
			word = WordForm(word)
		if type(word) is WordForm:
			# type == wordForm
			if self.len != word.len: return False
			if self.word != word.word: return False
			if self.accents != word.accents: return False
			return True
		else:
			print("error 0001: class wordForm/equal()/unexpected type of WORD parameter")
			return False

	# prepare and retunr string which contains all attributes of the word form
	def formatForDump(self):
		return "not defined"
	# load all attributes to SELF from string passed (string is taken from wordForm file
	def loadFromDump(self,line):
		pass
			

class InitialWordForm(WordForm):
	def __init__(self,word,partOfSpeech=None):
		WordForm.__init__(self,word)
		self.partOfSpeech=partOfSpeech

import time
import os

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
def LoadOperational():
	operDict = {}
	for line in open(ALLFORMS_OPERATIONAL_CP1251_FILE):
		line=line.strip('\n')
		wf=OperationalWordForm.fromDump(line)
		# todo: keyword is sterilized word. can match several different original forms. change ID to something "word:1" to have plain array
		if wf.sterilizedWord in operDict.keys():
			operDict[wf.sterilizedWord].append(wf)
		else:
			operDict[wf.sterilizedWord] = [wf]
	return operDict

def SaveOperational(operDict):
	# backup existing Operational File
	os.rename(ALLFORMS_OPERATIONAL_CP1251_FILE,backupFilename(ALLFORMS_OPERATIONAL_CP1251_FILE))
	file = open(ALLFORMS_OPERATIONAL_CP1251_FILE,"w")
	for word in operDict.keys():
		for operwf in operDict[word]:
			file.write(operwf.strForDump() + '\n')
	file.close()

import cProfile
def runProfiler():
	cProfile.run('LoadOperational()','LoadOperation_profile.txt')

