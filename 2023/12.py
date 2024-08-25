import re
from itertools import combinations

from functools import cache
import tqdm


def solve(data):
    total = 0
    for rec, num in data:
        t = recursion(rec, num)
        print(rec, num, t)
        total += t
    print(total)

@cache
def recursion(rec, nums):
    if len(rec) == 0:
        if len(nums) == 0:
            return 1
        return 0

    curr = rec[0]
    if curr == "#":
        if len(nums) == 0 or len(rec) < nums[0]:
            return 0

        if "." in rec[0 : nums[0]]:
            return 0

        if rec[nums[0] :].startswith("#"):
            return 0

        if len(rec) > nums[0]:
            if rec[nums[0]] == "?":
                return recursion(rec[nums[0] + 1 :].lstrip("."), nums[1:])

        return recursion(rec[nums[0] :].lstrip("."), nums[1:])
    elif curr == ".":
        return recursion(rec.lstrip("."), nums)
    elif curr == "?":
        return recursion("#" + rec[1:], nums) + recursion("." + rec[1:], nums)


def solve2(data):
    total = 0
    for rec, num in tqdm.tqdm(data):
        rec = "?".join(["".join(rec)] * 5)
        num = num * 5
        t = recursion(rec, num)
        total += t
    print(total)

def read_file():
    with open('data/12.in', 'r') as f:
        data = []
        for l in f.readlines():
            spl = l.strip().split(' ')
            record = spl[0]
            nums = re.findall('\d+', spl[1])
            data.append((record, tuple(map(int, nums))))

        return data


if __name__ == '__main__':
    data = read_file()
    solve(data)
    solve2(data)
