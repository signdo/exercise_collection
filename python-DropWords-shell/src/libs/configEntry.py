# -*- coding: UTF-8 -*-
"""
Description:
    修改单词字典的词条, 包括增加, 删除, 插入, 替换
Functions:
    replaceEntry:
        替换单词字典中的单个词条
    appendEntry:
        在单词字典末尾附加单个词条
    insertEntry:
        在单词字典中插入单个词条
        插入位置之后的元素将向后移动
    delEntry:
        在单词字典中删除单个词条
        删除位置之后的元素将向前移动
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

from libs.getScan import getInput
from src.libs.getNewContent import getNewWord
from src.libs.getNewContent import getNewExplain




def replaceEntry(words_dict: dict, index: str, debug_info: bool=True) -> bool:
    """
    Description:
        替换单词字典中的单个词条
    Args:
        word_dict:
            单词字典
        index:
            单词字典索引
            索引为字符串类型
        debug_info:
            是否打印调试信息
            默认打印
    Returns:
        True:
            修改成功
        False:
            取消修改或索引不存在
    """

    if not words_dict.get(index):
        if debug_info:
            print("此索引不存在!")
        return False

    for word, explain in words_dict[index].items():
        print(f"\n单词:\t{word}\n释义:\t{explain}")

    if not (new_word := getNewWord()):
        if debug_info:
            print("未能替换新词条至字典")
        return False
    else:
        words_dict[index] = {new_word: getNewExplain(new_word)}
        return True




def appendEntry(words_dict: dict, debug_info: bool=True) -> bool:
    """
    Description:
        在单词字典末尾附加单个词条
    Args:
        word_dict:
            单词字典
        debug_info:
            是否打印调试信息
            默认打印
    Returns:
        True:
            附加成功
        False:
            取消附加
    """

    if not (new_word := getNewWord()):
        if debug_info:
            print("未能附加新词条至字典")
        return False
    else:
        index = str(len(words_dict) + 1)
        words_dict[index] = {new_word: getNewExplain(new_word)}
        return True




def insertEntry(words_dict: dict, index: str, debug_info: bool=True) -> bool:
    """
    Description:
        在单词字典中插入单个词条
        插入位置之后的元素将向后移动
    Args:
        word_dict:
            单词字典
        index:
            单词插入的索引
            索引为字符串类型
        debug_info:
            是否打印调试信息
            默认打印
    Returns:
        True:
            插入成功
        False:
            取消插入或索引错误
    """

    if not words_dict.get(index):
        if debug_info:
            print("此索引不存在!")
        return False

    if not (new_word := getNewWord()):
        if debug_info:
            print("未能插入新词条至字典")
        return False

    new_explain = getNewExplain(new_word)

    for i in range(len(words_dict), int(index) - 1, -1):
        words_dict[str(i + 1)] = words_dict[str(i)]

    words_dict[index] = {new_word: new_explain}
    return True




def delEntry(words_dict: dict, index: str, debug_info: bool=True) -> bool:
    """
    Description:
        在单词字典中删除单个词条
        删除位置之后的元素将向前移动
    Args:
        word_dict:
            单词字典
        index:
            要删除的单词的索引
            索引为字符串类型
        debug_info:
            是否打印调试信息
            默认打印
    Returns:
        True:
            删除成功
        False:
            索引错误
    """

    if not words_dict.get(index):
        if debug_info:
            print("此索引不存在!")
        return False

    for i in range(int(index), len(words_dict)):
        words_dict[str(i)] = words_dict[str(i + 1)]
    
    del words_dict[str(len(words_dict))]
    return True
