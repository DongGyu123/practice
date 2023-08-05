#Open addressing

class _Entry():
  def __init__(self, key, value):
    self.key = key
    self.value = value

def _hash(key):
  return (key) % 100

class dict():
  def __init__(self):
    self._data = [ None ] * 100

  def _findkey(self, key):
    i = _hash(key)
    while self._data[i] is not None:
      if self._data[i].key == key:
        return (True, i)
      i = (i + 1) % 100
    return (False, i)

  def __contains__(self, key):
    found, i = self._findkey(key) 
    return found
  
  def __getitem__(self, key):
    found, i = self._findkey(key) 
    if found:
      return self._data[i].value
    else:
      raise ValueError(key)

  # 'ppp' exercise
  def __setitem__(self, key, value):
    found, i=self._findkey(key)
    if found:
      self._data[i].value=value
    else:
      self._data[i]=_Entry(key, value)
  
  def __repr__(self):
    s = ""
    for i in range(100):
      s += "%02d: " % i
      if self._data[i] is not None:
        s += str(self._data[i].key)
      s += "\n"
    return s
  

#Practical issues

class Point():
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __repr__(self):
    return "Point(%s, %s)" % (self.x, self.y)

#point 관련 내용을 안적었음. Hash 강의를 확인할 것.