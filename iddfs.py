# Iterative Deepning Depth First Search

# Code Submitted by- Abhisek Sharma 20CE10006 
#                    Abhishek Kumar 20CE10007
# Date-07-04-22

'''

CODE STARTS FROM HERE //

'''
#      0   ---->level 0
#     /  \
#    1     2 ----> Level 1
#  /   \  / \
# 3    4 5   6----> Level 2
#
# if our target is reached then the loop will stop and print the depth value

from collections import defaultdict
from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)
class Graph:
    
    def __init__(self, vertices):

        self.V = vertices
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

   # function to do depth first search
   
  # LEVEL 0- 0
  # LEVEL 1- 0 1 2
  # LEVEL 2- 0 1 3 (4)=>target  2 5 6
   
   


    def DFS(self, source, target, maximum_depth):
        print("Current Node:",source) # can be comment out 
        if source == target: return True


        if maximum_depth < 0: return False

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[source]:
            if (self.DFS(i, target, maximum_depth - 1)):
                return True
        return False

   # iterative deepning depth first search
    def IDDFS(self, source, target, maximum_depth):

        for i in range(maximum_depth):
            if (self.DFS(source, target, i)):
                return True
        return False


# Create a graph given in the above diagram
L1 = stdin.readline().strip().split()
V = int(L1[0])
E = int(L1[1])

g = Graph(V)

for i in range(E) :
    arr = stdin.readline().strip().split()
    first_v = int(arr[0])
    second_v = int(arr[1])
    g.addEdge(first_v, second_v)



source = 0
target=int(input("Enter target:"))
maximum_depth=int(input("Enter maximum depth:"))


if g.IDDFS(source, target, maximum_depth) == True:
    print("Target achieved with depth ",maximum_depth)
else:
    print("Target Failed with depth ",maximum_depth)

