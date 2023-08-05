# ppp' Exercise Sieve of Erathosthenes
# This is to find the prime numbers smaller than given N.

def sieve(n):
  '''finds the set of prime numbers smaller than n
  '''

  nums=set(range(2, n))
  for num in range(2, int(n+1)**0.5):
    if num in nums:
      for k in range(num*2, n+1, num):
        nums.remove(k)
  return nums._data

################################
########### caution! ###########
################################
num_list = list(range(10))

for item in num_list:  # error in other languages
  num_list.remove(item)

