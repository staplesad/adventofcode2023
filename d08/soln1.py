import math
import sys


def parse_input(filename):
    seq = None
    route = {}
    with open(filename) as fp:
        seq = list(fp.readline().strip())
        for line in fp:
            if line.strip() == "":
                continue
            step, pair = line.strip().split(" = ")
            left, right = pair.strip().split(", ")
            route[step] = (left[1:], right[:-1])
    return (seq, route)

def solve(seq, route):
    traverse = True
    stop = 'AAA'
    end = 'ZZZ'
    count = 0
    while stop != end:
        idx = count % len(seq)
        count += 1
        if seq[idx] == 'L':
            stop = route[stop][0]
        elif seq[idx] == 'R':
            stop = route[stop][1]
        else:
            print("somethings wrong")
    return count
if __name__=='__main__':
    if len(sys.argv) < 2:
        print("pass filename")
        sys.exit()
    else:
        filename = sys.argv[1]
    data = parse_input(filename)
    print(data)
    print(solve(*data))
