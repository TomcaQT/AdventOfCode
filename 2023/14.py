import re
from itertools import combinations
from copy import deepcopy
from functools import cache
import tqdm

states = {}

def solve(data):
    new_rocks = deepcopy(data)
    w, l = len(data[0]), len(data)
    for y in range(l):
        for x in range(w):
            if data[y][x] == 'O':
                move_stone(new_rocks, x, y, (0,-1))


    total = 0
    for y in range(l):
        for x in range(w):
            print(new_rocks[y][x], end='')
            if new_rocks[y][x] == 'O':
                total += l - y
        print('')

    print(total)

def listToTuple(function):
    def wrapper(*args):
        l= args[0]

        return tuple([tuple(line) for line in l])
    return wrapper

#your cached function
def move_stone(rocks, x, y, dir):
    w, l = len(rocks[0]), len(rocks)
    dx, dy = dir
    while True:
        x_n, y_n = x+dx, y+dy
        if y_n == -1 or x_n == -1 or y_n == l or x_n == w:
            return
        if rocks[y_n][x_n] == '.':
            rocks[y][x] = '.'
            rocks[y_n][x_n] = 'O'
            x, y = x_n, y_n
        else:
            return


def cycle(data):
    new_rocks = deepcopy(data)
    w, l = len(data[0]), len(data)
    for y in range(l):
        for x in range(w):
            if data[y][x] == 'O':
                move_stone(new_rocks, x, y, (0,-1))
    data = deepcopy(new_rocks)
    new_rocks = deepcopy(data)
    #print('after N')
    #pprint(data)
    for y in range(l):
        for x in range(w):
            if data[y][x] == 'O':
                move_stone(new_rocks, x, y, (-1,0))
    data = deepcopy(new_rocks)
    new_rocks = deepcopy(data)
    #print('after W')
    #pprint(data)
    for y in range(l-1,-1,-1):
        for x in range(w):
            if data[y][x] == 'O':
                move_stone(new_rocks, x, y, (0,1))
    data = deepcopy(new_rocks)
    new_rocks = deepcopy(data)
    #print('after S')
    #pprint(data)
    for y in range(l-1,-1,-1):
        for x in range(w-1,-1,-1):
            if data[y][x] == 'O':
                move_stone(new_rocks, x, y, (1,0))
    #print('after E')
    #pprint(new_rocks)
    return new_rocks


def solve2(data):
    w, l = len(data[0]), len(data)
    c, c_len = None, 0
    u = 1000000000
    mod = -1
    for i in tqdm.tqdm(range(u)):
        h = tuple([tuple(line) for line in data])
        if h not in states.keys():
            states[h] = get_val(h)
        else:
            if c is None:
                c = h
            elif c == h:
                print('Cycle of len ', c_len , i)
                mod = (u-i) % c_len
                print(mod)
            elif mod == -1:
                c_len += 1

            if mod != -1:
                mod = (u-i-1) % c_len-1
                if mod == 0:
                    break


        data = cycle(data)

    print('=======')
    total = 0
    for y in range(l):
        for x in range(w):
            print(data[y][x], end='')
            if data[y][x] == 'O':
                total += l - y
        print('')

    print(total)

def get_val(data):
    total = 0
    w, l = len(data[0]), len(data)
    for y in range(l):
        for x in range(w):
            if data[y][x] == 'O':
                total += l - y


def pprint(data):
    w, l = len(data[0]), len(data)
    for y in range(l):
        for x in range(w):
            print(data[y][x], end='')
        print('')

def read_file():
    with open('data/14.in', 'r') as f:
        lines = f.readlines()
        return [[c for c in l.strip()]for l in lines]


if __name__ == '__main__':
    data = read_file()
    solve(deepcopy(data))
    solve2(deepcopy(data))
