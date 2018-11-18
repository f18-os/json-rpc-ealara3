import json
class node:
    def __init__(self, name, children = []):
        self.name = name
        self.children = children
        self.val = 0
    def show(self, level=0):
        print("%s%s val=%d:" % (level*"  ", self.name, self.val))
        for c in self.children:
            c.show(level + 1)

def increment(graph):
    graph.val += 1;
    for c in graph.children:
        increment(c)

def CreateDict(graph, dictGraph = {}):
    #dictGraph.update({graph.name: graph.val})
    #dictGraph.update({graph.name: graph.val,})
    dict2 = {}
    chil={}
    for i in range(len(graph.children)):
        chil.update({graph.children[i].name: graph.children[i].val})             #this tells who is the children from the graph

    dict2.update({"value:":graph.val,"children":chil})

    #dictGraph.update({graph.name: dict2})
    for c in graph.children:                    #creates a dictionary of the graph
        dictGraph = CreateDict(c,dictGraph)

    dictGraph.update({graph.name: dict2})
    return dictGraph
