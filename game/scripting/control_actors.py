import constants
from game.scripting.action import Action
from game.other.point import Point


class ControlActorsAction(Action):
    """
    An input action that controls the snake.
    
    The responsibility of ControlActorsAction is to get the direction and move the snake's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction = Point(constants.CELL_SIZE, 0)

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        cycles = cast.get_actors("cycles")
        for i in range(2):
            cycle = cycles[i]
            keymap = cycle.get_keymap()
            # left
            if self._keyboard_service.is_key_down(keymap[1]):
                self._direction = Point(-constants.CELL_SIZE, 0)
            
            # right
            if self._keyboard_service.is_key_down(keymap[3]):
                self._direction = Point(constants.CELL_SIZE, 0)
            
            # up
            if self._keyboard_service.is_key_down(keymap[0]):
                self._direction = Point(0, -constants.CELL_SIZE)
            
            # down
            if self._keyboard_service.is_key_down(keymap[2]):
                self._direction = Point(0, constants.CELL_SIZE)

            cycle.turn_head(self._direction)