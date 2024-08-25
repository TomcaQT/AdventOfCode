from operator import itemgetter
from collections import Counter
import re
from tqdm import tqdm

c = {
    "A" : 14,
    "K" : 13,
    "Q" : 12,
    "J" : 1,
    "T" : 10,}
c.update({str(i):i for i in range(2,10)})

def get_comb(card):
    #print(card)
    cnt = Counter(card)
    jokers = cnt.get('J', 0)
    del cnt['J']
    if card == "JJJJJ":
        return 100
    x = cnt.most_common(5)

    cnt[x[0][0]] = x[0][1] + jokers
    return get_val_from_counter(cnt.most_common(5))



def get_val_from_counter(x):
    if len(x) == 1:
        return 100
    elif len(x) == 2:
        return 90 if x[0][1] == 4 else 80
    elif len(x) == 3:
        return 70 if x[0][1] == 3 else 60
    elif len(x) == 4:
        return 50
    else:
        return 10

def get_value(card):
    value = [get_comb(card)]
    [value.append(c.get(x)) for x in card]
    return value




def solve(data):
    total = 0
    cards = [get_value(card) + [card, bid] for card, bid in data]
    sorted_cards = sorted(cards, key=itemgetter(0,1,2,3,4,5))
    print(sorted_cards)
    total_win = sum([(i+1)*int(card[-1])for i, card in enumerate(sorted_cards)])
    print(total_win)

def read_file():
    with open('data/7.in', 'r') as f:
        return [tuple(l.strip().split(' ')) for l in f.readlines()]


if __name__ == '__main__':
    data = read_file()
    solve(data)