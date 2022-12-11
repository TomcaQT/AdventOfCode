import re
import numpy as np
import pandas as pd
import math
import copy


class Monkey:
    def __init__(self, items, operation, test, test_true, test_false):
        self.inspected = 0
        self.items = items
        self.operation = operation
        self.test = test
        self.test_true = test_true
        self.test_false = test_false

    def process(self, monkeys, part2=None):
        for item in self.items:
            self.inspected += 1
            new_item = eval(self.operation.replace('old', str(item)))
            if part2 is None:
                new_item = new_item // 3
            else:
                new_item = new_item % part2
            if new_item % self.test == 0:
                monkeys[self.test_true].catch_item(new_item)

            else:
                monkeys[self.test_false].catch_item(new_item)
        self.items = []

    def catch_item(self, item):
        self.items.append(item)


def solve_part_1(monkeys):
    for i in range(20):
        for monkey in monkeys:
            monkey.process(monkeys)
    best = list(sorted(map(lambda x: x.inspected, monkeys))[-2:])
    return best[0] * best[1]


def solve_part_2(monkeys, part2):
    for i in range(10000):
        for monkey in monkeys:
            monkey.process(monkeys, part2)
    best = list(sorted(map(lambda x: x.inspected, monkeys))[-2:])
    return best[0] * best[1]


def parse_raw_input(infile):
    lines, raw_data, data = [], None, None
    with open(infile, 'r') as f:
        data = f.read().split('\n\n')
    monkeys = []
    part2 = []
    for line in data:
        line = line.split('\n')[1:]
        items = list(map(int, line[0].split(':')[1].split(',')))
        op = line[1].split('=')[1]
        test, t, f = int(line[2].split(' ')[-1]), int(line[3].split(' ')[-1]), int(line[4].split(' ')[-1])
        part2.append(test)
        monkeys.append(Monkey(items, op, test, t, f))
    return monkeys, part2


def solve(infile):
    data, part2 = parse_raw_input(infile)
    print(solve_part_1(copy.deepcopy(data)))
    print(solve_part_2(copy.deepcopy(data), math.lcm(*part2)))
