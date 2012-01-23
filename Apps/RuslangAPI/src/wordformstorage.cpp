/* 
 * File:   wordformstorage.cpp
 * Author: Ustas
 *
 * Created on 2011-11-30
 */

#include <stdio.h>      // for ::save()
#include <iterator>
#include "wordformstorage.hpp"

unsigned long WordFormStorage::ID_counter = 1 ;

bool WordFormStorage::add(WordForm& wf)  
{
    pair< set<WordForm>::iterator, bool> wfRetValue ;
    wf.id=ID_counter ;
    wfRetValue = wfSet.insert(wf) ;
    if(wfRetValue.second==false)
       // such wordform already exists in SET
        return false ;
    lastAddedWordForm = &(*wfRetValue.first) ;
    ID_counter++ ;
    return true ; 
}

bool WordFormStorage::remove(const WordForm& wf)  
{
    
    return true ; 
}
void WordFormStorage::clear()  
{
    lastAddedWordForm=NULL ;
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

void WordFormStorage::load (const char* filename) 
{
    FILE* fin;
    fin=fopen(filename,"r") ;
    
    WordForm wf ("",0);
    unsigned long newWordID ;
    char newWord[256] ;
    int newWordLength=0;
    
    char newWordAccentBuffer[16] ;
    short newWordAccents[ACCENT_ARRAY_SIZE] ;
    int newWordAccentIndex=0;
    for(newWordAccentIndex=0;newWordAccentIndex<ACCENT_ARRAY_SIZE;newWordAccentIndex++)  
        newWordAccents[newWordAccentIndex]=0;
    newWordAccentIndex=0 ;
    
    
    while(!feof(fin))
    {
        fscanf(fin,"%ld;%s;%d;%s",&newWordID,newWord,&newWordLength,newWordAccentBuffer) ;
        wf.reset(newWord,newWordLength,newWordAccents) ;
        add(wf) ;
    }

    fclose(fin) ;
} 
const WordForm* WordFormStorage::lastAdded() const
{
    return lastAddedWordForm ;
}

WordFormStorage::WordFormStorage() 
{
    lastAddedWordForm=NULL ;
}
WordFormStorage::~WordFormStorage() 
{
    lastAddedWordForm=NULL ;
}
