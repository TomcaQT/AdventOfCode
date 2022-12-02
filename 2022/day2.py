import re
import numpy as np
import pandas as pd

shapes = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3,
}
rules = {
    'AY': 6,
    'AZ': 0,
    'BX': 0,
    'BZ': 6,
    'CX': 6,
    'CY': 0,
}
shapes2 = {'X': 0, 'Y': 3, 'Z': 6}
rules2 = {
    'AX': 3,
    'AZ': 2,
    'BX': 1,
    'BZ': 3,
    'CX': 2,
    'CZ': 1,
}


def solve_part_1(data):
    s1 = 0
    for x in data:
        o, p = x.split(' ')[0], x.split(' ')[1]
        s1 += shapes[p]
        if shapes[o] == shapes[p]:
            s1 += 3
        else:
            s1 += rules[f'{o}{p}']
    return s1


def solve_part_2(data):
    s1 = 0
    for x in data:
        o, p = x.split(' ')[0], x.split(' ')[1]
        s1 += shapes2[p]
        if p == 'Y':
            s1 += shapes[o]
        else:
            s1 += rules2[f'{o}{p}']
    return s1


def parse_raw_input(infile):
    lines, raw_data, data = [], None, None
    with open(infile, 'r') as f:
        data = f.read().split('\n')
    return data


def solve(infile):
    data = parse_raw_input(infile)
    print(solve_part_1(data))
    print(solve_part_2(data))
