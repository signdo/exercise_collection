#include "../include/menu.h"
#include "../include/tools.h"
#include "../include/main.h"

struct DB records[RECORD_NUM] = {
    {1, "ZhangSan", 'm', 30, "010-56253825", "zhang@abc.com"}
};
int currentRecordNum = 1;

int main(int argc, char * argv[]) {
    while(1) {
        switch(mainMenu()) {
            case 1:
                add();
                break;
            case 2:
                config();
                break;
            case 3:
                del();
                break;
            case 4:
                list();
                break;
            case 5:
                quit();
                break;
        }
    }
    return 0;
}

