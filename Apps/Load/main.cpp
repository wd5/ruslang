/* 
 * File:   main.cpp
 * Author: Ustas
 *
 * Created on 18 Сентябрь 2011 г., 13:00
 */

#include <cstdlib>
#include <locale>
#include <iostream>
#include <fstream>
#include <sstream>
#include <list>
#include <string>
#include <set>
#include <iterator>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include "cyrillic/russian_chars.hpp"
#include "cyrillic/cp1251.hpp"
#include "misctools.h"
#include "wordform.hpp"

using namespace std;
const char* inputAccentedWordsFileName = "d:/dev/RussianLanguage/Data/Collected/RussianWords_AllForms_Accents_86xxxBases_cp1251.txt" ;
const char* inputMissingWordsFileName = "d:/dev/RussianLanguage/Data/Collected/RussianWords_AllForms_Accents_missing_cp1251.txt" ;
const char* outputFileName = "d:/dev/RussianLanguage/Data/Created/RussianWords_AllForms_Len_Accents_cp1251.txt" ;

// set <WordForm,comp_WordForm> wordList ;
set <WordForm> wordList ; // WordForm operators == and < exist
cp1251 console ;

/*
 * parseLine parses line from files of this format:
 * mainform#form1,form2,form3,...
 * any formX can have one or multiple chars ' or ` as positions of accents in the word
 * files of this format are:
 * - RussianWords_AllForms_Accents_86xxxBases_cp1251.txt
 * - RussianWords_AllForms_Accents_missing_cp1251.txt
 */

unsigned long _ID_counter=1 ;
void parseLine (const char* line)
{
    enum {skippingHead,collectingWords} status=skippingHead ;
    char newWord[256] ;
    int newWordLength=0;
    bool lastCharYO=false ;
    
    short newWordAccents[ACCENT_ARRAY_SIZE] ;
    int newWordAccentIndex=0;
    for(newWordAccentIndex=0;newWordAccentIndex<ACCENT_ARRAY_SIZE;newWordAccentIndex++)  
        newWordAccents[newWordAccentIndex]=0;
    newWordAccentIndex=0 ;
    
    pair< set<WordForm>::iterator, bool> retValue ;
    WordForm wf ("",0);
    
    for(int i=0;line[i]!='\r'&&line[i]!='\n'&&line[i]!='\0';i++)
    {
        if(status==collectingWords)
        {
            if(line[i]==',')
            {
                if(newWord[0]=='-')
                {;}
                else
                {    
                    wf.reset(newWord,newWordLength,newWordAccents) ;
                    wf.id=_ID_counter ;
                    retValue = wordList.insert(wf) ;
                    if(retValue.second==false)
                    {   // such wordform already exists in SET

                    }
                    else
                    {    
                        _ID_counter++ ;
                        if(newWordAccents[0]==0)
                        {   // No accent found
                            FILE* noAccentFile = fopen("tmpNotAccentedWords.txt","a") ;
                            newWord[newWordLength]=0;
                            fprintf(noAccentFile,"%s\n",newWord); 
                            fclose(noAccentFile) ;
                        }
                    }
                }
                
                for(newWordAccentIndex=0;newWordAccentIndex<ACCENT_ARRAY_SIZE;newWordAccentIndex++)  
                    newWordAccents[newWordAccentIndex]=0;
                newWordAccentIndex=0 ;
                lastCharYO=false ;
                newWordLength=0;
            }
            else if(line[i]=='\'' || line[i]=='`')
            {
                if(lastCharYO==true) continue ; // avoid double accent
     
                lastCharYO=false ;
                if (newWordAccentIndex<ACCENT_ARRAY_SIZE)
                        newWordAccents[newWordAccentIndex++]=newWordLength ;
                else
                {
                    cout << "a word found with number of accents greater than " << ACCENT_ARRAY_SIZE << endl ;
                    cout << "line is below:" <<endl ;
                    char tmpStr[1024] ;
                    console.convert(line,strlen(line),tmpStr,1024) ;
                    cout << tmpStr << endl ;
                    exit(0) ;
                }    
            }
            else if(((unsigned char)line[i])==SMALL_YO_1251 || ((unsigned char)line[i])==CAPITAL_YO_1251) //  Russian YO is always accented
            {
                if (newWordAccentIndex<ACCENT_ARRAY_SIZE)
                        newWordAccents[newWordAccentIndex++]=newWordLength+1  ;
                else
                {
                    cout << "a word found with number of accents greater than " << ACCENT_ARRAY_SIZE << endl ;
                    cout << "line is below:" <<endl ;
                    char tmpStr[1024] ;
                    console.convert(line,strlen(line),tmpStr,1024) ;
                    cout << tmpStr << endl ;
                    exit(0) ;
                } 
                newWord[newWordLength++]=line[i] ;
                lastCharYO=true ;
            }
            else
            {
                newWord[newWordLength++]=line[i] ;
                lastCharYO=false ;
            }
        }
        else if(status==skippingHead)
        {
            lastCharYO=false ;
            if(line[i]=='#')
            {
                status=collectingWords;
                newWordLength=0;
                for(newWordAccentIndex=0;newWordAccentIndex<ACCENT_ARRAY_SIZE;newWordAccentIndex++)  
                    newWordAccents[newWordAccentIndex]=0;
                newWordAccentIndex=0 ;
            }
            else continue ;
        }
    }
    if(status==collectingWords)
    {    
        wf.reset(newWord,newWordLength,newWordAccents) ;
        wf.id=_ID_counter ;
        retValue = wordList.insert(wf) ;
        if(retValue.second==false)
        {   // such wordform already exists in SET
        }
        else
        {    
            _ID_counter++ ;
            if(newWordAccents[0]==0)
            {   // No accent found
                FILE* noAccentFile = fopen("tmpNotAccentedWords.txt","a") ;
                newWord[newWordLength]=0;
                fprintf(noAccentFile,"%s\n",newWord); 
                fclose(noAccentFile) ;
            }
        }
    }   
}

int main(int argc, char** argv) 
{
    clock_t starttime=clock() ;
    char buffer[4096] ;
    long counter=0 ;
    FILE* fin ;
    fin = fopen(inputAccentedWordsFileName,"r") ;
    if(fin)
    {
        cout << "Reading file: " << inputAccentedWordsFileName << endl ;
        while(fgets((char*)buffer,4096,fin))
        {
            parseLine(buffer) ;
            counter++; 
        }
        
        cout <<"Lines read: "<<counter<<endl ;
        fclose(fin) ;
    }
    cout << "Word forms added: " << wordList.size() << endl ;
    
    fin = fopen(inputMissingWordsFileName,"r") ;
    counter=0 ;
    if(fin)
    {
        cout << "Reading file: " << inputMissingWordsFileName << endl ;
        while(fgets((char*)buffer,4096,fin))
        {
            parseLine(buffer) ;
            counter++; 
        }

        cout <<"Lines read: "<<counter<<endl ;
        fclose(fin) ;
    }
    cout << "Total word forms added: " << wordList.size() << endl ;
    
    FILE* fout;
    fout=fopen(outputFileName,"w") ;

    set<WordForm>::iterator wi ;
    for(wi=wordList.begin();wi!=wordList.end();wi++)
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

//        // printing to console to check
//        unsigned char tmpStrConsole[512] ;
//        console.convert(tmpStr,wi->length,tmpStrConsole,512) ;
//        printf ("Console Word: %s\n",tmpStrConsole) ;
    }
    fclose(fout);
    clock_t endtime = clock() ;
    cout << "Execution time: " << (endtime-starttime)/CLOCKS_PER_SEC << "sec" << endl;
    return 0;
}
