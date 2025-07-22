#include <stdio.h>

#include "../inc/item.h"




void print_item(Item * item) {
    /* 
     * 显示一条采购记录的详细信息
     */

    if(!item) {
        printf("无记录!\n");
        return;
    }

    putchar('\n');
    printf("采购编号\t|  %s\n", item->id);
    printf("----------------+------------------\n");
    printf("零件名称\t|  %s\n", item->part);
    printf("采购日期\t|  %d 年 %d 月 %d 日\n", item->date[0], item->date[1], item->date[2]);
    printf("采购员  \t|  %s\n", item->buyer);
    printf("采购数量\t|  %d\n", item->count);
    printf("采购单价\t|  %.2f\n", item->price);
    printf("供货单位\t|  %s\n", item->department);
    putchar('\n');
}