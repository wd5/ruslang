# python utils for Russian Language project
# Author: ustaslive
# created : 2012-08-30
# last modified: 2012-08-30

# common shared variables
SOURCE_DATA_DIR_PATH=r"..\..\Data"
COLLECTED_DATA_DIR_PATH=SOURCE_DATA_DIR_PATH + r"\Collected"
CREATED_DATA_DIR_PATH=SOURCE_DATA_DIR_PATH + r"\Created"

RAW_ALL_FORMS_ACCENT_CP1251_FILE = COLLECTED_DATA_DIR_PATH + r"\RussianWords_AllForms_Accents_86xxxBases_cp1251.txt"
ALL_FORMS_CP1251_FILE = CREATED_DATA_DIR_PATH + r"\python_AllForms_CP1251.txt"

class wordForm:
	def __init__(self,wf):
		self.word=wf.replace("'","")
		self.len=len(self.word)
		self.accents=[]
		self.accents.append(wf.find("'")-1) # there can be more than 1 accent
	def print(self):
		print(self.word, self.len, self.accents)

	def equal(self,word):
		if type(word) is str:
			word = wordForm(word)
		if type(word) is wordForm:
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

