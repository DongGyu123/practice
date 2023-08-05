def sort_012(list_012):
  """
  >>> check(sort_012)

  >>> sort_012([0])
  [0]
  >>> sort_012([1,2])
  [1, 2]
  >>> sort_012([2,1,0])
  [0, 1, 2]
  >>> sort_012( [1, 1, 0, 0, 1] )
  [0, 0, 1, 1, 1]
  >>> sort_012( [1, 2, 2, 0, 1, 2, 2, 1, 1, 2] )
  [0, 1, 1, 1, 1, 2, 2, 2, 2, 2]
  >>> sort_012( [2, 0, 0, 2, 0, 0, 1, 0, 1, 0, 2, 1, 1, 2, 1, 2, 0, 0, 2, 1] )
  [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2]
  """
  # YOUR CODE HERE
  for last in range(len(list_012), 1, -1):
    for j in range(last-1):
      if list_012[j]> list_012[j+1]:
        t=list_012[j]
        list_012[j]=list_012[j+1]
        list_012[j+1]=t
  return list_012

def minimum_difference(unsorted_arr):
  """
  >>> check(minimum_difference)

  >>> minimum_difference([2,4,5,9,7])
  1
  >>> minimum_difference([34, 29, 88, 13, 60])
  5
  >>> minimum_difference( [62, 98, 45, 6, 5, 90, 95, 86, 48, 17, 100, 40, 41, 84, 35] )
  1
  """
  # YOUR CODE HERE 복잡하다 외워라 꼭!
  def merge(l_list, r_list):                    #Sorting Part(nested)
    i, j = 0, 0
    m_list = []

    while (i < len(l_list)) and (j < len(r_list)):
      if l_list[i] < r_list[j]:
        m_list.append(l_list[i])
        i += 1
      else:
        m_list.append(r_list[j])
        j += 1
    
    while (i < len(l_list)):
      m_list.append(l_list[i])
      i += 1
    while (j < len(r_list)):
      m_list.append(r_list[j])
      j += 1
    
    return m_list

  def merge_sort(un_arr):

    if len(un_arr) <= 1:
      return un_arr

    mid_i = len(un_arr) // 2
    left_list = merge_sort(un_arr[:mid_i])
    right_list = merge_sort(un_arr[mid_i:])
    return merge(left_list, right_list)

  sorted_arr = merge_sort(unsorted_arr)

  min_dif = abs(sorted_arr[0]-sorted_arr[1])  #Searching Part
  for i in range(1,len(sorted_arr)-1):
    if abs(sorted_arr[i] - sorted_arr[i+1]) < min_dif:
      min_dif = abs(sorted_arr[i]-sorted_arr[i+1])
  return min_dif

def minimum_sum(unsorted_arr):
  """
  >>> check(minimum_sum)

  >>> minimum_sum( [3] )
  3
  >>> minimum_sum( [3, 8] )
  11
  >>> minimum_sum([6,8,4,5,2,3])
  604
  >>> minimum_sum([5,3,0,7,4])
  82
  >>> minimum_sum( [2, 1, 0, 6] )
  18
  >>> minimum_sum( [2, 6, 6, 7] )
  93
  >>> minimum_sum( [1, 6, 1, 0, 4, 7, 1, 2] )
  1273
  """
  #YOUR CODE HERE
  def merge(l_list, r_list):                    #Sorting Part(nested)
    i, j = 0, 0
    m_list = []

    while (i < len(l_list)) and (j < len(r_list)):
      if l_list[i] < r_list[j]:
        m_list.append(l_list[i])
        i += 1
      else:
        m_list.append(r_list[j])
        j += 1
    
    while (i < len(l_list)):
      m_list.append(l_list[i])
      i += 1
    while (j < len(r_list)):
      m_list.append(r_list[j])
      j += 1
    
    return m_list

  def merge_sort(un_arr):

    if len(un_arr) <= 1:
      return un_arr

    mid_i = len(un_arr) // 2
    left_list = merge_sort(un_arr[:mid_i])
    right_list = merge_sort(un_arr[mid_i:])
    return merge(left_list, right_list)

  sorted_arr = merge_sort(unsorted_arr)

  n = len(sorted_arr)                           #Searching Part
  if n == 1:
    return sorted_arr[0]
  return int(''.join(map(str,sorted_arr[0:n:2]))) + int(''.join(map(str,sorted_arr[1:n:2])))

def unique_row(row, col, matrix):
  """
  >>> unique_row(3, 4, [1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1])
  [[1, 1, 0, 1], [1, 0, 0, 1]]
  >>> unique_row(6, 4, [-4, -7, 1, 6, -4, -1, 2, 5, -4, -1, 2, 5, -4, -7, 1, 6, -4, -7, 1, 6, -6, -3, 7, -2])
  [[-4, -7, 1, 6], [-4, -1, 2, 5], [-6, -3, 7, -2]]
  >>> unique_row(17, 3, [-5, -5, 7, 3, 2, -5, -5, -5, 7, -6, -5, 1, -6, -5, 1, -5, -5, 7, -6, -3, -9, 6, -1, 2, 6, -1, 2, 6, -1, 2, 3, 2, -5, -6, -5, 1, 3, 2, -5, -6, -5, 1, -6, -3, -9, 6, -1, 2, 3, 2, -5])
  [[-5, -5, 7], [3, 2, -5], [-6, -5, 1], [-6, -3, -9], [6, -1, 2]]
  >>> unique_row(17, 1, [9, 9, 0, -6, -6, 0, 4, 0, 0, -6, -6, 4, 4, 4, 4, -8, 4])
  [[9], [0], [-6], [4], [-8]]
  """
  # YOUR CODE HERE
  sets = set()
  re_list = []
  for i in range(0, len(matrix), col):
    new_ma = matrix[i: i + col]
    if tuple(new_ma) not in sets:
      re_list.append(new_ma)
    sets.add((tuple(new_ma)))
  return re_list

def cal_point(y_set, p_set, int_list):
  """
  >>> cal_point({1, 2, 3}, {4, 5, 6}, [1, 2, 3, 4, 5])
  1
  >>> cal_point({2, 4, 5, 6}, {10, 11, 7, 15}, [6, 3, 12, 12, 8, 9])
  1
  >>> cal_point({10, 6}, {8, 13}, [11, 6, 12, 3, 5, 9, 6, 12, 4, 5, 2, 7, 7])
  2
  >>> cal_point({11, 3, 5}, {10, 12, 15}, [9, 7, 3, 11, 3, 8, 3, 8])
  4

  """
  # YOUR CODE HERE
  score = 0
  for i in int_list:
    if i in y_set:
      score += 1
    if i in p_set:
      score -= 1
  return score

def larg_but_min_freq(arr,n) :
  """
  >>> larg_but_min_freq([1,2,3,3,3,3,3,4,5],9)
  5
  >>> larg_but_min_freq([2,2,5,50,1],5)
  50
  >>> larg_but_min_freq([1,1,1,2,2,2,3,3,2],9)
  3
  >>> larg_but_min_freq([1,1,1,2,2,2,3,3,3],9)
  3
  >>> larg_but_min_freq([-1,-1,-1,-2,-3,-4],6)
  -2
  >>> larg_but_min_freq([-1,2,-3,4,-5,6],6)
  6
  >>> larg_but_min_freq([1,1,1,1,1,1,1,1],8)
  1
  >>> larg_but_min_freq([1],1)
  1
  """
  d={}
  for i in arr:
    if i in d.keys():
      d[i]+=1
    else:
      d[i]=1
  array =[k for k,v in d.items() if min(d.values()) == v]
  return max(array)
#-> 지문을 똑바로 파악 못함. 반드시 확인할것

def maxDiffIndex(arr, n): 
  
  """
  >>> maxDiffIndex([2, 1, 3, 4, 2, 1, 5, 1, 7],9)
  6
  >>> maxDiffIndex([2, 2, 2],3)
  2
  >>> maxDiffIndex([1,2,3,4,5],5)
  0
  >>> maxDiffIndex([-1,2,-3,4,-5,1,1,-3],8)
  5
  >>> maxDiffIndex([1],1)
  0
  >>> maxDiffIndex([1,-1,1,-1,1,-1,1],7)
  6
  """
  number_data={}
  distance = {}
  for k in range(n) :
    if arr[k] not in number_data.keys() :
      number_data[arr[k]] = k
      distance[arr[k]]=0
    else : 
      distance[arr[k]] = k - number_data[arr[k]]
  
  return max(distance.values())
#-> 지문을 다시한번 확인할 것.

def find_time(s1, s2):
  """
  >>> find_time("abcdefghijklmnopqrstuvwxyz", "cba")
  4
  >>> find_time("zyxwvutsrqponmlkjihgfedcba", "a")
  25
  >>> find_time("wsjvfpcxkanqgeitdyuhobzmlr", "wrwr")
  75
  >>> find_time("cntzhyejxuodgpfsrbliqmwkav", "cccc")
  0
  >>> find_time("zkqsneutodrvyfbxpgchmiljaw", "ziayqbw")
  69
  """
  mp = [0] * 26
  for i in range(26):
    mp[ord(s1[i])-97] = i
  
  ans = 0
  pos = 0
  for i in range(len(s2)):
    ans += abs(mp[ord(s2[i])-97] - pos)
    pos = mp[ord(s2[i])-97]
  
  return ans

def find_longest_conseq_subseq(arr, n):
  """
  >>> find_longest_conseq_subseq([1, 9, 3, 10, 4, 20, 2], 7)
  4
  >>> find_longest_conseq_subseq([2, 6, 1, 9, 4, 5, 3], 7)
  6
  >>> find_longest_conseq_subseq([1, 9, 3, 10, 4, 20, 2], 7)
  4
  >>> find_longest_conseq_subseq([7, 6, 5, 4, 3, 2, 2], 7)
  6
  >>> find_longest_conseq_subseq([2, 2, 3, 3, 1, 1], 6)
  3
  """
  s = set()
  ans = 0

  for ele in arr:
    s.add(ele)

  for i in range(n):
    if (arr[i]-1) not in s:
      j = arr[i]
      while(j in s):
          j += 1
      ans = max(ans, j-arr[i])
  return ans