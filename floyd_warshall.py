# Floyd-Warshall Algorithm

v = 4
INF = 99999
def floydWarshall(graph):
    dist = list(map(lambda i: list(map(lambda j:j, i)) ,graph))
    for k in range(v):
        for i in range(v):
            for j in range(v):
                dist[i][j] = min(dist[i][j] , dist[i][k]+dist[k][j])
    printSolution(dist)

def printSolution(dist):
    for i in range(v):
        for j in range(v):
            if(dist[i][j] == INF):
                print('%7s' %("INF"),)
            else:
                print('%7d\t' %(dist[i][j]),)
            if j == v-1:
                print(" ")
graph = [[0,5,INF,10],
         [INF,0,3,INF],
         [INF, INF, 0, 1],
         [INF, INF, INF, 0]
         ]
floydWarshall(graph);