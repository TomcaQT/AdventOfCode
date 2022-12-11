import re
import numpy as np
import pandas as pd


def solve_part_1(data):
    x, c, res, check = 1, 0, [], range(20, 221, 40)
    cycles = []
    for cmd in data:
        v = 0
        if cmd == 'noop':
            c += 1
            cycles.append(x)
        else:
            v = int(cmd.split(' ')[1])
            cycles.extend([x, x])
            c += 2
        if len(check) > 0 and c >= check[0]:
            res.append(x*check[0])
            check = check[1:]
            x += v
        else:
            x += v
    return sum(res), cycles


def solve_part_2(data):
    w, h = 40, 6
    crt = ''
    for i, pos in enumerate(data):
        c = '#' if (i+1) % 40 in range(pos, pos+3) else '.'
        crt += c
        if (i+1) % 40 == 0 and i != 0:
            crt += '\n'

    return crt

def parse_raw_input(infile):
    lines, raw_data, data = [], None, None
    # with open(infile) as file:
    # lines = file.readlines()
    with open(infile, 'r') as f:
        raw_data = f.read().split('\n')
    return raw_data


def solve(infile):
    data = parse_raw_input(infile)
    o, c = solve_part_1(data)
    print(o)
    print(solve_part_2(c))
