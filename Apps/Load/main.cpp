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

set <WordForm,comp_WordForm> wordList ;
cp1251 console ;

/*
 * parseLine parses line from files of this format:
 * mainform#form1,form2,form3,...
 * any formX can have one or multiple chars ' or ` as positions of accents in the word
 * files of this format are:
 * - RussianWords_AllForms_Accents_86xxxBases_cp1251.txt
 * - RussianWords_AllForms_Accents_missing_cp1251.txt
 */


void parseLine (const unsigned char* line)
{
    enum {skippingHead,collectingWords} status=skippingHead ;
    unsigned char newWord[256] ;
    int newWordLength=0;
    bool lastCharYO=false ;
    
    int newWordAccents[ACCENT_ARRAY_SIZE] ;
    int newWordAccentIndex=0;
    for(newWordAccentIndex=0;newWordAccentIndex<ACCENT_ARRAY_SIZE;newWordAccentIndex++)  
        newWordAccents[newWordAccentIndex]=0;
    newWordAccentIndex=0 ;
    
    pair< set<WordForm,comp_WordForm>::iterator, bool> retValue ;
    for(int i=0;line[i]&&line[i]!='\r'&&line[i]!='\n';i++)
    {
        if(status==skippingHead)
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
        else if(status==collectingWords)
        {
            if(line[i]==',')
            {
                if(newWord[0]=='-')
                {;}
                else
                {    
                    WordForm *wf = new WordForm(newWord,newWordLength) ;
                    for(int j=0;j<ACCENT_ARRAY_SIZE && newWordAccents[j];j++)
                        wf->setAccent(newWordAccents[j]) ;
                    retValue = wordList.insert(*wf) ;
                    if(retValue.second==false)
                    {   // such wordform already exists
                        delete wf ;
                    }
                    else
                    {    
                        // No accent found
                        if(newWordAccents[0]==0)
                        {
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
                    printf("a word found with number of accents greater than %d\n", ACCENT_ARRAY_SIZE) ;
                    printf("line is below:\n") ;
                    unsigned char tmpStr[1024] ;
                    console.convert(line,strlen((const char*)line),tmpStr,1024) ;
                    printf("%s", tmpStr) ;
                    exit(0) ;
                }    
            }
            else if(((unsigned char)line[i])==SMALL_YO_1251 || ((unsigned char)line[i])==CAPITAL_YO_1251) //  Russian YO
            {
                if (newWordAccentIndex<ACCENT_ARRAY_SIZE)
                        newWordAccents[newWordAccentIndex++]=newWordLength+1  ;
                else
                {
                    printf("a word found with number of accents greater than %d\n", ACCENT_ARRAY_SIZE) ;
                    printf("line is below:\n") ;
                    unsigned char tmpStr[1024] ;
                    console.convert(line,strlen((const char*)line),tmpStr,1024) ;
                    printf("%s", tmpStr) ;
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
    }
    WordForm *wf = new WordForm(newWord,newWordLength) ;
    for(int k=0;k<ACCENT_ARRAY_SIZE && newWordAccents[k];k++)
           wf->setAccent(newWordAccents[k]) ;
    retValue = wordList.insert(*wf) ;
    if(retValue.second==false)  delete wf ;
}

int main(int argc, char** argv) 
{
    clock_t starttime=clock() ;
    unsigned char buffer[4096] ;
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
    set<WordForm, comp_WordForm>::iterator wi ;
    for(wi=wordList.begin();wi!=wordList.end();wi++)
    {
        unsigned char tmpStr[256] ;
        wi->str(tmpStr) ;
        fprintf(fout,"%s;%d;",tmpStr,wi->length);
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
    printf("Execution time: %d sec\n", (endtime-starttime)/CLOCKS_PER_SEC) ;
    return 0;
}
