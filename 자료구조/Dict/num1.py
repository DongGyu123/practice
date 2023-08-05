class dict():
  def __init__(self):
    self._data = []

  def __len__(self):
    return len(self._data)
  
  def __setitem__(self, k, value):
    i = self._findkey(k)
    if i >= 0:
      self._data[i] = (k, value)
    else:
      self._data.append((k, value))
    # di = dict()
    # di['5'] = [1, 2, 3, 4, 5]

  def _findkey(self, k):
    for i in range(len(self._data)):
      if k == self._data[i][0]:
        return i
    return -1

  def __contains__(self, k):
    return self._findkey(k) >= 0

  ################################
  ######## 'ppp' exercise ########
  ################################
  def __getitem__(self, k):
    # print(di['5']) => [1, 2, 3, 4, 5]
    i = self._findkey(k)
    if i >= 0:
      return self._data[i][1]
    else:
      raise KeyError(k)

  ################################
  ######## 'ppp' exercise ########
  ################################
  def get(self, k, v0=None):
    i = self._findkey(k)
    if i >= 0:
      return self._data[i][1]
    else:
      return v0


# 'ppp' exercise
def long_subarr_k(arr, k):
  '''Given an array arr containing len(arr) integers and an integer k, 
  long_subarr_k finds
    1) the length of the longest subarray
       with the sum of the elements equal to the given value k, and
    2) the list of elements summing to k.
  >>> long_subarr_k([10, 5, 2, 7, 1, 9], 15)
  (4, [5, 2, 7, 1])
  >>> long_subarr_k([-1, 2, 3], 6)
  0
  >>> long_subarr_k([-5, 8, -14, 2, 4, 12], -5)
  (5, [-5, 8, -14, 2, 4])
  '''
  result={}
  max_len=0
  
  for i in range(len(arr)):
    cur_sum=0
    for j in range(i, len(arr)):
      cur_sum+=arr[j]
      if cur_sum==k:
        num=j-i+1
        result[num]=arr[i:j+1]
        if num>max_len:
          max_len=num
  if max_len==0:
    return 0
  return (max_len, result(max_len))