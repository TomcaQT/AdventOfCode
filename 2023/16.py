import re
from itertools import combinations
from copy import deepcopy
from functools import cache
from typing import List

import tqdm

UP = (0,-1)
DOWN = (0,1)
LEFT = (-1,0)
RIGHT = (1,0)

dirs = {'R': RIGHT, 'L': LEFT, 'D': DOWN, 'U': UP}
x_d = 0

def solve(data):
    l = sum([int(dist) for dir, dist, _ in data if dir == 'D'])
    w_r, w_l = sum([int(dist) for dir, dist, _ in data if dir == 'R']), sum([int(dist) for dir, dist, _ in data if dir == 'L'])
    w = w_r + w_l
    x_d = w_l
    grid = [['.' for _x in range(w)]for _ in range(l)]
    x,y = 0,0
    for dir, dist, color in data:
        dir = dirs.get(dir)
        for i in range(int(dist)):
            x,y = x + dir[0], y+ dir[1]
            set_grid(grid, x,y, '#')

    pprint(grid)


def get_grid(grid,x,y):
    return grid[y][x + x_d]

def set_grid(grid,x,y, val):
    grid[y][x + x_d] = val

def solve2(data):
    pass


def pprint(data):
    print('=============')
    w, l = len(data[0]), len(data)
    for y in range(l):
        for x in range(w):
                print(data[y][x], end='')
        print('')

def read_file():
    with open('data/18.in', 'r') as f:
        lines = f.readlines()
        return [tuple(l.strip().split(' '))for l in lines]


if __name__ == '__main__':
    data = read_file()
    print(solve(deepcopy(data)))
    solve2(deepcopy(data))
