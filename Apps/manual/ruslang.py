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

import re
# an instance of a particular word form
class WordForm:
	def __init__(self,wf):
		self.word=wf
		self.word.replace("`","'") # normalize accent chars
		self.accents=[m.start() for m in re.finditer("'",seld.word)]
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

class InitialWordForm(WordForm):
	def __init__(self,word,chastRechi=None):
		WordForm.__init__(self,word)
		self.chastRechi=chastRechi
