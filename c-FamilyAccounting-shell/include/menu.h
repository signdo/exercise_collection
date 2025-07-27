/**
 * menu.c 的头文件
 */

int mainMenu(void);
void income(void);
void outcome(void);
void detail(void);

// 记录上限
#define RECORD_NUM 3

// 数据库
struct DB {
    int num;                // 记录序号
    char * io;              // 收入/支出
    double ioMony;          // 收支费用
    double countMony;       // 账户余额
    char explain[100];         // 收支说明
};


