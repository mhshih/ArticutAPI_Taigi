# -*- coding:utf-8 -*-

from ArticutAPI import Articut
from glob import iglob
import json
from pprint import pprint
import re
import tempfile

from sys import argv
username = ""
apikey = ""
articutTaigi = Articut(username, apikey)

import os
dirname = "dataCollection\\"
for filename in os.listdir(dirname):
    if filename.endswith(".html.txt"):
        try:
            f1 = open(dirname+filename, encoding="utf8")
            f2 = open(dirname+filename+".segmented.txt", "w", encoding="utf8")
            for line in f1:
                resultDICT = articutTaigi.parse(line, level="lv2")
                segmented = resultDICT['result_segmentation']
                print(" ".join(segmented.split('/')))
                f2.write(" ".join(segmented.split('/')))
            f2.close()
        except:
            pass

