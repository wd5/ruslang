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
#include "cyrillic//russian_chars.hpp"

using namespace std;
const char* inputAccentedWordsFileName = "d:\\dev\\RussianLanguage\\Data\\Collected\\RussianWords_AllForms_Accents_86xxxBases_cp1251.txt" ;
const char* inputMissingWordsFileName = "d:\\dev\\RussianLanguage\\Data\\Collected\\RussianWords_AllForms_Accents_missing_cp1251.txt" ;
const char* outputFileName = "d:\\dev\\RussianLanguage\\Data\\Created\\RussianWords_AllForms_Len_Accents_cp1251.txt" ;

static long debug_interrupt_counter=0;
const long exit_treshold=40 ;
void debug_break()
{
    if(exit_treshold >0 && ++debug_interrupt_counter>=exit_treshold) exit(0) ;
}

class WordForm
{
private:
    static char _string[512] ;
public:
    char* word ;
    int length ;
    int accent ;        // 0 - unknown, some info is missing, some words have no vocals
    WordForm(const char* str)
    {
        int len=strlen(str); 
        word=(char*)malloc(sizeof(char)*len) ;
        memcpy(word, str,len) ;
        length=len ;
        accent=0;
    }
    WordForm(const WordForm& wf)
    {
        length=wf.length ;
        accent=wf.accent ;
        word=(char*)malloc(sizeof(char)*length) ;
        memcpy(word, wf.word,length) ;
    }
    WordForm(const char* str,int len)
    {
        word=(char*)malloc(sizeof(char)*len) ;
        memcpy(word,str,len) ;
        length=len ;
        accent=0 ;
    }
    ~WordForm()
    {
        free(word);
        word=0 ;
        length=0 ;
        accent=0;
    }
    void setAccent(int accentPosition)
    {
        accent=accentPosition ;
    }
    const char* str()
    {
        memcpy(_string,word,length) ;
        _string[length]=0 ;
        return _string ;
    }
    const char* wstr()
    {
        memcpy(_string,word,length) ;
        _string[length]=0 ;
        return _string ;
    }
    const char* str_cp866()
    {
        return convert_str_cp1251_to_cp866(_string,word,length) ;
    }
};
char WordForm::_string[512] ;

class comp_WordForm
{
public:
    bool operator()(WordForm wf1, WordForm wf2) const
    { 
        // true if wf2 > wf1, false if wf2<=wf1
        int compareResult=strcmp_cp1251(wf1.word,wf1.length,wf2.word,wf2.length) ;
        if(compareResult==0)
        {
            if(wf1.accent>wf2.accent) compareResult=1 ;
            else if(wf1.accent<wf2.accent) compareResult=-1 ;
        }
        if (compareResult<0) return true ;
        return false ; 
    }
};

// list<WordForm> wordList ;
set <WordForm,comp_WordForm> wordList ;
void parseLine (const char* line)
{
    enum {skippingHead,collectingWords} status=skippingHead ;
    char newWord[256] ;
    int newWordLength=0;
    int newWordAccentPosition=0 ;
    pair< set<WordForm,comp_WordForm>::iterator, bool> retValue ;
    for(int i=0;line[i]&&line[i]!='\r'&&line[i]!='\n';i++)
    {
        if(status==skippingHead)
        {
            if(line[i]=='#')
            {
                status=collectingWords;
                newWordLength=0;
                newWordAccentPosition=0 ;
            }
            else continue ;
        }
        else if(status==collectingWords)
        {
            if(line[i]==',')
            {
                if(newWord[0]=='-')
                {
                    ;
                }
                else
                {    
                    WordForm *wf = new WordForm(newWord,newWordLength) ;
                    wf->setAccent(newWordAccentPosition) ;
                    retValue = wordList.insert(*wf) ;
                    if(retValue.second==false)
                    {
                        delete wf ;
                        // cout <<"oops"<<endl ;
                    }
                    else
                    {    
//      Detecting words without accents
                        // cout << "word added " << wf->str_cp866() << endl ;
                        // printf("word added %x\n",(int)(unsigned char)wf->str_cp866()[0]) ;
                        wchar_t xx[10] = {0x1004,0x1104,0x1204,0};
                        // printf("word added %s\n",xx) ;
                        cout << "word added " << xx[0] << endl ;
                        debug_break() ;
                        if(newWordAccentPosition==0)
                        {
                            FILE* noAccentFile = fopen("tmpNotAccentedWords.txt","a") ;
                            newWord[newWordLength]=0;
                            fprintf(noAccentFile,"%s\n",newWord); 
                            fclose(noAccentFile) ;
                        }
                    }
                }
                newWordAccentPosition=0;
                newWordLength=0;
            }
            else if(line[i]=='\'' || line[i]=='`')
            {
                if (newWordAccentPosition==0)
                 newWordAccentPosition=newWordLength ;
            }
            else if(((unsigned char)line[i])==SMALL_YO_1251) // small Russian YO
            {
                newWordAccentPosition=newWordLength+1 ;
                newWord[newWordLength++]=line[i] ;
            }
            else
            {
                newWord[newWordLength++]=line[i] ;
            }
        }
    }
    WordForm *wf = new WordForm(newWord,newWordLength) ;
    wf->setAccent(newWordAccentPosition) ;
    retValue = wordList.insert(*wf) ;
    if(retValue.second==false)  delete wf ;
}

int main(int argc, char** argv) 
{

    locale def ;
    cout << "Default locale: " << def.name() << endl ;
    locale current = cout.getloc() ;
    cout << "cout locale: " << current.name() << endl ;
    cout.imbue(locale("russian")) ;
    current = cout.getloc() ;
    cout << "cout en locale: " << current.name() << endl ;
    
    exit(0) ;
    
    char buffer[4096] ;
    long counter=0 ;
    FILE* fin = fopen(inputAccentedWordsFileName,"r") ;
    if(fin)
    {
        while(fgets(buffer,4096,fin))
        {
            parseLine(buffer) ;
            counter++; 
        }
        cout <<"Counter [1]:"<<counter<<endl ;
        fclose(fin) ;
    }
    cout << "List size [1]: " << wordList.size() << endl ;
    
    fin = fopen(inputMissingWordsFileName,"r") ;
    if(fin)
    {
        while(fgets(buffer,4096,fin))
        {
            parseLine(buffer) ;
            counter++; 
        }
        cout <<"Counter [2]:"<<counter<<endl ;
        fclose(fin) ;
    }
    cout << "List size [2]: " << wordList.size() << endl ;
    
    FILE* fout=fopen(outputFileName,"w") ;
    set<WordForm, comp_WordForm>::iterator wi ;
    for(wi=wordList.begin();wi!=wordList.end();wi++)
    {
        char tmpStr[256] ;
        memcpy(tmpStr,wi->word,wi->length) ;
        tmpStr[wi->length]='\0' ;
        fprintf(fout,"%s;%d;%d\n",tmpStr,wi->length,wi->accent);
    }
    fclose(fout);
 
    return 0;
}
