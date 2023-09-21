from collections import defaultdict
import random


class HNode():
  def __init__(self, space, row: int, col: int, index: int, size: int):
    self.space = space
    self.row = row
    self.col = col
    self.index = index
    self.size = size

  def get_elements(self):
    elements = []
    for row in range(self.row, self.row + self.size):
      for col in range(self.col, self.col + self.size):
        if self.space[row][col] != 0:
          elements.append(self.space[row][col])
    return elements


class HList():
  def __init__(self, space, node_size: int):
    self.space = space
    self.nodes = []
    self.node_size = node_size
    self.indexes = defaultdict()

  def add_node(self, row: int, col: int):
    index = len(self.nodes)
    self.indexes[(row, col)] = index
    self.nodes.append(HNode(self.space, row, col, index, self.node_size))

  def size_floor(self, x: int, node_size: int):
    return x - (x % node_size)
  
  def calculate_node_root(self, row: int, col: int):
    return (self.size_floor(row, self.node_size), self.size_floor(col, self.node_size))
  
  def search_near(self, row: int, col: int, scope: int):
    node_root = self.calculate_node_root(row, col)
    node_index = self.indexes[node_root]
    results = []
    for i in range(max(node_index - scope, 0), min(len(self.nodes), node_index + 2)):
      results.extend(self.nodes[i].get_elements())
    return results


def pregenerated_depth_1():
  return [(0, 0), (128, 0), (128, 128), (0, 128)]

def pregenerated_depth_2():
  return [
    (  0,   0), (  0,  64), ( 64,  64), ( 64,   0), 
    (128,   0), (192,   0), (192,  64), (128,  64), 
    (128, 128), (192, 128), (192, 192), (128, 192), 
    ( 64, 192), ( 64, 128), (  0, 128), (  0, 192), 
  ]

def pregenerated_depth_3():
  return []  # TODO

def create_space_256():
  space = []
  for _ in range(256):
    space.append([0] * 256)
  return space

def generate_points(space, count):
  for _ in range(count):
    row = random.randrange(len(space))
    col = random.randrange(len(space[0]))
    space[row][col] = str(row) + ", " + str(col)
  
def print_nonzero(space):
  for row in space:
    for val in row:
      if val != 0:
        print(val)

def main():
  # Setup & construct HList.
  space = create_space_256()
  points = pregenerated_depth_2()
  depth_2_node_size = 64
  hlist = HList(space, depth_2_node_size)
  
  # Add nodes into HList.
  for row, col in points:
    hlist.add_node(row, col)

  # Generate points in the 2D space.
  generate_points(space, 100)
  
  # Search and print results.
  search_row = 90
  search_col = 12
  search_h_width = 3
  print("Results near (90, 12):")
  for result in hlist.search_near(search_row, search_col, search_h_width):
    print(result)
 

if __name__ == "__main__":
  main()


