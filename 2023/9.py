import re
from math import lcm

import tqdm


def solve(data):
    total = 0
    for line in data:
        line = [int(l) for l in line]
        x = []
        while True:
            x.insert(0, line[-1])
            diffs = [line[i+1] - line[i] for i in range(len(line)-1)]
            line = diffs
            if all([n == 0 for n in line]):
                x.insert(0,0)
                break
        total += sum(x)
        #print(sum(x))


    print(total)

def solve2(data):
    total = 0
    for line in data:
        line = [int(l) for l in line]
        x = []
        while True:
            x.insert(0, line[0])
            diffs = [line[i+1] - line[i] for i in range(len(line)-1)]
            line = diffs
            if all([n == 0 for n in line]):
                x.insert(0,0)
                break
        print(x)
        curr = 0
        for i in range(len(x) - 1):
            curr = - curr + x[i+1]
        total += curr
        #print(sum(x))


    print(total)


def read_file():
    with open('data/9.in', 'r') as f:
        lines = f.readlines()
        return [l.strip().split(' ') for l in lines]


if __name__ == '__main__':
    data = read_file()
    solve(data)
    solve2(data)
