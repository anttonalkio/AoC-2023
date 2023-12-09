
def diff_adjacent_elements(lst) -> list[int]:
    return list(map(lambda x, y: y - x, lst[:-1], lst[1:]))


with open('input.txt', 'r') as f:
    lines = f.readlines()

sum = 0

for line in lines:
    line = list(map(int, line.strip().split()))
    all_zeros = False

    steps = [line]
    while(all_zeros == False):
        diff = diff_adjacent_elements(steps[-1])
        steps.append(diff)

        if(all(v == 0 for v in diff)):
            all_zeros = True
            break

    steps = list(reversed(steps))

    for i, step in enumerate(steps):
        if(i == 0):
            step.append(0)
            continue

        step.append(step[-1] + steps[i - 1][-1])

    sum += steps[-1][-1]

print(sum)

    