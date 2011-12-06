/* 
 * File:   lettersetstorage.hpp
 * Author: ustas
 *
 * Created on Dec 1, 2011, 00:19 AM
 * Last modified: 2011-12-01
 * 
 */

#ifndef LETTERSETSTORAGE_HPP
#define	LETTERSETSTORAGE_HPP

#include <cstring>
#include <cstdlib>
#include <set>
#include "letterset.hpp"
using namespace std ;

// const int MAX_WORD_LENGTH=256 ;


class LetterSetStorage
{
private:
    static unsigned long ID_counter ;
public:
    set <LetterSet> lsSet ;  

    LetterSetStorage() {}
    ~LetterSetStorage() { }
    
    bool add(LetterSet& ls) ;
    bool add(const WordForm& wf) ;
    bool remove(const LetterSet& ls) ;
    void clear() ;
    unsigned long size() const ;
    void save (const char* filename) const ;
};



#endif	/* LETTERSETSTORAGE_HPP */

