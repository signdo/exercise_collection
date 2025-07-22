# -*- coding: UTF-8 -*-
"""
Description:
    在操作系统中处理目录的工具
Functions:
    isDirs:
        判断传入的参数是否为目录名
    mkDirs:
        根据形参创建单层或多层级目录
    getPathList:
        获取参数目录下的所有路径列表
    getFilesPathList:
        获取参数目录下的所有文件路径列表
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

import os




def isDirs(dirs: str, debug_info: bool=True) -> bool:
    """
    Description:
        判断传入的参数是否为目录名
    Args:
        dirs:
            目录名必须以 '/' 结尾
        debug_info:
            是否打印调试信息
            默认打印
    Returns:
        True:
            是可用目录
        False:
            不是目录或目录不存在
    """

    if not dirs.endswith('/'):
        if debug_info:
            print(f"目录 '{dirs}' 应当以 '/' 结尾!")
        return False

    if not os.path.isdir(dirs):
        if debug_info:
            print(f"'{dirs}' 不是目录或该目录不存在!")
        return False

    return True




def mkDirs(dirs: str, debug_info: bool=True) -> bool:
    """
    Description:
        根据形参创建单层或多层级目录
    Args:
        dirs:
            单层或多层目录名
        debug_info:
            是否打印调试信息
            默认打印
    Returns:
        True:
            目录创建成功或已存在
        False:
            目录创建失败
    """

    if not dirs.endswith('/'):
        if debug_info:
            print(f"目录 '{dirs}' 应当以 '/' 结尾!")
        return False

    try:
        os.makedirs(dirs, exist_ok=True)
    except PermissionError:
        if debug_info:
            print(f"目录 '{dirs}' 无法访问, 请检查权限!")
        return False
    else:
        return True





def getPathList(dirs: str, debug_info: bool=True) -> list[str]:
    """
    Description:
        获取参数目录下的所有路径列表
    Args:
        dirs:
            目录名
        debug_info:
            是否打印调试信息
            默认打印
    Returns:
        None:
            路径列表为空或无法访问
        文件列表:
            路径列表获取成功
    """

    if not isDirs(dirs, debug_info=False):
        return None

    path_list = []

    try:
        for name in os.listdir(dirs):
            path_list.append(dirs + name)
    except PermissionError:
        if debug_info:
            print(f"目录 '{dirs}' 无法访问, 请检查权限!")
        return None
    else:
        return path_list
