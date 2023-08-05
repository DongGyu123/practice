# general tree => binary tree
class Tree:
  '''
  #    3
  #   / ＼
  #  1   2
  #     / ＼
  #    1   1
  >>> t = Tree(3, [Tree(1), Tree(2, [Tree(1), Tree(1)])])
  >>> t.label
  3
  >>> t.is_leaf()
  False
  >>> t.branches[0].is_leaf()
  True
  '''
  def __init__(self, label, branches=[]):
    self.label = label
    for branch in branches:
      assert isinstance(branch, Tree)
    self.branches = list(branches)

  def is_leaf(self):
    return not self.branches  # [] => False
  
def count_leaves(t):
   if t.is_leaf():
     return 1
   total=0
   for b in t.branches:
     total+=count_leaves(b)
   return total
  
def print_tree(t, indent=0):
    print(indent*" "+str(t.label))
    for b in t.branches:
      print_tree(b, indent+2)


def count_paths(t, total):
     if t.label==total:
       found=1
     else:
       found=0
     return found+sum([count_paths(b, total-t.label) for b in t.branches]) 
  """Return the number of paths from the root to any node in T
  for which the labels along the path sum to TOTAL.

  #      3
  # -1   1        1
  #      2  3    -1
  #      1
  >>> t = Tree(3, [Tree(-1), Tree(1, [Tree(2, [Tree(1)]), Tree(3)]), Tree(1, [Tree(-1)])])
  >>> count_paths(t, 3)
  2
  >>> count_paths(t, 4)
      2
      >>> count_paths(t, 5)
      0
     >>> count_paths(t, 6)
       1
      >>> count_paths(t, 7)
      2
      """
     