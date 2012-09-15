# coding=cp1251
# python graphical utils for Russian Language project
# Author: ustaslive
# created : 2012-00-09
# last modified: 2012-09-09

from tkinter import *
import ruslang
import random

DEFAULT_WORD_MASK="*"
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
		# TODO: below labels should be check box of attributes from dictionary
		Label(tForm,text="x",width=3).grid(row=line,column=1)
		Label(tForm,text="y",width=3).grid(row=line,column=2)

	def _fillTable(self,tableForm, mask=DEFAULT_WORD_MASK):
		# TODO: table need headers
		# TODO: table need to be dynamic
		k = list(self.operational.keys())
		klen = len(k)
		random.shuffle(k)
		# TODO: convert "* ? " template to regural expression
		if mask == DEFAULT_WORD_MASK or mask == "":
			for i in range(0,GUTIL_ANALYSIS_ONSCREEN_WORDS):
				if i<klen:
					self._createCell(tableForm,k[i],i)
		else:
			if mask.startswith(DEFAULT_WORD_MASK):
				mask=mask.replace(DEFAULT_WORD_MASK,"")
				cnt=0
				for i in range(0,klen):
					if k[i].endswith(mask):
						self._createCell(tableForm,k[i],i)
						cnt+=1
						if cnt >= GUTIL_ANALYSIS_ONSCREEN_WORDS:
							return
			else:
				if mask.endswith(DEFAULT_WORD_MASK):
					mask=mask.replace(DEFAULT_WORD_MASK,"")
					cnt=0
					for i in range(0,klen):
						if k[i].startswith(mask):
							self._createCell(tableForm,k[i],i)
							cnt+=1
							if cnt >= GUTIL_ANALYSIS_ONSCREEN_WORDS:
								return


	def _refreshWordList(self):
		self.tableForm.destroy()
		self.tableForm = Frame(self.analysisForm)
		self.tableForm.grid(row=2,column=0,columnspan=5)
		self._fillTable(self.tableForm,mask=self.analysisMask.get())

	def maskEnterCallback(self,event):
		self._refreshWordList()

	def _createMaskEntry(self,form):
		mask=Entry(form,width=20)
		mask.delete(0, END)
		mask.insert(0, DEFAULT_WORD_MASK)
		mask.focus_set()
		mask.bind('<Return>', self.maskEnterCallback)
		return mask

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
