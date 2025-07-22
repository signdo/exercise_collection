# -*- coding: UTF-8 -*-
"""
Description:
    用户对单词字典修改函数
Functions:
    userReplaceEntry:
        用户替换单词字典中的单个词条
    userAddEntry:
        用户在单词字典中添加单个词条
    userDelEntry:
        用户在单词字典中删除单个词条
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

from libs.terminalClear import terminalClear
from src.libs.selectWordsDictFile import selectWordsDictFile
from libs.getScan import getInput
from libs.JSONFileIO import loadDict
from libs.JSONFileIO import saveDict
from src.libs.mkShowWordsDict import showWordsDict
from src.libs.configEntry import replaceEntry
from src.libs.configEntry import insertEntry
from src.libs.configEntry import appendEntry
from src.libs.configEntry import delEntry



def userReplaceEntry(config: dict) -> None:
    """
    Description:
        用户替换单词字典中的单个词条
    Args:
        config:
            用户配置
    """

    terminalClear()

    if not (path := selectWordsDictFile(config["UserData"])):
        getInput("[回车以继续]")
        return None

    if not (words_dict := loadDict(path)):
            print("字典为空, 无法修改!")
            getInput("[回车以继续]")
            return None

    showWordsDict(words_dict, debug_info=False)

    while (index := getInput("请键入索引, 键入 'c' 以取消: ")) != 'c':
        if replaceEntry(words_dict, index):
            if saveDict(path, words_dict):
                print("修改完成!")
            getInput("[回车以继续]")
            return None

    getInput("[回车以继续]")
    return None




def userAddEntry(config: dict, is_insert: bool) -> None:
    """
    Description:
        用户在单词字典中添加单个词条
    Args:
        config:
            用户配置
        is_insert:
            是否插入
    """

    terminalClear()

    if not (path := selectWordsDictFile(config["UserData"])):
        getInput("[回车以继续]")
        return None

    if not (words_dict := loadDict(path)):
            print("字典为空, 无法修改!")
            getInput("[回车以继续]")
            return None

    showWordsDict(words_dict, debug_info=False)

    while (index := getInput("请键入索引, 键入 'c' 以取消: ")) != 'c':
        if (insertEntry(words_dict, index) if is_insert else appendEntry(words_dict)):
            if saveDict(path, words_dict):
                print("修改完成!")
            getInput("[回车以继续]")
            return None

    getInput("[回车以继续]")
    return None



def userDelEntry(config: dict) -> None:
    """
    Description:
        用户在单词字典中删除单个词条
    Args:
        config:
            用户配置
    """

    terminalClear()

    if not (path := selectWordsDictFile(config["UserData"])):
        getInput("[回车以继续]")
        return None

    if not (words_dict := loadDict(path)):
            print("字典为空, 无法修改!")
            getInput("[回车以继续]")
            return None

    showWordsDict(words_dict, debug_info=False)

    while (index := getInput("请键入索引, 键入 'c' 以取消: ")) != 'c':
        if delEntry(words_dict, index):
            if saveDict(path, words_dict):
                print("修改完成!")
            getInput("[回车以继续]")
            return None

    getInput("[回车以继续]")
    return None
