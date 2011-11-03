#include "russian_chars.hpp"
#include <stdio.h>

bool isRussianChar_cp1251(unsigned char a)
{
    if(a==CAPITAL_YO_1251 || a==SMALL_YO_1251 || (CAPITAL_A_1251 <= a && a <= SMALL_YA_1251))
        return true ;
    else
        return false ;
}

unsigned char shiftCodes_yo_cp1251(unsigned char c)
{
    if (CAPITAL_ZHE_1251<=c && c<=SMALL_YE_1251) c-- ; // all chars shifts to left 1 position
    else if (CAPITAL_A_1251<=c && c<=CAPITAL_YE_1251) c-=2 ; // all chars shift 2 position left due to CAP/SMA YO
    else if(c==SMALL_YO_1251) c=SMALL_YE_1251 ; // insert YO before ZHE and shift CAPITAL_A- SAMLL_YE left 1 position
    else if(c==CAPITAL_YO_1251) c=CAPITAL_DE_1251 ; // insert YO before ZHE (shifted already by SMALL_YO )
    // no shift for any char after SMALL_YO_1251: SMALL_ZHE_1251 and >
}

int charcmp_cp1251(unsigned char a, unsigned char b)
{
    // a>b => 1
    // a<b => -1
    // a == b => 0
    if(a==b) return 0 ;

    if(isRussianChar_cp1251(a) && isRussianChar_cp1251(b))
    {
        a=shiftCodes_yo_cp1251(a) ;
        b=shiftCodes_yo_cp1251(b) ;
    }
    if(a>b) return 1;
    else    return -1;
}

int strcmp_cp1251( const char* str1, int len1, const char* str2, int len2)
{
    int i=0 ;
    int compareResult=0 ;
    for(i=0;i<len1 && i<len2;i++)
    {
        if( (compareResult=charcmp_cp1251((unsigned char)str1[i],(unsigned char)str2[i]))==0 ) continue ;
    }
    if(compareResult==0)
    {
        if(len1>len2) compareResult=1 ;
        else if(len1<len2) compareResult=-1 ;
    }
    return compareResult ;
}

char convert_char_cp1251_to_cp866( unsigned char c)
{
    if(CAPITAL_A_1251<=c && c<=SMALL_PE_1251) c-=0x40 ;
    else if(SMALL_ER_1251<=c && c<=SMALL_YA_1251) c-=010 ;
    else if(c==CAPITAL_YO_1251) c=CAPITAL_YO_866 ;
    else if(c==SMALL_YO_1251) c=SMALL_YO_866 ;
    return c ;
}
char convert_char_cp866_to_cp1251( unsigned char c)
{
    if(CAPITAL_A_866<=c && c<=SMALL_PE_866) c+=0x40 ;
    else if(SMALL_ER_866<=c && c<=SMALL_YA_866) c+=010 ;
    else if(c==CAPITAL_YO_866) c=CAPITAL_YO_1251 ;
    else if(c==SMALL_YO_866) c=SMALL_YO_1251 ;
    return c ;
}
char* convert_str_cp1251_to_cp866(char* str866,const char* str1251, int len)
{
    for(int i=0;i<len;i++)
    {
        str866[i] = convert_char_cp1251_to_cp866(str1251[i]) ;
    }
    return str866 ;
}

char* convert_str_cp866_to_cp1251(char* str1251,const char* str866, int len)
{
    for(int i=0;i<len;i++)
    {
        str1251[i] = convert_char_cp866_to_cp1251(str866[i]) ;
    }
    return str1251 ;
}

int strcmp_cp866( const char* str1, int len1, const char* str2, int len2) 
{
    // not implemented yet, 2011-10-08
    return 0 ;
}

void hexing(const char* str)
{
    for(int i=0;str[i];i++)
    {
        printf("%x ",(unsigned int)(unsigned char) str[i]) ;
    }
}