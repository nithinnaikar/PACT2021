# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 20:32:29 2022

@author: Nithin
# Early DFS code, will not run- just an outline 
"""
def DFS_VISIT(graph, vertex):
    time += 1
    discovered[vertex] = time
    color[vertex] = "gray"
    
    for each neighbor in G[vertex]:
        if color[neighbor] == "white":
            predecessor[neighbor] = vertex
            DFS_VISIT(graph, neighbor)
    
    color[vertex] = "black"
    time += 1
    finished[vertex] = time
    
 
def DFS(G):
    color = ["white"] * len(G)
    predecessor = [None] * len(G)
    time = 0
    
    for each vertex in G:
        if color[vertex] == "white":
            DFS_VISIT(G, vertex)