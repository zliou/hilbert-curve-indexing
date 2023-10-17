from enum import Enum

"""
Direction enum, used to indicate which position in a square that the curve
either begins or ends in.

An enum name contains two cardinal directions: the first indicates the side
of the box, and the second indicates the half of the selected side.

For example, RIGHT_UP indicates the top half of the right side of the square:
   _ _
  |   | <-- RIGHT_UP
  |_ _|

"""
class Direction(Enum):
  UNSPECIFIED = 0
  LEFT_UP = 1
  LEFT_DOWN = 2
  DOWN_LEFT = 3
  DOWN_RIGHT = 4
  RIGHT_DOWN = 5
  RIGHT_UP = 6
  UP_RIGHT = 7
  UP_LEFT = 8

