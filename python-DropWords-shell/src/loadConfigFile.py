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

import json

from libs.JSONFileTools import mkJSONFile
from libs.JSONFileIO import saveDict
from libs.JSONFileIO import loadDict



def loadConfigFile() -> dict:
    """
    Description:
        加载用户的配置文件
    Returns:
        用户的自定义配置或默认配置
    """

    default_config = """
    {
        "UserData": "data/",
        "Resource": "res/",
        "ConfigPath": "config.json",
        "WordsRepeat": 3,
        "LastErrorDict": {}
    }
    """

    config = json.loads(default_config)

    if mkJSONFile(config["ConfigPath"], debug_info=False):
        saveDict(config["ConfigPath"], config)
        return config
    
    if user_config := loadDict(config["ConfigPath"]):
        return user_config
    else:
        return config