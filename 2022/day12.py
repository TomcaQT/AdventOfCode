import re
import sys

import numpy as np
import pandas as pd


def get_neis(pos, w, h):
    n = [pos + (0, 1), pos + (0, -1), pos + (1, 0), pos + (-1, 0)]
    neis = []
    for i, p in enumerate(n.copy()):
        if 0 <= p[0] < w and 0 <= p[1] < h:
            neis.append(p)
    return neis


def solve_part_1(data, start, end):
    q, v = [(start, [])], {}
    w, h = len(data[0]), len(data)

    while q:
        curr, path = q.pop(0)
        path.append(curr)
        v[(curr[0], curr[1])] = 1

        if (curr == end).all():
            return len(path) - 1

        neis = get_neis(curr, w, h)
        for n in neis:
            if (n[0], n[1]) not in v.keys() and data[n[1]][n[0]] - data[curr[1]][curr[0]] <= 1:
                q.append((n, path[:]))
                v[n[0], n[1]] = 1
    return None


def solve_part_2(data, start, end):
    starting_pos = [np.array([iy, ix]) for ix, row in enumerate(data) for iy, i in enumerate(row) if i == 1]
    res = sys.maxsize
    for s in starting_pos:
        l = solve_part_1(data, s, end)
        if l:
            res = min(res, l)
    return res



def parse_raw_input(infile):
    lines, raw_data, data = [], None, []
    start, end = (0, 0), (0, 0)
    with open(infile, 'r') as f:
        raw_data = f.read().split('\n')
    for i, line in enumerate(raw_data):
        if 'S' in line:
            start = np.array([line.index('S'), i])
        if 'E' in line:
            end = np.array([line.index('E'), i])
        data.append(list(map(lambda x: ord(x) - 96, line)))
    data[start[1]][start[0]] = 1
    data[end[1]][end[0]] = ord('z') - 96
    return data, start, end


def solve(infile):
    data, s, e = parse_raw_input(infile)
    print(solve_part_1(data, s, e))
    print(solve_part_2(data, s, e))
