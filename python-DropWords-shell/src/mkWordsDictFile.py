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

from libs.terminalClear import terminalClear
from libs.JSONFileTools import mkJSONFile
from libs.JSONFileTools import delJSONFile
from libs.JSONFileIO import saveDict
from libs.getScan import yesORno
from libs.getScan import getInput
from libs.JSONFileTools import getJSONFilesPathList
from src.libs.mkJSONFilePath import mkJSONFilePath
from src.libs.mkShowWordsDict import mkWordsDict




def mkWordsDictFile(dirs: str) -> bool:
    """
    Description:
        制作和保存单词本文件
    Args:
        dirs:
            保存单词本文件的位置
    Returns:
        True:
            单词本制作成功
        False:
            取消或无法制作单词本
            用户输入的内容将丢弃
    """

    terminalClear()

    getJSONFilesPathList(dirs, printf=True)

    path = mkJSONFilePath(dirs)
    exist_ok = False
    while True:
        if mkJSONFile(path, exist_ok=exist_ok):
            break
        else:
            if yesORno("是否覆盖原文件? 此操作无法撤销!", reverse=True):
                exist_ok = True
                continue
            else:
                getInput("[回车以返回]")
                return False


    if not (words_dict := mkWordsDict()):
        print("单词本内容为空, 保存失败!")
        delJSONFile(path)
        getInput("[回车以返回]")
        return False

    while True:
        if saveDict(path, words_dict):
            break
        if not yesORno("请检查目录并重试! 取消将不会保存任何内容!"):
            getInput("[回车以返回]")
            return False
        mkJSONFile(path)

    print("单词本保存成功!")
    getInput("[回车以返回]")
    return True
