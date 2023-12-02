import sys

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

def get_maxes(game):
    totals = {'r': 0, 'g':0, 'b':0}
    for rnd in game:
        for occ, col in rnd:
            if occ > totals[col]:
                totals[col] = occ
    return totals

def solve(games):
    powers = []
    for i, game in enumerate(games):
        maxes = get_maxes(game)
        power = maxes['r'] * maxes['g'] * maxes['b']
        powers.append(power)
    print(powers)
    return sum(powers)

if __name__=='__main__':
    if len(sys.argv) < 2:
        print("pass filename")
        sys.exit()
    else:
        filename = sys.argv[1]
    games = parse_input(filename)
    print(solve(games))
