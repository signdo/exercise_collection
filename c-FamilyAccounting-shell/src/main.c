#include "../include/menu.h"
#include "../include/tools.h"

// 数据库对象
struct DB record[RECORD_NUM] = {
    {1, "收入", 10000, 10000, "启动资金"}
};
// 当前记录条数
int currentRecordNum = 1;

int main(int argc, char * argv[]) {
    while(1) {
        switch(mainMenu()) {
            case 1:
                detail();
                break;
            case 2:
                income();
                break;
            case 3:
                outcome();
                break;
            case 4:
                quit();
                break;
        }
    }
    return 0;
}

