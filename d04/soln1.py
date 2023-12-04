import sys

def parse_input(filename):
    cards = []
    with open(filename) as fp:
        for line in fp:
            numbers = line.split(":")[-1].strip().split("|")
            clean_num = lambda x: int(x.strip()) if x else None
            winning = list(map(clean_num, numbers[0].strip().split(" ")))
            actual = list(filter(lambda x: x is not None, map(clean_num, numbers[1].strip().split(" "))))
            cards.append((winning, set(actual)))
    return cards

def calc_points(card):
    n_matches = 0
    for num in card[1]:
        if num in card[0]:
            n_matches += 1
    return 2**(n_matches-1) if n_matches > 0 else 0

def solve(cards):
    points = []
    for card in cards:
        points.append(calc_points(card))
    print(points)
    return sum(points)

if __name__=='__main__':
    if len(sys.argv) < 2:
        print("pass filename")
        sys.exit()
    else:
        filename = sys.argv[1]
    cards = parse_input(filename)
    print(solve(cards))
