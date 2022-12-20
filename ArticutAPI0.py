# -*- coding:utf-8 -*-

from ArticutAPI import Articut
from glob import iglob
import json
from pprint import pprint
import re
import tempfile

from sys import argv
username = "phonlab.nthu@gmail.com"
apikey = "IBUYB2Ro*nMe*HWuvmoZnBC+r5FjH3x"
if __name__ == "__main__":
    filename = argv[1]
    f1 = open(filename, encoding="utf8")
    f2 = open(filename+".segmented.txt", "w", encoding="utf8")
    articutTaigi = Articut(username, apikey)
    for line in f1:
        resultDICT = articutTaigi.parse(line, level="lv2")
        segmented = resultDICT['result_segmentation']
        print(" ".join(segmented.split('/')))
        f2.write(" ".join(segmented.split('/')))
    f2.close()
