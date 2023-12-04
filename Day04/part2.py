scores = []
cards = []

with open('input.txt', 'r') as f:
    lines = f.readlines()

    scores = [1 for _ in range(len(lines))]

    for line in lines:
        winning, mine = line.split(': ')[1].split('|')
        winning = [int(r.strip()) for r in winning.strip().split()]
        mine = [int(r.strip()) for r in mine.strip().split()]

        cards.append([winning, mine])

for id, card in enumerate(cards):            
    winning, mine = card
    both = set(mine).intersection(winning)

    if len(both) > 0:
        for i in range(1, len(both) + 1):
            scores[id + i] += scores[id]

print(sum(scores))