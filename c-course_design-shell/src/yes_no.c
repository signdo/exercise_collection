#include <stdio.h>
#include <ctype.h>
#include <stdbool.h>

extern void get_str(unsigned int len, char str[len], char * info);





bool yes_no(char * info, bool reverse) {
    /* 
     * 询问用户是否同意
     */

    char str[2];

    while(true) {
        printf("%s", info);

        if(reverse) {
            get_str(2, str, " [N/y]: ");
            if(str[0] == '\0' || tolower(str[0]) == 'n') {
                return false;
            } else if(tolower(str[0]) == 'y') {
                return true;
            }
        } else {
            get_str(2, str, " [Y/n]: ");
            if(str[0] == '\0' || tolower(str[0]) == 'y') {
                return true;
            } else if(tolower(str[0]) == 'n') {
                return false;
            }
        }
    }
}