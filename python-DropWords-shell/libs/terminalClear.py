# -*- coding: UTF-8 -*-
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

import os



def terminalClear(debug_info: bool=True) -> bool:
    """
    Description:
        Terminal 清屏
    Returns:
        True:
            清屏成功
        False:
            操作系统不兼容此命令
    """

    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')
    else:
        if debug_info:
            print("该系统不兼容清屏命令!")
        return False
    return True
