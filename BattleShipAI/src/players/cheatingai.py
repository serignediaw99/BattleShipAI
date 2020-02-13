from typing import List

from BattleShipAI.src import move, game_config, cell
from BattleShipAI.src.player import Player
from BattleShipAI.src.players.ai_player import AIPlayer


class CheatingAI(AIPlayer):
    def __init__(self, player_num: int, config: game_config.GameConfig, other_players: List["Player"]) -> None:
        super().__init__(player_num, config, other_players)

    def init_name(self, player_num: int, other_players: List["Player"]) -> None:
        self.name = f"Cheating AI {player_num}"

    def get_move(self) -> move.Move:
        opponent = self.opponents[0]
        for row_index in range(self.board.num_rows):
            for col_index in range(self.board.num_cols):
                if not opponent.board.has_been_fired_at(row_index, col_index):
                    if opponent.board.contents[row_index][col_index] != "*":
                        row = str(row_index)
                        col = str(col_index)
                        str_coords = row + ',' + col
        firing_location = move.Move.from_str(self, str_coords)
        return firing_location


