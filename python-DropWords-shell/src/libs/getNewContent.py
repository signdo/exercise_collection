# -*- coding: UTF-8 -*-
"""
Description:
    获取新的内容
    主要包括单词和单词释义
Functions:
    getNewWord:
        从键盘获取新单词并多次比较输入
        键入 'f' 以完成录入
    getNewExplain:
        从键盘获取新单词释义并询问结果是否正确
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
from libs.getScan import yesORno




def getNewWord(repeat: int=2, len_min_limit: int=2) -> str:
    """
    Description:
        从键盘获取新单词并多次比较输入
        键入 'c' 以取消录入
    Args:
        repeat:
            确认输入重复次数
            默认确认输入 2 次
        len_min_limit:
            限定单词的最小长度
            默认不得少于 2 字符
    Returns:
        新单词:
            输入并确认过的单词
        None:
            完成录入
    """

    loop = repeat
    get_word , get_again = '', ''

    while True:
        if loop == repeat:
            get_word = getInput("\n录入新单词, 键入 'c' 以取消: ")
            if get_word == 'c':
                return None
            elif len(get_word) < len_min_limit:
                print(f"词汇不得少于 {len_min_limit} 个字符!")
                continue

        elif loop >= 0:
            get_again = getInput(f"{get_word}    [{loop + 1}] > ")
            if get_again != get_word:
                print(f"当前输入 '{get_again}' 与内容不匹配, 请重新输入!")
                loop = repeat
                continue

        else:
            return get_word

        loop -= 1





def getNewExplain(word: str, len_min_limit: int=2) -> str:
    """
    Description:
        从键盘获取新单词释义并询问结果是否正确
    Args:
        word:
            需要解释的单词
        len_min_limit:
            限定释义的最小长度
            默认不得少于 2 字符
    Returns:
        新释义:
            输入并确认过的单词释义
    """

    while True:
        get_explain = getInput(f"\n请键入单词 '{word}' 的释义: ")

        if len(get_explain) < len_min_limit:
            print(f"释义至少需要 {len_min_limit} 个字符! ")
            continue
        
        if yesORno(f"{get_explain}  "):
            return get_explain
