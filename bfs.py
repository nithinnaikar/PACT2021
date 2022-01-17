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
    discovered = [False] * len(G.vertices)
    discovered[s] = True
    T = []
    L = []
    L[0] = [s]
    i = 0
    while len(L[i]) > 0:
        L[i + 1] = []
        for vertex in L[i]:
            for neighbor in G.get_neighbors(vertex):
                if discovered[neighbor] == False:
                    discovered[neighbor] = True
                    L[i + 1] += [neighbor]
                    T += [vertex, neighbor]
        i += 1
    return T


        
    
