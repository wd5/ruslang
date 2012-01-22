/* 
 * File:   wordform.hpp
 * Author: Victor
 *
 * Created on November 6, 2011, 3:16 PM
 */

#ifndef WORDFORM_HPP
#define	WORDFORM_HPP

#include <cstring>      // strlen
#include <cstdlib>     // for malloc(), and free()
#include "russian_chars.hpp" 
#include "cp1251.hpp"

const int ACCENT_ARRAY_SIZE=3 ;
class WordForm
{
private:
    static char _string[512] ;
public:
    char* word ;
    int length ;
    unsigned long id ;
    short accent [ACCENT_ARRAY_SIZE];        // 0 - unknown, some info is missing, some words have no vocals
    WordForm(const char* str)
    {
        int len=std::strlen((const char*) str); 
        word=(char*)std::malloc(sizeof(char)*len) ;
        std::memcpy(word, str,len) ;
        length=len ;
        resetAccent();
    }
    WordForm(const WordForm& wf)
    {
        length=wf.length ;
        resetAccent();
        for(int i=0;i<ACCENT_ARRAY_SIZE;i++)
                accent[i]=wf.accent[i] ;
        word=(char*)std::malloc(sizeof(char)*length) ;
        std::memcpy(word, wf.word,sizeof(char)*length) ;
        id=wf.id ;
    }
    WordForm(const char* str,int len)
    {
        word=(char*)std::malloc(sizeof(char)*len) ;
        std::memcpy(word,str,sizeof(char)*len) ;
        length=len ;
        resetAccent();
    }
    ~WordForm()
    {
        std::free(word);
        word=0 ;
        length=0 ;
        resetAccent();
        id=0 ;
    }
    void setAccent(int accentPosition)
    {
        for(int i=0;i<ACCENT_ARRAY_SIZE;i++)
        {
            if(accent[i]==0)
            {
                accent[i]=accentPosition ;
                return ;
            }
        }
    }
    void resetAccent()
    {
        for(int i=0;i<ACCENT_ARRAY_SIZE;i++)
                accent[i]=0;
    }
    const char* str()
    {
        std::memcpy(_string,word,length) ;
        _string[length]=0 ;
        return _string ;
    }
    char* str(char* s) const
    {
        std::memcpy(s,word,length) ;
        s[length]=0 ;
        return s ;
    }
    const  char* wstr()
    {
        std::memcpy(_string,word,length) ;
        _string[length]=0 ;
        return _string ;
    }
    const char* str_cp866()
    {
        return convert_str_cp1251_to_cp866(_string,word,length) ;
    }
    // bool operator==(const WordForm& wf) const ;
    bool operator<(const WordForm& wf) const ;
    WordForm& operator=(const WordForm& wf) 
    {
        std::free(word) ;
        length=wf.length ;
        id=wf.id ;
        resetAccent();
        for(int i=0;i<ACCENT_ARRAY_SIZE;i++)
                accent[i]=wf.accent[i] ;
        word=(char*)std::malloc(sizeof(char)*length) ;
        std::memcpy(word, wf.word,length) ;
        return *this ;
    }
    void reset( const char* str,int len, short acct[] )
    {
        std::free(word) ;
        word=(char*)std::malloc(sizeof(char)*len) ;
        std::memcpy(word,str,len) ;
        length=len ;
        resetAccent();
        for(int i=0;i<ACCENT_ARRAY_SIZE;i++)
            accent[i]=acct[i] ;
    }
    
};

#endif	/* WORDFORM_HPP */

