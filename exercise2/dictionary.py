from collections import defaultdict

class Graph:
    def __init__(self, fileName):
        file = open(fileName, 'r')
        str1 = file.readline()
        self.N = int(str1[0])
        self.M = int(str1[2])
        self.graph = defaultdict(int)

        for i in range(self.M):
            str2 = file.readline()
            u = str2[0]
            v = str2[2]
            self.graph[u+"."+v] = 1
    
    def printGraph(self):
        for i in self.graph:
            print(i + ": " + str(self.graph[i]))