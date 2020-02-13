import sys
from BattleShipAI.src import game
import random

#arg_2 = int(sys.argv[2])

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Not enough arguments given.')
    else:
        game_of_battle_ship = game.Game(sys.argv[1])
        game_of_battle_ship.play()
