import re
import numpy as np
import pandas as pd

neis = [
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
]


def check(cubes, x):
    x_min, x_max = min(cubes, key=lambda a: a[0])[0] - 1, max(cubes, key=lambda a: a[0])[0] + 1
    y_min, y_max = min(cubes, key=lambda a: a[1])[1] - 1, max(cubes, key=lambda a: a[1])[1] + 1
    z_min, z_max = min(cubes, key=lambda a: a[2])[2] - 1, max(cubes, key=lambda a: a[2])[2] + 1
    if x_min <= x[0] <= x_max and y_min <= x[1] <= y_max and z_min <= x[2] <= z_max:
        return True
    return False


def bfs(cubes, start, end):
    q = [start]
    v = set()
    v.add(start)
    res = []
    while q:
        x = q.pop(0)
        res.append(x)
        for n in neis:
            nei = (x[0] + n[0], x[1] + n[1], x[2] + n[2])
            if nei not in cubes.keys() and nei not in v and check(cubes, nei):
                q.append(nei)
                v.add(nei)
    return res


def solve_part_1(data):
    cubes = {coord: 1 for coord in data}
    res = 0
    for x in cubes.keys():
        sides = 6
        for n in neis:
            if (x[0] + n[0], x[1] + n[1], x[2] + n[2]) in cubes.keys():
                sides -= 1
        res += sides
    return res


def solve_part_2(data):
    res = 0
    cubes = {coord: 1 for coord in data}
    x = max(cubes, key=lambda a: a[0])[0] + 1
    y = max(cubes, key=lambda a: a[1])[1] + 1
    z = max(cubes, key=lambda a: a[2])[2] + 1

    inv_cubes = bfs(cubes, (0, 0, 0), (x, y, z))
    res = 0
    for x in inv_cubes:
        sides = 0
        for n in neis:
            if (x[0] + n[0], x[1] + n[1], x[2] + n[2]) in cubes.keys():
                sides += 1
        res += sides
    return res



def parse_raw_input(infile):
    lines, raw_data, data = [], None, None
    # with open(infile) as file:
    # lines = file.readlines()
    with open(infile, 'r') as f:
        raw_data = list(map(lambda x: tuple(map(int, x.split(','))), f.read().split('\n')))
    return raw_data


def solve(infile):
    data = parse_raw_input(infile)
    print(solve_part_1(data))
    print(solve_part_2(data))
