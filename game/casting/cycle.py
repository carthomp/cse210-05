import constants
from game.casting.actor import Actor
from game.other.point import Point


class Cycle(Actor):
    """
    A long limbless reptile.
    
    The responsibility of Snake is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self, keymap):
        super().__init__()
        self._segments = []
        self._keymap = keymap
        self._prepare_body()
    
    def get_keymap(self):
        return self._keymap

    def get_segments(self):
        return self._segments

    def move_next(self):
        # move all segments
        for segment in self._segments:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_head(self):
        return self._segments[0]

    def grow_tail(self, number_of_segments):
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            if self._keymap[0] == 'w':
                segment.set_color(constants.GREEN)
            else:
                segment.set_color(constants.PURPLE)
            self._segments.append(segment)

    def turn_head(self, velocity):
        self._segments[0].set_velocity(velocity)
    
    def _prepare_body(self):
        if self._keymap[0] == 'w':
            x = int(constants.MAX_X / 4)
        else:
            x = int(3 * constants.MAX_X / 4)
        y = int(constants.MAX_Y / 2)

        
        position = Point(x, y)
        velocity = Point(0, 1 * constants.CELL_SIZE)
        text = "8"
        if self._keymap[0] == 'w':
            color = constants.YELLOW
        else:
            color = constants.BLUE
            
        segment = Actor()
        segment.set_position(position)
        segment.set_velocity(velocity)
        segment.set_text(text)
        segment.set_color(color)
        self._segments.append(segment)