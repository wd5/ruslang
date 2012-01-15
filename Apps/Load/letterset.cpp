#include "letterset.hpp"
#include "wordform.hpp"
#include <cstring>

// total control
#include <iostream>

const int NUMBER_OF_LETTERS_IN_CP1251=256;
const int NUMBER_OF_LETTERS= NUMBER_OF_LETTERS_IN_CP1251;

void LetterSet::init(const char* str,int strSize)
{
    letters=NULL;
    cnt=NULL ;
    length=0 ;
    id=0 ;
    wfLinked=NULL ;
    wfLinkedCounter=0 ;
    short letterCounter[NUMBER_OF_LETTERS] = {0} ;
    int i;
    for(i=0;i<strSize;i++)
    {
        int charCode=(unsigned int)(unsigned char)str[i] ;
        if(letterCounter[charCode]==0)
            length++ ; // new char in word
        letterCounter[charCode]++ ;
    }
    letters=(char*)std::malloc(sizeof(char)*length) ;
    cnt=(short*)std::malloc(sizeof(short)*length) ;
    
    int positionInLetterSet=0 ; 
      
    for(int charCode=0;charCode<NUMBER_OF_LETTERS;charCode++)
    {
        if(letterCounter[charCode]>0)
        {
            letters[positionInLetterSet]=(char) charCode; 
            cnt[positionInLetterSet]=letterCounter[charCode]; 
            positionInLetterSet++ ;
        }
    }
}

LetterSet::LetterSet(const char* str) 
{
    init(str,std::strlen(str)) ;
}

LetterSet::LetterSet(const LetterSet& ls) 
{
    wfLinked=NULL ;
    wfLinkedCounter=0 ;
    length=ls.length ;
    letters=(char*)std::malloc(sizeof(char)*length) ;
    cnt=(short*)std::malloc(sizeof(short)*length) ;

    id=ls.id ;
    std::memcpy(letters,ls.letters,sizeof(char)*length) ;
    std::memcpy(cnt,ls.cnt,sizeof(short)*length) ;
    if(ls.wfLinkedCounter)
    {
        wfLinkedCounter = ls.wfLinkedCounter ;
        wfLinked=(unsigned long*) std::malloc(sizeof(unsigned long)*wfLinkedCounter) ;
        std::memcpy(wfLinked,ls.wfLinked,sizeof(unsigned long)*wfLinkedCounter) ;
    }
}

LetterSet::LetterSet(const WordForm& wf ) 
{
    init(wf.word,wf.length) ;
    link(wf) ;
}

void LetterSet::reset(const char* str, int strSize)
{
    if(letters) std::free(letters) ;
    if(cnt) std::free(cnt) ;
    if(wfLinked) std::free(wfLinked) ;
    init(str,strSize) ;
}

char* LetterSet::str(char* s) const
{
    int i;
    for(i=0;i<length;i++)
    {
        s[i*2]=letters[i];
        s[i*2+1]= number_codes[cnt[i]] ;
    }
    s[i*2]=0 ;
    return s ;
}
        
bool LetterSet::operator<(const LetterSet& ls) const 
{
    // true if this < wf

    char str1[1024], str2[1024] ;
    int len1=std::strlen(str(str1)) ;
    int len2=std::strlen(ls.str(str2)) ;
    int compareResult=cp1251::strcmp(str1,len1,str2,len2) ;
    if (compareResult<0) return true ;
    return false ; 
}

void LetterSet::link(const WordForm& wf) const
{
    unsigned int oldCounter=0 ;
    unsigned long oldWfLinked[256];
    
    if(wfLinkedCounter>0)
    {
        // control [C-0001]: algorithm does not allow adding the same WordForm (by ID) to LetterSet
        for(unsigned int i=0;i<wfLinkedCounter;i++)
        {
            if(wfLinked[i]==wf.id)
            {
                std::cerr << "unexpected [0x0010]: adding the same WordForm ID:" << wf.id << std::endl ;
                std::exit(0) ;
            }
        }
        // end of control [C-0001]
        
        oldCounter=wfLinkedCounter ;
        std::memcpy(oldWfLinked,wfLinked,sizeof(unsigned long)*oldCounter) ;
        std::free(wfLinked) ;
        wfLinkedCounter++ ;
        wfLinked = (unsigned long*) std::malloc(sizeof(unsigned long)*wfLinkedCounter) ;
        std::memcpy(wfLinked,oldWfLinked,sizeof(unsigned long)*oldCounter) ;
        wfLinked[wfLinkedCounter-1] = wf.id ;
    }
    else
    {
        wfLinked = (unsigned long*) std::malloc(sizeof(unsigned long)*1) ;
        wfLinkedCounter=1 ;
        wfLinked[0] = wf.id ;
    }
}
