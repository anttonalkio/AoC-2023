with open('input.txt', 'r') as f:
    lines = f.readlines()

time = int("".join([x for x in lines[0] if x.isdigit()]))
record = int("".join([x for x in lines[1] if x.isdigit()]))

ways_to_win = 0

for push_time in range(1, time):
    drive_time = time - push_time
    speed = push_time

    if(drive_time * speed > record):
        ways_to_win += 1

print(ways_to_win)