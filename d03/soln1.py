import sys

max_j = 0
max_i = 0

def is_special(ind):
    return isinstance(ind, str) and ind == '*'

def check_part(engine, start, end, row):
    surrounding = []
    if row > 0:
        surrounding.append(row-1)
    if row < max_j-1:
        surrounding.append(row+1)

    horz = list(range(start, end+1))
    if start > 0:
        horz.append(start-1)
        if is_special(engine[row][start-1]):
            return True
    if end < max_i-1:
        horz.append(end+1)
        if is_special(engine[row][end+1]):
            return True
    for i in horz:
        for j in surrounding:
            if is_special(engine[j][i]):
                return True
    return False

def toNum(parts):
    new_parts = []
    for num in parts:
        new_num = int("".join(map(str, num)))
        new_parts.append(new_num)
    return new_parts

def solve(engine):
    parts = []
    for j, row in enumerate(engine):
#        print(j)
        start = None
        end = None
        for i, checkpoint in enumerate(row):
#            print(i, checkpoint)
            if isinstance(checkpoint, int):
                if start is None:
                    start = i
                end = i
            else:
                if start is not None and end is not None:
                    if check_part(engine, start, end, j):
                        parts.append(row[start:end+1])
                    start, end = None, None
        if start is not None and end is not None:
            if check_part(engine, start, end, j):
                parts.append(row[start:end+1])
            start, end = None, None
    parts = toNum(parts)
#    print(parts)
    return sum(parts)

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
                elif char !='\n':
                    row.append('*')
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
