from collections import defaultdict
from heapq import heapify, heappop
import math
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

def pythagorean_search(space, row: int, col: int, radius: int):
  min_heap = []
  for r in range(len(space)):
    for c in range(len(space[0])):
      if space[r][c] == 0:
        continue
      dist = math.hypot(abs(row - r), abs(col - c))
      min_heap.append((dist, space[r][c]))
  heapify(min_heap)
  results = []
  while min_heap:
    dist, point = heappop(min_heap)
    if dist > radius:
      break
    else:
      results.append(point)
  return results


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
  hilbert_results = hlist.search_near(search_row, search_col, search_h_width)
  print("Hilbert results near (90, 12): (" \
        + str(len(hilbert_results)) + ") results")
  for result in hilbert_results:
    print(result)

  # Compare to Pythagorean/heap results.
  # We use a radius of 64 because it's 1.5 node_sizes.
  pythagorean_results = pythagorean_search(space, search_row, search_col, 96)
  print("Pythagorean results near (90, 12): (" \
        + str(len(pythagorean_results)) + ") results")
  for result in pythagorean_results:
    print(result)
  pythagorean_set = set(pythagorean_results)
  hilbert_set = set(hilbert_results)
  matches = hilbert_set & pythagorean_set
  print("Similarities: (" + str(len(matches)) + ") results")
  for point in matches:
    print(point)


  


if __name__ == "__main__":
  main()

