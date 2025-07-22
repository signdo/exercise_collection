#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#include "../inc/item.h"

extern bool set_id(Item * item);
extern bool set_part(Item * item);
extern bool set_date(Item * item);
extern bool set_buyer(Item * item);
extern bool set_count(Item * item);
extern bool set_price(Item * item);
extern bool set_department(Item * item);

extern void get_str(unsigned int len, char str[len], char * info);
extern bool yes_no(char * info, bool reverse);
extern void print_item(Item * item);




bool print_list(List list, bool by_id) {
    /* 
     * 根据条件查询对应的记录并显示
     * 如果 by_id 值为 true, 显示根据编号查询的结果
     * 否则显示根据零部件名称查询的结果
     * 返回 true 表示需要继续查询, 否则表示终止查询
     */

    Item * current = list;

    if(by_id) {
        char id[ID_LEN];
        get_str(ID_LEN, id, "请输入要查询的编号 (直接回车以退出查询): ");

        if(id[0] == '\0') {
            return false;
        }
        while(current != NULL && strcmp(current->id, id) != 0) {
            current = current->next;
        }
        print_item(current);

    } else {
        char part[PART_LEN];
        get_str(PART_LEN, part, "请输入要查询的零件名称 (直接回车以退出查询): ");

        if(part[0] == '\0') {
            return false;
        }
        while(current != NULL) {
            if(strcmp(current->part, part) == 0) {
                print_item(current);
            }
            current = current->next;
        }
        printf("\n已全部显示!\n");
    }
    return true;
}




List new_item(List list) {
    /* 
     * 新建一个采购条目
     * 返回 NULL 表示新建失败
     * 返回 List 类型表示新建成功
     */

    Item * new = (Item *)malloc(sizeof(Item));
    Item * current = list;

    new->next = NULL;

    while(true) {
        if(!set_id(new)) {
            free(new);
            return list;
        }

        while(current != NULL && strcmp(list->id, new->id) != 0) {
            current = current->next;
        }
        // list->id == new->id
        if(current != NULL) {
            printf("编号已存在! 请重新输入!\n");
            current = list;
            continue;
        }
        break;
    }

    if(!set_part(new) || !set_date(new)) {
        free(new);
        return list;
    }

    if(!set_buyer(new) || !set_count(new)) {
        free(new);
        return list;
    }

    if(!set_price(new) || !set_department(new)) {
        free(new);
        return list;
    }

    if(list == NULL) {
        printf("条目创建成功!\n");
        return new;
    } else {
        current = list;
        while(current->next != NULL) {
            current = current->next;
        }
        current->next = new;
        printf("条目创建成功!\n");
        return list;
    }
}




List del_item(List list) {
    /* 
     * 根据采购编号删除条目
     */

    if(list == NULL) {
        printf("采购记录为空! 无法删除!\n");
        return list;
    }

    char id[ID_LEN];
    get_str(ID_LEN, id, "请输入需要删除的条目编号 (直接回车以返回): ");
    if(id[0] == '\0') {
        return list;
    }

    Item * current = list;
    Item * next = list->next;

    // 先判断头节点是否为要删除的节点
    if(!strcmp(current->id, id)) {
        print_item(current);

        if(yes_no("确定要删除吗?", true)) {
            list = next;
            free(current);
            printf("删除成功!\n");
        }
        return list;
    }

    // 再迭代判断其他节点
    while(next != NULL && strcmp(next->id, id)) {
        current = next;
        next = next->next;
    }

    // 情况(1) next == NULL
    if(!next) {
        printf("没有找到对应编号的条目, 删除失败!\n");
        return list;
    }

    // 情况(2) next->id == id
    print_item(next);
    if(yes_no("确定要删除吗?", true)) {
        current->next = next->next;
        free(next);
        printf("删除成功!\n");
    }
    return list;
}



bool config_item(List list) {
    /* 
     * 根据采购编号修改一条记录
     */

    char id[ID_LEN];
    get_str(ID_LEN, id, "请输入需要修改的条目编号 (直接回车以返回): ");
    if(id[0] == '\0') {
        return false;
    }

    Item * current = list;

    while(current != NULL && strcmp(current->id, id)) {
        current = current->next;
    }
    if(!current) {
        printf("没有找到对应编号的条目, 修改失败!\n");
        return false;
    }

    print_item(current);

    set_part(current);
    set_date(current);
    set_buyer(current);
    set_count(current);
    set_price(current);
    set_department(current);

    printf("修改完成!\n");
    return true;
}

