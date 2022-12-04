import re
import numpy as np
import pandas as pd


def solve_part_1(data):

    rucksacks = [(line[:len(line)//2], line[len(line)//2:]) for line in data]
    res = 0
    for c1, c2 in rucksacks:
        checked = set()
        for c in c1:
            if c in c2 and c not in checked:
                res += ord(c) - 96 if c.islower() else ord(c) - 38
                checked.add(c)
    return res


def solve_part_2(data):
    res = 0
    for i in range(0, len(data), 3):
        c1, c2, c3 = data[i], data[i+1], data[i+2]
        for c in c1:
            if c in c2 and c in c3:
                res += ord(c) - 96 if c.islower() else ord(c) - 38
                break
    return res

def parse_raw_input(infile):
    lines, raw_data, data = [], None, None
    with open(infile) as file:
      lines = file.readlines()
    #with open(infile, 'r') as f:
       # raw_data = f.read().split('\n\n')
    return list(map(str.strip, lines))


def solve(infile):
    data = parse_raw_input(infile)
    print(solve_part_1(data))
    print(solve_part_2(data))
