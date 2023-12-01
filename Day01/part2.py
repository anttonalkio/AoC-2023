import re

mappings = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four' : '4',
    'five' : '5',
    'six' : '6',
    'seven' : '7',
    'eight' : '8',
    'nine' : '9'
}

def normalize(s):
    if len(s) == 1:
        return s
    
    return mappings[s]

numbers = []

with open('input.txt', 'r') as f:
    lines = f.readlines()

    for line in lines:
        leftmost = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', line)
        rightmost = re.findall(r'\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin', "".join(reversed(line)))

        final = int(normalize(leftmost[0]) + normalize("".join(reversed(rightmost[0]))))

        numbers.append(final)

print(sum(numbers))