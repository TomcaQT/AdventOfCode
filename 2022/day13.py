import functools
import re
import numpy as np
import pandas as pd
from itertools import zip_longest
import ast


def sign(a, b):
    if a-b == 0:
        return 0
    return 1 if a-b > 0 else -1


def check(x, y):
    if type(x) is int and type(y) is int:
        return sign(x, y)
    elif type(x) is int:
        x = [x]
    elif type(y) is int:
        y = [y]

    for a, b in list(zip_longest(x, y)):
        if a is None or b is None:
            if a is None and b is None:
                return 0
            return 1 if b is None else -1
        res = check(a, b)
        if res != 0:
            return res
    return 0


def solve_part_1(data):
    res = 0
    for i, d in enumerate(data):
        p1, p2 = d
        r = check(p1, p2)
        if r < 0:
            res += i+1
    return res


def solve_part_2(data):
    data = [item for t in data for item in t]
    data.append([[2]])
    data.append([[6]])

    data = sorted(data, key=functools.cmp_to_key(check))
    return (data.index([[2]]) + 1) * (data.index([[6]]) + 1)


def parse_raw_input(infile):
    lines, raw_data, data = [], None, []
    with open(infile, 'r') as f:
        raw_data = f.read().split('\n\n')
    data = [tuple(map(eval, line.split('\n'))) for line in raw_data]
    return data


def solve(infile):
    data = parse_raw_input(infile)
    print(solve_part_1(data))
    print(solve_part_2(data))

