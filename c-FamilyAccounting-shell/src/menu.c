#include <stdio.h>
#include <stdlib.h>
#include "../include/menu.h"
#include "../include/tools.h"

extern int currentRecordNum;
extern struct DB record[RECORD_NUM];

/**
 * 实现主菜单选择
 * 
 * @return int 菜单选择结果
 */
int mainMenu(void) {
    system("clear");
    printf(
        "-------- 家庭收支记账软件 --------\n\n"
        "\t 1. 收支明细\n"
        "\t 2. 登记收入\n"
        "\t 3. 登记支出\n"
        "\t 4. 退出程序\n\n"
        "请选择(1-4): "
    );
    return menuEnter();
}



/**
 * 实现收支明细显示
 */
void detail(void) {
    system("clear");
    printf("-------- 收支明细 --------\n\n");
    printf("序号\t收支\t收支金额\t账户金额\t说明\n");
    
    for(int i = 0; i < currentRecordNum; i ++) {
        printf(
            "%-7d %-9s %-15.2lf %-15.2lf %s\n",
            record[i].num,
            record[i].io,
            record[i].ioMony,
            record[i].countMony,
            record[i].explain
        );
    }
    printf("\nPress Enter to continue...");
    cleanChar();
}



/**
 * 实现登记收入
 */
void income(void) {
    system("clear");
    printf("-------- 登记收入 --------\n\n");
    if(currentRecordNum >= RECORD_NUM) {
        printf("数据库已满!\n");
        printf("Press Enter to continue...");
        cleanChar();
        return;
    }

    printf("本次收入金额: ");
    while(scanf("%10lf", &(record[currentRecordNum].ioMony)) != 1) {
        printf("输入错误, 请重新输入: ");
        cleanChar();
    }
    cleanChar();

    printf("本次收入说明: ");
    scanf("%99s", record[currentRecordNum].explain);
    cleanChar();

    record[currentRecordNum].num = currentRecordNum + 1;
    record[currentRecordNum].io = "收入";
    record[currentRecordNum].countMony = record[currentRecordNum].ioMony + record[currentRecordNum - 1].countMony;
    currentRecordNum ++;

    printf("\nPress Enter to continue...");
    cleanChar();
}



/**
 * 实现登记支出
 */
void outcome(void) {
    system("clear");
    printf("-------- 登记支出 --------\n\n");

    printf("本次支出金额: ");
    while(scanf("%10lf", &(record[currentRecordNum].ioMony)) != 1) {
        printf("输入错误, 请重新输入: ");
        cleanChar();
    }
    cleanChar();

    printf("本次支出说明: ");
    scanf("%99s", record[currentRecordNum].explain);
    cleanChar();

    record[currentRecordNum].num = currentRecordNum + 1;
    record[currentRecordNum].io = "支出";
    record[currentRecordNum].countMony = - record[currentRecordNum].ioMony + record[currentRecordNum - 1].countMony;
    currentRecordNum ++;

    printf("\nPress Enter to continue...");
    cleanChar();
}

