def left_view(arr):
  '''
  >>> left_view([1, 3, 2])
  [1, 3]
  >>> left_view([10, 20, 30, 40, 60, 0, 0])
  [10, 20, 40]
  >>> left_view([1, 2, 3, 4, 5, 6, 7, 0, 8])
  [1, 2, 4, 8]
  >>> left_view([1, 2, 3, 4, 5, 6, 7, 8, 9])
  [1, 2, 4, 8]
  >>> left_view([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
  [1, 2, 4, 8, 16]
  >>> left_view([8, 0, 2, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 1, 2])
  [8, 2, 3, 1]
  '''
  res = []
  i = 0

  while(True):
    if len(arr) <= i: break
    ni = 2*(i+1) - 1
    for j in range(i, ni):
      if arr[j] != 0:
        res.append(arr[j])
        break
    i = ni
  return res

print(left_view([8, 0, 2, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 1, 2]))
#2번문제: 다시 체크해보자. 제대로 이해하지 못함.
def height(arr, i):
  l = 2*i + 1
  r = 2*i + 2
  if len(arr) <= i: return 0
  elif arr[i] == 0: return 0
  else: return max(height(arr, l), height(arr, r)) + 1

def diameter_for_subtree(arr, i):
  l = 2*i + 1
  r = 2*i + 2
  if len(arr) <= i: return 0
  elif arr[i] == 0: return 0
  else:
    l_height = height(arr, l)
    r_height = height(arr, r)
    l_diameter = diameter_for_subtree(arr, l)
    r_diameter = diameter_for_subtree(arr, r)
    return max(l_height + r_height + 1, max(l_diameter, r_diameter))

def diameter(arr):
  '''
  >>> diameter([1, 3, 2])
  3
  >>> diameter([10, 20, 30, 40, 60, 0, 0])
  4
  >>> diameter([1, 2, 3, 4, 5, 0, 7, 0, 0, 10, 11, 0, 0, 0, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 31, 32, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 60, 61, 0, 0])
  9
  >>> diameter([1, 2, 3, 4, 5, 0, 7, 8, 9, 0, 11, 0, 0, 0, 0, 0, 0, 18, 0, 0, 0, 22, 23, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 36, 37, 0, 0, 0, 0, 0, 0, 0, 0, 0, 47, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
  9
  >>> diameter([1, 2, 3, 4, 5, 0, 0, 8, 9, 0, 11, 0, 0, 0, 0, 0, 0, 18, 0, 0, 0, 22, 23, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 36, 37, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
  8
  >>> diameter([])
  0
  '''
  return diameter_for_subtree(arr, 0)



#문제 내용이 조금 복잡해서 나중에 문제 내용만 확인해봐라
class HeapSort:
    """
    >>> Heap = HeapSort()

    >>> Heap.heap_sort([1,4,2,3,6,8,7,10,9,5], 10)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> Heap.heap_sort([19, 18, 3, 7, 9, 16, 12], 7)
    [3, 7, 9, 12, 16, 18, 19]
    >>> Heap.heap_sort([7, 18, 0, 5, 5, 15, 1], 7)
    [0, 1, 5, 5, 7, 15, 18]
    """
    #Heapify function to maintain heap property.
    def heapify(self, arr, n, i):
        # YOUR CODE HERE
        largest = i
        l = 2*i + 1
        r = 2*i + 2
        if l < n and arr[l] > arr[largest]:
            largest = l
        if r < n and arr[r] > arr[largest]:
            largest = r
        if largest != i:
            arr[i],arr[largest] = arr[largest],arr[i]
            self.heapify(arr,n,largest)
    
    #Function to build a Heap from array.
    def build_heap(self, arr,n):
        # YOUR CODE HERE
        idx = n//2 - 1
        for i in range(idx,-1,-1):
            self.heapify(arr,n,i)
    #Function to sort an array using Heap Sort.    
    def heap_sort(self, arr, n):
        # YOUR CODE HERE
        self.build_heap(arr,n)
        for i in range(n-1,0,-1):
            arr[i],arr[0] = arr[0],arr[i]
            self.heapify(arr,i,0)
        return arr
    

def k_largest(arr, n, k):
  """
  >>> k_largest([4, 3, 2, 1], 4, 2)
  [4, 3]
  >>> k_largest([43, 37, 87, 5, 8, 23, 7], 7, 4)
  [87, 43, 37, 23]
  >>> k_largest([17, 33, 48, 81, 17, 53, 70], 7, 1)
  [81]
  >>> k_largest([5, 94, 79, 51, 50, 74, 17, 98, 91, 34], 10, 3)
  [98, 94, 91]
  >>> k_largest([28, 84, 53, 39, 47, 33, 22, 49, 86, 53, 42, 50, 53, 30, 98, 60, 67, 95, 0, 33], 20, 9)
  [98, 95, 86, 84, 67, 60, 53, 53, 53]
  >>> k_largest([-57, -4, -60, -89, -81, -98, -57, 0, -64, -27], 10, 2)
  [0, -4]
  >>> k_largest([], 0, 0)
  []
  """
  # YOUR CODE HERE
  Heap = HeapSort()
  Heap.heap_sort(arr, n)
  r_list = []
  for l in range(k):
    r_list.append(arr.pop())
  return r_list

from queue import PriorityQueue
def kthLargest(arr,n) :
    """
    >>> kthLargest([3,2,1],2)
    5
    >>> kthLargest([2,6,4,1],3)
    11
    >>> kthLargest([1,2,3,4,5,6],3)
    18
    >>> kthLargest([1,2,3,6],5)
    5
    >>> kthLargest([1],1)
    1
    >>> kthLargest([1,2],3)
    1
    >>> kthLargest([1,2,3],3)
    3
    """
    # YOUR CODE HERE
    que = PriorityQueue()
    data = []
    for k in range(len(arr)) :
        sum_=0
        for t in range(k,len(arr)) :
            sum_+=arr[t]
            if sum_ not in data :
                data.append(sum_)
                que.put((-sum_,sum_))
    
    for k in range(n-1) :
        que.get()
        
    return que.get()[1]


def binTreeSortedLevels (arr):
    """
    >>> binTreeSortedLevels([1])
    [[1]]
    >>> binTreeSortedLevels([7,6,5,4,3,2,1])
    [[7], [5, 6], [1, 2, 3, 4]]
    >>> binTreeSortedLevels([1,2,3,4,5,6,7,8,9,10])
    [[1], [2, 3], [4, 5, 6, 7], [8, 9, 10]]
    >>> binTreeSortedLevels([5,6,4,9,2,1])
    [[5], [4, 6], [1, 2, 9]]
    >>> binTreeSortedLevels([])
    []
    """
    res = []
    i = 0
    
    ls = 1
    n = len(arr)
    while i < n:
        t = (1 << ls) - 1
        t = min (t, n)
        temp = sorted (arr[i : t])
        
        i = t
        ls += 1
        res.append (temp)
    return res