#!/usr/bin/env python3
import os
import sys


webCmd = 'open https://github.com/jimmysong/programmingbitcoin/'
myCmd = '/bin/bash --rcfile .venv/bin/activate | jupyter notebook'
atomCmd = 'atom code-ch'


if len(sys.argv) > 1 and sys.argv[1].isdigit() and int(sys.argv[1]) <= 14:
    chapterInt = int(sys.argv[1])
    if chapterInt < 10:
        chapter = f"0{sys.argv[1]}"
    else:
        chapter = sys.argv[1]

    webCmd += f"blob/master/ch{chapter}.asciidoc"
    if chapterInt < 14:
        myCmd += f" code-ch{chapter}"
        atomCmd += chapter
        os.system(atomCmd)


os.system(webCmd)
os.system(myCmd)
