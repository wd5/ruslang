# coding=cp1251
# python graphical utils for Russian Language project
# Author: ustaslive
# created : 2012-00-09
# last modified: 2012-09-09

from tkinter import *
import ruslang
import random

MASK_ANY_NUMBER_OF_CHARS="*"
MASK_ANY_SINGLE_CHAR = "?"
DEFAULT_WORD_MASK=MASK_ANY_NUMBER_OF_CHARS
GUTIL_WINDOW_MIN_WIDTH=500
GUTIL_WINDOW_MIN_HEIGHT=900
GUTIL_ANALYSIS_ONSCREEN_WORDS=30

class Gutil:

	def callbackWindowDeleted(self):
		print("info: window is being closed: do nothing at the moment, 2012-09-10")
		print("future: save unsaved data")
		self.rootTk.destroy()
		#self.rootTk.quit()

	def	quit(self):
		self.rootTk.quit()

	def dummyCallback(self):
		pass

	def aboutCallback(self):
		self.dummyCallback()

	def _createCell(self,tForm,word,line):
		Label(tForm,text=word,width=30,anchor=E).grid(row=line,column=0)
		# TODO: below labels should be radio box of attributes from dictionary 1.: part of speech

		Label(tForm,text="x",width=3).grid(row=line,column=1)
		Label(tForm,text="y",width=3).grid(row=line,column=2)

	def _passLengthCriteria(self,wordLength,fixLength,minLength,maxLength):
		if fixLength == 0 :
			if minLength==0 and maxLength==0:
				return True
			else:
				if minLength<=wordLength<=maxLength :
					return True
				else:
					return False
		else:
			if wordLength == fixLength:
				return True
			else:
				return False
		return True

	def _fillTable(self,tableForm, mask=DEFAULT_WORD_MASK, length=""):
		if ( (not MASK_ANY_NUMBER_OF_CHARS in mask) and (not MASK_ANY_SINGLE_CHAR in mask)):
			if mask in self.operational.keys():
				self._createCell(tableForm,mask,0)
			else:
				self._createCell(tableForm,"слово ["+mask+"] не найдено",0)
		fixLength=0
		minLength=0
		maxLength=0
		if "-" in length:
			# range of length defined
			minLength,maxLength = length.split('-')
			try:
				minLength = int(minLength)
				maxLength = int(maxLength)
				fixLength=0
				if maxLength<minLength:
					minLength=0
					maxLength=0
					self.statusUpdate("!!! Значение поля длины слова игнорировано: max<min")
				else:
					self.statusUpdate("")

			except ValueError:
				minLength=0
				maxLength=0
				length=0
				self.statusUpdate("!!! Значение поля длины слова игнорировано: некорректный формат min или max")
		else:
			# exact length of the word defined
			try:
				fixLength=int(length)
				self.statusUpdate("")
			except ValueError:
				fixLength=0
				minLength=0
				maxLength=0
				self.statusUpdate("!!! Значение поля длины слова игнорировано, нецифровое значение длины слова")

		# TODO: table need headers
		# TODO: table need to be dynamic: part of speech, sex if any
		k = list(self.operational.keys())
		kLen = len(k)
		random.shuffle(k)
		# TODO: convert "* ? " template to regural expression
		if mask == DEFAULT_WORD_MASK or mask == "":
			row=0
			for i in range(0,kLen):
				if self._passLengthCriteria(len(k[i]),fixLength,minLength,maxLength):
					self._createCell(tableForm,k[i],row)
					row += 1
					if row >= GUTIL_ANALYSIS_ONSCREEN_WORDS:
						return

		elif mask.startswith(DEFAULT_WORD_MASK):
			# todo: try "RE" here - will it improve performance?
			mask=mask.replace(DEFAULT_WORD_MASK,"")
			row=0
			for i in range(0,kLen):
				if k[i].endswith(mask) and self._passLengthCriteria(len(k[i]),fixLength,minLength,maxLength):
					self._createCell(tableForm,k[i],row)
					row+=1
					if row >= GUTIL_ANALYSIS_ONSCREEN_WORDS:
						return
		else:
			if mask.endswith(DEFAULT_WORD_MASK):
				mask=mask.replace(DEFAULT_WORD_MASK,"")
				row=0
				for i in range(0,kLen):
					if k[i].startswith(mask) and self._passLengthCriteria(len(k[i]),fixLength,minLength,maxLength):
						self._createCell(tableForm,k[i],row)
						row+=1
						if row >= GUTIL_ANALYSIS_ONSCREEN_WORDS:
							return

	def _refreshWordList(self):
		self.tableForm.destroy()
		self.tableForm = Frame(self.analysisForm)
		self.tableForm.grid(row=2,column=0,columnspan=5)
		self._fillTable(self.tableForm,mask=self.analysisMask.get(),length=self.lengthMask.get())

	def maskEnterCallback(self,event):
		self._refreshWordList()

	def _createMaskEntry(self,form):
		mask=Entry(form,width=20)
		mask.delete(0, END)
		mask.insert(0, DEFAULT_WORD_MASK)
		mask.focus_set()
		mask.bind('<Return>', self.maskEnterCallback)
		return mask

	def _createLengthEntry(self,form):
		length=Entry(form,width=6)
		length.bind('<Return>', self.maskEnterCallback)
		return length

	def _createAnalysisForm(self):	
		self.analysisForm=Frame(self.rootTk)
		self.analysisForm.pack(fill=BOTH,padx=10)

		Label(self.analysisForm,text="Анализ словоформ",fg="blue",anchor=W,height=2).grid(row=0,column=0)

		entryForm = Frame(self.analysisForm)
		entryForm.grid(row=1,column=0,columnspan=5)

		# 1.
		Label(entryForm,text="Шаблон:").pack(side=LEFT)

		# 2.
		self.analysisMask = self._createMaskEntry(entryForm)
		self.analysisMask.pack(side=LEFT)

		# 2.5 TODO: need entry field for word length: num = exactly, num1-num2 - between num1 and num2, empty or incorrect syntax - any
		self.lengthMask = self._createLengthEntry(entryForm)
		self.lengthMask.pack(side=LEFT)

		# 3.
		Button(entryForm,text="Обновить",command=self._refreshWordList).pack(side=LEFT)

		# 4.
		self.tableForm = Frame(self.analysisForm)
		self.tableForm.grid(row=2,column=0,columnspan=5)
		self._fillTable(self.tableForm)

		return self.analysisForm
		
	def statusUpdate(self,newStatus):
		self.statusbar['text'] = newStatus
	
	def loadRawWordForms(self,forceLoad=False):
		if not forceLoad and self.allFormsOperationalLoaded:
			return
		self.statusUpdate("Загрузка необработанных словоформ... ждите")
		self.operational = ruslang.LoadOperational() 
		self.statusUpdate("Необработанные словоформы загружены")
		self.allFormsOperationalLoaded = True
		
	def switchToAnalyzeRawWordForms(self):
		self.currentForm.destroy()
		self.loadRawWordForms(forceLoad=True)
		self.currentForm = self._createAnalysisForm()
	
	def saveCurrentChanges(self):
		ruslang.SaveOperational(self.operational)


	def _createMenu(self):
		menu=Menu(self.rootTk)
		self.rootTk.config(menu=menu)
		self.filemenu=Menu(menu)
		menu.add_cascade(label="Файлы",menu=self.filemenu)
		self.filemenu.add_command(label="Открыть Недообработанные", command=self.switchToAnalyzeRawWordForms)
		self.filemenu.add_command(label="Открыть Номиналы", command=self.dummyCallback)
		self.filemenu.add_command(label="Сохранить изменения", command=self.saveCurrentChanges)
		self.filemenu.add_command(label="Выход", command=self.quit)
		
		self.dictmenu=Menu(menu)
		menu.add_cascade(label="Словарь",menu=self.dictmenu)
		self.dictmenu.add_command(label="Номиналы", command=self.dummyCallback)
		self.dictmenu.add_command(label="Словоформы", command=self.dummyCallback)
		self.dictmenu.add_separator()
		self.dictmenu.add_command(label="Из файла...", command=self.dummyCallback)
		
		self.helpmenu=Menu(menu)
		menu.add_cascade(label="Помощь",menu=self.helpmenu)
		self.helpmenu.add_command(label="О программе...", command=self.aboutCallback)
		
	def _createStatusBar(self):
		self.statusbar = Label(self.rootTk, text="...", bd=1, relief=SUNKEN, anchor=W)
		self.statusbar.pack(side=BOTTOM, fill=X)

	def _createInitForm(self):
		self.initForm=Frame(self.rootTk)
		self.initForm.pack(fill=BOTH,padx=10)
		Label(self.initForm,text="Статистика по базам данным",fg="blue",anchor=W,height=2).grid(row=0,column=0)

		Label(self.initForm,text="Всего слов в базе данных :",anchor=W,width=25).grid(row=1,column=0)
		Label(self.initForm,text="150 000",anchor=E,bd=1,relief=SUNKEN,width=10).grid(row=1,column=1)
		
		Label(self.initForm,text="Номинальных :",anchor=W,width=25).grid(row=2,column=0)
		Label(self.initForm,text="10 000",anchor=E,bd=1,relief=SUNKEN,width=10).grid(row=2,column=1)
		
		Label(self.initForm,text="Странных :",anchor=W,width=25).grid(row=3,column=0)
		Label(self.initForm,text="5 000",anchor=E,bd=1,relief=SUNKEN,width=10).grid(row=3,column=1)
		
		Label(self.initForm,text="Корней :",anchor=W,width=25).grid(row=4,column=0)
		Label(self.initForm,text="3 000",anchor=E,bd=1,relief=SUNKEN,width=10).grid(row=4,column=1)

		Label(self.initForm,text="Самодельных :",anchor=W,width=25).grid(row=5,column=0)
		Label(self.initForm,text="3 000",anchor=E,bd=1,relief=SUNKEN,width=10).grid(row=5,column=1)
		return self.initForm
		
		
	def __init__(self):
		self.rootTk = Tk()
		self.rootTk.minsize(GUTIL_WINDOW_MIN_WIDTH,GUTIL_WINDOW_MIN_HEIGHT)
		self.rootTk.title("Словооборот")
		self.rootTk.wm_iconbitmap('ruslang.ico')
		self.rootTk.protocol('WM_DELETE_WINDOW', self.callbackWindowDeleted)
		
		self._createMenu()
		# TODO: create tool bar with icons
		self._createStatusBar()
		self.currentForm=self._createInitForm()
		
		self.allFormsOperationalLoaded = False 
	

	def restoreLastState(self):
		pass
		
	def run(self):
		self.rootTk.mainloop()



def run():
	gu = Gutil()
	gu.restoreLastState()
	gu.run()


if __name__ == "__main__":
	run()
