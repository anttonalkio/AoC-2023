with open('input.txt', 'r') as f:
    line = f.read()

def hash(str):
    current_value = 0
    for c in str:
        current_value += ord(c)
        current_value = (current_value * 17) % 256
    return current_value

boxes = [{} for _ in range(256)]

steps = line.strip().split(',')

for step in steps:
    if '=' in step:
        label, value = step.split('=')
        step_hash = hash(label)
        boxes[step_hash][label] = int(value)
    
    if '-' in step:
        label = step.split('-')[0]
        step_hash = hash(label)
        if label in boxes[step_hash]:
            del boxes[step_hash][label]
        

focusing_power = 0

for i, box in enumerate(boxes, start=1):
    for j, lens in enumerate(box.items(), start=1):
        focusing_power += i * j * lens[1]

print(focusing_power)
