#
# usage: python n58.py {file name}
#


import sys
import xml.etree.cElementTree as ET


if __name__ == '__main__':
    fname = sys.argv[1]
    froot = ET.parse(fname).getroot()
    fsl = []
    for dependencies in froot.iterfind('.//dependencies'):
        if dependencies.get('type') == 'collapsed-dependencies':
            pre_d, nusbj_d, dobj_d = {}, {}, {}
            for dep in dependencies.iterfind('./dep'):
                dep_type = dep.get('type')
                pid = int(dep.find('governor').get('idx'))
                if dep_type == 'nsubj' or dep_type == 'dobj':
                    pre_d[pid] = dep.findtext('governor')
                    dtxt = dep.findtext('dependent')
                    if dep_type == 'nsubj':
                        nusbj_d[pid] = dtxt
                    else:
                        dobj_d[pid] = dtxt
            for k, v in pre_d.items():
                tmp = []
                if nusbj_d.get(k) is not None and dobj_d.get(k) is not None:
                    tmp.append([nusbj_d[k], v, dobj_d[k]])
                if tmp != []:
                    fsl.append(tmp)
    for fs in fsl:
        for s in fs:
            print('\t'.join(s))
