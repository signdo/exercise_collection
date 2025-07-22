# -*- coding: UTF-8 -*-
"""
Description:
    用户用于学习的函数
Functions:
    userEntryRepeat:
        用户抄单词
    userGuessEntry:
        用户猜单词
        保存猜错的单词到配置文件中
    userShowWordsDict:
        显示用户单词本内容
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

from libs.JSONFileIO import loadDict
from libs.JSONFileIO import saveDict
from libs.getScan import getInput
from libs.terminalClear import terminalClear
from src.libs.selectWordsDictFile import selectWordsDictFile
from src.libs.entryRepeat import entryRepeat
from src.libs.guessEntry import guessEntry
from src.libs.mkShowWordsDict import showWordsDict




def userEntryRepeat(config: dict, random_entry: bool) -> None:
    """
    Description:
        用户抄单词
    Args:
        config:
            用户配置
        random_entry:
            单词是否随机
    """

    terminalClear()

    if not (path := selectWordsDictFile(config["UserData"])):
        if not (path := selectWordsDictFile(config["Resource"])):
            getInput("[回车以继续]")
            return None
    
    entryRepeat(loadDict(path), repeat=config["WordsRepeat"], random_entry=random_entry)
    print("单词已全部抄完!")
    getInput("[回车以继续]")
    return None




def userGuessEntry(config: dict, guess_word: bool, random_guess: bool, random_entry: bool) -> None:
    """
    Description:
        用户猜单词
        保存猜错的单词到配置文件中
    Args:
        config:
            用户配置
        guess_word:
            是否猜单词模式
        random_guess:
            是否随机猜单词或猜释义
            当设置为 False 时, 取决于 <guess_word> 的取值
            当设置为 True 时, <guess_word> 参数无效
        random_entry:
            随机词条模式
    """

    terminalClear()

    if not (path := selectWordsDictFile(config["UserData"])):
        if not (path := selectWordsDictFile(config["Resource"])):
            getInput("[回车以继续]")
            return None

    err_entry = guessEntry(loadDict(path), guess_word=guess_word, random_guess=random_guess, random_entry=random_entry)
    print(f"单词已全部猜完, 猜错单词 {len(err_entry)} 个!")
    showWordsDict(err_entry, debug_info=False)

    config["LastErrorDict"] = err_entry
    saveDict(config["ConfigPath"], config)
    getInput("[回车以继续]")
    return None




def userShowWordsDict(config: dict, last_err: bool=False):
    """
    Description:
        显示用户单词本内容
    Args:
        config:
            用户配置
        last_err:
            是否仅显示上次猜错的单词
            默认不显示
    """

    terminalClear()

    if last_err:
        showWordsDict(config["LastErrorDict"])
        getInput("[回车以继续]")
        return None

    if not (path := selectWordsDictFile(config["UserData"])):
        if not (path := selectWordsDictFile(config["Resource"])):
            getInput("[回车以继续]")
            return None

    showWordsDict(loadDict(path))
    getInput("[回车以继续]")
    return None
