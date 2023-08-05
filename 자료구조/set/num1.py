#set ADT

class set():
  def __init__(self, items=None):
    self._data = []  # empty list = empty set
    if items:
      for item in items:
        self.add(item)

  def __contains__(self, item):
    
    return item in self._data

  def __len__(self):
    return len(self._data)

  def add(self, item):
    if item not in self._data:
      self._data.append(item)

  def remove(self, item):
    if item in self._data:
      self._data.remove(item) # use the default `remove` for lists
    else:
      raise KeyError(item)
  
  def discard(self, item):
    if item in self._data:
      self._data.remove(item) # use remove for list

  ################################
  ######## 'ppp' exercise ########
  ################################
  def __eq__(self, t):
    if len(self)!=len(t):
      return False
    return self.is_subset(t)

  ################################
  ######## 'ppp' exercise ########
  ################################
  def is_subset(self, t):
    # checks if s <= t
    for item in self._data:
      if item not in t:
        return False
    return True

  ################################
  ######## 'ppp' exercise ########
  ################################
  def is_superset(self, t):
    # checks if s >= t
    return t.is_subset(self)

  ################################
  ######## 'ppp' exercise ########
  ################################
  def union(self, t):
    # should be non-destructive
    new_set = set()
    new_set._data.extend(self._data)  # copy elements to new set
    for item in t:
      new_set.add(item)
    return new_set
    
  def __iter__(self):
    return _SetIterator(self._data)

  def __repr__(self):
    s = "ListSet("
    sep = ""
    for item in self._data:
      s += sep + repr(item)
      sep = ","
    return s + ")"


class _SetIterator():
  def __init__(self, l):
    self._l = l
    self._current = 0
  
  def __iter__(self):
    return self
    
  def __next__(self):
    if self._current < len(self._l):
      entry = self._l[self._current]
      self._current += 1
      return entry
    else:      
      raise StopIteration