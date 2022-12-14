import copy
import re
import numpy as np
import pandas as pd

def dirs(x):
    return [(x[0], x[1]+1), (x[0]-1, x[1]+1), (x[0]+1, x[1]+1)]


def solve_part_1(data):
    void = max(data, key=lambda x: x[1])
    init, curr = (500, 0), (500, 0)
    res = 0
    while True:
        if curr[1] > void[1]:
            break
        for d in dirs(curr):
            if d not in data.keys():
                curr = d
                break
        else:
            data[curr] = 'O'
            curr = init
            res += 1

    return res

def solve_part_2(data):
    void = max(data, key=lambda x: x[1])[1]+2
    init, curr = (500, 0), (500, 0)
    res = 0
    while True:
        if init in data.keys():
            break
        for d in dirs(curr):
            if d not in data.keys() and d[1] != void:
                curr = d
                break
        else:
            data[curr] = 'O'
            curr = init
            res += 1

    return res


def parse_raw_input(infile):
    lines, raw_data, data = [], None, {}
    # with open(infile) as file:
    # lines = file.readlines()
    with open(infile, 'r') as f:
        raw_data = f.read().split('\n')
    for line in raw_data:
        coords = list(map(lambda a: (int(a[0]), int(a[1])), [x.split(',') for x in [coords for coords in line.split(' -> ')]]))
        for x, y in zip(coords, coords[1:]):
            x1, x2, y1, y2 = min(x[0], y[0]), max(x[0], y[0]), min(x[1], y[1]), max(x[1], y[1])
            for c in [(i, j) for i in range(x1, x2+1) for j in range(y1, y2+1)]:
                data[c] = '#'
    return data


def solve(infile):
    data = parse_raw_input(infile)
    print(solve_part_1(copy.deepcopy(data)))
    print(solve_part_2(copy.deepcopy(data)))
