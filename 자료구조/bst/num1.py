class _Node():
  def __init__(self, key, value, left=None, right=None):
    self.key = key
    self.value = value
    self.left = left
    self.right = right

  def _find(self, key):
    if key == self.key:
      return self
    if key < self.key:
      return self.left._find(key) if self.left else None
    else:
      return self.right._find(key) if self.right else None
#      5
#     /
#    3
#   / \
#  2   4
  # 'ppp' exercise
  def _find_first(self):  # find_smallest
    return self.left._find_first() if self.left else self

  def _find_last(self):  # find_largest
    # 1st approach: recursion
    return self.right._find_last() if self.right else self

  def _insert(self, key, value):
    # 1st case: there is already a node with the given key in the BST
    #           => update the existing node
    if key == self.key:
      self.value = value
    
    # 2nd case: there is no node with the given key in the BST
    #           => find the right place and create a new node
    elif key < self.key:
      if self.left is None:
        self.left = _Node(key, value)
      else:
        self.left._insert(key, value)
    else:
      if self.right is None:
        self.right = _Node(key, value)
      else:
        self.right._insert(key, value)
#      5
  #    /   \
  #   3     9
  #  / \   / \
  # 2   4 7  11
  
  # Returns the new root.
  def _remove(self, key):
    # 1st case: the node of interest has two children
    #           => need to maintain the BST property
    #           1) remove the node
    #           2) exchange the deleted node with the smallest value
    #             in the right subtree (the smallest value among
    #             the right subtrees, but larger than the left part)
    # 2nd case: the node of interest has one or zero child
    #           => just remove the node (+new connection; substitution)
    
    if key < self.key and self.left is not None:
      self.left = self.left._remove(key)
    elif key > self.key and self.right is not None:
      self.right = self.right._remove(key)
    elif key == self.key:
      # 1st case: two children
      if self.left is not None and self.right is not None:
        # Need to remove self, but has two children
        n = self.right._find_first()
        self.key = n.key
        self.value = n.value
        self.right = self.right._remove_first()
      # 2nd case
      else:
        # Need to remove self, which has zero or one child
        return self.left if self.left else self.right
    return self

  def _remove_first(self):
    if self.left is None:  # current node is the smallest
      return self.right
    else:
      self.left = self.left._remove_first()
      return self
    


#Implementation of dict using a BST

class dict():
  def __init__(self):
    self._root = None

  def __str__(self):
    return self._root._description(0) if self._root else "[]"

  def _find(self, key):
    return self._root._find(key) if self._root else None

  def __getitem__(self, key):
    n = self._find(key)
    if n is None:
      raise KeyError(key)
    return n.value 

  def get(self, key, v=None):
    n = self._find(key)
    return n.value if n else v

  def __contains__(self, key):
    return self._find(key) is not None

  def firstkey(self):
    return self._root._find_first().key if self._root else None

  def lastkey(self):
    return self._root._find_last().key if self._root else None

  def __delitem__(self, key):
    if self._root:
      self._root = self._root._remove(key)
  
  # 'ppp' exercise
  def __setitem__(self, key, value):
    if self._root is None:
      self._root = _Node(key, value)
    else:
      self._root._insert(key, value)