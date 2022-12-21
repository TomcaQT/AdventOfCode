import copy
import re
import numpy as np
import pandas as pd


def get_loc(x, new_array):
    to_move = new_array.index(x)
    loc = (to_move + x)
    if x > 0 and loc >= len(new_array):
        return (loc % len(new_array)) + 1
    elif x < 0 and loc <= 0:
        return (loc - 1)% len(new_array)
    return loc


def solve_part_1(data):
    indices = [i for i in range(len(data))]
    n = len(data)
    for i, x in enumerate(data):
        value = data[i]
        location_of_index = indices.index(i)
        indices.pop(location_of_index)
        insert_at = (location_of_index + value) % (n - 1)
        indices.insert(insert_at, i)

    new_array = [data[i] for i in indices]
    zero = new_array.index(0)
    a, b, c = new_array[(zero+1000) % len(data)], new_array[(zero+2000) % len(data)], new_array[(zero+3000) % len(data)]
    return a + b + c


def solve_part_2(data):
    data = list(map(lambda x: x * 811589153, data))
    indices = [i for i in range(len(data))]
    n = len(data)
    for _ in range(10):
        for i, x in enumerate(data):
            value = data[i]
            location_of_index = indices.index(i)
            indices.pop(location_of_index)
            insert_at = (location_of_index + value) % (n - 1)
            indices.insert(insert_at, i)

    new_array = [data[i] for i in indices]
    zero = new_array.index(0)
    a, b, c = new_array[(zero + 1000) % len(data)], new_array[(zero + 2000) % len(data)], new_array[
        (zero + 3000) % len(data)]
    return a + b + c


def parse_raw_input(infile):
    lines, raw_data, data = [], None, None
    # with open(infile) as file:
    # lines = file.readlines()
    with open(infile, 'r') as f:
        raw_data = f.read().split('\n')

    return list(map(int, raw_data))


def solve(infile):
    data = parse_raw_input(infile)
    print(solve_part_1(data))
    print(solve_part_2(data))
