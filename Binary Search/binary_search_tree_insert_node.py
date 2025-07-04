"""
##INSTRUCTIONS:

Check if the BST is empty.
Check if the data to insert is smaller than the current node's data.
Check if the data to insert is greater than the current node's data.

"""

## SOLUTION:

class BinarySearchTree:
  def __init__(self):
    self.root = None

  def insert(self, data):
    new_node = TreeNode(data)
    # Check if the BST is empty
    if self.root == None:
      self.root = new_node
      return
    else:
      current_node = self.root
      while True:
        # Check if the data to insert is smaller than the current node's data
        if data < current_node.data:
          if current_node.left_child == None:
            current_node.left_child = new_node
            return 
          else:
            current_node = current_node.left_child
        # Check if the data to insert is greater than the current node's data
        elif data > current_node.data:
          if current_node.right_child == None:
            current_node.right_child = new_node
            return
          else:
            current_node = current_node.right_child

bst = CreateTree()
bst.insert("Pride and Prejudice")
print(search(bst, "Pride and Prejudice"))


## OUTPUT:

True