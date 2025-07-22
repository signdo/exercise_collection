#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
site: https://github.com/Mo-yis/dropWords
clone: git@github.com:Mo-yis/dropWords.git
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

from src.menu import menu
from src.loadConfigFile import loadConfigFile
from src.mkWordsDictFile import mkWordsDictFile
from src.showWordsDictFiles import showWordsDictFiles
from src.deleteWordsDictFile import deleteWordsDictFile
from src.userFunc import *
from src.userConfigWordsDict import *



config = loadConfigFile()

while (code := menu()) != 'r':
    if code == 'a':
        mkWordsDictFile(config["UserData"])
    elif code == 'b':
        showWordsDictFiles(config)
    elif code == 'c':
        deleteWordsDictFile(config["UserData"])
    
    elif code == 'd':
        userEntryRepeat(config, random_entry=True)
    elif code == 'e':
        userEntryRepeat(config, random_entry=False)
    
    elif code == 'f':
        userGuessEntry(config, guess_word=False, random_guess=False, random_entry=True)
    elif code == 'g':
        userGuessEntry(config, guess_word=False, random_guess=False, random_entry=False)

    elif code == 'h':
        userGuessEntry(config, guess_word=True, random_guess=False, random_entry=True)
    elif code == 'i':
        userGuessEntry(config, guess_word=True, random_guess=False, random_entry=False)

    elif code == 'j':
        userGuessEntry(config, guess_word=True, random_guess=True, random_entry=True)
    elif code == 'k':
        userGuessEntry(config, guess_word=True, random_guess=True, random_entry=False)
    
    elif code == 'l':
        userShowWordsDict(config)
    elif code == 'm':
        userShowWordsDict(config, last_err=True)

    elif code == 'n':
        userReplaceEntry(config)
    elif code == 'o':
        userAddEntry(config, is_insert=False)
    elif code == 'p':
        userAddEntry(config, is_insert=True)
    elif code == 'q':
        userDelEntry(config)