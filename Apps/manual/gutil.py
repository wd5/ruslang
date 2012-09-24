# coding=cp1251
# python graphical utils for Russian Language project
# Author: ustaslive
# created : 2012-00-09
# last modified: 2012-09-09

# todo: replace all leading tabs to 4-space as per PEP-8

from tkinter import *
import ruslang
import random
import re

MASK_ANY_NUMBER_OF_CHARS="*"
MASK_ANY_SINGLE_CHAR = "?"
DEFAULT_WORD_MASK=MASK_ANY_NUMBER_OF_CHARS
GUTIL_WINDOW_MIN_WIDTH=1000
GUTIL_WINDOW_MIN_HEIGHT=900
GUTIL_ANALYSIS_ONSCREEN_WORDS=30

def compileCompareOperator(mask):
	if mask=="": mask = DEFAULT_WORD_MASK
	# todo: bug ru.match('членский','ч???ск?*й') ==	True
	return re.compile("^" + mask.replace('?','.').replace('*','.*') + "$")

def match(word,comparator):
	if comparator.search(word)==None: return False
	else: return True

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

	def _parseLengthMask(self,lengthMask):
		fixLength=0
		minLength=0
		maxLength=0
		if "-" in lengthMask:
			# range of length defined
			minLength,maxLength = lengthMask.split('-')
			try:
				minLength = int(minLength)
				maxLength = int(maxLength)
				fixLength=0
				if maxLength<minLength:
					minLength=0
					maxLength=0
					# todo: where to save such strings. not in code as it may change after porting, or accident file encoding change
					self.statusUpdate("!!! Значение поля длины слова игнорировано: max<min")
				else:
					self.statusUpdate("")

			except ValueError:
				minLength=0
				maxLength=0
				lengthMask=0
				self.statusUpdate("!!! Значение поля длины слова игнорировано: некорректный формат min или max")
		elif lengthMask == "":
			fixLength=0
			minLength=0
			maxLength=0
		else:
			# exact length of the word defined
			try:
				fixLength=int(lengthMask)
				self.statusUpdate("")
			except ValueError:
				fixLength=0
				minLength=0
				maxLength=0
				self.statusUpdate("!!! Значение поля длины слова игнорировано, нецифровое значение длины слова")
		return fixLength,minLength,maxLength

	def _createColumnTitle(self,tForm,title,col):
		Label(tForm,text=title,bg='grey',relief=SUNKEN,bd=1).grid(row=0,column=col,sticky=W+E)

	def _createTitle(self,tableForm):
		col=0
		self._createColumnTitle(tableForm,"Слово",col=col); col+=1
		self._createColumnTitle(tableForm,"Номинал",col=col); col+=1
		self._createColumnTitle(tableForm,"Часть речи",col=col); col+=1

	def _createTableRow(self,tForm,word,line):
		Label(tForm,text=word,width=30,anchor=E).grid(row=line,column=0,columnspan=3)

	def _createTableRowFromDictItem(self,tForm,dictItem,line):
		Label(tForm,text=dictItem.word,width=30,anchor=E).grid(row=line,column=0)
		nominalCellForm = Frame(tForm)
		nominalCellForm.grid(row=line,column=1)

		# todo: link to real value in [dictItem]: dictItem.nominal
		nominalVar = StringVar()
		nominalVar.set("0")
		# todo: encode
		nominals=[
			("да","y"),
			("нет","n"),
			("?","0")
		]
		for lbl,val in nominals:
			Radiobutton(nominalCellForm,text=lbl,variable=nominalVar,value=val,indicatoron=0,width=2).pack(side=LEFT)

		partCellForm = Frame(tForm)
		partCellForm.grid(row=line,column=2)
		# todo: link to real value in [dictItem]: dictItem.partsOfSpeech
		partVar = StringVar()
		partVar.set("0")
		# todo: encode
		partsOfSpeech = [
			("сущ","n"),
			("прил","a"),
			("глаг","v"),
			("нареч","av"),
			("предл","p"),
			("местоим","pn"),
			("междом","i"),
			("союз","c"),
			("частица","pa"),
			("числ","nu"),
			("неизв","u"),
			("?","0")
			]
		for lbl,val in partsOfSpeech:
			Radiobutton(partCellForm,text=lbl,variable=partVar,value=val,indicatoron=0,width=6).pack(side=LEFT)

	def _fillTable(self,tableForm, mask=DEFAULT_WORD_MASK, lengthMask="",shuffle=False):
		row=0
		self._createTitle(tableForm)

		row+=1
		if ((not MASK_ANY_NUMBER_OF_CHARS in mask) and (not MASK_ANY_SINGLE_CHAR in mask)):
			# no mask special chars means exact word match. ignoring length.
			if mask in self.operational.keys():
				# todo: must list not only [0] element but all matching [mask]
				self._createTableRowFromDictItem(tableForm,self.operational[mask][0],row);	row+=1
			else:
				# todo: encode
				self._createTableRow(tableForm,"слово ["+mask+"] не найдено",row);	row+=1
			return

		fixLength,minLength,maxLength=self._parseLengthMask(lengthMask)

		# TODO: table need headers
		# TODO: table need to be dynamic: part of speech, sex if any
		k = list(self.operational.keys())
		kLen = len(k)
		# TODO: no need to shuffle every time, expecialy when exact match is requested
		if shuffle:	random.shuffle(k)

		if mask == DEFAULT_WORD_MASK or mask == "":
			# no char mask, only LENGTH is counted
			for i in range(0,kLen):
				if self._passLengthCriteria(len(k[i]),fixLength,minLength,maxLength):
					# todo: must list not only [0] element but all matching k[i]
					self._createTableRowFromDictItem(tableForm,self.operational[k[i]][0],row); row += 1
					if row >= GUTIL_ANALYSIS_ONSCREEN_WORDS:
						break
		else:
			comparator=compileCompareOperator(mask)
			for i in range(0,kLen):
				if self._passLengthCriteria(len(k[i]),fixLength,minLength,maxLength) and comparator.match(k[i]) :
					# todo: must list not only [0] element but all matching k[i]
					self._createTableRowFromDictItem(tableForm,self.operational[k[i]][0],row); row+=1
					if row >= GUTIL_ANALYSIS_ONSCREEN_WORDS:
						break
		if row <=1 :	# only title was printed
			# todo: encode
			self._createTableRow(tableForm,"по шаблону ["+mask+"] ничего не найдено",0)

	def _refreshWordList(self):
		self.tableForm.destroy()
		self.tableForm = Frame(self.analysisForm)
		self.tableForm.grid(row=2,column=0,columnspan=5)
		self._fillTable(self.tableForm,mask=self.analysisMask.get(), lengthMask=self.lengthMask.get())

	def _shuffleWordList(self):
		self.tableForm.destroy()
		self.tableForm = Frame(self.analysisForm)
		self.tableForm.grid(row=2,column=0,columnspan=5)
		self._fillTable(self.tableForm,mask=self.analysisMask.get(), lengthMask=self.lengthMask.get(),shuffle=True)


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

		# todo: encode
		Label(self.analysisForm,text="Анализ словоформ",fg="blue",anchor=W,height=2).grid(row=0,column=0,sticky=W)

		entryForm = Frame(self.analysisForm)
		entryForm.grid(row=1,column=0,columnspan=5,sticky=W)

		# 1.
		# todo: encode
		Label(entryForm,text="Шаблон:").pack(side=LEFT)

		# 2.
		self.analysisMask = self._createMaskEntry(entryForm)
		self.analysisMask.pack(side=LEFT)

		# 2.5
		self.lengthMask = self._createLengthEntry(entryForm)
		self.lengthMask.pack(side=LEFT)

		# 2.6 todo: match words in dict with YO with E in mask

		# 3.
		# todo: encode
		Button(entryForm,text="Обновить",command=self._refreshWordList).pack(side=LEFT)

		# 3.5
		# todo: encode
		Button(entryForm,text="Встряхнуть",command=self._shuffleWordList).pack(side=LEFT)

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
		# todo: encode
		self.statusUpdate("Загрузка необработанных словоформ... ждите")
		self.operational = ruslang.LoadOperational()
		# todo: encode
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
		# todo: encode
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
