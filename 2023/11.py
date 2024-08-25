import re
from itertools import combinations
import tqdm


def solve(data):
    total = 0
    mapp, galaxies, empty_lines, empty_cols = data
    galaxies_pairs = combinations(galaxies, 2)
    for start, end in galaxies_pairs:
        s_x, s_y = start
        e_x, e_y = end
        if e_x < s_x:
            s_x, e_x = e_x, s_x
        if e_y < s_y:
            s_y, e_y = e_y, s_y
        d_x = [1 for x in empty_cols if s_x <= x <= e_x]
        d_y = [1 for y in empty_lines if s_y <= y <= e_y]
        l = abs(s_x - e_x) + abs(s_y - e_y) + sum(d_x) + sum(d_y)
        total += l
    print(total)


def solve2(data):
    total = 0
    mapp, galaxies, empty_lines, empty_cols = data
    galaxies_pairs = combinations(galaxies, 2)
    for start, end in galaxies_pairs:
        s_x, s_y = start
        e_x, e_y = end
        if e_x < s_x:
            s_x, e_x = e_x, s_x
        if e_y < s_y:
            s_y, e_y = e_y, s_y
        d_x = [1_000_000 - 1 for x in empty_cols if s_x <= x <= e_x]
        d_y = [1_000_000 - 1 for y in empty_lines if s_y <= y <= e_y]
        l = abs(s_x - e_x) + abs(s_y - e_y) + sum(d_x) + sum(d_y)
        total += l
    print(total)


def read_file():
    with open('data/11.in', 'r') as f:
        lines = [l.strip() for l in f.readlines()]
        empty_lines = []
        empty_cols = []
        for y, line in enumerate(lines):

            if is_empty(line):
                empty_lines.append(y)

        for x in range(len(lines[0])):
            col = [l[x] for l in lines]
            if is_empty(col):
                empty_cols.append(x)

        galaxies = [(x,y) for y, l in enumerate(lines) for x, c in enumerate(l.strip()) if c == '#']
        return [[c for c in l.strip()]for l in lines], galaxies, empty_lines, empty_cols


if __name__ == '__main__':
    data = read_file()
    solve(data)
    solve2(data)
