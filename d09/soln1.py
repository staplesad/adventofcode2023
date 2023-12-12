import math
import sys


def parse_input(filename):
    original_seqs = []
    with open(filename) as fp:
        for line in fp:
            original_seqs.append(list(map(int, line.strip().split(" "))))
    return original_seqs

def get_next(seq):
    seq_seq = [seq]
    while any(s != 0 for s in seq_seq[-1]):
        seq_seq.append([j-i for i, j in zip(seq_seq[-1], seq_seq[-1][1:])])
    #    print(seq_seq[-1])
    final_val = 0
    for s in seq_seq[-2::-1]:
        final_val += s[-1]
    return final_val

def solve(og_seqs):
    extrap = []
    for seq in og_seqs:
        extrap.append(get_next(seq))
    print(extrap)
    return sum(extrap)

if __name__=='__main__':
    if len(sys.argv) < 2:
        print("pass filename")
        sys.exit()
    else:
        filename = sys.argv[1]
    data = parse_input(filename)
    print(data)
    print(solve(data))
