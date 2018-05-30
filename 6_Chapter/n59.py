#
# usage: python n59.py {file name}
#


import sys
import xml.etree.cElementTree as ET


if __name__ == '__main__':
    fname = sys.argv[1]
    froot = ET.parse(fname).getroot()
    fsl = []

    for parse in froot.iter('parse'):
        ptext = parse.text.strip().split()
        sl = []
        for i, v in enumerate(ptext):
            if v == '(NP':
                cnt = 0
                tmp = []
                for vv in ptext[i:]:
                    if vv.find('(') != -1:
                        cnt += 1
                    if vv.find(')') != -1:
                        cnt -= vv.count(')')
                        tmp.append(vv.replace(')', ''))
                    if cnt == 0:
                        sl.append(tmp)
                        break
        fsl.append(sl)

    for sl in fsl:
        for s in sl:
            print(' '.join(s))
