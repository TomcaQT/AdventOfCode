import re
import sys
from collections import namedtuple
import numpy as np
import pandas as pd

sys.setrecursionlimit(1000000)


class State(namedtuple('State', 'o, c, obs, g, o_robots, c_robots, obs_robots, g_robots')):
    pass


max_minutes = 24


def simulate(minutes, s: State, blueprint, mem: {}):
    if minutes == max_minutes:
        return s.g
    if s in mem.keys():
        state = mem[s]
        if minutes > state[1]:
            return 0
        return state[0]
    g = [0]
    max_o = max(blueprint[1], blueprint[2], blueprint[3], blueprint[5])
    max_c = blueprint[4]
    max_obs = blueprint[6]
    demand_o, demand_c, demand_obs = max_o * (max_minutes - minutes), max_c * (max_minutes - minutes), max_obs * (max_minutes - minutes)


    if s.o >= blueprint[1] and s.o_robots < max_o and s.o < demand_o:
        g.append(simulate(minutes + 1, State(s.o + s.o_robots - blueprint[1], s.c + s.c_robots, s.obs + s.obs_robots, s.g + s.g_robots,
                            s.o_robots + 1, s.c_robots, s.obs_robots, s.g_robots), blueprint, mem))
    if s.o >= blueprint[2] and s.c_robots < max_c and s.c < demand_c:
        g.append(simulate(minutes + 1, State( s.o + s.o_robots - blueprint[2], s.c + s.c_robots, s.obs + s.obs_robots, s.g + s.g_robots,
                            s.o_robots, s.c_robots+1, s.obs_robots, s.g_robots), blueprint, mem))
    if s.o >= blueprint[3] and s.c >= blueprint[4] and s.obs_robots < max_obs and s.obs < demand_obs:
        g.append(simulate(minutes + 1, State( s.o + s.o_robots - blueprint[3], s.c + s.c_robots - blueprint[4], s.obs + s.obs_robots, s.g + s.g_robots,
                            s.o_robots, s.c_robots, s.obs_robots + 1, s.g_robots), blueprint, mem))
    if s.o >= blueprint[5] and s.obs >= blueprint[6]:
        g.append(simulate(minutes + 1, State( s.o + s.o_robots - blueprint[5], s.c + s.c_robots, s.obs + s.obs_robots - blueprint[6], s.g + s.g_robots,
                            s.o_robots, s.c_robots, s.obs_robots, s.g_robots + 1), blueprint, mem))
    g.append(simulate(minutes + 1, State( s.o + s.o_robots, s.c + s.c_robots, s.obs + s.obs_robots, s.g + s.g_robots,
                            s.o_robots, s.c_robots, s.obs_robots, s.g_robots), blueprint, mem))
    max_g = max(g)
    mem[s] = (max_g, minutes)
    return max_g


def solve_part_1(data):
    max_g = []
    global max_minutes
    max_minutes = 24
    for blueprint in data:
        blueprint = list(map(int, blueprint))
        max_g.append((blueprint[0], simulate(0,State( 0, 0, 0, 0, 1, 0, 0, 0), blueprint, {})))
        print(f'Blueprint {blueprint[0]}: {max_g[-1]}')

    m = map(lambda x: x[0]*x[1], max_g)

    return sum(m)


def solve_part_2(data):
    res = 1
    global max_minutes
    max_minutes = 31
    for blueprint in data[0:3]:
        blueprint = list(map(int, blueprint))

        g = simulate(0, State(0, 0, 0, 0, 1, 0, 0, 0), blueprint, {})
        print(f'Blueprint {blueprint[0]}  >>> {g}')
        res *= g

    return res


def parse_raw_input(infile):
    lines, raw_data, data = [], None, None
    # with open(infile) as file:
    # lines = file.readlines()
    with open(infile, 'r') as f:
        raw_data = list(map(lambda x: re.findall(r'\d+', x), f.read().split('\n')))
    return raw_data


def solve(infile):
    data = parse_raw_input(infile)
    print(solve_part_1(data))
    print(solve_part_2(data))
