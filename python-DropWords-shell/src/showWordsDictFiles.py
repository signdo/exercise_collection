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
from libs.JSONFileTools import getJSONFilesPathList
from libs.getScan import getInput



def showWordsDictFiles(config: dict) -> None:
    """
    Description:
        显示单词本文件
    Args:
        config:
            用户配置
    """

    terminalClear()

    print()
    getJSONFilesPathList(config["UserData"], printf=True)
    print()
    getJSONFilesPathList(config["Resource"], printf=True)
    print("\n文件显示完成!")
    getInput("[回车以继续]")
