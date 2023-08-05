#Merge Sort
def merge(a, b):
  i = 0
  j = 0
  res = []
  while i < len(a) and j < len(b):
    va = a[i]
    vb = b[j]
    if va <= vb:
      res.append(va)
      i += 1
    else:
      res.append(vb)
      j += 1
  res.extend(a[i:])
  res.extend(b[j:])
  return res

def merge_sort(a):
  if len(a) <= 1:
    return a
  mid = len(a) // 2
  left_half = merge_sort(a[:mid])
  right_half = merge_sort(a[mid:])
  return merge(left_half, right_half)


# Quick sort

def quick_sort(a):
  if len(a) <= 1:
    return a
  pivot = a[len(a) // 2]
  small = []
  equal = []
  large = []
  for x in a:
    if x < pivot:
      small.append(x)
    elif x == pivot:
      equal.append(x)
    else:
      large.append(x)
  return quick_sort(small) + equal + quick_sort(large)


# Quick sort-inplace
def partition(a, lo, hi):
  p = (lo + hi)//2
  pivot = a[p]
  a[p] = a[hi]  # Swap pivot with last item
  a[hi] = pivot

  i = lo - 1
  j = hi
  while i < j: 
    i += 1 
    while a[i] < pivot: 
      i += 1
    j -= 1
    while a[j] > pivot and j > lo: 
      j -= 1
    if i < j:
      t = a[i]; a[i] = a[j]; a[j] = t  # swap a[i] and a[j]
  a[hi] = a[i]
  a[i] = pivot # Put pivot where it belongs
  return i     # index of pivot

# sort range a[lo:hi+1]
def quick_sort1(a, lo, hi):
  if (lo < hi):
    pivot = partition(a, lo, hi)
    quick_sort1(a, lo, pivot - 1)
    quick_sort1(a, pivot  + 1, hi)