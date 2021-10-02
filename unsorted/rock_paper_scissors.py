def rules(shape_a, shape_b):
    shape_rules = {
        ('paper', 'rock'): 'paper',
        ('rock', 'scissor'): 'rock',
        ('paper', 'scissor'): 'scissor'
    }

    return shape_rules.get(
        tuple(sorted([shape_a, shape_b])), 'draw'
    )
import random


class Player:
    def __init__(self, shape):
        self.shape = shape
    
    def strategy_random(self):
        self.shape = random.choice(['rock', 'paper', 'scissor'])
        return self.shape
        

player_a = Player('rock')
player_b = Player('paper')

# assert rules(player_a, player_b) == 'paper'



games = [(player_a.strategy_random(), player_b.strategy_random()) for _ in range(10)]
results = [rules(a, b) for a, b in games]

print(results)