#include "russian_chars.hpp"
#include <stdio.h>

unsigned char template_order_cp1251[] = 
{
0x00,	0x01,	0x02,	0x03,	0x04,	0x05,	0x06,	0x07,	0x08,	0x09,	0x0A,	0x0B,	0x0C,	0x0D,	0x0E,	0x0F,
0x10,	0x11,	0x12,	0x13,	0x14,	0x15,	0x16,	0x17,	0x18,	0x19,	0x1A,	0x1B,	0x1C,	0x1D,	0x1E,	0x1F,
0x20,	0x21,	0x22,	0x23,	0x24,	0x25,	0x26,	0x27,	0x28,	0x29,	0x2A,	0x2B,	0x2C,	0x2D,	0x2E,	0x2F,
0x30,	0x31,	0x32,	0x33,	0x34,	0x35,	0x36,	0x37,	0x38,	0x39,	0x3A,	0x3B,	0x3C,	0x3D,	0x3E,	0x3F,
0x40,	0x41,	0x42,	0x43,	0x44,	0x45,	0x46,	0x47,	0x48,	0x49,	0x4A,	0x4B,	0x4C,	0x4D,	0x4E,	0x4F,
0x50,	0x51,	0x52,	0x53,	0x54,	0x55,	0x56,	0x57,	0x58,	0x59,	0x5A,	0x5B,	0x5C,	0x5D,	0x5E,	0x5F,
0x60,	0x61,	0x62,	0x63,	0x64,	0x65,	0x66,	0x67,	0x68,	0x69,	0x6A,	0x6B,	0x6C,	0x6D,	0x6E,	0x6F,
0x70,	0x71,	0x72,	0x73,	0x74,	0x75,	0x76,	0x77,	0x78,	0x79,	0x7A,	0x7B,	0x7C,	0x7D,	0x7E,	0x7F,
0x80,	0x81,	0x82,	0x83,	0x84,	0x85,	0x86,	0x87,	0x88,	0x89,	0x8A,	0x8B,	0x8C,	0x8D,	0x8E,	0x8F,
0x90,	0x91,	0x92,	0x93,	0x94,	0x95,	0x96,	0x97,	0x98,	0x99,	0x9A,	0x9B,	0x9C,	0x9D,	0x9E,	0x9F,
0xA0,	0xA1,	0xA2,	0xA3,	0xA4,	0xA5,	0xA6,	0xA7,	0xA8,	0xA9,	0xAA,	0xAB,	0xAC,	0xAD,	0xAE,	0xAF,
0xB0,	0xB1,	0xB2,	0xB3,	0xB4,	0xB5,	0xB6,	0xB7,	0xB8,	0xB9,	0xBA,	0xBB,	0xBC,	0xBD,	0xBE,	0xBF,
0xC0,	0xC1,	0xC2,	0xC3,	0xC4,	0xC5,	0xC6,	0xC7,	0xC8,	0xC9,	0xCA,	0xCB,	0xCC,	0xCD,	0xCE,	0xCF,
0xD0,	0xD1,	0xD2,	0xD3,	0xD4,	0xD5,	0xD6,	0xD7,	0xD8,	0xD9,	0xDA,	0xDB,	0xDC,	0xDD,	0xDE,	0xDF,
0xE0,	0xE1,	0xE2,	0xE3,	0xE4,	0xE5,	0xE6,	0xE7,	0xE8,	0xE9,	0xEA,	0xEB,	0xEC,	0xED,	0xEE,	0xEF,
0xF0,	0xF1,	0xF2,	0xF3,	0xF4,	0xF5,	0xF6,	0xF7,	0xF8,	0xF9,	0xFA,	0xFB,	0xFC,	0xFD,	0xFE,	0xFF

} ;


unsigned char order_cp1251[] = 
{
0x00,	0x01,	0x02,	0x03,	0x04,	0x05,	0x06,	0x07,	0x08,	0x09,	0x0A,	0x0B,	0x0C,	0x0D,	0x0E,	0x0F,
0x10,	0x11,	0x12,	0x13,	0x14,	0x15,	0x16,	0x17,	0x18,	0x19,	0x1A,	0x1B,	0x1C,	0x1D,	0x1E,	0x1F,
0x20,	0x21,	0x22,	0x23,	0x24,	0x25,	0x26,	0x27,	0x28,	0x29,	0x2A,	0x2B,	0x2C,	0x2D,	0x2E,	0x2F,
0x30,	0x31,	0x32,	0x33,	0x34,	0x35,	0x36,	0x37,	0x38,	0x39,	0x3A,	0x3B,	0x3C,	0x3D,	0x3E,	0x3F,
0x40,	0x41,	0x42,	0x43,	0x44,	0x45,	0x46,	0x47,	0x48,	0x49,	0x4A,	0x4B,	0x4C,	0x4D,	0x4E,	0x4F,
0x50,	0x51,	0x52,	0x53,	0x54,	0x55,	0x56,	0x57,	0x58,	0x59,	0x5A,	0x5B,	0x5C,	0x5D,	0x5E,	0x5F,
0x60,	0x61,	0x62,	0x63,	0x64,	0x65,	0x66,	0x67,	0x68,	0x69,	0x6A,	0x6B,	0x6C,	0x6D,	0x6E,	0x6F,
0x70,	0x71,	0x72,	0x73,	0x74,	0x75,	0x76,	0x77,	0x78,	0x79,	0x7A,	0x7B,	0x7C,	0x7D,	0x7E,	0x7F,
0x80,	0x81,	0x82,	0x83,	0x84,	0x85,	0x86,	0x87,	0x88,	0x89,	0x8A,	0x8B,	0x8C,	0x8D,	0x8E,	0x8F,
0x90,	0x91,	0x92,	0x93,	0x94,	0x95,	0x96,	0x97,	0x98,	0x99,	0x9A,	0x9B,	0x9C,	0x9D,	0x9E,	0x9F,
0xA0,	0xA1,	0xA2,	0xA3,	0xA4,	0xA5,	0xA6,	0xA7,	0xC4,	0xA8,	0xA9,	0xAA,	0xAB,	0xAC,	0xAD,	0xAE,
0xAF,	0xB0,	0xB1,	0xB2,	0xB3,	0xB4,	0xB5,	0xB6,	0xE5,	0xB7,	0xB8,	0xB9,	0xBA,	0xBB,	0xBC,	0xBD,
0xBE,	0xBF,	0xC0,	0xC1,	0xC2,	0xC3,	0xC5,	0xC6,	0xC7,	0xC8,	0xC9,	0xCA,	0xCB,	0xCC,	0xCD,	0xCE,
0xCF,	0xD0,	0xD1,	0xD2,	0xD3,	0xD4,	0xD5,	0xD6,	0xD7,	0xD8,	0xD9,	0xDA,	0xDB,	0xDC,	0xDD,	0xDE,
0xDF,	0xE0,	0xE1,	0xE2,	0xE3,	0xE4,	0xE6,	0xE7,	0xE8,	0xE9,	0xEA,	0xEB,	0xEC,	0xED,	0xEE,	0xEF,
0xF0,	0xF1,	0xF2,	0xF3,	0xF4,	0xF5,	0xF6,	0xF7,	0xF8,	0xF9,	0xFA,	0xFB,	0xFC,	0xFD,	0xFE,	0xFF
} ;

unsigned char number_codes[10] = 
{
    0x30, 0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37, 0x38, 0x39
} ;

using namespace cp1251 ;

bool cp1251::isRussianChar(char signeda)
{
    unsigned char a = (unsigned char)signeda ;
    if((cp1251::CAPITAL_A <= a 
            // && a <= cp1251::SMALL_YA // commented due to compiler warning
                                        // comparison is always true due to limited range of data type
        ) || a==cp1251::SMALL_YO || a==cp1251::CAPITAL_YO )
        return true ;
    else
        return false ;
}

unsigned char shiftCodes_yo_cp1251(unsigned char c)
{
    if (cp1251::CAPITAL_ZHE<=c && c<=cp1251::SMALL_YE) c-- ; // all chars shifts to left 1 position
    else if (cp1251::CAPITAL_A<=c && c<=cp1251::CAPITAL_YE) c-=2 ; // all chars shift 2 position left due to CAP/SMA YO
    else if(c==cp1251::SMALL_YO) c=cp1251::SMALL_YE ; // insert YO before ZHE and shift CAPITAL_A- SAMLL_YE left 1 position
    else if(c==cp1251::CAPITAL_YO) c=cp1251::CAPITAL_DE ; // insert YO before ZHE (shifted already by SMALL_YO )
    // no shift for any char after cp1251::SMALL_YO: cp1251::SMALL_ZHE and >
    return c ;
}

int cp1251::charcmp(char signeda, char signedb)
{
    // a>b => 1
    // a<b => -1
    // a == b => 0
    unsigned char a=(unsigned char)signeda ;
    unsigned char b=(unsigned char)signedb ;
    if(a==b) return 0 ;

    if(isRussianChar(signeda) && isRussianChar(signedb))
    {
        a=shiftCodes_yo_cp1251(a) ;
        b=shiftCodes_yo_cp1251(b) ;
    }
    if(a>b) return 1;
    else    return -1;
}

int cp1251::strcmp( const char* str1, int len1, const char* str2, int len2)
{
    int i=0 ;
    for(i=0;i<len1 && i<len2;i++)
    {
        if( str1[i] == str2[i] ) continue ;
        if( order_cp1251[(unsigned char)(str1[i])] < order_cp1251[(unsigned char)(str2[i])])
            return -1 ;
        else
            return 1 ;
    }
    // strings are equal, checking length
    if          (len1>len2) return  1 ;
    else if     (len1<len2) return -1 ;
    // else (len1 == len2) == true
        
    return 0 ;
}

unsigned char convert_char_cp1251_to_cp866( unsigned char c)
{
    if(cp1251::CAPITAL_A<=c && c<=cp1251::SMALL_PE) c-=0x40 ;
    else if(cp1251::SMALL_ER<=c
            // && c<=cp1251::SMALL_YA           // excluded due to compiler warning
                                                // comparison is always true due to limited range of data type
            ) c-=010 ;
    else if(c==cp1251::CAPITAL_YO) c=cp866::CAPITAL_YO ;
    else if(c==cp1251::SMALL_YO) c=cp866::SMALL_YO ;
    return c ;
}
unsigned char convert_char_cp866_to_cp1251( unsigned char c)
{
    if(cp866::CAPITAL_A<=c && c<=cp866::SMALL_PE) c+=0x40 ;
    else if(cp866::SMALL_ER<=c && c<=cp866::SMALL_YA) c+=010 ;
    else if(c==cp866::CAPITAL_YO) c=cp1251::CAPITAL_YO ;
    else if(c==cp866::SMALL_YO) c=cp1251::SMALL_YO ;
    return c ;
}
 char* convert_str_cp1251_to_cp866(char* str866,const  char* str1251, int len)
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
        printf("%x ",(unsigned int) (unsigned char) str[i]) ;
    }
}
