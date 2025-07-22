/* 
 * 链表存储采购信息
 * 此头文件用于定义采购信息单向链表
 */

#ifndef _ITEM_H_
    #define _ITEM_H_

    #define ID_LEN      11      // 采购编号长度
    #define PART_LEN    50      // 零部件名称长度
    #define BUYER_LEN   50      // 采购员名称长度
    #define DEPART_LEN  50      // 部门名称长度

    typedef struct item {
        char id[ID_LEN];                // 采购编号
        char part[PART_LEN];            // 零部件名称
        int date[3];                    // 采购日期
        char buyer[BUYER_LEN];          // 采购员
        int count;                      // 采购数量
        float price;                    // 采购单价
        char department[DEPART_LEN];    // 供货单位

        struct item * next;
    } Item;

    typedef Item * List;

#endif
