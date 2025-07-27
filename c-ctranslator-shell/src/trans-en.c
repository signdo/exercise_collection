#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define HEADSTR "trans en:zh "
#define ENDSTR  " | more"

/*
 * Cycle translation from English to Chinese.
 * You must have installed translate-shell.
 */
int main(void) {
    char input[512];

    system("clear");
    printf(
        "Welcome to Circular Translator.\n"
        "The program will translate English to Chinese.\n"
        "Please avoid entering too many characters!\n"
        "Using [Ctrl-c] or [Ctrl-d] to quit.\n\n"
        "Please enter a word: "
    );
    while(scanf("%500s", input) != EOF) {
        char string[526] = HEADSTR;

        system("clear");
        while(getchar() != '\n')
            continue;

        strcat(string, input);
        strcat(string, ENDSTR);
        system(string);
        printf("Please enter a word: ");
    }
    putchar('\n');
    return 0;
}

