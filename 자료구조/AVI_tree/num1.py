class _Node():
  def __init__(self, key, value, left=None, right=None, height=0):
    self.key = key
    self.value = value
    self.left = left
    self.right = right
    self.height = height

  def _left_height(self):
    return -1 if self.left is None else self.left.height

  def _right_height(self):
    return -1 if self.right is None else self.right.height

  def _recompute_height(self):
    """Recompute the height from subtree height, 
    return True if node is unbalanced."""
    left = self._left_height()
    right = self._right_height()
    self.height = max(left, right) + 1
    return abs(right - left) > 1
  
  # 'ppp' exercise
  def _rotate_left(self):
    # returns new root
    root = self.right  # self: z
    self.right = root.left
    self._recompute_height()
    root.left = self
    root._recompute_height()
    return root

  def _rotate_right(self):
    root = self.left
    self.left = root.right
    self._recompute_height()
    root.right = self
    root._recompute_height()
    return root

  def _restructure(self):
    if self._right_height() > self._left_height():  # case 1
      if self.right._left_height() > self.right._right_height():  # case 3
        self.right = self.right._rotate_right()
      return self._rotate_left()
    else:  # left height > right height
      if self.left._right_height() > self.left._left_height():
        self.left = self.left._rotate_left()
      return self._rotate_right()

  def _description(self, level):
    ls = self.left._description(level+1) if self.left else ""
    rs = self.right._description(level+1) if self.right else ""
    return ls + str(self.key) + ("(%d) " % level) + rs

  def _find_first(self):
    p = self
    while p.left is not None:
      p = p.left
    return p

  def _find_last(self):
    p = self
    while p.right is not None:
      p = p.right
    return p

  def _find(self, key):
    if key == self.key:
      return self
    if key < self.key:
      return self.left._find(key) if self.left else None
    else:
      return self.right._find(key) if self.right else None

  # 'ppp' exercise
  def _insert(self, key, value):
    if key == self.key:
      self.value = value
      return self
    if key < self.key:
      if self.left is None:
        self.left = _Node(key, value)
      else:
        self.left = self.left._insert(key, value)
    else:
      if self.right is None:
        self.right = _Node(key, value)
      else:
        self.right = self.right._insert(key, value)
    if self._recompute_height():
      return self._restructure()
    return self

  # Remove node with smallest key in the subtree rooted at this node
  # Returns the new root.
  def _remove_first(self):
    if self.left is None:
      return self.right
    self.left = self.left._remove_first()
    if self._recompute_height():
      return self._restructure()
    return self

  # Returns the new root.
  def _remove(self, key):
    if key < self.key and self.left is not None:
      self.left = self.left._remove(key)
    elif key > self.key and self.right is not None:
      self.right = self.right._remove(key)
    elif key == self.key:
      if self.left is not None and self.right is not None:
        # Need to remove self, but has two children
        n = self.right._find_first()
        self.key = n.key
        self.value = n.value
        self.right = self.right._remove_first()
      else:
        # Need to remove self, which has zero or one child
        # No restructuring needed in this case
        return self.left if self.left else self.right
    if self._recompute_height():
      return self._restructure()
    return self