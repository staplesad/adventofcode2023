import sys
from collections import defaultdict

def parse_input(filename):
    seeds = None
    maps = defaultdict(dict)
    map_seq= []
    with open(filename) as fp:
        current_map = None
        for line in fp:
            print(line)
            if line.split(":")[0] == "seeds":
                seeds = (list(map(int, line.split(":")[1].strip().split(" "))))
            elif line.split(" ")[-1] == "map:\n":
                current_map = line.split(" ")[0].strip()
                map_seq.append(current_map)
            elif line.strip() == "":
                continue
            else:
                numbers = tuple(map(lambda x: int(x.strip()) if x.strip() != '' else None, line.split(" ")))
                numbers = [n for n in numbers if n is not None]
                s_to_d = {(numbers[1], numbers[1]+numbers[2]): (numbers[0], numbers[0]+numbers[2])}
                maps[current_map].update(s_to_d)
    return seeds, maps, map_seq

def find_destination(seed, maps, map_seq):
    dest = seed
    print(dest)
    for map_name in map_seq:
        print(map_name)
        for source_range in maps[map_name]:
            start, end = source_range
            if dest >= start and dest < end:
                print(source_range)
                index = dest - start
                dest = maps[map_name][source_range][0] + index
                break
        print(dest)
    return dest

def solve(seeds, maps, map_seq):
    print(maps)
    print(len(seeds))
    all_dests = []
    for i, seed in enumerate(seeds):
        all_dests.append(find_destination(seed, maps, map_seq))
    return min(all_dests)

if __name__=='__main__':
    if len(sys.argv) < 2:
        print("pass filename")
        sys.exit()
    else:
        filename = sys.argv[1]
    seeds, maps, m_seq = parse_input(filename)
    print(solve(seeds, maps, m_seq))
