import sys, csv
twblg_lines = sys.stdin #教育部閩南語辭典830650_11000900254_Attach1.tsv 
twblg_reader = csv.reader(twblg_lines, delimiter="\t")
headers = next(twblg_reader)
print("\t".join("n_no, POS, 詞目, 音讀, 異用字, 又見音, 近義詞, 反義詞, 詞目, 例句斷詞, Chinese_example_sent ,釋義, 方言差, 鹿港, 三峽, 台北, 宜蘭, 台南, 高雄, 金門, 馬公, 新竹, 台中".split(",")))

from ArticutAPI_Taigi import ArticutTG
username = "phonlab.nthu@gmail.com"
apikey = "IBUYB2Ro*nMe*HWuvmoZnBC+r5FjH3x"
articutTaigi = ArticutTG(username, apikey)

import re
tp = fn = 0
for n_no,詞目,音讀,異用字,又見音,近義詞,反義詞,釋義1,釋義2,釋義3,釋義4,釋義5,釋義6,釋義7,釋義8,釋義9,釋義10,釋義11,釋義12,釋義13,釋義14,釋義15,方言差,鹿港,三峽,台北,宜蘭,台南,高雄,金門,馬公,新竹,台中 in twblg_reader:
    for 釋義 in [釋義1,釋義2,釋義3,釋義4,釋義5,釋義6,釋義7,釋義8,釋義9,釋義10,釋義11,釋義12,釋義13,釋義14,釋義15]:
        P = re.match(pattern="(\d\.)?【(?P<POS>.)】", string=釋義)
        if P:
#           print(P.group("POS"), n_no, 詞目, 音讀, 釋義)

            try:
                example = 釋義.split("例")[1][1:]
                Taigi_example_sent = re.split(pattern=r"[A-z\u00C0-\u017F]", string=example)[0]
                Chinese_example_sent = example.split('(')[1]
                Chinese_example_sent = Chinese_example_sent.split(')')[0]
#               print(P.group("POS"), 詞目, n_no, Taigi_example_sent, Chinese_example_sent)#, 釋義)#resultDICT['result_segmentation'])

                resultDICT = articutTaigi.parse(inputSTR=Taigi_example_sent, level="lv1", convert="TL")
                resultLIST = resultDICT['result_segmentation'].split("/")
                if 詞目 in resultLIST:
                    print("O", end="\t")
                    tp += 1
                else:
                    print("X", end="\t")
                    fn += 1
                print(n_no, P.group("POS"), 詞目, 音讀, 異用字, 又見音, 近義詞, 反義詞, 詞目, resultDICT['result_segmentation'], Chinese_example_sent ,釋義, 方言差, 鹿港, 三峽, 台北, 宜蘭, 台南, 高雄, 金門, 馬公, 新竹, 台中, sep="\t")
            except:
                pass
recall  = tp / (tp + fn) # 標準答案內我有對幾個的比率
#precision=tp / (tp + fp) # 我的答案內有幾個跟標準答案一樣的比率 
print(f"recall = tp / (tp + fn) = {tp} / ({tp} + {fn}) = {recall}")
