import re
import numpy as np
import pandas as pd

rocks = [
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)],
    [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (1, 0), (0, 1), (1, 1)]
]


def debug_cave(cave):
    if len(cave) == 0:
        return
    max_y = max(cave.keys(), key=lambda x: x[1])[1]
    for y in range(max_y, 0-1, -1):
        line = ''
        for x in range(7):
            c = '#' if (x, y) in cave.keys() else '.'
            line += c
        print(f'|{line}|')

def simulate(data, max_rocks):
    cave = {}
    w = 7
    jet, jets = 0, len(data)
    for i in range(0, max_rocks):
        rock = rocks[i % 5]
        y = max(cave.keys(), key=lambda x: x[1])[1] + 4 if len(cave) > 0 else 3
        x = 2
        #simulation of falling
        while True:
            #apply wind
            dir = 1 if data[jet % jets] == '>' else -1
            jet += 1
            rock_left, rock_right = min(rock, key=lambda r: r[0])[0] + x, max(rock, key=lambda r: r[0])[0] + x
            if rock_left + dir >= 0 and rock_right + dir <= 6:
                for tile in rock:
                    if (x + tile[0] + dir, y + tile[1]) in cave.keys():
                        break
                else:
                    x += dir
            #try move
            for tile in rock:
                if (x + tile[0], y + tile[1] - 1) in cave.keys() or y + tile[1] - 1 < 0:
                    #cant move
                    for t in rock:
                        cave[x + t[0], y + t[1]] = '#'
                    break
            else:
                y -= 1
                continue
            break

    return max(cave.keys(), key=lambda x: x[1])[1] + 1


def solve_part_1(data):
    return simulate(data, 2022)


def solve_part_2(data):
    return simulate(data, 1000000000000)


def parse_raw_input(infile):
    lines, raw_data, data = [], None, None
    # with open(infile) as file:
    # lines = file.readlines()
    with open(infile, 'r') as f:
        raw_data = f.read().split('\n')
    return raw_data[0]


def solve(infile):
    data = parse_raw_input(infile)
    print(solve_part_1(data))
    print(solve_part_2(data))
