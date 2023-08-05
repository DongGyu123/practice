#Binary Tree Definition and Traversals

class BTree:
  def __init__(self, label=0, left=None, right=None):
    self.label = label
    self.left  = left
    self.right = right


def sum_path_list(t, prev_sum=0):
    
  lst = [t.label + prev_sum]
  sum_path = t.label + prev_sum

  if t.is_leaf():
    return lst
  else:
    for i in range(len(t.branches)):
      lst += sum_path_list(t.branches[i], sum_path)
    return lst  



def print_preorder(t):
  if t:
    print(t.label, end=" ")
    print_preorder(t.left)
    print_preorder(t.right)

def print_postorder(t):
  if t:
    print_postorder(t.left)
    print_postorder(t.right)
    print(t.label, end=" ")

def print_inorder(t):
  if t:
    print_inorder(t.left)
    print(t.label, end=" ")
    print_inorder(t.right)

def min_leaf_depth(t):
  if t.is_leaf():
    return 0
  return 1+min(map(min_leaf_depth, t.branches))
    
    
def depth_path_list(t, prev_depth=-1):

  if t.is_leaf():
    return [prev_depth + 1]
  else:
    lst = []
    for i in range(len(t.branches)):
      lst += depth_path_list(t.branches[i], prev_depth + 1)
    return lst