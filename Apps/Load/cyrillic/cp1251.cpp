/* 
 * File:   cp1251.cpp
 * Author: Ustas
 * 
 * Created on : 2011-11-06
 * 
 * Environment:
 * Windows Vista ENG 64
 * g++ 4.3.4
 * NetBeans 7.0.1
 * CMD.EXE font "Lucida Console"
 * Internal Russian/Cyrillic CHARs are stored in Win CP1251 codepage.
 * 
 * Problem: internal strings (in 1251) are not correctly displayed in CMD window.
 * investigation showed that MBCS are correctly displayed. (single char for ANSI, and 2-bytes for Cyrr. ex: 0xD0B0 - Russian small A)
 * this function converts all Russian chars from CP1251 to Multi-Byte UTF-8 charset)
 * this is solely needed for printing to CMD.
 * 
 */


#include "cp1251.hpp"



void cp1251::init()
{
    mbutf8_code[0xC0]= 0x90D0 ; // CAPITAL_A_1251=0xC0;
    mbutf8_code[0xC1]= 0x91D0 ; // CAPITAL_BE_1251=0xC1;
    mbutf8_code[0xC2]= 0x92D0 ; // CAPITAL_WE_1251=0xC2;
    mbutf8_code[0xC3]= 0x93D0 ; // CAPITAL_GE_1251=0xC3;
    mbutf8_code[0xC4]= 0x94D0 ; // CAPITAL_DE_1251=0xC4;
    mbutf8_code[0xC5]= 0x95D0 ; // CAPITAL_YE_1251=0xC5;
    mbutf8_code[0xA8]= 0x81D0 ; // CAPITAL_YO_1251=0xA8; // ---------
    mbutf8_code[0xC6]= 0x96D0 ; // CAPITAL_ZHE_1251=0xC6;
    mbutf8_code[0xC7]= 0x97D0 ; // CAPITAL_ZE_1251=0xC7;
    mbutf8_code[0xC8]= 0x98D0 ; // CAPITAL_I_1251=0xC8;
    mbutf8_code[0xC9]= 0x99D0 ; // CAPITAL_J_1251=0xC9;
    mbutf8_code[0xCA]= 0x9AD0 ; // CAPITAL_KA_1251=0xCA;
    mbutf8_code[0xCB]= 0x9BD0 ; // CAPITAL_EL_1251=0xCB;
    mbutf8_code[0xCC]= 0x9CD0 ; // CAPITAL_EM_1251=0xCC;
    mbutf8_code[0xCD]= 0x9DD0 ; // CAPITAL_EN_1251=0xCD;
    mbutf8_code[0xCE]= 0x9ED0 ; // CAPITAL_O_1251=0xCE;
    mbutf8_code[0xCF]= 0x9FD0 ; // CAPITAL_PE_1251=0xCF;
    mbutf8_code[0xD0]= 0xA0D0 ; // CAPITAL_ER_1251=0xD0;
    mbutf8_code[0xD1]= 0xA1D0 ; // CAPITAL_ES_1251=0xD1;
    mbutf8_code[0xD2]= 0xA2D0 ; // CAPITAL_TE_1251=0xD2;
    mbutf8_code[0xD3]= 0xA3D0 ; // CAPITAL_U_1251=0xD3;
    mbutf8_code[0xD4]= 0xA4D0 ; // CAPITAL_FE_1251=0xD4;
    mbutf8_code[0xD5]= 0xA5D0 ; // CAPITAL_HE_1251=0xD5;
    mbutf8_code[0xD6]= 0xA6D0 ; // CAPITAL_CE_1251=0xD5;
    mbutf8_code[0xD7]= 0xA7D0 ; // CAPITAL_CHE_1251=0xD7;
    mbutf8_code[0xD8]= 0xA8D0 ; // CAPITAL_SHE_1251=0xD8;
    mbutf8_code[0xD9]= 0xA9D0 ; // CAPITAL_SCHE_1251=0xD9;
    mbutf8_code[0xDA]= 0xAAD0 ; // CAPITAL_HARDSIGN_1251=0xDA;
    mbutf8_code[0xDB]= 0xABD0 ; // CAPITAL_YY_1251=0xDB;
    mbutf8_code[0xDC]= 0xACD0 ; // CAPITAL_SOFTSIGN_1251=0xDC;
    mbutf8_code[0xDD]= 0xADD0 ; // CAPITAL_E_1251=0xDD;
    mbutf8_code[0xDE]= 0xAED0 ; // CAPITAL_YU_1251=0xDE;
    mbutf8_code[0xDF]= 0xAFD0 ; // CAPITAL_YA_1251=0xDF;


    mbutf8_code[0xE0]= 0xB0D0 ; // SMALL_A_1251=0xE0; 
    mbutf8_code[0xE1]= 0xB1D0 ; // SMALL_BE_1251=0xE1;
    mbutf8_code[0xE2]= 0xB2D0 ; // SMALL_WE_1251=0xE2;
    mbutf8_code[0xE3]= 0xB3D0 ; // SMALL_GE_1251=0xE3;
    mbutf8_code[0xE4]= 0xB4D0 ; // SMALL_DE_1251=0xE4;
    mbutf8_code[0xE5]= 0xB5D0 ; // SMALL_YE_1251=0xE5;
    mbutf8_code[0xB8]= 0x91D1 ; // SMALL_YO_1251=0xB8; // -----------
    mbutf8_code[0xE6]= 0xB6D0 ; // SMALL_ZHE_1251=0xE6;
    mbutf8_code[0xE7]= 0xB7D0 ; // SMALL_ZE_1251=0xE7;
    mbutf8_code[0xE8]= 0xB8D0 ; // SMALL_I_1251=0xE8;
    mbutf8_code[0xE9]= 0xB9D0 ; // SMALL_J_1251=0xE9;
    mbutf8_code[0xEA]= 0xBAD0 ; // SMALL_KA_1251=0xEA;
    mbutf8_code[0xEB]= 0xBBD0 ; // SMALL_EL_1251=0xEB;
    mbutf8_code[0xEC]= 0xBCD0 ; // SMALL_EM_1251=0xEC;
    mbutf8_code[0xED]= 0xBDD0 ; // SMALL_EN_1251=0xED;
    mbutf8_code[0xEE]= 0xBED0 ; // SMALL_O_1251=0xEE;
    mbutf8_code[0xEF]= 0xBFD0 ; // SMALL_PE_1251=0xEF;
    mbutf8_code[0xF0]= 0x80D1 ; // SMALL_ER_1251=0xF0;
    mbutf8_code[0xF1]= 0x81D1 ; // SMALL_ES_1251=0xF1;
    mbutf8_code[0xF2]= 0x82D1 ; // SMALL_TE_1251=0xF2;
    mbutf8_code[0xF3]= 0x83D1 ; // SMALL_U_1251=0xF3;
    mbutf8_code[0xF4]= 0x84D1 ; // SMALL_FE_1251=0xF4;
    mbutf8_code[0xF5]= 0x85D1 ; // SMALL_HE_1251=0xF5;
    mbutf8_code[0xF6]= 0x86D1 ; // SMALL_CE_1251=0xF6;
    mbutf8_code[0xF7]= 0x87D1 ; // SMALL_CHE_1251=0xF7;
    mbutf8_code[0xF8]= 0x88D1 ; // SMALL_SHE_1251=0xF8;
    mbutf8_code[0xF9]= 0x89D1 ; // SMALL_SCHE_1251=0xF9;
    mbutf8_code[0xFA]= 0x8AD1 ; // SMALL_HARDSIGN_1251=0xFA;
    mbutf8_code[0xFB]= 0x8BD1 ; // SMALL_YY_1251=0xFB;
    mbutf8_code[0xFC]= 0x8CD1 ; // SMALL_SOFTSIGN_1251=0xFC;
    mbutf8_code[0xFD]= 0x8DD1 ; // SMALL_E_1251=0xFD;
    mbutf8_code[0xFE]= 0x8ED1 ; // SMALL_YU_1251=0xFE;
    mbutf8_code[0xFF]= 0x8FD1 ; // SMALL_YA_1251=0xFF;
}

bool cp1251::is_ru(unsigned char ch)
{
    if((CAPITAL_A_1251 <= ch && ch <= SMALL_YA_1251) || ch==CAPITAL_YO_1251 || ch==SMALL_YO_1251 )
        return true ;
    else
        return false ;
}

char* cp1251::convert( const char* cp1251_in, int in_size, char* mbutf8_out, int out_size) 
{
    int mbutf8_out_i=0 ;
    for(int i=0;i<in_size;i++)
    {
        if(!cp1251::is_ru(cp1251_in[i]))
        {
            mbutf8_out[mbutf8_out_i]=cp1251_in[i] ;
            mbutf8_out_i++;
        }
        else
        {
            wchar_t mb_char = mbutf8_code[cp1251_in[i]] ;
            mbutf8_out[mbutf8_out_i]= *((char*) &mb_char) ;
            mbutf8_out_i++;
            mbutf8_out[mbutf8_out_i]= *(((char*) &mb_char)+1) ;
            mbutf8_out_i++;
        }
        if(mbutf8_out_i>=out_size-1)     
        {
            mbutf8_out[mbutf8_out_i] = NULL ;
            return mbutf8_out ; // no space in mbutf8 buffer
        }
    }
    mbutf8_out[mbutf8_out_i] = NULL ;
    return mbutf8_out ;
}