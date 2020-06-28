class Graph:
    def __init__(self, fileName):
        self.graph = []
        file = open(fileName, 'r')
        str1 = file.readline()
        self.N = int(str1[0])
        self.M = int(str1[2])

        for i in range(self.M):
            str2 = file.readline()
            u = int(str2[0])
            v = int(str2[2])
            self.graph.append([u, v])
    
    def printGraph(self):
        print(self.graph)