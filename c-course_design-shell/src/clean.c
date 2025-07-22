#include <stdlib.h>
#include <string.h>
#include <sys/utsname.h>
#include <stdbool.h>




bool clean(void) {
    /* 
     * 清屏
     */

    struct utsname unameData;
    uname(&unameData);

    if(!strcmp(unameData.sysname, "Linux")) {
        system("clear");
        return true;
    } else if(!strcmp(unameData.sysname, "Windows")) {
        system("cls");
        return true;
    } else if(!strcmp(unameData.sysname, "MacOS")) {
        system("clear");
        return true;
    }
    return false;
}