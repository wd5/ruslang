#include "letterset.hpp"
#include "wordform.hpp"
#include <cstring>

// debug
#include <iostream>


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
   
//    std::cout << "init debug:" ; 
            
    for(int charCode=0;charCode<NUMBER_OF_LETTERS;charCode++)
    {
        if(letterCounter[charCode]>0)
        {
            letters[positionInLetterSet]=(char) charCode; 
            cnt[positionInLetterSet]=letterCounter[charCode]; 
//            if( letterCounter[charCode] == 0 )
//            {
//                std::cerr << "fatal[0x0002]: number of chars is ZERO" << std::endl ;
//                exit(-1) ;
//            }
            positionInLetterSet++ ;
//            std::cout << charCode<< "[" << letterCounter[charCode] <<"]" ;

        }
    }
    
    // debug
//   std::cout << std::endl ;

    
}

LetterSet::LetterSet(const char* str) 
{
    init(str,std::strlen(str)) ;
}

LetterSet::LetterSet(const LetterSet& ls) 
{
    length=ls.length ;
    letters=(char*)std::malloc(sizeof(char)*length) ;
    cnt=(short*)std::malloc(sizeof(short)*length) ;
    id=ls.id ;
    std::memcpy(letters,ls.letters,sizeof(char)*length) ;
    std::memcpy(cnt,ls.cnt,sizeof(short)*length) ;
}

LetterSet::LetterSet(const WordForm& wf ) 
{
    init(wf.word,wf.length) ;
}

void LetterSet::reset(const char* str, int strSize)
{
    if(letters) std::free(letters) ;
    if(cnt) std::free(cnt) ;
    init(str,strSize) ;
}

char* LetterSet::str(char* s) const
{
    int i;
    for(i=0;i<length;i++)
    {
        s[i*2]=letters[i];
        
//        if(cnt[i]==0)
//        {
//            std::cerr << "fatal[0x0001]: number of chars is ZERO" << std::endl ;
//            std::cerr << "debug: length=" << length << "; id=" << id << std::endl ;
//            exit(-1) ;
//        }
        s[i*2+1]= number_codes[cnt[i]] ;
    }
    s[i*2]=0 ;
    
    //debug
    //std::cout << "ls::str:" << s << " | "; 
    //hexing(s) ;
    //std::cout << std::endl ;
    
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
