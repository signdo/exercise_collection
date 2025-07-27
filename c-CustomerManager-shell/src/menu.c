#include <stdio.h>
#include <stdlib.h>
#include "../include/main.h"
#include "../include/menu.h"
#include "../include/tools.h"

extern struct DB records[RECORD_NUM];
extern int currentRecordNum;

// 主菜单
int mainMenu(void) {
    system("clear");
    printf(
            "-------- 客户信息管理软件 --------\n\n"
            "           1. 添加客户\n"
            "           2. 修改客户\n"
            "           3. 删除客户\n"
            "           4. 客户列表\n"
            "           5. 退出程序\n\n"
            "请选择(1-5): "
          );
    return menuEnter();
}



// 1. 添加客户
void add(void) {
    system("clear");
    printf("-------- 添加客户 --------\n\n");
    if(currentRecordNum >= RECORD_NUM) {
        printf("数据库已满!\n");
        pause();
        return;
    }
    records[currentRecordNum].num = currentRecordNum + 1;

    printf("姓名: ");
    set20Char(records[currentRecordNum].name);

    printf("性别[male/female]: ");
    setSex(&(records[currentRecordNum].sex));

    printf("年龄: ");
    setAge(&(records[currentRecordNum].age));

    printf("电话: ");
    set20Char(records[currentRecordNum].phone);

    printf("邮箱: ");
    set20Char(records[currentRecordNum].email);

    currentRecordNum ++;
    pause();
}



// 2. 修改客户
void config(void) {
    int code = 0;

    system("clear");
    printf("-------- 修改客户 --------\n\n");
    printf("请选择待修改客户的编号[-1退出]: ");
    while(!scanf("%d", &code) || code > currentRecordNum) {
        printf("输入错误, 请重新输入: ");
        cleanChar();
    }
    cleanChar();
    if(code < 1) return;

    code --;    // 设置同下标值
    if(!records[code].num) {
        printf("该客户信息已被删除! \n");
        pause();
        return;
    }
    printf("姓名(%s): ", records[code].name);
    set20Char(records[code].name);

    if(records[code].sex == 'm')
        printf("性别(%s)[male/female]: ", "男");
    else
        printf("性别(%s)[male/female]: ", "女");
    setSex(&(records[code].sex));

    printf("年龄(%d): ", records[code].age);
    setAge(&(records[code].age));

    printf("电话(%s): ", records[code].phone);
    set20Char(records[code].phone);

    printf("邮箱(%s): ", records[code].email);
    set20Char(records[code].email);

    pause();
}



// 3. 删除客户
void del(void) {
    int code = 0;

    system("clear");
    printf("-------- 删除客户 --------\n\n");
    printf("请选择待删除客户编号[-1退出]: ");
    while(!scanf("%d", &code) || code > currentRecordNum) {
        printf("输入错误, 请重新输入: ");
        cleanChar();
    }
    cleanChar();
    if(code < 1) return;
    code --;    // 设置同下标值

    if(!records[code].num) {
        printf("该客户信息已被删除! \n");
        pause();
        return;
    }
    printf("确定删除?[y/N]: ");
    if(getchar() == 'y') {
        records[code].num = 0;
        printf("删除成功!\n");
    }
    cleanChar();
    pause();
}



// 4. 客户列表
void list(void) {
    system("clear");
    printf("-------- 客户列表 --------\n\n");
    printf("编号     姓名       性别    年龄     电话            邮箱\n");
    for(int i = 0; i < currentRecordNum; i ++) {
        if(!records[i].num) {
            printf("%-8d 该客户信息已被删除!\n", i + 1);
            continue;
        }
        printf("%-8d ", records[i].num);
        printf("%-10s ", records[i].name);
        if(records[i].sex == 'm')
            printf("%-8s ", "男");
        else
            printf("%-8s ", "女");
        printf("%-8d ", records[i].age);
        printf("%-15s ", records[i].phone);
        printf("%s\n", records[i].email);
    }
    putchar('\n');
    pause();
}

