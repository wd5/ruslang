# coding=cp1251
# python graphical utils for Russian Language project
# Author: ustaslive
# created : 2012-00-09
# last modified: 2012-09-09

from tkinter import *
import ruslang

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

	def _createAnalysisForm(self):	
		self.analysisForm=Frame(self.rootTk)
		self.analysisForm.pack(fill=BOTH,padx=10)
		
		Label(self.analysisForm,text="������ ���������",fg="blue",anchor=W,height=2).grid(row=0,column=0)
		
		entryForm = Frame(self.analysisForm)
		entryForm.grid(row=1,column=0,columnspan=5)
		Label(entryForm,text="������:").pack(side=LEFT)
		Entry(entryForm,width=20).pack(side=LEFT)
		Button(entryForm,text="��������").pack(side=LEFT)
		
		tableForm = Frame(self.analysisForm)
		tableForm.grid(row=2,column=0,columnspan=5)
		
		Label(tableForm,text="�����").grid(row=0,column=0)
		Label(tableForm,text="x").grid(row=0,column=1)
		Label(tableForm,text="y").grid(row=0,column=2)
		
		Label(tableForm,text="�����").grid(row=1,column=0)
		Label(tableForm,text="x").grid(row=1,column=1)
		Label(tableForm,text="y").grid(row=1,column=2)
		
		Label(tableForm,text="�����").grid(row=2,column=0)
		Label(tableForm,text="x").grid(row=2,column=1)
		Label(tableForm,text="y").grid(row=2,column=2)
		

		
		
		return self.analysisForm
		
	def statusUpdate(self,newStatus):
		self.statusbar['text'] = newStatus
	
	def loadRawWordForms(self):
		if self.allFormsOperationalLoaded == True : return
		self.statusUpdate("�������� �������������� ���������... �����")
		self.operational = ruslang.LoadOperational() 
		self.statusUpdate("�������������� ���������� ���������")
		self.allFormsOperationalLoaded = True
		
	def switchToAnalyzeRawWordForms(self):
		self.currentForm.destroy()
		self.loadRawWordForms()
		self.currentForm = self._createAnalysisForm()
	
	def saveCurrentChanges(self):
		pass

	def _createMenu(self):
		menu=Menu(self.rootTk)
		self.rootTk.config(menu=menu)
		self.filemenu=Menu(menu)
		menu.add_cascade(label="�����",menu=self.filemenu)
		self.filemenu.add_command(label="������� ����������������", command=self.switchToAnalyzeRawWordForms)
		self.filemenu.add_command(label="������� ��������", command=self.dummyCallback)
		self.filemenu.add_command(label="��������� ���������", command=self.saveCurrentChanges)
		self.filemenu.add_command(label="�����", command=self.quit)
		
		self.dictmenu=Menu(menu)
		menu.add_cascade(label="�������",menu=self.dictmenu)
		self.dictmenu.add_command(label="��������", command=self.dummyCallback)
		self.dictmenu.add_command(label="����������", command=self.dummyCallback)
		self.dictmenu.add_separator()
		self.dictmenu.add_command(label="�� �����...", command=self.dummyCallback)
		
		self.helpmenu=Menu(menu)
		menu.add_cascade(label="������",menu=self.helpmenu)
		self.helpmenu.add_command(label="� ���������...", command=self.aboutCallback)
		
	def _createStatusBar(self):
		self.statusbar = Label(self.rootTk, text="...", bd=1, relief=SUNKEN, anchor=W)
		self.statusbar.pack(side=BOTTOM, fill=X)

	def _createInitForm(self):
		self.initForm=Frame(self.rootTk)
		self.initForm.pack(fill=BOTH,padx=10)
		Label(self.initForm,text="���������� �� ����� ������",fg="blue",anchor=W,height=2).grid(row=0,column=0)

		Label(self.initForm,text="����� ���� � ���� ������ :",anchor=W,width=25).grid(row=1,column=0)
		Label(self.initForm,text="150 000",anchor=E,bd=1,relief=SUNKEN,width=10).grid(row=1,column=1)
		
		Label(self.initForm,text="����������� :",anchor=W,width=25).grid(row=2,column=0)
		Label(self.initForm,text="10 000",anchor=E,bd=1,relief=SUNKEN,width=10).grid(row=2,column=1)
		
		Label(self.initForm,text="�������� :",anchor=W,width=25).grid(row=3,column=0)
		Label(self.initForm,text="5 000",anchor=E,bd=1,relief=SUNKEN,width=10).grid(row=3,column=1)
		
		Label(self.initForm,text="������ :",anchor=W,width=25).grid(row=4,column=0)
		Label(self.initForm,text="3 000",anchor=E,bd=1,relief=SUNKEN,width=10).grid(row=4,column=1)

		Label(self.initForm,text="����������� :",anchor=W,width=25).grid(row=5,column=0)
		Label(self.initForm,text="3 000",anchor=E,bd=1,relief=SUNKEN,width=10).grid(row=5,column=1)
		return self.initForm
		
		
	def __init__(self):
		self.rootTk = Tk()
		self.rootTk.minsize(500, 500)
		self.rootTk.title("�����������")
		self.rootTk.wm_iconbitmap('ruslang.ico')
		self.rootTk.protocol('WM_DELETE_WINDOW', self.callbackWindowDeleted)
		
		self._createMenu()
		self._createStatusBar()
		self.currentForm=self._createInitForm()
		
		self.allFormsOperationalLoaded = False 
	

	def restoreLastState(self):
		pass
		
	def run(self):
		self.rootTk.mainloop() ;



def run():
	gu = Gutil()
	gu.restoreLastState()
	gu.run()


#if __name__ == "__main__":
#	run()
