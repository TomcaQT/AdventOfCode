import re
from math import lcm

import tqdm


def solve(instructions, data):
    total = 0
    mapping = {}
    for line in data:
        m = re.findall('([A-Z]{3})', line)
        src, l, r = m
        mapping[src] = {'L': l, 'R': r}

    curr = 'AAA'
    i = 0
    while curr != 'ZZZ':
        step = instructions[i]
        curr = mapping.get(curr).get(step)

        total += 1
        i += 1
        if i == len(instructions):
            i = 0
    print(total)

def solve2(instructions, data):
    total = 0
    mapping = {}
    for line in data:
        m = re.findall('([A-Z]{3})', line)
        src, l, r = m
        mapping[src] = {'L': l, 'R': r}

    curr = [x for x in mapping.keys() if x[2] == 'A']
    i = 0
    m = []
    for a in curr:
        i = 0
        total = 0
        while a[2] != 'Z':
            step = instructions[i]
            a = mapping.get(a).get(step)

            total += 1
            i += 1
            if i == len(instructions):
                i = 0
        m.append(total)
    print(lcm(*m))


def read_file():
    with open('data/8.in', 'r') as f:
        lines = f.readlines()
        instructions = lines[0].strip()

        return instructions, [l.strip() for l in lines[2:]]


if __name__ == '__main__':
    ins,data = read_file()
    solve(ins,data)
    solve2(ins,data)
    for i in tqdm.tqdm(range(13289612809129)):
        x = i + i