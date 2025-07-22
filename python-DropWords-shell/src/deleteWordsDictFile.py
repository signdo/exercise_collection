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
from src.libs.selectWordsDictFile import selectWordsDictFile
from libs.JSONFileTools import delJSONFile
from libs.getScan import yesORno
from libs.getScan import getInput



def deleteWordsDictFile(dirs: str) -> bool:
    """
    Description:
        删除单词本文件
    Args:
        dirs:
            单词本文件路径
    Returns:
        True:
            删除成功
        False:
            删除失败
    """

    terminalClear()

    if not (path := selectWordsDictFile(dirs)):
        getInput("[回车以返回]")
        return False

    if yesORno("真的要删除么? 此操作不可撤销!", reverse=True):
        delJSONFile(path)

    getInput("[回车以返回]")
    return True