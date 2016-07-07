#!/usr/bin/env python3

import sys
import math

from common import print_solution, read_input


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def solve(cities):
    N = len(cities)

    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])

    current_city = 0
    last_city =0
    unvisited_cities = set(range(1, N))
    solution = [current_city]

    def distance_from_current_city(to):
        return dist[current_city][to]

    sum = 0.0
    while unvisited_cities:
        next_city = min(unvisited_cities, key=distance_from_current_city)
        sum += dist[current_city][next_city]
        unvisited_cities.remove(next_city)
        solution.append(next_city)
        current_city = next_city
    sum += dist[current_city][last_city]

    opt = opt_2(solution,dist)
    result = or_opt(opt,dist)

    return result,dist


def opt_2(solution,dist):
  #  print solution
    N = len(solution)
    total = 0
    rev_solution=[]
    while True:
        count = 0
        for a1 in range(N-2):
            a2 = a1 + 1
            for b1 in range(a1+2,N):
                if b1 == N - 1:
                    b2 = 0
                else:
                    b2 = b1 + 1
                if  a1!=0 or b2 != 0:
                    c1 = dist[solution[a1]][solution[a2]]
                    c2 = dist[solution[b1]][solution[b2]]
                    c3 = dist[solution[a1]][solution[b1]]
                    c4 = dist[solution[a2]][solution[b2]]
                    if c1+c2 > c3+c4:
                        rev_solution = solution[a2:b1+1]
                        solution[a2:b1+1] = rev_solution[::-1]
                        
                        count += 1
                    else:
                        rev_solution = solution
                        
        total += count
        if count == 0:break
    return solution


def or_opt(opt2,dist):
    N = len(opt2)
    total = 0
    while True:
        count = 0
        for i in xrange(N):
            i0 = i - 1
            i1 = i + 1
            if i0 < 0: i0 = N - 1
            if i1 == N: i1 = 0
            for j in xrange(N):
                j1 = j + 1
                if j1 == N: j1 = 0
                if j != i and j1 != i:
                    l1 = dist[opt2[i0]][opt2[i]] 
                    l2 = dist[opt2[i]][opt2[i1]]
                    l3 = dist[opt2[j]][opt2[j1]] 
                    l4 = dist[opt2[i0]][opt2[i1]]
                    l5 = dist[opt2[j]][opt2[i]]  
                    l6 = dist[opt2[i]][opt2[j1]] 
                    if l1 + l2 + l3 > l4 + l5 + l6:
                        p = opt2[i]
                        opt2[i:i + 1] = []
                        if i < j:
                            opt2[j:j] = [p]
                        else:
                            opt2[j1:j1] = [p]
                        count += 1
        total += count
        if count == 0: break
    return opt2

def total_distance(result,dist):
    sum = 0
    list = result[:]
    first = list.pop(0)
    city1 = first
    for a in list:
        city2 = a
        sum += dist[city1][city2]
        city1 = city2
    sum += dist[city1][first]
    return sum
        

if __name__ == '__main__':
    assert len(sys.argv) > 1
    solution,dist = solve(read_input(sys.argv[1]))
    sum = total_distance(solution,dist)
    print_solution(solution)
    print sum
