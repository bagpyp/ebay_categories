from anytree import Node, RenderTree
import pandas as pd

def pt(root):
    print(RenderTree(root))


ect = pd.read_csv('ebayCatFiltered.csv').fillna('0')

ebay = Node('ebay')
a = ect.a.unique()

for x0 in a:
    y0 = Node(x0,ebay)
    b = ect[ect.a==x0].b.unique()
    for x1 in b:
        if x1 != '0':
            y1 = Node(x1,y0)
            c = ect[ect.b==x1].c.unique()
            for x2 in c:
                if x2 != '0':
                    y2 = Node(x2,y1)
                    d = ect[ect.c==x2].d.unique()
                    for x3 in d:
                        if x3 != '0':
                            y3 = Node(x3,y2)
                            e = ect[ect.d==x3].e.unique()
                            for x4 in e:
                                if x4 != '0':
                                    y4 = Node(x4,y3)
                                    f = ect[ect.e==x4].f.unique()
                                    for x5 in f:
                                        if x5 != '0':
                                            y5 = Node(x5,y4)
                                            

pt(ebay)

