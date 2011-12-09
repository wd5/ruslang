/* 
 * File:   letterset.hpp
 * Author: ustas
 *
 * Created on November 19, 2011, 12:13 AM
 * Last modified: 2011-12-01
 * 
 */

#ifndef LETTERSET_HPP
#define	LETTERSET_HPP

#include <cstring>
#include <cstdlib>
#include "wordform.hpp"

// const int MAX_WORD_LENGTH=256 ;

class LetterSet
{
public:
    char* letters ;
    short* cnt ;
    int length ;
    unsigned long id ;
    mutable unsigned long *wfLinked ;
    mutable unsigned int wfLinkedCounter ;
    LetterSet(const LetterSet& ls) ;
    LetterSet(const WordForm& wf ) ;
    LetterSet(const char* str) ;
    LetterSet(const char* str, int strLength) ;
    ~LetterSet()
    {
        if(letters) 
        { 
            std::free(letters); 
            letters=NULL;

        } 
        if(cnt) 
        { 
            std::free(cnt); 
            cnt=NULL;
        }
        length=0 ; 
    }
    void init(const char* str,int strSize) ;
    void reset(const char* str,int strSize) ;
    char* str( char* s) const ;
    bool operator<(const LetterSet& ls) const ; 
    void link(const WordForm& wf) const ; 
};

#endif	/* LETTERSET_HPP */

