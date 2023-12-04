score = 0

with open('input.txt', 'r') as f:
    lines = f.readlines()

    for line in lines:
        winning, mine = line.split(': ')[1].split('|')
        winning = [int(r.strip()) for r in winning.strip().split()]
        mine = [int(r.strip()) for r in mine.strip().split()]

        both = set(mine).intersection(winning)

        if len(both) > 0:
            score += 1 * 2 ** (len(both) - 1)

print(score)