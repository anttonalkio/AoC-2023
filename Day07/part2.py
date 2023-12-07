from collections import Counter
import functools

with open('input.txt', 'r') as f:
    lines = f.readlines()

kinds = {
    'high-card': [],
    'one-pair': [],
    'two-pairs': [],
    'three-of-kind': [],
    'full-house': [],
    'four-of-kind': [],
    'five-of-kind': []
}

ranks = ['J','2','3','4','5','6','7','8','9','T','Q','K','A']

def best_hand(hand: str):
    groups = Counter(hand)

    highest_kind = 8
    highest_kind_hand = 'five-of-kind'
    
    for c in [x for x in groups.keys() if x != 'J']:
        subtituted = hand.replace('J', c)

        prio, kind = hand_category(subtituted)

        if prio < highest_kind:
            highest_kind = prio
            highest_kind_hand = kind

    return highest_kind_hand

def hand_category(hand):
    groups = Counter(hand)

    if any(letter for letter,count in groups.items() if count == 5):
        return (1, 'five-of-kind')

    if any(letter for letter,count in groups.items() if count == 4):
        return (2,'four-of-kind')

    if len(groups) == 2:
        return (3,'full-house')

    if any(letter for letter,count in groups.items() if count == 3):
        return (4,'three-of-kind')

    if len(groups) == 3:
        return (5,'two-pairs')

    if len(groups) == 4:
        return (6,'one-pair')

    if len(groups) == 5:
        return (7,'high-card')

    raise Exception(f'Hand not recognized: {hand}')

def compare(hand1, hand2):
    for x in range(6):
        if ranks.index(hand1[0][x]) < ranks.index(hand2[0][x]):
            return -1
        if ranks.index(hand1[0][x]) > ranks.index(hand2[0][x]):
            return 1
    return 0

for line in lines:
    hand, bid = line.strip().split(' ')
    if('J' in hand):
        kind = best_hand(hand)
    else:
        _, kind = hand_category(hand)
    
    kinds[kind].append((hand, int(bid)))


final_ranks = []
for key in kinds.keys():
    final_ranks.extend(sorted(kinds[key], key=functools.cmp_to_key(compare)))

print(sum(x[1] * i for i, x in enumerate(final_ranks, start=1)))
