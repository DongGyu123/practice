class _Node():
  def __init__(self, value, left=None, right=None):
    self.data = value
    self.left = left
    self.right = right

  def list_to_tree(self, i_list, i):
    if (2*i+1) < len(i_list) and i_list[2*i+1] is not None:
      l = _Node(i_list[2*i+1])
      self.left = l
      l.list_to_tree(i_list, 2*i+1)
    if (2*i+2) < len(i_list) and i_list[2*i+2] is not None:
      r = _Node(i_list[2*i+2])
      self.right = r
      r.list_to_tree(i_list, 2*i+2)
  

class BinarySearchTree():

  def __init__(self) :
    self.root = None
  
  def insert(self,data) :
    self.root = self.insert_value(self.root,data)

    return self.root is not None

  def insert_value(self,node,data) :
    if node is None :
      node = _Node(data)
    else :
      if data < node.data :
        node.left = self.insert_value(node.left,data)
      else :
        node.right = self.insert_value(node.right,data)

    return node

def test_bst(i_list) :
  test = BinarySearchTree()
  for k in range(0,len(i_list)) :
    if k==0 :
      test.insert(i_list[0])
    else:
      test.insert_value(test.root,i_list[k])

  return test.root

#문제 3 => 얘는 포기 ㅋㅋㅋ
def sum_leaf_nodes(first_node):
  """
  >>> sum_leaf_nodes(test_bst([7,3,8,1,5,10,4]))
  15
  >>> sum_leaf_nodes(test_bst([3]))
  3
  >>> sum_leaf_nodes(test_bst([10,9,8,7,6,5,4,3,2,1]))
  1
  >>> sum_leaf_nodes(test_bst([3,3,3,3,3,3,3,4]))
  4
  >>> sum_leaf_nodes(test_bst([10,100,1000,10000]))
  10000
  """
  if first_node is None:
    return 0
  elif first_node.left is None and first_node.right is None:
    return first_node.data
  return sum_leaf_nodes(first_node.left)+sum_leaf_nodes(first_node.right)

### THIS IS FOR MAKING TEST CASES ###
def test_case(i_list) -> _Node :
  root = _Node(i_list[0])
  root.list_to_tree(i_list, 0)
  return root
### THIS IS FOR MAKING TEST CASES ###

def is_bst(root) -> bool:
  """
  >>> is_bst(test_case([7,3,8,1,5,None,10,None,None,4]))
  True
  >>> is_bst(test_case([5,3,8,2,4,7,9,1,None,None,None,6,None,None,10]))
  True
  >>> is_bst(test_case([2,1,3]))
  True
  >>> is_bst(test_case([4,1,5,3,2]))
  False

  """
  # YOUR CODE HERE
  import math

  if not root:
    return True
        
  stack = [(root, -math.inf, math.inf)]
        
  while stack:
    root, lower, upper = stack.pop()
        
    if not root:
      continue
    val = root.data
    if val <= lower or val >= upper:
      return False
                
    stack.append((root.right, val, upper))
    stack.append((root.left, lower, val))
            
  return True


def lowest_common_ancestor(root, n1, n2):
  """
  >>> lowest_common_ancestor(test_bst([7,3,8,1,5,10,4]), 1, 4)
  3
  >>> lowest_common_ancestor(test_bst([20,10,22,8,15,21,27,2,9,24,40,1]), 21, 24)
  22
  >>> lowest_common_ancestor(test_bst([1,2,3,4,5,6,7,8,9]), 7, 9)
  7
  >>> lowest_common_ancestor(test_bst([8,3,10,1,6,14,4,7,13]), 1, 7)
  3
  """
  # YOUR CODE HERE
  anc = root
  while root:
    if root.data > n1 and root.data > n2:
      root = root.left
    elif root.data < n1 and root.data < n2:
      root = root.right
    else:
      anc = root
      break
  return anc.data


class TreeNode(object):
    def __init__(self, val):
      self.val = val
      self.left = None
      self.right = None
      self.height = 1

class AvlTree(object):
  def insert(self, root, key):
    if not root:
      return TreeNode(key)
    elif key < root.val:
      root.left = self.insert(root.left, key)
    else:
      root.right = self.insert(root.right, key)

    root.height = 1 + max(self.get_height(root.left),
            self.get_height(root.right))

    balance = self.get_balance(root)

    if balance > 1 and key < root.left.val:
      return self.right_rotate(root)

    if balance < -1 and key > root.right.val:
      return self.left_rotate(root)

    if balance > 1 and key > root.left.val:
      root.left = self.left_rotate(root.left)
      return self.right_rotate(root)

    if balance < -1 and key < root.right.val:
      root.right = self.right_rotate(root.right)
      return self.left_rotate(root)

    return root

  def left_rotate(self, z):

    y = z.right
    T2 = y.left

    # Perform rotation
    y.left = z
    z.right = T2

    # Update heights
    z.height = 1 + max(self.get_height(z.left),
            self.get_height(z.right))
    y.height = 1 + max(self.get_height(y.left),
            self.get_height(y.right))

    # Return the new root
    return y

  def right_rotate(self, z):

    y = z.left
    T3 = y.right

    # Perform rotation
    y.right = z
    z.left = T3

    # Update heights
    z.height = 1 + max(self.get_height(z.left),
            self.get_height(z.right))
    y.height = 1 + max(self.get_height(y.left),
            self.get_height(y.right))

    # Return the new root
    return y

  def get_height(self, root):
    if not root:
      return 0

    return root.height

  def get_balance(self, root):
    if not root:
      return 0

    return self.get_height(root.left) - self.get_height(root.right)
  
  def pre_order(self, root, result):
    if not root:
      return

    result.append(root.val)
    self.pre_order(root.left, result)
    self.pre_order(root.right, result)

def solution(arr):
  """
  >>> solution([10, 20, 30, 40, 50, 25])
  [30, 20, 10, 25, 40, 50]
  >>> solution([10, 10, 20, 20, 30, 30])
  [20, 10, 10, 20, 30, 30]
  >>> solution([70, 20, 25, 23, 55, 17, 19, 82, 99])
  [25, 20, 17, 19, 23, 70, 55, 82, 99]
  >>> solution([9, 1, 8, 2, 7, 3, 6, 4])
  [7, 2, 1, 4, 3, 6, 8, 9]
  >>> solution([-1, 10, 5, 4, 2, -10])
  [2, -1, -10, 5, 4, 10]
  >>> solution([0, 0, 0, 0, 1, 1])
  [0, 0, 0, 0, 1, 1]
  """
  my_tree = AvlTree()
  root = None
  for a in arr:
    root = my_tree.insert(root, a)
  result = []
  my_tree.pre_order(root, result)
  return result