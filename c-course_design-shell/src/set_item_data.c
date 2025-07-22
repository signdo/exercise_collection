#include <stdio.h>
#include <string.h>
#include <stdbool.h>

#include "../inc/item.h"

extern void get_str(unsigned int len, char str[len], char * info);
extern bool yes_no(char * info, bool reverse);





bool set_id(Item * item) {
    /* 
     * 获取采购编号
     */

    char id[ID_LEN];

    get_str(ID_LEN, id, "请输入条目编号 (直接回车取消): ");
    if(id[0] == '\0') {
        return false;
    }

    printf("您输入的是: [ %s ] ", id);
    if(yes_no("确定吗?", false)) {
        strcpy(item->id, id);
        return true;
    } else {
        return false;
    }
}




bool set_part(Item * item) {
    /* 
     * 获取零配件的名称
     */

    char part[PART_LEN];

    get_str(PART_LEN, part, "请输入零配件名称 (直接回车取消): ");
    if(part[0] == '\0') {
        return false;
    }

    printf("您输入的是: [ %s ] ", part);
    if(yes_no("确定吗?", false)) {
        strcpy(item->part, part);
        return true;
    } else {
        return false;
    }
}




bool set_date(Item * item) {
    /* 
     * 获取采购日期
     * 格式: 年 月 日
     * 输入非数字符号取消
     */

    int date[3];

    while(true) {
        printf("请输入采购日期 (格式: 年 月 日, 输入非数字符号取消): ");
        int flag = scanf("%d %d %d", &date[0], &date[1], &date[2]);
        while(getchar() != '\n');

        if(!flag) {
            return false;
        }

        if(flag != 3) {
            printf("输入有误! 请重新输入!\n");
            continue;
        }

        if(date[0] < 1 || date[0] > 9999) {
            printf("年份格式有误! 请重新输入!\n");
            continue;
        }

        if(date[1] < 1 || date[1] > 12) {
            printf("月份格式有误! 请重新输入!\n");
            continue;
        }

        int day_in_month = 0;
        switch(date[1]) {
            case 4: case 6: case 9: case 11:
                day_in_month = 30;
                break;
            case 2:
                if((date[0] % 4 == 0 && date[0] % 100 != 0) || date[0] % 400 == 0) {
                    day_in_month = 29;
                } else {
                    day_in_month = 28;
                }
                break;
            default:
                day_in_month = 31;
        }

        if(date[2] < 1 || date[2] > day_in_month) {
            printf("日份输入有误! 请重新输入!\n");
            continue;
        } else {
            printf("您输入的是: [ %d 年 %d 月 %d 日 ] ", date[0], date[1], date[2]);
            if(yes_no("确定吗?", false)) {
                for(int i = 0; i < 3; i ++) {
                    item->date[i] = date[i];
                }
                return true;
            } else {
                return false;
            }
        }
    }
}



bool set_buyer(Item * item) {
    /* 
     * 获取采购员姓名
     */
    
    char buyer[BUYER_LEN];

    get_str(BUYER_LEN, buyer, "请输入采购员姓名 (直接回车取消): ");
    if(buyer[0] == '\0') {
        return false;
    }

    printf("您输入的是: [ %s ] ", buyer);
    if(yes_no("确定吗?", false)) {
        strcpy(item->buyer, buyer);
        return true;
    } else {
        return false;
    }
}




bool set_count(Item * item) {
    /* 
     * 获取采购数量
     */

    int count, flag;

    while(true) {
        printf("请输入采购数量 (输入非数字符号取消): ");
        flag = scanf("%d", &count);
        while(getchar() != '\n');

        if(count < 0) {
            printf("您输入的数值不合法, 请重新输入!\n");
            continue;
        }
        break;
    }

    if(flag) {
        printf("您输入的是: [ %d ] ", count);
        if(yes_no("确定吗?", false)) {
            item->count = count;
            return true;
        }
    }
    return false;
}




bool set_price(Item * item) {
    /* 
     * 获取采购单价
     */
    
    float price;
    int flag;

    while(true) {
        printf("请输入采购单价 (输入非数字符号取消): ");
        flag = scanf("%f", &price);
        while(getchar() != '\n');

        if(price < 0) {
            printf("您输入的数值不合法, 请重新输入!\n");
            continue;
        }
        break;
    }

    if(flag) {
        printf("您输入的是: [ %.2f ] ", price);
        if(yes_no("确定吗?", false)) {
            item->price = price;
            return true;
        }
    }
    return false;
}




bool set_department(Item * item) {
    /* 
     * 获取供货单位的名称
     */
    
    char department[DEPART_LEN];

    get_str(DEPART_LEN, department, "请输入供货单位的名称 (直接回车取消): ");
    if(department[0] == '\0') {
        return false;
    }

    printf("您输入的是: [ %s ] ", department);
    if(yes_no("确定吗?", false)) {
        strcpy(item->department, department);
        return true;
    } else {
        return false;
    }
}
