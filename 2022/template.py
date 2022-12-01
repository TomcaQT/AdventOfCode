import re
import numpy as np
import pandas as pd


def solve_part_1(data):
    pass


def solve_part_2(data):
    pass


def parse_raw_input(infile):
    lines, raw_data, data = [], None, None
    # with open(infile) as file:
    # lines = file.readlines()
    with open(infile, 'r') as f:
        raw_data = f.read().split('\n\n')
    return data


def solve(infile):
    data = parse_raw_input(infile)
    print(solve_part_1(data))
    print(solve_part_2(data))
