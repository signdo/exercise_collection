#include <stdio.h>
#include <stdbool.h>

extern void get_str(unsigned int len, char str[len], char * info);



int menu(bool debug) {
    /* 
     * 用户主菜单
     * 若 debug 为 true 则提供显示所有条目的选项
     * 返回选项
     */

    char select[2];
    int options = 6;

    printf("##   汽车零部件采购管理程序   ##\n\n");

    printf("1.\t添加一条采购记录\n");
    printf("2.\t根据编号显示记录\n");
    printf("3.\t根据零部件名称显示记录\n");
    printf("4.\t根据编号修改记录\n");
    printf("5.\t根据编号删除记录\n");
    printf("6.\t退出软件\n");

    if(debug) {
        printf("\n7.\t调试: 显示所有记录\n");
        options = 7;
    }

    while(true) {
        get_str(2, select, "\n请输入选项代号: ");

        if(select[0] == '\0') {
            continue;
        } else if(select[0] < '1' || select[0] > ('0' + options)) {
            printf("输入不合法, 请重新输入!\n");
            continue;
        }
        return select[0] - '0';
    }
}