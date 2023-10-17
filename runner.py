from enum import Enum

"""
Position enum, used to indicate which position in a square that the curve
either begins or ends in.

An position enum value contains two cardinal directions: the first indicates
the side of the box, and the second indicates the half of the selected side.

For example, RIGHT_UP indicates the top half of the right side of the square:
   _ _
  |   | <-- RIGHT_UP
  |_ _|

"""
class Position(Enum):
  UNSPECIFIED = 0
  LEFT_UP = 1
  LEFT_DOWN = 2
  DOWN_LEFT = 3
  DOWN_RIGHT = 4
  RIGHT_DOWN = 5
  RIGHT_UP = 6
  UP_RIGHT = 7
  UP_LEFT = 8


ADJACENT_POSITION = {
  Position.LEFT_UP: Position.LEFT_DOWN, 
  Position.LEFT_DOWN: Position.LEFT_UP,
  Position.DOWN_LEFT: Position.DOWN_RIGHT,
  Position.DOWN_RIGHT: Position.DOWN_LEFT,
  Position.RIGHT_DOWN: Position.RIGHT_UP,
  Position.RIGHT_UP: Position.RIGHT_DOWN,
  Position.UP_RIGHT: Position.UP_LEFT,
  Position.UP_LEFT: Position.UP_RIGHT,
}

OPPOSITE_POSITION = {
  Position.LEFT_UP: Position.RIGHT_UP,
  Position.LEFT_DOWN: Position.RIGHT_DOWN,
  Position.DOWN_LEFT: Position.UP_LEFT,
  Position.DOWN_RIGHT: Position.UP_RIGHT,
  Position.RIGHT_DOWN: Position.LEFT_DOWN,
  Position.RIGHT_UP: Position.LEFT_UP,
  Position.UP_RIGHT: Position.DOWN_RIGHT,
  Position.UP_LEFT: Position.DOWN_LEFT,
}

class HCurve:
  def __init__(self, height, width, depth):
    self.height = height
    self.width = width
    self.depth = depth
    self.y_step = height // (2 ** depth)
    self.x_step = width // (2 ** depth)

  def test_steps(self, start: Position, end: Position):
    if end == ADJACENT_POSITION[start]:
      print("adjacent")
    elif end == OPPOSITE_POSITION[start]:
      print("opposite")
    else:
      print("invalid positions")


def main():
  h = HCurve(256, 256, 2)
  h.test_steps(Position.UP_LEFT, Position.UP_RIGHT)
  h.test_steps(Position.UP_LEFT, Position.DOWN_LEFT)
  h.test_steps(Position.UP_LEFT, Position.DOWN_RIGHT)


if __name__ == "__main__":
  main()
    

