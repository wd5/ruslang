# coding=cp1251
# python graphical utils for Russian Language project
# Author: ustaslive
# created : 2012-00-09
# last modified: 2012-09-09

from tkinter import *
import ruslang

class Gutil:

	def dummyCallback(self):
		pass

	def aboutCallback(self):
		self.dummyCallback()

	def switchToAnalyzeRawWordForms(self):
		self.loadRawWordForms()
		self.switchToRawAnalysisForm()
	
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
		self.filemenu.add_command(label="�����", command=self.rootTk.quit)
		
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

	def __init__(self):
		self.rootTk = Tk()
		self.rootTk.minsize(500, 500)
		self.rootTk.title("�����������")
		self.rootTk.wm_iconbitmap('ruslang.ico')
		
		self._createMenu()
		self._createStatusBar()



	def restoreLastState(self):
		pass
		
	def run(self):
		self.rootTk.mainloop() ;






def run():
	gu = Gutil()
	gu.restoreLastState()
	gu.run()


#if __name__ == "__main__":
	run()
