/* 
 * File:   cp1251.hpp
 * Author: Ustas
 *
 * Created on November 6, 2011, 1:01 PM
 */

#ifndef CP1251_HPP
#define	CP1251_HPP

#include <map>
#include "russian_chars.hpp"

class codepage1251      // CodePage cp1251 manipulator
{
public:
    codepage1251() {init();};
    char* convert( const  char* cp1251_in, int in_size,  char* mbutf8_out, int out_size) ; // maxlength = size of mbutf8 in bytes
    static bool is_ru(unsigned char ch) ;
    static bool is_space(unsigned char ch) ;
    static bool is_capital(unsigned char ch) ;
    static bool is_small(unsigned char ch) ;
    
    
private:
    void init() ;
    std::map<unsigned char, wchar_t> mbutf8_code;
        // std::map<wchar_t, unsigned char> cp1251_code; // reverse conversion; not implemented
};

#endif	/* CP1251_HPP */

