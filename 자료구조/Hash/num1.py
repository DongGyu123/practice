#Chaining

class _Node():
  def __init__(self, key, value, next=None):
    self.key = key
    self.value = value
    self.next = next

def _hash(key):
  return (key) % 100

class dict():
  def __init__(self):
    self._data = [ None ] * 100 # the memory space we have is 100

  def __contains__(self, key):
    return self._findnode(key) is not None
  
  def _findnode(self, key):
    i = _hash(key)     # memory location
    p = self._data[i]  # the head of the linked list at memory location i
    while p is not None:
      if p.key == key:
        return p
      p = p.next
    return None
  
  # print(d[k]) -> value of the item with the key k
  def __getitem__(self, key):
    p = self._findnode(key)
    if p:
      return p.value
    else:
      raise ValueError(key)
  
  # 'ppp' exercise
  def __setitem__(self, key, value):  # d[k] = v
    p=self._findnode(key)
    if p:
      p.value=value
    else:
      h=_hash(key)
      self._data[h]=_Node(key, value, self._data[h])
  
  def __repr__(self):
    s = ""
    for i in range(100):
      s += "%02d: " % i
      p = self._data[i]
      while p is not None:
        s += str(p.key) + " "
        p = p.next
      s += "\n"
    return s