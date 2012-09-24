# coding=cp1251
# python utils for Russian Language project
# Author: ustaslive
# created : 2012-08-30
# last modified: 2012-08-30

# todo: replace all leading tabs to 4-space as per PEP-8

import ruslang as rl

plainWordInitialForms={}
plainWordAllForms={}

def removeAccents(w):
    return w.replace("`","").replace("'","")

# create full sent of non-accented word forms from the file
# all words are lowercase
def readRawPlain():
    plainWordForms=set([])
    for line in open(rl.RAW_ALL_FORMS_ACCENT_CP1251_FILE,"r"):
        line=line.rstrip('\n')
        initialWord,wordForms = line.split('#')
        wordForms = removeAccents(wordForms)
        wordForms = wordForms.lower()

        for w in wordForms.split(','):
            plainWordForms.add(w)
    return plainWordForms

# same as readRawPlain() but does not remove accents and does not cange the case
# accepts words as they are
def readRawPlain2():
    plainWordForms=set([])
    for line in open(rl.RAW_ALL_FORMS_ACCENT_CP1251_FILE,"r"):
        line=line.rstrip('\n')
        initialWord,wordForms = line.split('#')

        for w in wordForms.split(','):
            plainWordForms.add(w)
    return plainWordForms

# todo: replace all non-ascii chars with "\x, \u or \U escapes" as per PEP-8
def duplicateYOwords(dictSet):
    yoWords = set([])
    for w in dictSet:
        if 'ё' in w:
            yoWords.add(w.replace('ё','е'))
    dictSet.update(yoWords)

def chaset(w):
    cc={}
    for c in w:
        if c in cc.keys():
            cc[c] = cc[c]+1
        else:
            cc[c] = 1 ;
    result=""
    ks=list(cc.keys())
    ks.sort()
    for c in ks:
        result = result + c+str(cc[c])
    return result

# group anagrams
def groupAnagrams(dict):
    anagrams = {}
    for w in dict:
        cc=chaset(w)
        if cc in anagrams.keys():
            anagrams[cc].append(w)
        else:
            anagrams[cc] = [w]
    return anagrams

def findAnagrams(anagrams,word):
    lchaset = chaset(word)
    if lchaset in anagrams.keys():
        return anagrams[lchaset(word)]
    return [lchaset]

# save groupped anagrams
# do not save words which do now have an anagram - single
def writeAnagrams(anagrams):
    anaSizes = {}   # sizes of groups
    for cc in anagrams.keys():
        sz = len(anagrams[cc])
        if sz <= 1 : continue   # at least 2 words must exist for anagram
        if sz in anaSizes.keys():
            anaSizes[sz].append(cc)
        else:
            anaSizes[sz] = [cc]
    szKeys = list(anaSizes.keys())
    szKeys.sort(key=None,reverse=True)

    size=len(anagrams)
    fname=filename(rl.CREATED_DATA_DIR_PATH + r"\anagrams_cp1251_"+str(size))
    f=open(fname,"w")

    for size in szKeys:
        chasetList = anaSizes[size]
        for cc in chasetList:
            wordList = anagrams[cc]
            wordList.sort()
            f.write(cc+":"+",".join(wordList)+"\n")
    f.close()

def writeRawPlain(plainWordForms):
    pwf = set(plainWordForms)
    size=len(pwf)
    fname=filename(rl.CREATED_DATA_DIR_PATH + r"\plain_word_forms_cp1251_"+str(size))
    f=open(fname,"w")
    for w in pwf :
        f.write(w+"\n")
    f.close()

# find words in dict that almost exactly match the word
# lengths are equeal
# 1 char can differ
def findLikes1(dictSet,word):
    words=[w for w in dictSet if len(w)==len(word)]
    wset=set(word)
    likes = set([])
    for w in words:
        if len(set(w)^wset) <=2:
            miss=0
            for i in range(0,len(word)):
                if w[i] != word[i]: miss = miss+1
            if miss <=1:
                likes.add(w)
    return likes

def findLikes1_sizeAware(wordsSized,word):
    words=wordsSized
    wLen=len(word)
    wset=set(word)
    likes = set([])
    for w in words:
        if len(set(w)^wset) <=2:
            miss=0
            for i in range(0,wLen):
                if w[i] != word[i]: miss = miss+1
            if miss <=1:
                likes.add(w)
    return likes

def findLikesGlobal():
    fullDict = readRawPlain()
    dict = {}
    for wordLength in range(3,15):
        dict[wordLength] = [w for w in fullDict if len(w)==wordLength]

    SIZE=4
    with open (filename(rl.CREATED_DATA_DIR_PATH + r"\likes_cp1251_"+ str(SIZE)), "w") as file:
        for w in dict[SIZE]:
            likes = findLikes1_sizeAware(dict[SIZE],w)
            if len(likes) > 1:
                file.write(w + "#" + ",".join(likes)+"\n")

# create a form/set of chars for a real word
# the form allows to match different words by 'sound like'
# example: D is replaced with T => DATE will match TATE as well (if TATE existed)
def soundUniform(w):
    uw = w
    # todo: encode
    uw = uw.replace('б','п')
    uw = uw.replace('г','к')
    uw = uw.replace('д','т')
    uw = uw.replace('ж','ш')
    uw = uw.replace('з','с')
    uw = uw.replace('в','ф')
    # to be continued: TSA = CA, CHIVO = CHEGO, NN = N, doubled consonant
    return uw
            
# a dictionary of uniforms (unified word forms, unified by sound)
# result is { 'uniform' : [wordform1, wordform2, ...] }
def generateUnidict(dictSet):
    unidict = {}
    for w in dictSet:
        uw = soundUniform(w)
        if uw in unidict.keys() :
            unidict[uw].append(w)
        else:
            unidict[uw] = [w]
    return unidict

# short version of Uniform Dict - remove all instances which have no consonant
def removeSingleUniform(unidict):
    return {key:unidict[key] for key in list(unidict.keys()) if len(unidict[key])>1 }

def findConsonant(dictSet,word):
    # words=[w for w in dictSet if len(w)==len(word)]    # not exactly as somtimes 2-chars and 1-char sounds can match
    pass


def updateFiles():
    print("Loading word worms file...",end="")
    fullWordFormSet=readRawPlain()
    print("done",end="\n")

    print("Populating word form set with non-YO duplicates...",end="")
    duplicateYOwords(fullWordFormSet)
    print("done",end="\n")

    print("Generating anagram's list...",end="")
    grouppedAnagrams = groupAnagrams(fullWordFormSet)
    print("done",end="\n")

    print("Saving word forms...",end="")
    writeRawPlain(fullWordFormSet)
    print("done",end="\n")

    print("Saving anagrams...",end="")
    writeAnagrams(grouppedAnagrams)
    print("done",end="\n")

def createPlainWordFile():
    fullWordFormSet=readRawPlain2()
    writeRawPlain(fullWordFormSet)



import time

def filename(keyword):
    dt = time.localtime()
    timePart = time.strftime("_%Y%m%d%H%M%S",dt)
    return keyword + timePart + ".txt"

##if __name__ == '__main__':
##    readRaw()
##    print(len(plainWordInitialForms))
##    print(len(plainWordAllForms))

def _testYO():
    dt_test1_start=time.gmtime()
    dt_test1_end=time.gmtime()
    dt_test2_start=time.gmtime()
    dt_test2_end=time.gmtime()
    print("Test 1:", dt_test1_end-dt_test1_start)
    print("Test 2:", dt_test2_end-dt_test2_start)

if __name__ == '__main__':
    createPlainWordFile()
