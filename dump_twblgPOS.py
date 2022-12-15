import sys, csv
targetPOSs = sys.argv[1:]
twblg_lines= sys.stdin #moe_dict/教育部閩南語辭典830650_11000900254_Attach1.tsv 
twblg_reader = csv.reader(twblg_lines, delimiter="\t")
headers = next(twblg_reader)

import re, json
POSlist = []
for n_no,詞目,音讀,異用字,又見音,近義詞,反義詞,釋義1,釋義2,釋義3,釋義4,釋義5,釋義6,釋義7,釋義8,釋義9,釋義10,釋義11,釋義12,釋義13,釋義14,釋義15,方言差,鹿港,三峽,台北,宜蘭,台南,高雄,金門,馬公,新竹,台中 in twblg_reader:
    try:
        for 釋義 in [釋義1,釋義2,釋義3,釋義4,釋義5,釋義6,釋義7,釋義8,釋義9,釋義10,釋義11,釋義12,釋義13,釋義14,釋義15]:
            P = re.match(pattern="(\d\.)?【(?P<POS>.)】", string=釋義)
            if P:
#               print(P.group("POS"), n_no, 詞目, 音讀, 釋義)
                if P.group("POS") in targetPOSs:
                    POSlist.append(詞目)
                    print(P.group("POS"), n_no, 詞目, 音讀, 釋義)
    except:
        pass
#print(sorted(POSlist))

twblg2articutPOS = {
        "熟":"IDIOM",
        "時":"TIME",
        "形":"MODIFIER",
        "副":"MODIFIER",
        "動":"ACTION",
        "量":"ENTITY_classifier",
        }
targetPOS = targetPOSs[0]
articutPOS = twblg2articutPOS[targetPOS]
fp = open(file=articutPOS+".json", mode="w")
json.dump(obj=POSlist, fp=fp, ensure_ascii=False)
