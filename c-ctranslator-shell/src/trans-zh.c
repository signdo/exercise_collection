#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define HEADSTR "trans zh:en "
#define ENDSTR  " | more"

/*
 * Cycle translation from Chinese to English.
 * You must have installed translate-shell.
 */
int main(void) {
    char input[512];

    system("clear");
    printf(
        "欢迎使用循环翻译.\n"
        "程序会将中文翻译成英文.\n"
        "请避免输入过多字符!\n"
        "使用[Ctrl-c]或[Ctrl-d]退出.\n\n"
        "请输入一个短语: "
    );
    while(scanf("%500s", input) != EOF) {
        char string[526] = HEADSTR;

        system("clear");
        while(getchar() != '\n')
            continue;

        strcat(string, input);
        strcat(string, ENDSTR);
        system(string);
        printf("请输入一个短语: ");
    }
    putchar('\n');
    return 0;
}

