/* 
 * File:   wordformstorage.hpp
 * Author: Victor
 *
 * Created on November 30, 2011, 23:26 PM
 * Last modified: 2011-12-01
 * 
 */

#ifndef WORDFORMSTORAGE_HPP
#define	WORDFORMSTORAGE_HPP

#include <set>
#include "wordform.hpp"
using namespace std;

class WordFormStorage
{
private:
     static unsigned long ID_counter ;
     const WordForm*  lastAddedWordForm ;
public:
    set <WordForm> wfSet ;  
    WordFormStorage() ;
    ~WordFormStorage() ;
    bool add(WordForm& wf) ;

    bool remove(const WordForm& wf) ;
    void clear() ;
    unsigned long size() const ;
    void save (const char* filename) const ;
    void load (const char* filename) ;
    const WordForm* lastAdded() const ;
};


#endif	/* WORDFORMSTORAGE_HPP */

