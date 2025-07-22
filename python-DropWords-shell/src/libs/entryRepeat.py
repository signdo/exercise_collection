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
from src.libs.getEntryList import getEntryList




def entryRepeat(words_dict: dict, repeat: int=3, random_entry: bool=False) -> None:
    """
    Description:
        不重复单词表抄写模式
        同时显示当前单词和释义
        默认每个单词按顺序出现, 抄写 3 遍
    Args:
        words_dict:
            单词字典
        repeat:
            单词重复次数. 默认每个单词重复 3 次
        random_mode:
            随机词条模式. 默认不随机
    """

    entry_list = getEntryList(words_dict, random_mode=random_entry)
    index = 1

    for entry in entry_list:
        print()
        for loop in range(1, repeat + 1):
            for word, explain in entry.items():
                input_word = getInput(f"[{index}] {loop}\t\t{word}    {explain}  |  ")
                if input_word != word:
                    print("写错啦!")
        index += 1
    return None
