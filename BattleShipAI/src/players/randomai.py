from typing import List

from BattleShipAI.src import move, game_config
from BattleShipAI.src.player import Player
from BattleShipAI.src.players.ai_player import AIPlayer


class RandomAI(AIPlayer):
    def __init__(self, player_num: int, config: game_config.GameConfig, other_players: List["Player"]) -> None:
        super().__init__(player_num, config, other_players)

    def init_name(self, player_num: int, other_players: List["Player"]) -> None:
        self.name = f"Random AI {player_num}"

    def get_move(self) -> move.Move:
        pass