import re

with open('input.txt', 'r') as f:
    lines = f.readlines()

    numbers = []

    for line in lines:
        stripped = re.sub("[^0-9]", "", line)
        result = int(stripped[0] + stripped[-1])
        numbers.append(result)

    print(sum(numbers))