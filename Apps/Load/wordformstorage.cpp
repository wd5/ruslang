/* 
 * File:   wordformstorage.cpp
 * Author: Ustas
 *
 * Created on 2011-11-30
 */

#include <stdio.h>      // for ::save()
#include "wordformstorage.hpp"
#include <iterator>


unsigned long WordFormStorage::ID_counter = 1 ;

bool WordFormStorage::add(WordForm& wf)  
{
    pair< set<WordForm>::iterator, bool> wfRetValue ;
    wf.id=ID_counter ;
    wfRetValue = wfSet.insert(wf) ;
    if(wfRetValue.second==false)
       // such wordform already exists in SET
        return false ;
    ID_counter++ ;
    return true ; 
}
bool WordFormStorage::remove(const WordForm& wf)  
{
    
    return true ; 
}
void WordFormStorage::clear()  
{

}

unsigned long WordFormStorage::size()  const
{
    return wfSet.size() ; 
}

void WordFormStorage::save (const char* filename) const
{
    FILE* fout;
    fout=fopen(filename,"w") ;

    set<WordForm>::iterator wi ;
    for(wi=wfSet.begin();wi!=wfSet.end();wi++)
    {
        char tmpStr[256] ;
        wi->str(tmpStr) ;
        fprintf(fout,"%ld;%s;%d;",wi->id,tmpStr,wi->length);
        if(wi->accent[0]==0)
            fprintf(fout,"0");
        else
            for(int i=0;i<ACCENT_ARRAY_SIZE;i++)
            {
                if(wi->accent[i]>0)
                {
                    if(i>0) fprintf(fout,",") ;
                    fprintf(fout,"%d", wi->accent[i]);
                }
            }
        fprintf (fout,"\n") ;
    }
    fclose(fout);
 
}

WordFormStorage::WordFormStorage() 
{

}
WordFormStorage::~WordFormStorage() 
{

}
