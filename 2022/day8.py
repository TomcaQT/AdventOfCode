import re
import numpy as np
import pandas as pd


def check_vis(data, t):
    return all(get_vis(data, t))


def get_vis(data, t, rev=False):
    return list(d < t for d in data) if not rev else list(reversed(list(d < t for d in data)))


def solve_part_1(data):
    res = 0
    for y, l in enumerate(data):
        for x, t in enumerate(l):
            if check_vis(data[y][0:x], t) or check_vis(data[y][x+1:], t) or \
                    check_vis(column(data, x)[0:y], t) or check_vis(column(data, x)[y+1:], t):
                res += 1
    return res


def get_vis_count(x):
    return x.index(False)+1 if False in x else len(x)


def solve_part_2(data):
    res = 0
    for y, _l in enumerate(data):
        for x, t in enumerate(_l):
            l, r = get_vis(data[y][0:x], t, True), get_vis(data[y][x + 1:], t)
            u, d = get_vis(column(data, x)[0:y], t, True), get_vis(column(data, x)[y + 1:], t)
            tmp = get_vis_count(l) * get_vis_count(r) * get_vis_count(u) * get_vis_count(d)
            res = max(tmp, res)
    return res


def column(matrix, i):
    return [row[i] for row in matrix]


def parse_raw_input(infile):
    lines, raw_data, data = [], None, []
    # with open(infile) as file:
    # lines = file.readlines()
    with open(infile, 'r') as f:
        raw_data = f.read().split('\n')
    for line in raw_data:
        l = []
        l.extend(list(map(int, [*line])))
        data.append(l)
    return data


def solve(infile):
    data = parse_raw_input(infile)
    print(solve_part_1(data))
    print(solve_part_2(data))
