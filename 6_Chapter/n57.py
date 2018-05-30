#
# usage: python n57.py {file name}
#


import sys
import pydot
import xml.etree.cElementTree as ET


if __name__ == '__main__':
    fname, snumber = sys.argv[1], int(sys.argv[2])-1
    froot = ET.parse(fname).getroot()
    fedges = []

    for dependencies in froot.iterfind('.//dependencies'):
        if dependencies.get('type') == 'collapsed-dependencies':
            tmp = []
            for dep in dependencies.iterfind('./dep'):
                gnovernor = dep.findtext('governor')
                dependent = dep.findtext('dependent')
                if dependent != '.' and dependent != ',':
                    tmp.append((gnovernor, dependent))
            fedges.append(tmp)

    g = pydot.graph_from_edges(fedges[snumber])
    g.write_jpeg('n57-{}.jpg'.format(snumber+1), prog='dot')
