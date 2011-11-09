/* 
 * File:   wordform.cpp
 * Author: Ustas
 *
 * Created on 2011-11-06
 */

#include <string.h>
#include <stdlib.h>
#include "wordform.hpp"

char WordForm::_string[512] ;

bool WordForm::operator<(const WordForm& wf) const 
{
    // true if this < wf
    int compareResult=strcmp_cp1251(word,length,wf.word,wf.length) ;
    if(compareResult==0)
    {
        for(int i=0;i<ACCENT_ARRAY_SIZE;i++)
        {
            if(accent[i]>wf.accent[i]) 
            {
                compareResult=1 ;
                break ;
            }
            else if(accent[i]<wf.accent[i])
            {
                compareResult=-1 ;
                break;
            }
        }
    }
    if (compareResult<0) return true ;
    return false ; 
}
