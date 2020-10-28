class Node: 

    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key

# Insert Node
    def insert(self, data):
        if self.val:
            if data < self.val:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.val:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.val = data  
      
# Print the Tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.val),
        if self.right:
            self.right.PrintTree() 
          
                            
# Inorder tree traversal 
def printInorder(root): 
    if root: 
        printInorder(root.left) 
        print(root.val)
        printInorder(root.right) 

    
# Postorder tree traversal 
def printPostorder(root):  
    if root: 
        printPostorder(root.left)
        printPostorder(root.right)  
        print(root.val)

  
# Preorder tree traversal 
def printPreorder(root): 
    if root: 
        print(root.val)
        printPreorder(root.left)  
        printPreorder(root.right) 

  
# Driver code 
root = Node(4) 
root.insert(2)
root.insert(3)
root.insert(1)
root.insert(5)
root.insert(6)


print("Binary tree is")
root.PrintTree()

print("Preorder traversal of binary tree is")
printPreorder(root) 

print ("Inorder traversal of binary tree is")
printInorder(root) 

print ("Postorder traversal of binary tree is")
printPostorder(root)