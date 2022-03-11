import constants

from game.casting.cast import Cast
from game.casting.score import Score
from game.casting.cycle import Cycle
from game.scripting.script import Script
from game.scripting.control_actors import ControlActorsAction
from game.scripting.move_actors import MoveActorsAction
from game.scripting.handle_collisions import HandleCollisionsAction
from game.scripting.draw_actors import DrawActorsAction
from game.scripting.update_scores import UpdateScores
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.other.color import Color
from game.other.point import Point


def main():
    
    # create the cast
    cast = Cast()
    # create 2 cycles and 2 scores - wasd for the first, ijkl for the second
    for i in range(2):
        if not i:
            keymap = ['w', 'a', 's', 'd']
        else:
            keymap = ['i', 'j', 'k', 'l']
        cycle = Cycle(keymap)
        cycle.set_velocity(Point(0, - constants.CELL_SIZE))
        cast.add_actor("cycles", cycle)
        cast.add_actor("scores", Score())
   
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("update", UpdateScores())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()