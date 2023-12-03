import sys

all_digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def find_number(line):
    running_number = ""
    for c in line:
        if c.isdigit():
            return c
        else:
            running_number += c
            while not any(d.startswith(running_number) for d in all_digits):
                running_number = running_number[1:]
            if any(d == running_number for d in all_digits):
                return str(all_digits.index(running_number) + 1)
    return 0

def find_rev_number(line):
    running_number = ""
    for c in line:
        if c.isdigit():
            return c
        else:
            running_number += c
            while not any(d.endswith(running_number[::-1]) for d in all_digits):
                running_number = running_number[1:]
            if any(d == running_number[::-1] for d in all_digits):
                return str(all_digits.index(running_number[::-1]) + 1)
    return 0


def calibration_values(input_str):
    c_nums = []
    for line in input_str.split("\n"):
        if not line:
            continue
        first = find_number(line)
        second = find_rev_number(line[::-1])
        print(first, second)
        c_nums.append(int(first + second))
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
