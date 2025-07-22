# -*- coding: UTF-8 -*-
"""
Description:
    读写 JSON 文件
Functions:
    saveDict:
        将传入的字典对象保存到文件
        如果文件不存在则创建文件
    loadDict:
        加载 JSON 文件中的字典
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
import json

from libs.JSONFileTools import isJSONFile




def saveDict(path: str, dictionary: dict, debug_info: bool=True) -> bool:
    """
    Description:
        将传入的字典对象保存到文件
        如果文件不存在则创建文件
    Args:
        path:
            文件路径名
        dictionary:
            字典对象
        debug_info:
            是否打印调试信息
            默认打印
    Returns:
        True:
            文件写入成功
        False:
            文件写入失败
    """

    if not isJSONFile(path):
        return False

    try:
        with open(path, mode='w', encoding='utf-8') as json_file:
            json.dump(dictionary, json_file, indent=4)
    except PermissionError:
        if debug_info:
            print(f"路径 '{path}' 无法访问, 请检查权限!")
        return False
    else:
        return True





def loadDict(path: str, debug_info: bool=True) -> dict:
    """
    Description:
        加载 JSON 文件中的字典
    Args:
        path:
            JSON 文件路径名
        debug_info:
            是否打印调试信息
            默认打印
    Returns:
        字典:
            成功加载的字典
        None:
            读取文件内容失败或文件内容为空
    """

    if not isJSONFile(path):
        return None

    try:
        with open(path, mode='r', encoding='utf-8') as json_file:
            dictionary = json.load(json_file)
    except json.decoder.JSONDecodeError:
        if debug_info:
            print(f"文件 '{path}' 内容无法解析!")
        return None
    except PermissionError:
        if debug_info:
            print(f"路径 '{path}' 无法访问, 请检查权限!")
        return None
    else:
        return dictionary
