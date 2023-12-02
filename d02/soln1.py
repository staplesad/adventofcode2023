import sys

known_totals = {'r': 12, 'g': 13, 'b': 14}

def parse_round(cube_string):
    colours = cube_string.split(",")
    colours = [c.strip().split(" ") for c in colours]
    colours = [(int(n), c[0]) for n, c in colours]
    return colours

def parse_input(filename):
    games = []
    with open(filename) as fp:
        for line in fp:
            all_cubes = line.split(":")[1]
            seq = all_cubes.split(";")
            tuples = list(map(parse_round, seq))
            #print(tuples)
            games.append(tuples)
    return games

def compare_totals(game):
    for rnd in game:
        for occ, col in rnd:
            if occ > known_totals[col]:
                return True
    return False

def solve(games):
    possible_ids = []
    for i, game in enumerate(games):
        if not compare_totals(game):
            possible_ids.append(i+1)
    print(possible_ids)
    return sum(possible_ids)

if __name__=='__main__':
    if len(sys.argv) < 2:
        print("pass filename")
        sys.exit()
    else:
        filename = sys.argv[1]
    games = parse_input(filename)
    print(solve(games))
