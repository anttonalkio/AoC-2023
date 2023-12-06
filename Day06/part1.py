from collections import defaultdict
from functools import reduce

with open('input.txt', 'r') as f:
    lines = f.readlines()

times = [int(x) for x in lines[0].strip().split(' ')[1:] if x != '']
records = [int(x) for x in lines[1].strip().split(' ')[1:] if x != '']

ways_to_win = defaultdict(int)

for time, record in zip(times, records):
    for push_time in range(1, time):
        drive_time = time - push_time
        speed = push_time

        if(drive_time * speed > record):
            ways_to_win[time] += 1

print(reduce((lambda x, y: x * y), ways_to_win.values()))