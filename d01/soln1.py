import sys

def calibration_values(input_str):
    c_nums = []
    for line in input_str.split("\n"):
        if not line:
            continue
        line_nums = [0, 0]
        first_digit = False
        for c in line:
            if c.isdigit():
                if not first_digit:
                    line_nums[0] = c
                    first_digit = True
                else:
                    line_nums[1] = c
        if line_nums[1] == 0:
            line_nums[1] = line_nums[0]
        print(line_nums)
        c_nums.append(int(line_nums[0]+ '' + line_nums[1]))
    return c_nums

def read_input(filename):
    with open(filename) as fp:
        input_str = fp.read()
    return input_str

def get_soln(filename):
    inp = read_input(filename)
    vals = calibration_values(inp)
    return sum(vals)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("pass filename")
        sys.exit()
    else:
        filename = sys.argv[1]

    print(get_soln(filename))
