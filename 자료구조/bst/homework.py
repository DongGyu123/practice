import doctest

#사전에 필요한 코드들
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

