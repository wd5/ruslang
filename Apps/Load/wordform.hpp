/* 
 * File:   wordform.hpp
 * Author: Victor
 *
 * Created on November 6, 2011, 3:16 PM
 */

#ifndef WORDFORM_HPP
#define	WORDFORM_HPP

#include "cyrillic/russian_chars.hpp"
#include "cyrillic/cp1251.hpp"

const int ACCENT_ARRAY_SIZE=3 ;
class WordForm
{
private:
    static unsigned char _string[512] ;
public:
    unsigned char* word ;
    int length ;
    short accent [ACCENT_ARRAY_SIZE];        // 0 - unknown, some info is missing, some words have no vocals
    WordForm(const unsigned char* str)
    {
        int len=strlen((const char*) str); 
        word=(unsigned char*)malloc(sizeof(unsigned char)*len) ;
        memcpy(word, str,len) ;
        length=len ;
        resetAccent();
    }
    WordForm(const WordForm& wf)
    {
        length=wf.length ;
        resetAccent();
        for(int i=0;i<ACCENT_ARRAY_SIZE;i++)
                accent[i]=wf.accent[i] ;
        word=(unsigned char*)malloc(sizeof(unsigned char)*length) ;
        memcpy(word, wf.word,length) ;
    }
    WordForm(const unsigned char* str,int len)
    {
        word=(unsigned char*)malloc(sizeof(unsigned char)*len) ;
        memcpy(word,str,len) ;
        length=len ;
        resetAccent();
    }
    ~WordForm()
    {
        free(word);
        word=0 ;
        length=0 ;
        resetAccent();
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
    const unsigned char* str()
    {
        memcpy(_string,word,length) ;
        _string[length]=0 ;
        return _string ;
    }
    unsigned char* str(unsigned char* s) const
    {
        memcpy(s,word,length) ;
        s[length]=0 ;
        return s ;
    }
    const unsigned char* wstr()
    {
        memcpy(_string,word,length) ;
        _string[length]=0 ;
        return _string ;
    }
    const unsigned char* str_cp866()
    {
        return convert_str_cp1251_to_cp866(_string,word,length) ;
    }
};


class comp_WordForm
{
public:
    bool operator()(WordForm wf1, WordForm wf2) const
    { 
        // true if wf2 > wf1, false if wf2<=wf1
        int compareResult=strcmp_cp1251(wf1.word,wf1.length,wf2.word,wf2.length) ;
        if(compareResult==0)
        {
            for(int i=0;i<ACCENT_ARRAY_SIZE;i++)
            {
                if(wf1.accent[i]>wf2.accent[i]) 
                {
                    compareResult=1 ;
                    break ;
                }
                else if(wf1.accent[i]<wf2.accent[i])
                {
                    compareResult=-1 ;
                    break;
                }
            }
        }
        if (compareResult<0) return true ;
        return false ; 
    }

};



#endif	/* WORDFORM_HPP */

