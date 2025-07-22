# -*- coding: UTF-8 -*-
"""
Description:
    获取输入和判断操作
Functions:
    getInput:
        从键盘获取字符串并处理异常
    yesORno:
        判断是否同意 [Y/n] 或 [N/y]
        回车默认为大写字母的选择
"""

"""
            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
                    Version 2, December 2004

 Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>

 Everyone is permitted to copy and distribute verbatim or modified
 copies of this license document, and changing it is allowed as long
 as the name is changed.

            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

  0. You just DO WHAT THE FUCK YOU WANT TO.
"""




def getInput(print_info: str, debug_info: bool=True) -> str:
    """
    Description:
        从键盘获取字符串并处理异常
    Args:
        print_info:
            提示用户输入的信息
        debug_info:
            是否打印调试信息
            默认打印
    Returns:
        字符串或空字符串
    """

    try:
        scan = input(print_info)
    except KeyboardInterrupt:
        if debug_info:
            print("\n程序中止!\n")
        exit()
    except EOFError:
        if debug_info:
            print("\n程序中止!\n")
        exit()
    else:
        return scan




def yesORno(print_info: str, reverse: bool=False) -> bool:
    """
    Description:
        判断是否同意 [Y/n] 或 [N/y]
        回车默认为大写字母的选择
    Args:
        print_info:
            提示用户输入的信息
        reverse:
            反转默认的选择
            默认回车为 True
    Returns:
        True:
            同意
        False:
            拒绝
    """

    while True:
        if reverse:
            if not (select := getInput(print_info + " [N/y]: ")):
                return False
        else:
            if not (select := getInput(print_info + " [Y/n]: ")):
                return True

        if select.lower() == 'y':
            return True
        elif select.lower() == 'n':
            return False
