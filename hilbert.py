import random


class HNode():
  def __init__(row: int, col: int, index: int):
    self.row = row
    self.col = col
    self.index = index


class HList():
  def __init__():
    self.nodes = []

  def append_node(node: HNode):
    self.nodes.append(node)

  def add_node(row: int, col: int):
    index = len(self.nodes)
    self.nodes.append(HNode(row, col, index))


def pregenerated_depth_1():
  return [(0, 0), (127, 0), (127, 127), (0, 127)]

def pregenerated_depth_2():
  return [
    (  0,   0), (  0,  63), ( 63,  63), ( 63,   0), 
    (127,   0), (191,   0), (191,  63), (127,  63), 
    (127, 127), (191, 127), (191, 191), (127, 191), 
    ( 63, 191), ( 63, 127), (  0, 127), (  0, 191), 
  ]

def pregenerated_depth_3():
  return []  # TODO

def create_space_256():
  space = []
  for _ in range(256):
    space.append([0] * 256)

def generate_points(space, count):
  for _ in range(count):
    row = random.randrange(len(space))
    col = random.randrange(len(space[0]))
    space[row][col] = str(row) + ", " + str(col)
  
generate_points(space, 20)

def print_nonzero(space):
  for row in space:
    for val in row:
      if val != 0:
        print(val)

