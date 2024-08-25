import re
from itertools import combinations
from copy import deepcopy
from functools import cache
import tqdm


def hash(s):
    value = 0
    for c in s:
        value += ord(c)
        value *= 17
        value = value % 256
    return value

def solve(data):
    print(sum([hash(s) for s in data]))


def solve2(data):
    boxes = [{} for _ in range(256)]
    for d in data:
        if '=' in d:
            label, focal = d.split('=')
            box = boxes[hash(label)]
            box[label] = focal
        else:
            label = d[:-1]
            box = boxes[hash(label)]
            if label in box.keys():
                boxes[hash(label)].pop(label)

    total = 0
    for i in range(256):
        box = boxes[i]
        for slot, focal in enumerate(box.values()):
            total += (i+1) * (slot+1) * int(focal)
    print(total)

def read_file():
    with open('data/15.in', 'r') as f:
        lines = f.readlines()
        data = []
        for l in lines:
            data.extend(l.strip().split(','))
        return data


if __name__ == '__main__':
    data = read_file()
    solve(data)
    solve2(data)
