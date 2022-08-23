from ai import AI
from gameTest import Creature
from random import choice
from time import perf_counter

t = perf_counter()
creatureNum = 4
tf = [True, False]
creatures = [Creature(choice(tf), choice(tf), choice(tf), choice(tf))\
     for ii in range(creatureNum)]
ai = AI(creatures)
print(AI.optimizeBruteForce(ai.graph))
print(f'Total time: {perf_counter()-t}')