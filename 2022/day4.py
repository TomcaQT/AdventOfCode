import re
import numpy as np
import pandas as pd


def solve_part_1(data):
    res = 0
    elves = [x.strip().split(',') for x in data]
    for x in elves:
        x1, x2 = list(map(int, x[0].split('-'))), list(map(int, x[1].split('-')))
        if x1[0] >= x2[0] and x1[1] <= x2[1]:
            res += 1
            continue
        if x2[0] >= x1[0] and x2[1] <= x1[1]:
            res += 1
    return res


def solve_part_2(data):
    res = 0
    elves = [x.strip().split(',') for x in data]
    for x in elves:
        x1, x2 = list(map(int, x[0].split('-'))), list(map(int, x[1].split('-')))
        intersection = [value for value in range(x1[0],x1[1]+1) if value in range(x2[0], x2[1]+1)]
        if len(intersection) > 0:
            res += 1
    return res


def parse_raw_input(infile):
    lines, raw_data, data = [], None, None
    # with open(infile) as file:
    # lines = file.readlines()
    with open(infile, 'r') as f:
        raw_data = f.read().split('\n')
    return raw_data


def solve(infile):
    data = parse_raw_input(infile)
    print(solve_part_1(data))
    print(solve_part_2(data))
