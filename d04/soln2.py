import sys
from collections import Counter
from itertools import chain

def parse_input(filename):
    cards = {}
    with open(filename) as fp:
        for line in fp:
            card_num = int(line.split(":")[0].split(" ")[-1])
            numbers = line.split(":")[-1].strip().split("|")
            clean_num = lambda x: int(x.strip()) if x else None
            winning = list(map(clean_num, numbers[0].strip().split(" ")))
            actual = list(filter(lambda x: x is not None, map(clean_num, numbers[1].strip().split(" "))))
            cards[card_num] = (winning, set(actual))
    return cards

def n_matches(card):
    n_matches = 0
    for num in card[1]:
        if num in card[0]:
            n_matches += 1
    return n_matches

def calc_card_numbers(card_num, card):
    matches = n_matches(card)
    new_cards = list(range(card_num+1, card_num+1+matches))
    return new_cards

def solve(cards):
    counts = {k: 1 for k in cards.keys()}
    for k in counts:
        inc_cards = calc_card_numbers(k, cards[k])
        for card_num in inc_cards:
            counts[card_num] += counts[k]
    return sum(counts.values())

if __name__=='__main__':
    if len(sys.argv) < 2:
        print("pass filename")
        sys.exit()
    else:
        filename = sys.argv[1]
    cards = parse_input(filename)
    print(solve(cards))
