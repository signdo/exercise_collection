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
from libs.getScan import getInput




def menu() -> str:
    """
    Description:
        命令行菜单, 显示用户的可选选项
    Returns:
        单个字符
    """

    terminalClear()

    print("\t命令行背单词\n")

    print("a.\t制作单词本并另存为文件")
    print("b.\t显示所有单词本")
    print("c.\t删除自定义单词本")
    print()
    print("d.\t抄单词 [单词随机]")
    print("e.\t抄单词 [单词不随机]")

    print("f.\t猜释义 [单词随机]")
    print("g.\t猜释义 [单词不随机]")

    print("h.\t猜单词 [单词随机]")
    print("i.\t猜单词 [单词不随机]")

    print("j.\t随机猜单词和释义 [单词随机]")
    print("k.\t随机猜单词和释义 [单词不随机]")
    print()
    print("l.\t显示某个单词本内容")
    print("m.\t显示上次猜错的单词本内容")
    print()
    print("n.\t修改单词本中的词条")
    print("o.\t追加词条")
    print("p.\t插入词条")
    print("q.\t删除词条")

    print("r.\t退出")

    while True:
        char = getInput("\n[请选择] ")
        if len(char) > 1:
            continue
        elif not char.islower():
            continue
        return char
