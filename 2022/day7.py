import re
import numpy as np
import pandas as pd


def create_fs(data):
    fs = {'/': 0}
    path = '/'
    for line in data[1:]:
        split = line.strip().split(' ')
        if re.match(r'^\$ cd', line) is not None:
            if split[2] == '..':
                path = path[0:path[:-1].rfind('/')+1]
            else:
                path += f'{split[2]}/'
                if path not in fs.keys():
                    fs[path] = 0
        elif re.match(r'^\$ ls', line) is not None:
            continue
        elif split[0] != 'dir':
            fs[path] += int(split[0])
    return fs


def solve_part_1(data):
    fs = create_fs(data)
    for x in fs.keys():
        for y in fs.keys():
            if x != y and re.match(f'^{x}', y) is not None:
                fs[x] += fs[y]
    return fs, sum([x for x in fs.values() if x <= 100000])


def solve_part_2(data):
    return min([x for x in data.values() if x >= 30000000 - (70000000 - data['/'])])


def parse_raw_input(infile):
    lines, raw_data, data = [], None, None
    with open(infile) as file:
        data = file.readlines()
    return data


def solve(infile):
    data = parse_raw_input(infile)
    fs, res = solve_part_1(data)
    print(res)
    print(solve_part_2(fs))
