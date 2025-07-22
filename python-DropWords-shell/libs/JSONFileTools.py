# -*- coding: UTF-8 -*-
"""
Description:
    在操作系统中处理 JSON 文件的工具
Functions:
    isJSONFile:
        判断传入的参数是否为 JSON 文件
    mkJSONFile:
        创建空白 JSON 文件
        如果文件存在默认创建失败
    delJSONFile:
        删除 JSON 文件
        此操作不可撤销!
    getJSONFilesPathList:
        获取目录下的所有 JSON 文件路径列表
        默认不打印内容
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
import pathlib

from libs.dirTools import mkDirs
from libs.dirTools import getPathList



def isJSONFile(path: str, debug_info: bool=True) -> bool:
    """
    Description:
        判断传入的参数是否为 JSON 文件
    Args:
        path:
            文件的路径名, 包括路径和文件名
            参数必须以 '.json' 结尾
        debug_info:
            是否打印调试信息
            默认打印
    Returns:
        True:
            文件存在且是 JSON 文件
        False:
            文件不存在或不是 JSON 文件
    """

    if not path.endswith('.json'):
        if debug_info:
            print(f"文件路径 '{path}' 应当以 '.json' 结尾!")
        return False

    if not os.path.isfile(path):
        if debug_info:
            print(f"文件路径 '{path}' 不是文件或文件不存在!")
        return False

    return True




def mkJSONFile(path: str, exist_ok: bool=False, debug_info: bool=True) -> bool:
    """
    Description:
        创建空白 JSON 文件
        如果文件存在默认创建失败
    Args:
        path:
            文件路径名
        exist_ok:
            是否允许已存在的文件作为创建的文件?
            默认不允许
        debug_info:
            是否打印调试信息
            默认打印
    Returns:
        False:
            文件创建失败或已存在
        True:
            文件创建成功
    """
    file_name = path.split('/')[-1]

    if not file_name.endswith('.json'):
        if debug_info:
            print(f"文件名 '{file_name}' 应当以 '.json' 结尾!")
        return False

    dirs = path.rstrip(file_name)

    if not dirs:
        dirs = './'
    if not mkDirs(dirs):
        return False

    try:
        pathlib.Path(path).touch(exist_ok=exist_ok)
    except FileExistsError:
        if debug_info:
            print(f"文件 '{path}' 已存在!")
        return False
    except PermissionError:
        if debug_info:
            print(f"路径 '{path}' 无法访问, 请检查权限!")
        return False
    else:
        return True




def delJSONFile(path: str, debug_info: bool=True) -> bool:
    """
    Description:
        删除 JSON 文件
        此操作不可撤销!
    Args:
        path:
            JSON 文件路径名
        debug_info:
            是否打印调试信息
            默认打印
    Returns:
        True:
            文件删除成功
        False:
            文件不存在或删除失败
    """

    if not isJSONFile(path, debug_info=False):
        return False

    try:
        os.unlink(path)
    except PermissionError:
        if debug_info:
            print(f"路径 '{path}' 无法访问, 请检查权限!")
        return False
    else:
        return True




def getJSONFilesPathList(dirs: str, printf: bool=False) -> list[str]:
    """
    Description:
        获取目录下的所有 JSON 文件路径列表
        默认不打印内容
    Args:
        dirs:
            目录名
        printf:
            格式化打印 JSON 文件路径列表
    Returns:
        None:
            JSON 文件路径列表为空
        文件列表:
            JSON 文件路径列表获取成功
    """

    if not (path_list := getPathList(dirs)):
        if printf:
            print(f"目录 '{dirs}' 中的内容为空!")
        return None

    if printf:
        print("编号\t文件路径名")

    json_list = []
    num = 1

    for path in path_list:
        if isJSONFile(path, debug_info=False):
            json_list.append(path)
            if printf:
                print(f"[{num}]\t{path}")
                num += 1

    return json_list
