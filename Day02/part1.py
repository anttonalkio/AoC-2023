import re

class Game:
    def __init__(self, input, limits: dict):
        self.limits = limits
        self.game_id = int(re.search(r'^Game (\d+):', input).group(1))
        self.sets = [[y for y in x.split(', ')] for x in input.split(':')[1].strip().split('; ')]
    
    def is_possible(self) -> bool:
        for set in self.sets:
            for color, count in self.limits.items():
                if count < sum([int(num) for num, col in [cube.split(' ') for cube in set] if col == color]):
                    return False
                  
        return True

ids = []

with open('input.txt', 'r') as f:
    lines = f.readlines()

    for line in lines:
        game = Game(line, {'red': 12, 'green': 13, 'blue': 14})

        if game.is_possible():
             ids.append(game.game_id)


print(sum(ids))