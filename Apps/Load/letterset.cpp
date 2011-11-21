#include "letterset.hpp"
#include "wordform.hpp"
#include <cstring>

const int NUMBER_OF_LETTERS_IN_CP1251=256;
const int NUMBER_OF_LETTERS= NUMBER_OF_LETTERS_IN_CP1251;

void LetterSet::init(const char* str,int strSize)
{
    letters=NULL;
    cnt=NULL ;
    length=0 ;
    id=0 ;
    short letterCounter[NUMBER_OF_LETTERS] = {0} ;
    int i;
    for(i=0;i<strSize && i<NUMBER_OF_LETTERS;i++)
    {
        int charCode=(unsigned int)(unsigned char)str[i] ;
        if(letterCounter[charCode]==0)
            length++ ; // new char in word
        letterCounter[charCode]++ ;
    }
    letters=(char*)malloc(sizeof(char)*length) ;
    cnt=(short*)malloc(sizeof(short)*length) ;
    
    int positionInLetterSet=0 ; 
    for(int charCode=0;charCode<NUMBER_OF_LETTERS;charCode++)
    {
        if(letterCounter[charCode]>0)
        {
            letters[positionInLetterSet]=charCode; 
            cnt[positionInLetterSet]=letterCounter[charCode]; 
            positionInLetterSet++ ;
        }
    }
}

LetterSet::LetterSet(const char* str) 
{
    init(str,strlen(str)) ;
}

LetterSet::LetterSet(const LetterSet& ls) 
{
    length=ls.length ;
    letters=(char*)malloc(sizeof(char)*length) ;
    cnt=(short*)malloc(sizeof(short)*length) ;
    std::memcpy(letters,ls.letters,length) ;
    std::memcpy(cnt,ls.cnt,length) ;
}

LetterSet::LetterSet(const WordForm& wf ) 
{
    init(wf.word,wf.length) ;
}

void LetterSet::reset(const char* str, int strSize)
{
    if(letters) free(letters) ;
    if(cnt) free(cnt) ;
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