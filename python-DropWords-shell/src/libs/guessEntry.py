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

import random

from libs.getScan import getInput
from src.libs.getEntryList import getEntryList




def guessEntry(words_dict: dict, guess_word: bool=True, random_guess: bool=False, random_entry: bool=False) -> dict:
    """
    Description:
    Args:
        words_dict:
            单词字典
        guess_word:
            是否猜单词模式
            默认猜单词模式
        random_guess:
            是否随机猜单词或猜释义
            默认为不随机, 此时取决于 <guess_word> 的取值
            当设置为 True 时, <guess_word> 参数无效
        random_entry:
            随机词条模式
            默认不随机
    Returns:
        单词字典:
            猜错或未填入的单词字典
        空字典:
            全猜对
    """

    entry_list = getEntryList(words_dict, random_mode=random_entry)
    index = 1
    err_entry = {}

    for entry in entry_list:
        if random_guess:
            guess_word = bool(random.getrandbits(1))
        print()

        for word, explain in entry.items():
            if guess_word:
                scan = getInput(f"[{index}]\t {explain}  |  ")
                if scan != word:
                    print(f"猜错了! 正确答案是: {word}")
                    err_entry[index] = entry
            else:
                scan = getInput(f"[{index}]\t {word}  |  ")
                print(f"{word}  的意思是:  {explain}")
                if not scan:
                    print("未填入答案, 词条将被记录! ")
                    err_entry[index] = entry
        index += 1

    return err_entry
