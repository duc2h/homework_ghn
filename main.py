from exercise2 import adjacencymatrix, listofedges, adjacencylist, dictionary
from exercise1 import bfsdfs


if __name__ == "__main__":
    # adjacency matrix
    print("adjacency matrix")
    graph1 = adjacencymatrix.Graph("input.txt")
    graph1.printGraph()

    # list of edges
    print("list of edges")
    graph2 = listofedges.Graph("input.txt")
    graph2.printGraph()
    
    # adjacency list
    print("adjacency list")
    graph3 = adjacencylist.Graph("input.txt")
    graph3.printGraph()

    # map with combined key
    print("map with combined key")
    graph4 = dictionary.Graph("input.txt")
    graph3.printGraph()

    # BFS and DFS
    print("BFS and DFS")
    graph5 = bfsdfs.Graph("input.txt")
    graph5.BFS("output.txt")
    graph5.DFS("output.txt")
    print("Done")