import re
from itertools import combinations
from copy import deepcopy
from functools import cache
from typing import List
import tqdm
from abc import ABC, abstractmethod

lp = 0
hp = 0
LOW = 0
HIGH = 1

class Module(ABC):
    def __init__(self, name):
        self.name = name
        self.inputs = {}
        self.outputs = {}
        self.to_sent = LOW
        self.ignore = False

    def add_input(self, i):
        if i.name in self.inputs.keys():
            return
        self.inputs[i.name] = i

    def add_output(self, o):
        self.outputs[o.name] = o

    @abstractmethod
    def rec_signal(self, signal, src):
        pass

    def process(self):
        if self.ignore:
            return []
        for o in self.outputs.values():
            if self.to_sent == LOW:
                global lp
                lp += 1
            else:
                global hp
                hp += 1
            o.rec_signal(self.to_sent, self)
            print(f'{self.name} - {"LOW" if self.to_sent == 0 else "HIGH"} - -> {o.name}')
        return [o for o in self.outputs]


class BlankModule(Module):

    def rec_signal(self, signal, src):
        return

    def process(self):
        return

class BModule(Module):

    def rec_signal(self, signal, src):
        return

class FModule(Module):

    def __init__(self, name):
        super().__init__(name)
        self.status = False

    def rec_signal(self, signal, src):
        if signal == HIGH:
            self.ignore = True
            return
        self.ignore = False
        self.status = not self.status
        self.to_sent = HIGH if self.status else LOW

    def process(self):
        return super().process()
class CModule(Module):

    def __init__(self, name):
        super().__init__(name)
        self.mem = {}

    def add_input(self, i):
        super().add_input(i)
        self.mem[i.name] = LOW

    def rec_signal(self, signal, src):
        self.mem[src.name] = signal

    def process(self):
        if all([m == HIGH for m in self.mem.values()]):
            self.to_sent = LOW
        else:
            self.to_sent = HIGH
        return super().process()


def solve(data):
    modules = {}
    for inp in [line[0] for line in data]:
        if inp == 'broadcaster':
            type = 'B'
        else:
            type = inp[0]
            inp = inp[1:]

        input_module = BModule(inp) if type == 'B' else FModule(inp) if type == '%' else CModule(inp)
        modules[inp] = input_module

    for i, line in enumerate(data):
        inp, outs = line[0], line[1].split(', ')
        if inp != 'broadcaster':
            inp = inp[1:]
        [modules[inp].add_output(modules.get(o, BlankModule(o))) for o in outs]
        [modules[o].add_input(modules[inp]) for o in outs if o in modules.keys()]

    button_press = 1
    global lp
    global hp
    lp = button_press
    hp = 0
    for i in range(button_press):
        print(f"===== Button Press {i} ======")
        q = ['broadcaster']

        while len(q) > 0:
            to_process = modules.get(q.pop(0))
            if to_process is None:
                continue
           # print(f'Processing: {to_process.name}')
            to_add = to_process.process()
            #print(f'Adding: {to_add}')
            q.extend(to_add)

    print(f'Lows: {lp} X Highs {hp} = {lp*hp}')

def solve2(data):
    pass


def pprint(data):
    print('=============')
    w, l = len(data[0]), len(data)
    for y in range(l):
        for x in range(w):
            print(data[y][x], end='')
        print('')

def read_file():
    with open('data/20.in', 'r') as f:
        lines = f.readlines()
        return [l.strip().split(' -> ') for l in lines]


if __name__ == '__main__':
    data = read_file()
    solve(deepcopy(data))
    solve2(deepcopy(data))
