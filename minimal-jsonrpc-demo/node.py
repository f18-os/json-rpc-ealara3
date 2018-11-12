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
    dictGraph.update({graph.name: graph.val})
    for c in graph.children:
        dictGraph = CreateDict(c,dictGraph)
    #dictGraph.update({graph.name: graph.val})
    return dictGraph
