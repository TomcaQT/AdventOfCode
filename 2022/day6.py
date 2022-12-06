import re
import numpy as np
import pandas as pd


def solve_p(data, x):
    for i in range(len(data)-x):
        if len(set(data[i:i+x])) == x:
            return i+x


def parse_raw_input(infile):
    lines, raw_data, data = [], None, None
    with open(infile, 'r') as f:
        raw_data = f.read().split('\n')[0]
    return raw_data


def solve(infile):
    data = parse_raw_input(infile)
    print(solve_p(data, 4))
    print(solve_p(data, 14))
