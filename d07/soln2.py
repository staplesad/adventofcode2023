import math
import sys
from collections import Counter
card_order = "AKQT98765432J"


def parse_input(filename):
    hands = []
    bids = []
    with open(filename) as fp:
        for line in fp:
            hand, bid = line.strip().split(" ")
            hands.append(hand)
            bids.append(bid)
    return (hands, bids)

def max_card(hand):
    strengths = list(map(lambda x: card_order.index(x), list(hand)))
    return strengths

def classify_hand(hand):
    counts = Counter(hand)
    new_counts = dict(counts)
    if 'J' in new_counts:
        n_j = new_counts.pop('J')
        best_card = counts.most_common()[0][0]
        if best_card == 'J':
            if n_j == 5:
                best_card='K'
                new_counts[best_card] = 0
            else:
                best_card =counts.most_common()[1][0]
        new_counts[best_card]+=n_j
    print(hand, new_counts)
    if sorted(list(new_counts.values())) == [5]:
        order = 1
    elif sorted(list(new_counts.values())) == [1, 4]:
        order = 2
    elif sorted(list(new_counts.values())) == [2, 3]:
        order = 3
    elif sorted(list(new_counts.values())) == [1, 1, 3]:
        order = 4
    elif sorted(list(new_counts.values())) == [1, 2, 2]:
        order = 5
    elif sorted(list(new_counts.values())) == [1, 1, 1, 2]:
        order = 6
    else:
        order = 7
    return order

def rank_hands(hands):
    overall_rank = map(lambda x: (classify_hand(x), max_card(x)), hands)
    ranking_tuple = [(r, i) for i, r in enumerate(overall_rank)]
    for a in sorted(ranking_tuple):
        print(a, hands[a[-1]])
    return [t[-1] for t in sorted(ranking_tuple)]

def solve(hands, bids):
    # list of input indices ordered by rank
    ranks = rank_hands(hands)
    amounts = []
    for i, bid in enumerate(bids):
        rank = len(ranks) - ranks.index(i)
        amounts.append(int(bid)*rank)
    return sum(amounts)

if __name__=='__main__':
    if len(sys.argv) < 2:
        print("pass filename")
        sys.exit()
    else:
        filename = sys.argv[1]
    data = parse_input(filename)
    print(data)
    print(solve(*data))
