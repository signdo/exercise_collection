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

from libs.getScan import getInput
from libs.getScan import yesORno




def mkJSONFilePath(dirs: str, default: bool=True) -> str:
    """
    Description:
        默认按用户输入的文件编号返回特定 JSON 文件路径
        或者按用户输入的文件名返回文件路径
    Args:
        dirs:
            目录名
        default:
            默认使用特定文件名命名文件
            WordsList [文件编号].json
            自定义文件名中不能包含以下字符之一
            < > / \ | : * ?
    Returns:
        字符串:
            JSON 文件路径名
    """

    def haveIllegalChar(string: str) -> str:
        for char in ['<', '>', '/', '\\', '|', ':', '*', '?']:
            if char in string:
                return char
        return None

    while True:
        if default:
            gets = getInput("输入 JSON 文件名编号: ")

            if not gets:
                continue
            if not gets.isdigit():
                print("编号只能包含数字!")
                continue
            if len(gets) > 20:
                print("编号过长!")
                continue

            path = dirs + "WordsDict[" + gets + "].json"

        else:
            gets = getInput("输入文件名: ")

            if not gets:
                continue
            if len(gets) > 20:
                print("文件名过长!")
                continue

            if char := haveIllegalChar(gets):
                print(f"文件名不能含有 {char} 符号!")
                continue

            path = dirs + gets + ".json"

        if yesORno(f"文件将被命名为 '{path}' 确认?"):
            return path
