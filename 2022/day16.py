import copy
import re
import numpy as np
import pandas as pd


def solve_part_1(data, valves_open):
    minutes = 30
    flow = 0
    paths = {}
    for v in list(valves_open.keys()) + ["AA"]:
        for w in list(valves_open.keys()) + ["AA"]:
            if v == w:
                continue
            paths[(v, w)] = get_shortest_path(data, v, w)
            paths[(w, v)] = paths[(v, w)]
    return get_flow(0, 'AA', 30, copy.deepcopy(valves_open), data, paths)


def get_shortest_path(data, start, end):
    q, v = [(start, [])], {}
    while q:
        curr, path = q.pop(0)
        path.append(curr)
        v[curr] = 1

        if curr == end:
            return path

        for n in data[curr][0]:
            if n not in v.keys():
                q.append((n, path[:]))
                v[n] = 1
    return None


def di(d):
    return int(''.join(['1' if i else '0' for i in d.values()]), 2)


mem = {}
def get_flow(flow, curr, minutes, valves_open, data, paths):
    state = (curr, minutes, di(valves_open))
    if state in mem.keys():
        return mem[state]
    max_flow = flow
    if minutes <= 0 or all(valves_open.values()):
        return flow
    for valve in valves_open.keys():
        if valves_open[valve] or valve == curr:
            continue
        path = paths[(curr, valve)]
        new_valves_open = copy.deepcopy(valves_open)
        new_valves_open[valve] = True
        new_minutes = minutes - len(path) + 1
        new_flow = flow + (data[valve][1] * (new_minutes - 1))
        f = get_flow(new_flow, valve, new_minutes-1, valves_open=new_valves_open, data=data, paths=paths)
        max_flow = max(f, max_flow)
    mem[state] = max_flow
    return max_flow






def solve_part_2(data):
    pass


def parse_raw_input(infile):
    valves_open, raw_data, data = {}, None, {}
    # with open(infile) as file:
    # lines = file.readlines()
    with open(infile, 'r') as f:
        raw_data = f.read().split('\n')
    for line in raw_data:
        valves = re.findall(r'([A-Z]{2})', line)
        flow = int(re.findall(r'(\d+)', line)[0])
        data[valves[0]] = (valves[1:], flow)
        if flow > 0:
            valves_open[valves[0]] = False

    return data, valves_open


def solve(infile):
    data, valves_open = parse_raw_input(infile)
    print(f'Good values 1460 and 2117')
    print(solve_part_1(data, valves_open=valves_open))
    print(solve_part_2(data))
