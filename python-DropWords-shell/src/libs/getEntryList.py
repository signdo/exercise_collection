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




def getEntryList(words_dict: dict, random_mode: bool=False) -> list[dict]:
    """
    Description:
        从单词字典获取不重复的词条列表
    Args:
        words_dict:
            单词字典
        random_mode:
            随机模式
            默认不随机
    Returns:
        词条列表
    """

    if random_mode:
        return random.sample(list(words_dict.values()), len(words_dict))
    else:
        return list(words_dict.values())
