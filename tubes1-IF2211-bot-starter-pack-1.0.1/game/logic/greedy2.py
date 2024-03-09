# Nama : Jimly Nur Arif
# NIM  : 13522123
# Institut Teknologi Bandung

# import random
from typing import Optional

from game.logic.base import BaseLogic
from game.models import GameObject, Board, Position
from ..util import get_direction


class heran(BaseLogic):
    def __init__(self):
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.goal_position: Optional[Position] = None
        self.current_direction = 0


        
    def nearest_distance(self, board_bot: GameObject, board: Board):
        radius_from_base = 18
        nearest_distance = 1000
        current_position = board_bot.position

        reset_button_position = [d for d in board.game_objects if d.type == "DiamondButtonGameObject"][0].position
        nearest_diamond_coord = reset_button_position

        for diamondsWillTake in board.diamonds:
            delta_x = abs(diamondsWillTake.position.x - board_bot.properties.base.x)
            delta_y = abs(diamondsWillTake.position.y - board_bot.properties.base.y)
            if (delta_x + delta_y) <= radius_from_base:

                delta_x = abs(current_position.x - diamondsWillTake.position.x)
                delta_y = abs(current_position.y - diamondsWillTake.position.y)
                if (delta_x + delta_y) <= nearest_distance :
                    if diamondsWillTake.properties.points == 2 and board_bot.properties.diamonds == 4:
                        continue
                    else:
                        nearest_distance = delta_x + delta_y
                        nearest_diamond_coord = diamondsWillTake.position

        if board_bot.properties.diamonds == 4 and nearest_diamond_coord == reset_button_position:
            # back to base, because we already 4 diamonds and there is no blue diamond in radius
            nearest_diamond_coord = board_bot.properties.base

        return nearest_diamond_coord
    
    def next_move(self, board_bot: GameObject, board: Board):
        props = board_bot.properties

        # Uncomment to see various condition about the bot and board 
        # for x in board.diamonds:
        #     print(x.position)
        nearest_diamond = self.nearest_distance(board_bot, board)
        # print("\nstart\n")
        # print(nearest_diamond, "bot", board_bot.position, "endbot")
        # print("\nend\n")
        # print("base", board_bot.properties.base)  #Base(y=3, x=7)
        # print("delay", board.minimum_delay_between_moves)

        # print("milisecond", board_bot.properties.milliseconds_left) 
        time_left = board_bot.properties.milliseconds_left

        base_distance = abs(board_bot.position.x - board_bot.properties.base.x) + abs(board_bot.position.y - board_bot.properties.base.y)

        # Assuming 1 move takes 0.25 second
        time_back_base = base_distance * 250

        # Analyze new state
        if props.diamonds == 5 or time_left <= time_back_base + 500:
            # Move to base
            delta_x, delta_y = get_direction(
                board_bot.position.x,
                board_bot.position.y,
                board_bot.properties.base.x,
                board_bot.properties.base.y,
            )

        else:
            delta_x, delta_y = get_direction(
                board_bot.position.x,
                board_bot.position.y,
                nearest_diamond.x,
                nearest_diamond.y,
            )
        return delta_x, delta_y