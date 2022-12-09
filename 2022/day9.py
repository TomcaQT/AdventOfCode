import re
import numpy as np
import pandas as pd


dirs = {
    'U': (0, 1),
    'D': (0, -1),
    'R': (1, 0),
    'L': (-1, 0)
}


def check(x, y):
    return abs(x[0] - y[0]) > 1 or abs(x[1] - y[1]) > 1


def solve_part_1(data):
    res = set()
    head = np.array([0, 0])
    tail = np.array([0, 0])
    res.add((tail[0], tail[1]))
    for d, x in data:
        for _ in range(int(x)):
            last_head = head.copy()
            head += dirs[d]
            if check(head, tail):
                tail = last_head
                res.add((tail[0], tail[1]))
    return len(res)


def solve_part_2(data):
    res = set()
    rope = np.zeros(20).reshape((10, 2))
    last = np.zeros(20).reshape((10, 2))
    res.add((rope[-1][0], rope[-1][1]))
    for d, x in data:
        for _ in range(int(x)):
            rope[0] += dirs[d]
            for r in range(1, len(rope)):
                if check(rope[r], rope[r-1]):
                    diff = rope[r-1] - rope[r]
                    rope[r] += (np.sign(diff[0]), np.sign(diff[1]))

            res.add((rope[-1][0], rope[-1][1]))
    return len(res)


def parse_raw_input(infile):
    lines, raw_data, data = [], None, None
    with open(infile, 'r') as f:
        raw_data = f.read().split('\n')
    return list(map(lambda x: x.split(' '), raw_data))


def solve(infile):
    data = parse_raw_input(infile)
    print(solve_part_1(data))
    print(solve_part_2(data))
