#
# usage: python n44.py {file name} number
#
from n41 import load_cabocha_file_chunk
import sys
import pydot


if __name__ == '__main__':
    fn, num = sys.argv[1], int(sys.argv[2])
    target = load_cabocha_file_chunk(fn)
    edges = []

    for c in target[num-1]:
        ml, ml2 = c.morphs, target[num-1][c.dst].morphs
        s1, s2 = '', ''
        if c.dst == -1:
            continue
        for m1, m2 in zip(ml, ml2):
            if m1.pos != '記号':
                s1 += m1.surface
            if m2.pos != '記号':
                s2 += m2.surface
        if s1 != '' and s2 != '':
            edges.append((s1, s2))

    g = pydot.graph_from_edges(edges)
    g.write_jpeg('n44.jpg', prog='dot')
