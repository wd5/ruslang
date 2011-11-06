
#include <stdlib.h>

static long debug_interrupt_counter=0;
const long exit_treshold=40 ;
void debug_break()
{
    if(exit_treshold >0 && ++debug_interrupt_counter>=exit_treshold) exit(0) ;
}