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
#    last_city =0
#    unvisited_cities = set(range(1, N))
    solution = [current_city]

    def distance_from_current_city(to):
        return dist[current_city][to]

    xs =[]
    
    def perm(head,rest):
#        xs =[]
        if not rest:
            head.append(0)
            xs.append(head)
#            return xs

        for i in rest:
            h = head[:]
            h.append(i)
            r = rest[:]
            r.remove(i)
            perm(h,r)

  #  kaizyo = math.factorial(N)
 #   zenbu = list(range(kaizyo))
    perm([],list(range(1,N)))
    print xs


    max = 10000000

    for conbi in xs:
        print conbi
        sum = 0.0
        for i in conbi:
            sum += dist[current_city][i]
            current_city = i

        if max > sum:
            max = sum
            solution = conbi
            solution.insert(0,0)

    print max
    return solution


if __name__ == '__main__':
    assert len(sys.argv) > 1
    solution = solve(read_input(sys.argv[1]))
    print_solution(solution)
