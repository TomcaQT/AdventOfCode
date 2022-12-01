import re
import numpy as np
import pandas as pd
import utils


def solve_part_1(data):
    return data[0]


def solve_part_2(data):
    return sum(data[:3])


def parse_raw_input(infile: str):
    lines, raw_data = [], None
    with open(infile, 'r') as f:
        raw_data = f.read().split('\n\n')
    data = sorted([sum([int(cal)for cal in elf.split('\n')]) for elf in raw_data], reverse=True)
    return data

def solve(infile):
    data = parse_raw_input(infile)
    print(solve_part_1(data))
    print(solve_part_2(data))
