# Priority Queue with binary heap
#       A(1)    
#      /   \
#     B(2)  C(3)  
#   /   \      \
#  D(4)  E(5)   F(7)

# if (say)parent = p 
# then left_child = 2 * p 
# and right_child = 2 * p + 1

class PriorityQueue():
  DEFAULT_CAPACITY = 100

  def __init__(self):
    self._data = [ None ] * PriorityQueue.DEFAULT_CAPACITY
    self._size = 0
      
  def __len__(self):
    return self._size

  def findmin(self):
    if self._size == 0:
      raise ValueError("empty priority queue")
    return self._data[1]  # O(1)

  def insert(self, x):
    if self._size + 1 == len(self._data):
      # double size of the array storing the data
      self._data.extend( [ None ] * len(self._data) )
    self._size += 1
    hole = self._size
    
    # bubble up
    while x < self._data[hole // 2]:
      # exchange the values of the child and the parent
      self._data[hole] = self._data[hole // 2]
      hole //= 2  # inspect the next parent
    self._data[hole] = x
    
  def deletemin(self):
    min_item = self.findmin()         # raises error if empty
    self._data[1] = self._data[self._size]
    self._size -= 1
    self._bubble_down(1)
    return min_item

  # 'ppp' exercise
  def _bubble_down(self, i):
    value = self._data[i]
    hole = i
    child = self._smaller_child(hole, value)
    while child != 0:
      self._data[hole] = self._data[child]
      hole = child
      child = self._smaller_child(hole, value)
    self._data[hole] = value

  # 'ppp' exercise
  # Is one child smaller than element's value?
  # Returns the index of the smaller child, or 0 if no child is smaller
  def _smaller_child(self, index, value):
    child = 2 * index
    if child <= self._size:
      if child != self._size and self._data[child + 1] < self._data[child]:
        child += 1
      if self._data[child] < value:
        return child
    return 0
  
