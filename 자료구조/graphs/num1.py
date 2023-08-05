#find union
class DisjointSets:
  """
  >>> ds = DisjointSets(10)
  >>> ds.union(1, 2)
  >>> ds.union(2, 5)
  >>> ds.union(5, 6)
  >>> ds.union(6, 7)
  >>> ds.union(3, 8)
  >>> ds.union(8, 9)
  >>> ds.connected(1, 5)
  True
  >>> ds.connected(5, 7))
  True
  >>> ds.connected(4, 9)
  False
  >>> ds.union(9, 4)
  >>> ds.connected(4, 9)
  True
  """
  def __init__(self, size):
    self.root = [i for i in range(size)]

  def find(self, x):  # returns the root of x; O(1)
    return self.root[x]
  
  def connected(self, x, y):  # O(1)
    return self.find(x) == self.find(y)
  
  # 'ppp' exercise
  def union(self, x, y):  # O(N)
    # check the roots of x and y
    # if they do not match, update the roots
    root_x = self.find(x)  # self.root[x]
    root_y = self.find(y)
    if root_x != root_y:
      for i in range(len(self.root)):
        if self.root[i] == root_y:
          self.root[i] = root_x

#quick find
class DisjointSets:
  
  def __init__(self, size):
    self.root = [i for i in range(size)]

  # 'ppp' exercise
  def find(self, x):  # < O(N)
    while x != self.root[x]:
      x = self.root[x]
    return x
  
  # 'ppp' exercise
  def union(self, x, y):  # < O(N)
    root_x = self.find(x)
    root_y = self.find(y)
    if root_x != root_y:
      self.root[root_y] = root_x

  def connected(self, x, y):  # < O(N)
    return self.find(x) == self.find(y)

#Union by rank
class DisjointSets:
  
  def __init__(self, size):
    self.root = [i for i in range(size)]
    self.rank = [1] * size

  def find(self, x):  # O(log N)
    while x != self.root[x]:
      x = self.root[x]
    return x
  
  def connected(self, x, y):  # O(log N)
    return self.find(x) == self.find(y)

  def union(self, x, y):  # O(log N)
    root_x = self.find(x)
    root_y = self.find(y)
    if root_x != root_y:
      if self.rank[root_x] > self.rank[root_y]:
        self.root[root_y] = root_x
      elif self.rank[root_x] < self.rank[root_y]:
        self.root[root_x] = root_y
      else:  # x and y have the same rank
        self.root[root_y] = root_x
        self.rank[root_x] += 1


class DisjointSets:
  def __init__(self, size):
    self.root = [i for i in range(size)]

  # 'ppp' exercise
  # 5 <- 4 <- 3 <- 2 <- 1 (linked list > tree)
  # ind : [1, 2, 3, 4, 5]
  # root: [2, 3, 4, 5, 5]
  # find: [5, 5, 5, 5, 5]
  def find(self, x):
    if x == self.root[x]:
      return x
    self.root[x] = self.find(self.root[x])
    return self.root[x]
  
  def union(self, x, y):
    root_x = self.find(x)
    root_y = self.find(y)
    if root_x != root_y:
      self.root[root_y] = root_x

  def connected(self, x, y):
    return self.find(x) == self.find(y)
  
class DisjointSets:
  def __init__(self, size):
    self.root = [i for i in range(size)]
    # Use a rank array to record the height of each vertex,
    # i.e., the "rank" of each vertex.
    # The initial "rank" of each vertex is 1, because each of them is
    # a standalone vertex with no connection to other vertices.
    self.rank = [1] * size

  # The find function here is the same as
  # that in the disjoint set with path compression.
  def find(self, x):
    if x == self.root[x]:
      return x
    self.root[x] = self.find(self.root[x])
    return self.root[x]

  # The union function with union by rank
  def union(self, x, y):
    root_x = self.find(x)
    root_y = self.find(y)
    if root_x != root_y:
      if self.rank[root_x] > self.rank[root_y]:
        self.root[root_y] = root_x
      elif self.rank[root_x] < self.rank[root_y]:
        self.root[root_x] = root_y
      else:
        self.root[root_y] = root_x
        self.rank[root_x] += 1

  def connected(self, x, y):
    return self.find(x) == self.find(y)