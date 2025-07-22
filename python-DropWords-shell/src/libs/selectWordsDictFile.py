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

from libs.JSONFileTools import getJSONFilesPathList
from libs.getScan import getInput




def selectWordsDictFile(dirs: str) -> str:
    """
    Description:
        输入文件序号, 选择一个文件返回其路径
    Args:
        dirs:
            需要选择文件的目录
    Returns:
        None:
            目录为空或无法访问
        文件路径:
            选择的可用路径
    """
    if not (json_list := getJSONFilesPathList(dirs, printf=True)):
        return None

    while True:
        if not (num := getInput("请键入文件序号, 键入 'c' 以取消: ")):
            continue
        if num == 'c':
            return None

        try:
            if (num := int(num) - 1) < 0:
                raise IndexError
            path = json_list[num]
        except ValueError:
            print("文件编号只能为数字!")
            continue
        except IndexError:
            print("文件不存在!")
            continue
        else:
            return path
