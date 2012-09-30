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
    # todo: bug ru.match('членский','ч???ск?*й') == True
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

    def quit(self):
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

    def _passPartCriteria(self,dictItem):
        itemPartOfSpeechValue="0"
        if hasattr(dictItem,'partOfSpeech'):
            itemPartOfSpeechValue = getattr(dictItem,'partOfSpeech')

        filterVarName = {
            # value in Dict DB against StringVar variable name
            "n":"filterNounVar",    # noun
            "a":"filterAdjectiveVar",    # adjective
            "v":"filterVerbVar",    # verb
            "av":"filterAdverbVar",    # adverb
            "p":"filterPrepositionVar",    # preposition
            "pn":"filterPronounVar",    # pronoun
            "i":"filterInterjectionVar",    # interjection, exclamation
            "c":"filterConjunctionVar",    # conjunction
            "pa":"filterParticleVar",    # grammatical particle
            "nu":"filterNumeralVar",    # numeral
            "u":"filterUnknownPartVar",    # unknown
            "0":"filterPartNotCheckedVar"   # not checked
        }

        if hasattr(self,filterVarName[itemPartOfSpeechValue]):
            if getattr(self,filterVarName[itemPartOfSpeechValue]).get() == "y":
                return True
            else:
                return False
        else:
            return True

        return True

    def _passNominalCriteria(self,dictItem):
        itemNominalValue="0"
        if hasattr(dictItem,'nominal'):
            itemNominalValue = getattr(dictItem,'nominal')

        filterVarName = {
            # value in Dict DB against StringVar variable name
            "y":"filterNominalYesVar",    # noun
            "n":"filterNominalNoVar",    # adjective
            "0":"filterNominalNotCheckedVar"   # not checked
        }

        if hasattr(self,filterVarName[itemNominalValue]):
            if getattr(self,filterVarName[itemNominalValue]).get() == "y":
                return True
            else:
                return False
        else:
            return True

        return True


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

    def _createColumnTitle(self,tForm,title):
        return Label(tForm,text=title,bg='grey',relief=SUNKEN,bd=1)

    def _createWordColumnSubtitle(self,tForm,text):
        return Label(tForm,text=text,bg='grey',relief=SUNKEN,bd=1)

    def _createNominalFilter(self,cell,attrName,label):
        if not hasattr(self,attrName):
            setattr(self,attrName,StringVar())
            getattr(self,attrName).set("y")
        return Checkbutton(cell,text=label,variable=getattr(self,attrName),onvalue="y",offvalue="n",indicatoron=0)

    def _createNominalColumnFilter(self,tForm):
        cell=Frame(tForm)

        self._createNominalFilter(cell,'filterNominalYesVar','да').pack(side=LEFT)
        self._createNominalFilter(cell,'filterNominalNoVar','нет').pack(side=LEFT)
        self._createNominalFilter(cell,'filterNominalNotCheckedVar','?').pack(side=LEFT)

        return cell

    def _createPartFilter(self,rootWidget,attrName,label):
        if not hasattr(self,attrName):
            setattr(self,attrName,StringVar())
            getattr(self,attrName).set("y")
        return Checkbutton(rootWidget,text=label,variable=getattr(self,attrName),onvalue="y",offvalue="n",indicatoron=0,width=6)

    def _createPartColumnFilter(self,tForm):
        cell=Frame(tForm)

        partsOfSpeech = [
            ("filterNounVar","сущ"),
            ("filterAdjectiveVar","прил"),
            ("filterVerbVar","глаг"),
            ("filterAdverbVar","нареч"),
            ("filterPrepositionVar","предл"),
            ("filterPronounVar","местоим"),
            ("filterInterjectionVar","междом"),
            ("filterConjunctionVar","союз"),
            ("filterParticleVar","частица"),
            ("filterNumeralVar","числ"),
            ("filterUnknownPartVar","неизв"),
            ("filterPartNotCheckedVar","?")
        ]

        for p,label in partsOfSpeech:
            self._createPartFilter(cell,p,label).pack(side=LEFT)

        return cell

    def _createNominalColumnSubtitle(self,tForm):
        cell=Frame(tForm)
        Label(cell,text="su",bg='grey',relief=SUNKEN,bd=1).pack(side=LEFT,fill=X)
        return cell

    def _createPartColumnSubtitle(self,tForm):
        cell=Frame(tForm)
        Label(cell,text="subpart",bg='grey',relief=SUNKEN,bd=1).pack(side=LEFT,fill=X)
        return cell

    def _createTitle(self,tableForm):
        # text header
        self._createColumnTitle(tableForm,"Слово").grid(row=0,column=0,sticky=W+E)
        self._createColumnTitle(tableForm,"Номинал").grid(row=0,column=1,sticky=W+E)
        self._createColumnTitle(tableForm,"Часть речи").grid(row=0,column=2,sticky=W+E)

        # by column filter
        # todo: create "by column" filter with CHECKBOXes => any check selected and match - the records is displeyed
        # todo: noun+ verb+ adj- unknown- => display all nouns and verbs. do not display ADJ and UNKN
        # todo: by default: all selected.
        self._createWordColumnSubtitle(tableForm,"Фильтр =>").grid(row=1,column=0,sticky=W+E)
        self._createNominalColumnFilter(tableForm).grid(row=1,column=1,sticky=W+E)
        self._createPartColumnFilter(tableForm).grid(row=1,column=2,sticky=W+E)

        # mass selector
        self._createWordColumnSubtitle(tableForm,"Выбор колонки =>").grid(row=2,column=0,sticky=W+E)
        # todo: create checkAll/uncheck selection for nominal value - 3 options
        self._createNominalColumnSubtitle(tableForm).grid(row=2,column=1,sticky=W+E)
        # todo: create checkAll/uncheck selection for part value - ~10 options
        self._createPartColumnSubtitle(tableForm).grid(row=2,column=2,sticky=W+E)

    def _createTableRow(self,tForm,word,line):
        Label(tForm,text=word,width=30,anchor=E).grid(row=line,column=0,columnspan=3)

    def _nomCallback(self,item,var):
        item.nominal = str(var.get())

    # todo: merge _createNominalCell and _create*Cell to pne unoversal function with parameters
    def _createNominalCell(self, tForm, dictItem):
        nominalCellForm = Frame(tForm)

        nominalVar = StringVar()
        self.nominalVars.append(nominalVar)
        # todo: link to real value in [dictItem]: dictItem.nominal
        if not hasattr(dictItem,'nominal'):
            dictItem.nominal = "0"
        nominalVar.set(dictItem.nominal)

        # todo: encode
        nominals=[
            ("да","y"),
            ("нет","n"),
            ("?","0")
        ]
        for lbl,val in nominals:
            Radiobutton(nominalCellForm,
                        text=lbl,
                        variable=nominalVar,
                        indicatoron=0,
                        value=val,
                        command=lambda : self._nomCallback(dictItem,nominalVar)
            ).pack(side=LEFT)

        return nominalCellForm

    def _partCallback(self,item,var):
        item.partOfSpeech = str(var.get())

    def _createPartOfSpeechCell(self,tForm,dictItem):
        partCellForm = Frame(tForm)
        # todo: link to real value in [dictItem]: dictItem.partsOfSpeech
        partVar = StringVar()
        self.partVars.append(partVar)
        # todo: select default value does not work
        if not hasattr(dictItem,'partOfSpeech'):
            dictItem.partOfSpeech = "0"
        partVar.set(dictItem.partOfSpeech)

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
            Radiobutton(partCellForm,
                        text=lbl,
                        variable=partVar,
                        value=val,
                        indicatoron=0,
                        width=6,
                        command=lambda : self._partCallback(dictItem,partVar)
                ).pack(side=LEFT)

        return partCellForm

    def _createTableRowFromDictItem(self,tForm,dictItem,line):

        Label(tForm,text=dictItem.word,width=30,anchor=E).grid(row=line,column=0)
        # todo: create with button "..." "Edit details" which goes to a form for particular part of speech. can be selected only if part is choosen already

        self._createNominalCell(tForm,dictItem).grid(row=line,column=1)
        self._createPartOfSpeechCell(tForm,dictItem).grid(row=line,column=2)


    def _fillTable(self,tableForm, mask=DEFAULT_WORD_MASK, lengthMask="",shuffle=False):
        row=0
        self.nominalVars = []
        self.partVars = []
        self._createTitle(tableForm)

        row+=3  # this number depends on the # of rows printd in _createTitle call.
        if ((not MASK_ANY_NUMBER_OF_CHARS in mask) and (not MASK_ANY_SINGLE_CHAR in mask)):
            # no mask special chars means exact word match. ignoring length.
            if mask in self.operational.keys():
                # todo: must list not only [0] element but all matching [mask]
                self._createTableRowFromDictItem(tableForm,self.operational[mask][0],row); row+=1
            else:
                # todo: encode
                self._createTableRow(tableForm,"слово ["+mask+"] не найдено",row);    row+=1
            return

        fixLength,minLength,maxLength=self._parseLengthMask(lengthMask)

        # TODO: table need headers
        # TODO: table need to be dynamic: part of speech, sex if any
        keywordList = list(self.operational.keys())
        keywordListLen = len(keywordList)
        # TODO: no need to shuffle every time, expecialy when exact match is requested
        #if shuffle:
        #    random.shuffle(keywordList)

        statisticInfo=""
        statCount=0
        if mask == DEFAULT_WORD_MASK or mask == "":
            # no char mask, only LENGTH is counted
            for i in range(0,keywordListLen):
                keyWord = keywordList[i]
                statCount += 1
                if shuffle:
                    keyWord = random.sample(keywordList,1)[0]
                if (self._passLengthCriteria(len(keyWord),fixLength,minLength,maxLength) and
                    self._passPartCriteria(self.operational[keyWord][0]) and
                    self._passNominalCriteria(self.operational[keyWord][0])
                    ):
                    # todo: must list not only [0] element but all matching keywordList[i]
                    #todoo: BUG runtime error here
                    self._createTableRowFromDictItem(tableForm,self.operational[keyWord][0],row); row += 1
                    if row >= GUTIL_ANALYSIS_ONSCREEN_WORDS:
                        break
        else:
            comparator=compileCompareOperator(mask)
            for i in range(0,keywordListLen):
                keyWord = keywordList[i]
                statCount += 1
                if shuffle:
                    keyWord = random.sample(keywordList,1)[0]
                if (self._passLengthCriteria(len(keyWord),fixLength,minLength,maxLength) and
                    comparator.match(keyWord) and
                    self._passPartCriteria(self.operational[keyWord][0]) and
                    self._passNominalCriteria(self.operational[keyWord][0])
                    ):
                    # todo: must list not only [0] element but all matching keywordList[i]
                    self._createTableRowFromDictItem(tableForm,self.operational[keyWord][0],row); row+=1
                    if row >= GUTIL_ANALYSIS_ONSCREEN_WORDS:
                        break
        if row <=1 :    # only title was printed
            # todo: encode
            self._createTableRow(tableForm,"по шаблону ["+mask+"] ничего не найдено",0)
        else:
            self.statisticUpdate("checked "+str(statCount)+" records in dictionary")

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
        # 2.7 todo: more filters: exclude when all fields known

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

        # 5. extra functions
        # todo: 5.1 clean up 'created" directory from temp backup files: not *_save.txt, not original filenames, all timestamped backups but last one
        #

        return self.analysisForm
        
    def statusUpdate(self,newStatus):
        self.status_bar['text'] = newStatus
        self.rootTk.update()

    def statisticUpdate(self,newStatus):
        self.statistic_bar['text'] = newStatus
        self.rootTk.update()


    def loadRawWordForms(self,forceLoad=False):
        if not forceLoad and self.allFormsOperationalLoaded:
            return
        # todo: encode
        self.statusUpdate("Загрузка необработанных словоформ, шаг 1... ждите")
        self.operational_zero = ruslang.LoadOperational()

        self.statusUpdate("Загрузка необработанных словоформ, шаг 2... ждите")
        self.operational = ruslang.indexed_by_sterilized(self.operational_zero)

        # todo: encode
        self.statusUpdate("Необработанные словоформы загружены")
        self.allFormsOperationalLoaded = True
        
    def switchToAnalyzeRawWordForms(self):
        self.currentForm.destroy()
        self.loadRawWordForms(forceLoad=True)
        self.currentForm = self._createAnalysisForm()

    def saveCurrentChanges(self):
        self.statusUpdate("Обновление словаря словоформ... ждите")
        ruslang.SaveOperational(self.operational_zero)
        self.statusUpdate("Словарь обновлён")


    def _createMenu(self):
        menu=Menu(self.rootTk)
        self.rootTk.config(menu=menu)
        self.file_menu=Menu(menu)
        # todo: encode
        menu.add_cascade(label="Файлы",menu=self.file_menu)
        self.file_menu.add_command(label="Открыть Недообработанные", command=self.switchToAnalyzeRawWordForms)
        self.file_menu.add_command(label="Открыть Номиналы", command=self.dummyCallback)
        self.file_menu.add_command(label="Сохранить изменения", command=self.saveCurrentChanges)
        self.file_menu.add_command(label="Выход", command=self.quit)
        
        self.dict_menu=Menu(menu)
        menu.add_cascade(label="Словарь",menu=self.dict_menu)
        self.dict_menu.add_command(label="Номиналы", command=self.dummyCallback)
        self.dict_menu.add_command(label="Словоформы", command=self.dummyCallback)
        self.dict_menu.add_separator()
        self.dict_menu.add_command(label="Из файла...", command=self.dummyCallback)
        
        self.help_menu=Menu(menu)
        menu.add_cascade(label="Помощь",menu=self.help_menu)
        self.help_menu.add_command(label="О программе...", command=self.aboutCallback)
        
    def _createStatusBar(self):
        self.status_bar = Label(self.rootTk, text="...", bd=1, relief=SUNKEN, anchor=W)
        self.status_bar.pack(side=BOTTOM, fill=X)

    def _createStatisticBar(self):
        self.statistic_bar = Label(self.rootTk, text="...", bd=1, relief=SUNKEN, anchor=W)
        self.statistic_bar.pack(side=BOTTOM, fill=X)


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
        self._createStatisticBar()

        self.currentForm=self._createInitForm()
        
        self.allFormsOperationalLoaded = False

        self.nominalVars=[]
        self.partVars=[]


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
