#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "../include/tools.h"

int menuEnter(void) {
    int code = 0;
    while((code = getchar()) < '1' || code > '5') {
        printf("输入有误, 请重新输入: ");
        cleanChar();
    }
    cleanChar();
    return code - '0';
}



void cleanChar() {
    while(getchar() != '\n')
        continue;
}



void pause(void) {
    printf("Press Enter to continue...");
    cleanChar();
}



void quit(void) {
    char ch = 0;
    printf("确定退出?[Y/n]: ");
    if((ch = getchar()) == 'y' || ch == 'Y' || ch == '\n')
        exit(EXIT_SUCCESS);
    cleanChar();
}


// 获取19个字符到字符数组, 最后一个字符为'\0'
void set20Char(char arr[]) {
    scanf("%19s", arr);
    cleanChar();
}



void setSex(char * sex) {
    char ch = 0;
    while((ch = getchar()) != '\n') {
        if(ch == 'f' || ch == 'F') {
            cleanChar();
            *sex = 'f';
            return;
        } else if(ch == 'm' || ch == 'M') {
            cleanChar();
            *sex = 'm';
            return;
        } else if(ch == '\n')
            return;
        printf("输入错误, 请重新输入[male/female]: ");
        cleanChar();
    }
}


void setAge(int * age) {
    char input[20];
    int flag = 1;
    while(flag) {
        scanf("%19s", input);
        if(input[0] != '\n') {
            if(input[0] > '9' || input[0] < '1') {
                printf("输入错误, 请重新输入: ");
                continue;
            }
            *age = atoi(input);
        }
        flag = 0;
        cleanChar();
    }
}

