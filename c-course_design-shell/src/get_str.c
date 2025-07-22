#include <stdio.h>




void get_str(unsigned int len, char str[len], char * info) {
    /* 
     * 输出提示信息
     * 从键盘获取字符串, 保存在传入的数组中
     * 清空多余缓存输入
     * 
     * 注意! 传入的数组长度应当不小于 2
     * 当直接回车时, 字符串的首元素为 '\0'
     */

    printf("%s", info);

    if(len == 1) {
        str[0] = '\0';
        while(getchar() != '\n');
    }else {
        char achar;
        int i = 0;

        while(i < len - 1) {
            if((achar = getchar()) == '\n') {
                break;
            }
            str[i] = achar;
            i ++;
        }
        str[i] = '\0';
        
        if(achar != '\n') {
            while(getchar() != '\n');
        }
    }
}