#Selection Sort
def find_min_index1(a):
  mindex = 0
  for k in range(1, len(a)):
    if a[k] < a[mindex]:
      mindex = k
  return mindex

def selection_sort(a):
  if len(a) <= 1:
    return a
  k = find_min_index1(a)
  return [a[k]]+selection_sort(a[:k] + a[k+1:])

#print(selection_sort([2, 0, 4, 1, 4, 5, 5, 8, 9, 10]))

#inplace + recursive implementation
def find_min_index2(a, i):
  mindex = i
  for k in range(i+1, len(a)):
    if a[k] < a[mindex]:
      mindex = k
  return mindex

def selection_sort_inplace(a, i=0):
  if len(a) - i <= 1:
    return
  k = find_min_index2(a, i)
  # exchange a[i] and a[k]
  t = a[i]
  a[i] = a[k]
  a[k] = t
  # sort the rest
  selection_sort_inplace(a, i+1)
# a=[2, 4, 0, 0, 9, 12, 22, 10, -1]
# selection_sort_inplace(a)
# print(a)

