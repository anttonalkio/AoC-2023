with open('input.txt', 'r') as f:
    line = f.read()

def hash(str):
    current_value = 0
    for c in str:
        current_value += ord(c)
        current_value = (current_value * 17) % 256
    return current_value

steps = line.strip().split(',')

print(sum([hash(step) for step in steps]))