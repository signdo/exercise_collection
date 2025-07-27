#include <stdio.h>
#include <stdlib.h>
#include "../include/tools.h"

/**
 * 实现菜单选择结果输出
 * @return int 1到4
 */
int menuEnter(void) {
    int code = 0;
    
    // 输入错误判断
    while(!scanf("%1d", &code) || code < 1 || code > 4) {
        cleanChar();
        printf("输入有误, 请重新输入: ");
    }
    getchar();

    return code;
}



/**
 * 实现程序退出询问
 */
void quit(void) {
    printf("确定要退出程序吗? [Y/n]: ");
    char q = getchar();
    if((q == 'Y') || (q == 'y') || (q == '\n'))
        exit(EXIT_SUCCESS);
    cleanChar();
}


/**
 * 清除残余输入缓冲内容
 */
void cleanChar(void) {
    while(getchar() != '\n')
        continue;
}

