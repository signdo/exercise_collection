# -*- coding: UTF-8 -*-
"""
Description:
    生成新的单词字典文件, 以及显示单词字典内容
Functions:
    mkWordsDict:
        生成新的单词字典文件
        先录入词汇再录入释义
    showWordsDict:
        按行格式化显示单词字典内容
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

from src.libs.getNewContent import getNewWord
from src.libs.getNewContent import getNewExplain




def mkWordsDict() -> dict:
    """
    Description:
        生成新的单词字典文件
        先录入词汇再录入释义
    Returns:
        单词字典:
            返回一个非空字典
        空字典:
            未录入任何内容
    """

    words_dict = {}

    num = 0
    while True:
        new_word = getNewWord()

        if not new_word:
            break
        else:
            num += 1
            words_dict[str(num)] = {new_word: ''}

    for entry in words_dict.values():
        for word in entry.keys():
            entry[word] = getNewExplain(word)

    return words_dict





def showWordsDict(words_dict: dict, debug_info: bool=True) -> None:
    """
    Description:
        按行格式化显示单词字典内容
    Args:
        words_dict:
            单词字典
        debug_info:
            是否打印调试信息
            默认打印
    """

    if not words_dict:
        if debug_info:
            print("单词字典内容为空!")
        return None

    for num, entry in words_dict.items():
        for word, explain in entry.items():
            print("[{}]\t{:<18} |    {}".format(num, word, explain))

    return None
