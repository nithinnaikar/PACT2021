# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 22:01:49 2022

@author: Nithin
"""
       
def BFS(G, s):
    '''
   Breadth-first search function used to traverse a graph breadth-first.
   
   Parameters
   ----------
   
   adj. list: adjacency list representation of an undirected graph
   
   s: starting vertex
   
   Returns
   -------
   
   T: BFS tree with all vertices reachable from s 
   (i.e. all vertices in the connected component containing s)
   '''
    discovered = [False] * len(G)
    discovered[s] = True
    T = []
    L = []
    L.append([s])
    i = 0
    while len(L[i]) > 0:
        if len(L) != i + 2:
            L.append([])
        for vertex in L[i]:
            for neighbor in G[vertex]:
                if discovered[neighbor] == False:
                    discovered[neighbor] = True
                    L[i + 1].append(neighbor)
                    T.append((vertex, neighbor)) 
        i += 1
    return T

    
graph = {0: [1, 3],
         1: [0, 2],
         2: [1],
         3: [0]}

T = BFS(G = graph, s = 1)
print(T)
