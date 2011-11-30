#include "lettersetstorage.hpp"
#include "wordform.hpp"
#include <cstring>
#include <iterator>
#include <stdio.h> // for printf

// debug
#include <iostream>

unsigned long LetterSetStorage::ID_counter =1;

const int NUMBER_OF_LETTERS_IN_CP1251=256;
const int NUMBER_OF_LETTERS= NUMBER_OF_LETTERS_IN_CP1251;

bool LetterSetStorage::add(LetterSet& ls) 
{
    pair< set<LetterSet>::iterator, bool> lsRetValue ;
    
    ls.id=ID_counter;
    lsRetValue = lsSet.insert(ls) ;
    if(lsRetValue.second==false )
        return false ;
    ID_counter++ ;
    return true ;
}
bool LetterSetStorage::remove(const LetterSet& ls) 
{
    return true ;
}
void LetterSetStorage::clear() 
{
    
}
unsigned long LetterSetStorage::size() const 
{
    return lsSet.size() ;
}
void LetterSetStorage::save (const char* filename) const 
{
    FILE* fout=fopen(filename,"w") ;

    set<LetterSet>::iterator ls ;
    for(ls=lsSet.begin();ls!=lsSet.end();ls++)
    {
        char tmpStr[256] ;
        fprintf(fout,"%ld;%s",ls->id,ls->str(tmpStr));
        fprintf (fout,"\n") ;
    }
    fclose(fout);
}