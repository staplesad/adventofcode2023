import math
import sys

def parse_input(filename):
    data ={}
    with open(filename) as fp:
        for line in fp:
            parts = line.strip().split(":")
            l_type = parts[0]
            numbers = [int(x.strip()) for x in parts[1].split(" ") if x.strip()!=""]
            data[l_type] = numbers
    return data

def calc_possibilities(time, distance):
    dists = []
    for i in range(1, time):
        length = i*(time-i)
        if length > distance:
            dists.append(length)
    return dists

def solve(data):
    n_poss = []
    for i in range(len(data["Time"])):
        poss_dists = calc_possibilities(data["Time"][i], data["Distance"][i])
        n_poss.append(len(poss_dists))
    print(n_poss)
    return math.prod(n_poss)

if __name__=='__main__':
    if len(sys.argv) < 2:
        print("pass filename")
        sys.exit()
    else:
        filename = sys.argv[1]
    data = parse_input(filename)
    print(data)
    print(solve(data))
