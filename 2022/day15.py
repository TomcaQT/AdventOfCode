import re
import numpy as np
import pandas as pd


def dist(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])


def cut_y(y, sensor, beacon):
    d = dist(sensor, beacon)
    dy = abs(y - sensor[1])
    if dy > d:
        return None
    return [sensor[0] - (d - dy), sensor[0] + (d - dy)]


def cut_all(y, sensors, beacons):
    cuts = []
    for i, sensor in enumerate(sensors):
        c = cut_y(y, sensor, beacons[i])
        if c:
            cuts.append(c)

    cuts = sorted(cuts, key=lambda x: x[0])
    mcuts = []
    a, b = None, None
    for cut in cuts:
        a = cut[0] if not a else a
        b = cut[1] if not b else b

        if cut[0] <= b + 1 and cut[1] > b:
            b = cut[1]
        elif cut[0] > b + 1:
            mcuts.append([a, b])
            a = cut[0]
            b = cut[1]

    if a and b:
        mcuts.append([a, b])
    return mcuts


def solve_part_1(sensors, beacons, y):
    mcuts = cut_all(y, sensors, beacons)
    res = 0
    for cut in mcuts:
        res += cut[1] - cut[0]
    return res


def solve_part_2(sensors, beacons, maximum):
    for y in range(0, maximum + 1):
        mcuts = cut_all(y, sensors, beacons)
        if len(mcuts) > 1 and 0 <= mcuts[0][1] <= maximum:
            return (mcuts[0][1] + 1) * 4000000 + y
    return




def parse_raw_input(infile):
    raw_data, sensors, beacons = [], [], []
    with open(infile, 'r') as f:
        raw_data = f.read().split('\n')
    for l in raw_data:
        m = re.findall(r'([0-9-]+)', l)
        m = [m[0], m[1], m[2], m[3]]
        coords = list(map(int, m))
        sensors.append((coords[0], coords[1]))
        beacons.append((coords[2], coords[3]))
    return sensors, beacons


def solve(infile, y, maximum):
    sensors, beacons = parse_raw_input(infile)
    print(solve_part_1(sensors, beacons, y))
    print(solve_part_2(sensors, beacons, maximum))
