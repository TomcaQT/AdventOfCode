import copy
import re
import numpy as np
import pandas as pd


def isdecimal(x):
    try:
        value = int(x)
        return True
    except ValueError:
        return False


def try_replace(data, monkey, op):
    s = op.split(' ')
    if s[0] in data.keys():
        new = data[s[0]]
        if isdecimal(new):
            data[monkey] = data[monkey].replace(s[0], new)
    if s[2] in data.keys():
        new = data[s[2]]
        if isdecimal(new):
            data[monkey] = data[monkey].replace(s[2], new)

def expand(data, x):
    if len(re.findall(r'[a-z]', x)) <= 0:
        return x
    s = x.split('r')
    if()
    return expand()


def solve_part_1(data):
    res = expand(data, x)
    return str(eval(res))
    while True:
        for monkey in data.keys():
            if not isdecimal(data[monkey]):
                if len(re.findall(r'[a-z]', data[monkey])) > 0:
                    try_replace(data, monkey, data[monkey])
                if len(re.findall(r'[a-z]', data[monkey])) <= 0:
                    data[monkey] = str(int(eval(data[monkey])))
            if monkey == 'root' and isdecimal(data[monkey]):
                return data[monkey]


def solve_part_2(data_old):

    i = 0
    while True:
        data = copy.deepcopy(data_old)
        data['root'] = data['root'].replace('+', '==')
        data['humn'] = f'{i}'
        while True:
            for monkey in data.keys():
                if not isdecimal(data[monkey]):
                    if len(re.findall(r'[a-z]', data[monkey])) > 0:
                        try_replace(data, monkey, data[monkey])
                    if len(re.findall(r'[a-z]', data[monkey])) <= 0:
                        data[monkey] = str(int(eval(data[monkey])))
                if monkey == 'root' and isdecimal(data[monkey]):
                    if int(data[monkey]) == 1:
                        return i
                    else:
                        break
        i += 1


def parse_raw_input(infile):
    lines, raw_data, data = [], None, {}
    # with open(infile) as file:
    # lines = file.readlines()
    with open(infile, 'r') as f:
        raw_data = f.read().split('\n')
    for line in raw_data:
        s = line.split(":")
        data[s[0]] = s[1].strip()
    return data


def solve(infile):
    data = parse_raw_input(infile)
    print(solve_part_1(copy.deepcopy(data)))
    print(solve_part_2(copy.deepcopy(data)))
