/* 
 * File:   russian_chars.hpp
 * Author: ustas
 *
 * Created on 3 Октябрь 2011 г., 0:25
 */

#ifndef RUSSIAN_CHARS_HPP
#define	RUSSIAN_CHARS_HPP


namespace cp1251
{
    const unsigned char CAPITAL_A=0xC0;
    const unsigned char CAPITAL_BE=0xC1;
    const unsigned char CAPITAL_WE=0xC2;
    const unsigned char CAPITAL_GE=0xC3;
    const unsigned char CAPITAL_DE=0xC4;
    const unsigned char CAPITAL_YE=0xC5;
    const unsigned char CAPITAL_YO=0xA8; // ---------
    const unsigned char CAPITAL_ZHE=0xC6;
    const unsigned char CAPITAL_ZE=0xC7;
    const unsigned char CAPITAL_I=0xC8;
    const unsigned char CAPITAL_J=0xC9;
    const unsigned char CAPITAL_KA=0xCA;
    const unsigned char CAPITAL_EL=0xCB;
    const unsigned char CAPITAL_EM=0xCC;
    const unsigned char CAPITAL_EN=0xCD;
    const unsigned char CAPITAL_O=0xCE;
    const unsigned char CAPITAL_PE=0xCF;
    const unsigned char CAPITAL_ER=0xD0;
    const unsigned char CAPITAL_ES=0xD1;
    const unsigned char CAPITAL_TE=0xD2;
    const unsigned char CAPITAL_U=0xD3;
    const unsigned char CAPITAL_FE=0xD4;
    const unsigned char CAPITAL_HE=0xD5;
    const unsigned char CAPITAL_CE=0xD5;
    const unsigned char CAPITAL_CHE=0xD7;
    const unsigned char CAPITAL_SHE=0xD8;
    const unsigned char CAPITAL_SCHE=0xD9;
    const unsigned char CAPITAL_HARDSIGN=0xDA;
    const unsigned char CAPITAL_YY=0xDB;
    const unsigned char CAPITAL_SOFTSIGN=0xDC;
    const unsigned char CAPITAL_E=0xDD;
    const unsigned char CAPITAL_YU=0xDE;
    const unsigned char CAPITAL_YA=0xDF;


    const unsigned char SMALL_A=0xE0;
    const unsigned char SMALL_BE=0xE1;
    const unsigned char SMALL_WE=0xE2;
    const unsigned char SMALL_GE=0xE3;
    const unsigned char SMALL_DE=0xE4;
    const unsigned char SMALL_YE=0xE5;
    const unsigned char SMALL_YO=0xB8; // -----------
    const unsigned char SMALL_ZHE=0xE6;
    const unsigned char SMALL_ZE=0xE7;
    const unsigned char SMALL_I=0xE8;
    const unsigned char SMALL_J=0xE9;
    const unsigned char SMALL_KA=0xEA;
    const unsigned char SMALL_EL=0xEB;
    const unsigned char SMALL_EM=0xEC;
    const unsigned char SMALL_EN=0xED;
    const unsigned char SMALL_O=0xEE;
    const unsigned char SMALL_PE=0xEF;
    const unsigned char SMALL_ER=0xF0;
    const unsigned char SMALL_ES=0xF1;
    const unsigned char SMALL_TE=0xF2;
    const unsigned char SMALL_U=0xF3;
    const unsigned char SMALL_FE=0xF4;
    const unsigned char SMALL_HE=0xF5;
    const unsigned char SMALL_CE=0xF6;
    const unsigned char SMALL_CHE=0xF7;
    const unsigned char SMALL_SHE=0xF8;
    const unsigned char SMALL_SCHE=0xF9;
    const unsigned char SMALL_HARDSIGN=0xFA;
    const unsigned char SMALL_YY=0xFB;
    const unsigned char SMALL_SOFTSIGN=0xFC;
    const unsigned char SMALL_E=0xFD;
    const unsigned char SMALL_YU=0xFE;
    const unsigned char SMALL_YA=0xFF;
    
    bool isRussianChar(char signeda) ;
    int charcmp(char signeda, char signedb) ;
    int strcmp( const  char* str1, int len1, const  char* str2, int len2) ;
} ;

namespace ANSI
{
    const unsigned char NUMBER_0 = 0x30 ;
    const unsigned char NUMBER_1 = 0x31 ;
    const unsigned char NUMBER_2 = 0x32 ;
    const unsigned char NUMBER_3 = 0x33 ;
    const unsigned char NUMBER_4 = 0x34 ;
    const unsigned char NUMBER_5 = 0x35 ;
    const unsigned char NUMBER_6 = 0x36 ;
    const unsigned char NUMBER_7 = 0x37 ;
    const unsigned char NUMBER_8 = 0x38 ;
    const unsigned char NUMBER_9 = 0x39 ;

} ;

namespace cp866
{
    const unsigned char CAPITAL_A=0x80;
    const unsigned char CAPITAL_BE=0x81;
    const unsigned char CAPITAL_WE=0x82;
    const unsigned char CAPITAL_GE=0x83;
    const unsigned char CAPITAL_DE=0x84;
    const unsigned char CAPITAL_YE=0x85;
    const unsigned char CAPITAL_YO=0xF0; // ---------
    const unsigned char CAPITAL_ZHE=0x86;
    const unsigned char CAPITAL_ZE=0x87;
    const unsigned char CAPITAL_I=0x88;
    const unsigned char CAPITAL_J=0x89;
    const unsigned char CAPITAL_KA=0x8A;
    const unsigned char CAPITAL_EL=0x8B;
    const unsigned char CAPITAL_EM=0x8C;
    const unsigned char CAPITAL_EN=0x8D;
    const unsigned char CAPITAL_O=0x8E;
    const unsigned char CAPITAL_PE=0x8F;
    const unsigned char CAPITAL_ER=0x90;
    const unsigned char CAPITAL_ES=0x91;
    const unsigned char CAPITAL_TE=0x92;
    const unsigned char CAPITAL_U=0x93;
    const unsigned char CAPITAL_FE=0x94;
    const unsigned char CAPITAL_HE=0x95;
    const unsigned char CAPITAL_CE=0x95;
    const unsigned char CAPITAL_CHE=0x97;
    const unsigned char CAPITAL_SHE=0x98;
    const unsigned char CAPITAL_SCHE=0x99;
    const unsigned char CAPITAL_HARDSIGN=0x9A;
    const unsigned char CAPITAL_YY=0x9B;
    const unsigned char CAPITAL_SOFTSIGN=0x9C;
    const unsigned char CAPITAL_E=0x9D;
    const unsigned char CAPITAL_YU=0x9E;
    const unsigned char CAPITAL_YA=0x9F;


    const unsigned char SMALL_A=0xA0;
    const unsigned char SMALL_BE=0xA1;
    const unsigned char SMALL_WE=0xA2;
    const unsigned char SMALL_GE=0xA3;
    const unsigned char SMALL_DE=0xA4;
    const unsigned char SMALL_YE=0xA5;
    const unsigned char SMALL_YO=0xF1; // -----------
    const unsigned char SMALL_ZHE=0xA6;
    const unsigned char SMALL_ZE=0xA7;
    const unsigned char SMALL_I=0xA8;
    const unsigned char SMALL_J=0xA9;
    const unsigned char SMALL_KA=0xAA;
    const unsigned char SMALL_EL=0xAB;
    const unsigned char SMALL_EM=0xAC;
    const unsigned char SMALL_EN=0xAD;
    const unsigned char SMALL_O=0xAE;
    const unsigned char SMALL_PE=0xAF;
    const unsigned char SMALL_ER=0xE0;
    const unsigned char SMALL_ES=0xE1;
    const unsigned char SMALL_TE=0xE2;
    const unsigned char SMALL_U=0xE3;
    const unsigned char SMALL_FE=0xE4;
    const unsigned char SMALL_HE=0xE5;
    const unsigned char SMALL_CE=0xE6;
    const unsigned char SMALL_CHE=0xE7;
    const unsigned char SMALL_SHE=0xE8;
    const unsigned char SMALL_SCHE=0xE9;
    const unsigned char SMALL_HARDSIGN=0xEA;
    const unsigned char SMALL_YY=0xEB;
    const unsigned char SMALL_SOFTSIGN=0xEC;
    const unsigned char SMALL_E=0xED;
    const unsigned char SMALL_YU=0xEE;
    const unsigned char SMALL_YA=0xEF;

    int strcmp_cp866( const  char* str1, int len1, const  char* str2, int len2) ;
}

char* convert_str_cp1251_to_cp866(char* str866,const char* str1251, int len) ;
char* convert_str_cp866_to_cp1251(char* str1251,const char* str866, int len) ;
void hexing(const char* str) ;
extern unsigned char number_codes[10] ; 

#endif	/* RUSSIAN_CHARS_HPP */

