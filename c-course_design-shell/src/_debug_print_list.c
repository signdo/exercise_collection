#include <stdio.h>
#include <stdbool.h>

#include "../inc/item.h"

extern void print_item(Item * item);




bool _debug_print_list(List list) {
    /* 
     * 调试: 输出所有条目
     */
    
    if(!list) {
        printf("无记录!\n");
        return false;
    }

    Item * current = list;
    int count = 0;

    while(current != NULL) {
        print_item(current);
        count ++;
        current = current->next;
    }

    printf("\n显示完成, 共 %d 条记录!\n", count);
    return true;
}