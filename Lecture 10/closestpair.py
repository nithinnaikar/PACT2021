# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 17:11:48 2022

@author: Nithin
"""
import itertools
import math

points = []

def distance(x1, y1, x2, y2):
    '''
    Distance function used to compute the distance between two points.
    
    Parameters
    ----------
    
    x1: x-coordinate of point 1
    y1: y-coordinate of point 1
    x2: x-coordinate of point 2
    y2: y-coordinate of point 2

    
    Returns
    -------
    
    distance: distance between point 1 and point 2
    '''
    return math.sqrt((x2 - x1)^2 + (y2 - y1)^2)

def ClosestPair(points):
    '''
    Closest Pair function used to find the closest pair of points in a coordinate plane.
    
    Parameters
    ----------
    
    points: sequence of tupled 2-dimensional cartesian coordinate points

    
    Returns
    -------
    
    delta: distance between closest pair of points (can also be modifed to return closest pair)
    '''
    if len(points) <= 3:
        distances = []
        combinations = list(itertools.combinations(points, 2))
        for (point1, point2) in combinations:
            dist = distance(point1[0], point1[1], point2[0], point2[1])
            distances.append(dist)
        min_distance = min(distances)
        return min_distance
        #return combinations[distances.index(min_distance)]
    else:
        L = len(points)/2
        points_left, points_right = points[:L], points[L:]
        delta_left, delta_right = ClosestPair(points_left), ClosestPair(points_right)
        delta = min(delta_left, delta_right)
        
        points_prime = [point for point in points if distance(point[0], point[1], L, point[1]) < delta]
        points_prime.sort(key = lambda point: point[1])
        
        distances = []
        for i in range(len(points_prime)):
            for j in range(i+1, i+7):
                dist = distance(points_prime[i][0], points_prime[i][1], points_prime[j][0], points_prime[j][1])
                distances.append(dist)
        delta_prime = min(distances)
        return min(delta, delta_prime)