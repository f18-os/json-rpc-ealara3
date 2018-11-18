from node import *
import json

def CreateTree(input):
    dictGraph =json.loads(input)
    l = list(dictGraph.keys())

    print("OVERHERE")
    dict2 = {}
    v ={}
    for x in l:                             #create the nodes
        dict2[x] = node(x,list(dictGraph[x]['children'].keys()))
        v[x] = dictGraph[x]['value:']
        #print(x," here", dictGraph[x]['children'].keys(), " val ",v[x])
    print("//////////////////////////////////////////////")
    print(dict2['leaf2'].children)

    for x in l:                #inserting
        dict2[x].val = v[x]
        #print("new",x, "val",v)
        #print("here",x)

    #print("PRINTING ",dict2)
    return dict2["root"]
def show(root, level=0):
    print("%s%s val=%d:" % (level*"  ", root.name, root.val))
    for c in root.children:
        c.show(level + 1)
