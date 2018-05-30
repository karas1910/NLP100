#
# usage: python n56.py {file name}
#


import sys
import xml.etree.cElementTree as ET


if __name__ == '__main__':
    fname = sys.argv[1]
    froot = ET.parse(fname)
    fsentencel = []

    for sentences in froot.iterfind('./document/sentences/sentence'):
        s = []
        for word in sentences.iter('word'):
            s.append(word.text)
        fsentencel.append(s)

    for coreference in froot.iterfind('./document/coreference/coreference'):
        for mention in coreference.iter('mention'):
            pre_mention = ''
            if mention.get('representative') == 'true':
                pre_mention = mention.findtext('text').split()
            else:
                snumber = int(mention.findtext('sentence'))-1
                sstart = int(mention.findtext('start'))-1
                send = int(mention.findtext('end'))-1
                stmp = list(fsentencel[snumber])
                fsentencel[snumber] = []

                for i in range(sstart):
                    fsentencel[snumber].append(stmp[i])

                for w in pre_mention:
                    fsentencel[snumber].append(w)
                for i in range(sstart, send+1):
                    if i == sstart:
                        fsentencel[snumber].append('('+stmp[i])
                    elif i == send:
                        fsentencel[snumber].append(stmp[i]+')')
                    else:
                        fsentencel[snumber].append(stmp[i])

                for i in range(send+1, len(stmp)):
                    fsentencel[snumber].append(stmp[i])

    for s in fsentencel:
        print(' '.join(s))
