import re
from tqdm import tqdm


def solve(data):
    mapping = {}
    h = {}

    seeds = data[0].split(': ')[1].split(' ')

    source, dest = '', ''
    map = {}
    for l in tqdm(data[1:]):
        m = re.search('([a-z]+)-to-([a-z]+)', l)
        if m:
            #print(m.group(1), m.group(2))
            source, dest = m.group(1), m.group(2)
            h[source] = dest
            map = {}
            mapping[source] = map
            continue
        m = re.search('(\d+) (\d+) (\d+)', l)
        if m:
            dest_start, source_start, range_len = int(m.group(1)), int(m.group(2)), int(m.group(3))
            map.update({(source_start, source_start+range_len): (dest_start, dest_start+range_len)})

    min_loc = 1197665086
    for s in seeds:
        src = 'seed'
        x = int(s)
        #print(f"{src}: {x}")
        while src != 'location':

            #print(f"{src}: {x} -> {h[src]}: {map.get(x,x)}")
            x = m_get(mapping,src,x)

            src = h[src]

        if int(x) < min_loc:
            min_loc = int(x)
    print(f'part1: {min_loc}')

    min_loc = []
    seeds = [int(s) for s in seeds]
    r = [(seeds[i], seeds[i]+seeds[i+1]) for i in range(0, len(seeds), 2)]
    for s in tqdm(r):
        src = 'seed'
        ranges = [s]
        #print(f"{src}: {x}")
        while src != 'location':

            #print(f"{src}: {x} -> {h[src]}: {map.get(x,x)}")
            ranges = m_get2(mapping,src,ranges)
            src = h[src]
        ranges = sorted(ranges, key=lambda tup: tup[0])
        min_loc.append(ranges[0])


    print(f'part2: {sorted(min_loc, key=lambda tup: tup[0])[0][0]}')


def m_get2(mapping,src, ranges):
    map = mapping[src]
    x = sorted(map.items(), key=lambda tup: tup[0][0])
    new_ranges = []
    #print(f"{src}: {ranges}")
    #print(f"Mapping: {x}")
    for r in ranges:
        min_r, max_r = r
        prev_k, prev_v = None, None
        curr = min_r
        for k,v in x:
            min_k, max_k = k
            min_v, max_v = v
            if min_r > max_k:
                continue


            if curr < min_k:
                overlap_range = min(max_r, min_k) - curr
                new_ranges.append((curr,curr+overlap_range))
                curr += overlap_range

            overlap_range = min(max_r, max_k) - curr
            new_ranges.append((min_v + curr - min_k, min_v + curr - min_k+overlap_range))
            curr += overlap_range
            if curr == max_r:
                break
        if curr < max_r:
            new_ranges.append((curr, max_r))
    return new_ranges

def m_get(mapping,src, x):
    map = mapping[src]
    for k,v in map.items():
        min_k, max_k = k
        min_v, max_v = v
        if min_k <= x < max_k:
            return min_v + (x - min_k)
    return x




def read_file():
    with open('data/5.in', 'r') as f:
        return [l.strip() for l in f.readlines()]


if __name__ == '__main__':
    data = read_file()
    solve(data)