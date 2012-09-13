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
class NonExistingPartOfSpeech(Exception):
	pass


class OperationalWordForm:

	def notAccented(self):
		return self.originalForm.replace("'","").replace("`","")
		
	def findAccents(self): #dummy yet
		self.accents=[]
		numOfAccents=0
		for i in range(0,len(self.originalForm)):
			if self.originalForm[i] in "'`":
				self.accents.append(i-numOfAccents)
				numOfAccents += 1		# CHAR position in string shifts with accents inside
		return self.accents

	def __init__(self,original=""):
		self.originalForm=original
		self.word=self.notAccented()
		self.sterelizedWord = self.word[:]
		self.findAccents()
		
		
	def _getAttributes(self,attributes):
		print("debug: test")
		for attrPair in attributes.split(';'):
			print("debug: attrpair:" + str(attrPair)) 
			attr,val=attrPair.split('=')
			if attr == "part" :
				self.partOfSpeech=val
			else: 
				if attr=="acc":
					self.accents=val.split(',')
				else:
					print ("[MAJOR] Operational::getAttrib: word [<not implemented>]: unrecognized attribute[" + attr+"] value ["+val+"]")
				
		
	def initFromDump(self,dumpString):
		res = dumpString.split('#')
		self.originalForm=res[0]
		if len(res)>1:
			self.word=res[1]
			if len(res)>2:
				self._getAttributes(res[2])
			else:
				pass
		else:
			self.word=self.notAccented()
			self.accents = self.findAccents()
	
	def strForDump(self):
		dumpString=self.word + "#"+ self.originalForm + "#" + ",".join(self.accents)
		if hasattr(self,'partOfSpeech'):
			dumpString = dumpString + ";" + self.partOfSpeech
		
		return dumpString

	def setPart(self,part):
		if part in possiblePartsOfSpeech:
			self.partOfSpeech=part
		else:
			raise NonExistingPartOfSpeech
		


# an instance of a particular word form
class WordForm:
	def __init__(self,wf):
		self.word=wf
		self.word.replace("`","'") # normalize accent chars
		self.accents=[m.start() for m in re.finditer("'",self.word)]
		self.word = notAccented()
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
			pass
		else:
			print("error 0001: class wordForm/equal()/unexpected type of WORD parameter")
			return False
		return False
	# prepare and retunr string which contains all attributes of the word form
	def formatForDump(self):
		return "not defined"
	# load all attributes to SELF from string passed (string is taken from wordForm file
	def loadFromDump(self,line):
		pass
			

class InitialWordForm(WordForm):
	def __init__(self,word,chastRechi=None):
		WordForm.__init__(self,word)
		self.chastRechi=chastRechi

		
import time
import os

def backupFilename(filename):
	dt = time.localtime()
	timePart = time.strftime("%Y%m%d%H%M%S",dt)
	return filename.replace(".txt","_"+timePart+".txt")
		
#
# operDict is "dictionary" object of a format
# { "word" : [OperationalWordForm(), OperationalWordForm(),...] }
# where the key "word" is sterelized word form: without accent, capitalized, etc 
# and OperationalWordForm - attributed object, with attrs which are determined from line in Oper file
# there can be several OperWF per key word, then can differ in pat of speach, worm, ...
#
def LoadOperational():
	operDict = {}
	for line in open(ALLFORMS_OPERATIONAL_CP1251_FILE):
		wf=OperationalWordForm()
		wf.initFromDump(line)
		if wf.sterelizedWord in operDict.keys():
			operDict[wf.sterelizedWord].append(wf)
		else:
			operDict[wf.sterelizedWord] = [wf]
	return operDict

def SaveOperational(operDict):
	# backup existing Operational File
	os.rename(ALLFORMS_OPERATIONAL_CP1251_FILE,backupFilename(ALLFORMS_OPERATIONAL_CP1251_FILE))
	file = open(ALLFORMS_OPERATIONAL_CP1251_FILE,"w")
	for word in operDict.keys():
		for operwf in operDict[word]:
			file.write(operwf.strForDump() + '\n')
	file.close()

