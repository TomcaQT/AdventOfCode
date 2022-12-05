import re
import numpy as np
import pandas as pd


stackstring = '''
[Q]         [N]             [N]    
[H]     [B] [D]             [S] [M]
[C]     [Q] [J]         [V] [Q] [D]
[T]     [S] [Z] [F]     [J] [J] [W]
[N] [G] [T] [S] [V]     [B] [C] [C]
[S] [B] [R] [W] [D] [J] [Q] [R] [Q]
[V] [D] [W] [G] [P] [W] [N] [T] [S]
[B] [W] [F] [L] [M] [F] [L] [G] [J]
'''


def parse_stacks():
    lines = list(reversed(stackstring.split('\n')[1:-1]))
    stacks = [[] for i in range(1, len(lines[0]), 4)]
    for line in lines:
        for x, i in enumerate(range(1, len(line), 4)):
            if line[i] != ' ':
                stacks[x].append(line[i])
    return stacks


def solve_part_1(data):
    stacks = parse_stacks()
    for line in data:
        m, f, t = line[0], line[1]-1, line[2]-1
        to_move, stacks[f] = stacks[f][-m:], stacks[f][:-m]
        stacks[t].extend(reversed(to_move))
    return ''.join(list(map(lambda x: x.pop(), stacks)))


def solve_part_2(data):
    stacks = parse_stacks()
    for line in data:
        m, f, t = line[0], line[1] - 1, line[2] - 1
        to_move, stacks[f] = stacks[f][-m:], stacks[f][:-m]
        stacks[t].extend(to_move)
    return ''.join(list(map(lambda x: x.pop(), stacks)))


def parse_raw_input(infile):
    lines, raw_data, data = [], None, []
    with open(infile, 'r') as f:
        raw_data = f.read().split('\n')
    for x in raw_data:
        matches = re.findall(r'move ([0-9]+) from ([0-9]+) to ([0-9]+)', x)
        matches = list(map(int, *matches))
        data.append(matches)
    return data


def solve(infile):
    data = parse_raw_input(infile)
    print(solve_part_1(data))
    print(solve_part_2(data))
