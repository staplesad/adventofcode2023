import sys

max_j = 0
max_i = 0

def maybe_gear(ind):
    return isinstance(ind, str) and ind == '*'


def toNum(num_list):
    return int("".join(map(str, num_list)))

def key_indexes(engine):
    idxs = []
    for j, row in enumerate(engine):
        for i, char in enumerate(row):
            if maybe_gear(char):
                idxs.append((j, i))
    return idxs

def expand_number(engine, idx):
    start = idx[1]
    end = idx[1]
    while start > 0:
        if not isinstance(engine[idx[0]][start-1], int):
            break
        start -= 1
    while end < max_i - 1:
        if not isinstance(engine[idx[0]][end+1], int):
            break
        end += 1
    return (start, end)

def count_nearby_numbers(engine, idx):
    vert = [idx[0]]
    if idx[0] > 0:
        vert.append(idx[0]-1)
    if idx[0] < max_j - 1:
        vert.append(idx[0]+1)
    hor = [idx[1]]
    if idx[1] > 0:
        hor.append(idx[1]-1)
    if idx[1] < max_i - 1:
        hor.append(idx[1]+1)
    seen_numbers = set()
    for j in vert:
        for i in hor:
            if (j, i) == idx:
                continue
            if isinstance(engine[j][i], int):
                num_bounds = expand_number(engine, (j, i))
                if num_bounds not in seen_numbers:
                    seen_numbers.add((j, num_bounds))
    if len(seen_numbers)==2:
        return seen_numbers
    return None


def solve(engine):
    gears = key_indexes(engine)
    actual_gears = []
    for idx in gears:
        numbers = count_nearby_numbers(engine, idx)
        if numbers:
            actual_gears.append((idx[0], numbers))
    print(actual_gears)
    ratios = []
    for gear in actual_gears:
        ratio = 1
        for row, num in gear[1]:
            ratio *= toNum(engine[row][num[0]:num[1]+1])
        ratios.append(ratio)
    return sum(ratios)

def parse_input(filename):
    global max_i
    global max_j
    matrix = []
    with open(filename) as fp:
        for line in fp:
            row = []
            for char in line:
                if char.isdigit():
                    row.append(int(char))
                elif char == '.':
                    row.append(None)
                elif char == '*':
                    row.append('*')
                elif char !='\n':
                    row.append(None)
            matrix.append(row)
    max_j = len(matrix)
    max_i = len(matrix[0])
    return matrix

if __name__=='__main__':
    if len(sys.argv) < 2:
        print("pass filename")
        sys.exit()
    else:
        filename = sys.argv[1]
    engine = parse_input(filename)
#    print(engine)
    print(solve(engine))
