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

ranks = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']

def compare(hand1, hand2):
    for x in range(6):
        if ranks.index(hand1[0][x]) < ranks.index(hand2[0][x]):
            return -1
        if ranks.index(hand1[0][x]) > ranks.index(hand2[0][x]):
            return 1
    return 0

for line in lines:
    hand, bid = line.strip().split(' ')
    groups = Counter(hand)

    if any(letter for letter,count in groups.items() if count == 5):
        kinds['five-of-kind'].append((hand, int(bid)))
        continue

    if any(letter for letter,count in groups.items() if count == 4):
        kinds['four-of-kind'].append((hand, int(bid)))
        continue

    if len(groups) == 2:
        kinds['full-house'].append((hand, int(bid)))
        continue

    if any(letter for letter,count in groups.items() if count == 3):
        kinds['three-of-kind'].append((hand, int(bid)))
        continue

    if len(groups) == 3:
        kinds['two-pairs'].append((hand, int(bid)))
        continue

    if len(groups) == 4:
        kinds['one-pair'].append((hand, int(bid)))
        continue

    if len(groups) == 5:
        kinds['high-card'].append((hand, int(bid)))
        continue

    raise Exception(f'Hand not recognized: {hand}')


#print(kinds)
final_ranks = []
for key in kinds.keys():
    final_ranks.extend(sorted(kinds[key], key=functools.cmp_to_key(compare)))

#sorted_l = sorted(kinds['two-pairs'], key=functools.cmp_to_key(compare))

print(sum(x[1] * i for i, x in enumerate(final_ranks, start=1)))

#print(final_ranks)