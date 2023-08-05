#Insertion sort 닥치고 외울것!!
def sorted_linear_search(a, x):
  for i in range(len(a)):
    if a[i] >= x:
      return i
  return len(a)

def insertion_sort1(a):
  if len(a) <= 1:
    return a
  b = insertion_sort1(a[:-1])
  k = sorted_linear_search(b, a[-1])
  b.insert(k, a[-1])
  print(b)
  return b

print(insertion_sort1([3, 2, 1, 0, 0, 30, 33]))

#ppp 1 닥치고 외워라
def insertion_sort2(a, j):
  if j<=1:
    return
  insertion_sort2(a, j-1)
  k=j-1
  x=a[k]
  while k>0 and a[k-1]>x:
    a[k]=a[k-1]
    k-=1
  a[k]=x

#ppp buble sort
def bubble_sort(a):
  for last in range(len(a), 1, -1):
    flipped=False
    for j in range(last-1):
      if a[j]>a[j+1]:
        flipped=True
        t=a[j]
        a[j]=a[j+1]
        a[j+1]=t
    if not flipped:
      return