from collections import defaultdict

class Graph:
    def __init__(self, fileName):
        file = open(fileName, 'r')
        str1 = file.readline()
        self.N = int(str1[0])
        self.M = int(str1[2])
        self.graph = defaultdict(list)

        for i in range(self.M):
            str2 = file.readline()
            u = str2[0]
            v = str2[2]
            self.graph[u].append(v)
            self.graph[v].append(u)
        str3 = file.readline()
        self.S = str3[0]
        self.E = str3[2]

    def DFS(self, fileName):
        stack = [(self.S, [self.S])]
        results = []
        while stack:
            (vertex, path) = stack.pop()
            for next_node in set(self.graph[vertex]) - set(path):
                if next_node == self.E:
                    results.append(path + [next_node])
                else:
                    stack.append((next_node, path + [next_node]))

        f = open(fileName, 'a')
        f.write("Result of deep first search: ")
        for result in results:
            f.write("\n")
            f.write(self.listToString(result))
        f.write("\n")
        f.close()
    

    def BFS(self, fileName):
        queue = [(self.S, [self.S])]
        results = []
        while queue:
            (vertex, path) = queue.pop(0)
            for next_node in set(self.graph[vertex]) - set(path):
                if next_node == self.E:
                    results.append(path + [next_node])
                    f = open(fileName, 'a')
                    f.write("Result of breadth first search: ")
                    for result in results:
                        f.write("\n")
                        f.write(self.listToString(result))
                    f.write("\n")
                    f.close()
                    return
                else:
                    queue.append((next_node, path + [next_node]))

    # convert array to string
    def listToString(self, s):
        str1 = " " 
        return (str1.join(s))