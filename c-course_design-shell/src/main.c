#include <stdio.h>
#include <stdbool.h>
#include <string.h>

#include "../inc/item.h"

extern int menu(bool debug);
extern bool clean(void);
extern void to_continue(void);
extern bool yes_no(char * info, bool reverse);

extern List new_item(List list);
extern bool print_list(List list, bool by_id);
extern bool config_item(List list);
extern List del_item(List list);

extern bool _debug_print_list(List list);





int main(int argc, char * argv[]) {
    /* 
     * 汽车零部件采购管理程序
     * 
     * Author: signdo
     * ID: https://github.com/signdo
     * Class: https://github.com/signdo
     * LICENSE: 仅供课程设计使用
     * 
     */

    // 创建采购信息链表头指针
    List list = NULL;

    // 根据程序启动时传入的参数决定是否启用调试模式
    bool debug = false;
    for(int i = 1; i < argc; i ++) {
        if(!strcmp(argv[i], "--debug-mode")) {
            debug = true;
            break;
        } else if(!strcmp(argv[i], "--help")) {
            printf("使用方法: %s [选项] ...\n", argv[0]);
            printf("选项:\n");

            printf(" --debug-mode\n\t\t启用调试模式。\n\t\t"
                "这将在程序主菜单中显示一个输出所有条目的选项。\n");
            printf(" --help\n\t\t打印这个程序的帮助信息。\n\n");

            printf("Author: signdo\nID: 202062528\n");
            printf("Class: https://github.com/signdo\n\n");
            return 0;
        } else {
            printf("%s: 未知参数!\n使用 '--help' 显示相关用法!\n", argv[i]);
            return 1;
        }
    }

    while(true) {
        clean();

        switch(menu(debug)) {
            case 1: // 添加一条采购记录
                clean();
                list = new_item(list);
                to_continue();
                break;

            case 2: // 根据编号显示记录
                clean();
                while(print_list(list, true));
                to_continue();
                break;

            case 3: // 根据零部件名称显示记录
                clean();
                while(print_list(list, false));
                to_continue();
                break;

            case 4: // 根据编号修改记录
                clean();
                config_item(list);
                to_continue();
                break;

            case 5: // 根据编号删除记录
                clean();
                list = del_item(list);
                to_continue();
                break;

            case 6: // 退出
                if(yes_no("确定要退出吗?", true)) {
                    return 0;
                }
                break;

            case 7: // 调试: 输出所有条目
                clean();
                _debug_print_list(list);
                to_continue();
                break;
        }
    }
    return 0;
}
