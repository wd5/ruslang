/* 
 * File:   main.cpp
 * Author: Victor
 *
 * Created on February 19, 2012, 2:57 AM
 */

#include <cstdlib>
#include "rlist.hpp"

using namespace std;

/*
 * 
 */
int main(int argc, char** argv)
{
    rList Words;
    
    int *intA = new int ;
    *intA=10 ;
    
    int *intB = new int ;
    *intB=20 ;
    
    Words.add(intA,1) ;
    Words.add(intB,2) ;
    
    
    Words.empty() ;
    return 0;
}

