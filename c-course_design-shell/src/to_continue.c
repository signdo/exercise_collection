#include <stdio.h>



void to_continue(void) {
    /* 
     * 程序暂停
     */
    printf("[ 回车以继续 ]");
    while(getchar() != '\n');

    return;
}