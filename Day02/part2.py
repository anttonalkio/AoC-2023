import re

class Game:
    def __init__(self, input):
        self.game_id = int(re.search(r'^Game (\d+):', input).group(1))
        self.sets = [[y for y in x.split(', ')] for x in input.split(':')[1].strip().split('; ')]
    
    def power(self):
        max_blues, max_reds, max_greens = 0, 0, 0
        
        for set in self.sets:
            blues = max([int(num) for num, col in [cube.split(' ') for cube in set] if col == 'blue'], default=0)
            max_blues = max(max_blues, blues)

            reds = max([int(num) for num, col in [cube.split(' ') for cube in set] if col == 'red'], default=0)
            max_reds = max(max_reds, reds)

            greens = max([int(num) for num, col in [cube.split(' ') for cube in set] if col == 'green'], default=0)
            max_greens = max(max_greens, greens)
            
        return max_blues * max_reds * max_greens

sum = 0

with open('input.txt', 'r') as f:
    lines = f.readlines()

    for line in lines:
        game = Game(line)

        sum += game.power()


print(sum)