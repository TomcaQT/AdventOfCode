plan = list(map(str.split, open('data/18.in')))

dirs = {'R': 1, 'D': 1j, 'L': -1, 'U': -1j,
        '0': 1, '1': 1j, '2': -1, '3': -1j}


def f(steps, pos=0, ans=1):
    for s in steps:
        pos += s.real
        ans += s.imag * pos + abs(s) * 0.5

    return ans


print(f((dirs[d] * int(s)) for d, s, _ in plan),
      f((dirs[c[7]] * int(c[2:7], 16)) for _, _, c in plan))
