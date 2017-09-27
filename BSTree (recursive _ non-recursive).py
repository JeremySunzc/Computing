# A Binary Search Tree (BST) Example

#==========================================================================
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#==========================================================================    
class BSTree:   # binary serach tree
    
    def __init__(self):
        # initializes the root
        self.root = None
   
    #-----------------------------------------------------------------------
    # Adds new nodes (Recursive)
    def insert(self, tree, value):
        if tree == None:
            self.root = TreeNode(value)
        else:
            if value < tree.value:    # if value is less than the stored one
                if tree.left == None:
                    tree.left = TreeNode(value)                
                else:
                    self.insert(tree.left, value)     # goes to left subtree
            else:                               # else goes to right subtree
                if tree.right == None:
                    tree.right = TreeNode(value)                    
                else:
                    self.insert(tree.right, value)
                   
    #-----------------------------------------------------------------------
    # Adds new nodes (Non-recursive)
    def insert(self, tree, value):
        if tree == None:
            self.root = TreeNode(value)
        else:
            inserted = False
            curNode = self.root
            while not inserted:
                if value < curNode.value:  # goes to left subtree
                    if curNode.left == None:
                        curNode.left = TreeNode(value)
                        inserted = True
                    else:
                        curNode = curNode.left
                else:                      # goes to right subtree 
                    if curNode.right == None:
                        curNode.right = TreeNode(value)
                        inserted = True
                    else:
                        curNode = curNode.right
           
    #--------------------------------------------------------------------------         
    # Gets the root of the tree
    def getRoot(self):
        return self.root
    
    #--------------------------------------------------------------------------
    # Looks for a value in the tree (Recursive)
    # Returns None if not found else returns the node found
    def search(self, tree, target):
        if tree == None:
            return None
        else:
            if target == tree.value:
                return tree              # if found
            elif target < tree.value:
                return self.search(tree.left, target)
            else:
                return self.search(tree.right, target)
    
    #---------------------------------------------------------------------------
    # Looks for a value in the tree (Non-recursive)
    # Returns None if not found else returns the node found
    def search(self, tree, target):
        found = False
        curNode = tree
        while not found and curNode != None:
            if target == curNode.value:
                    found = True
            elif target < curNode.value:
                    curNode = curNode.left
            else:
                    curNode = curNode.right
        if found:
            return curNode
        else:
            return None      # not found
    		
    #-----------------------------------------------------------------------------
    # Gets the parent of the specified node to search for
    def getParent(self, curNode, target, parent):
        if curNode == None:
            return None
        elif curNode.value == target.value:
            return parent
        else:
            if target.value < curNode.value:
                return self.getParent(curNode.left, target, curNode)
            elif target.value > curNode.value:
                return self.getParent(curNode.right, target, curNode)
            
    #------------------------------------------------------------------------------
    # Non-recursive deletion
    def delete(self, tree, target):

        nodeToDel = self.search(tree, target)      # search for the node 
        if nodeToDel == None:
            print (target,'does not exist !')
            return
        
        # get parent of the node to be deleted
        nodeParent = self.getParent(tree, nodeToDel, None)   

        # if node to be deleted has two children 
        if (nodeToDel.left and nodeToDel.right) != None:    

            # find predecseeor
            predNode = nodeToDel.left      
            while predNode.right != None:
                predNode = predNode.right
                
            # set value of the node to be deleted to the value of the pred node
            nodeToDel.value = predNode.value
            
            # delete the predecessor node
            if nodeToDel.left == predNode :   
                nodeToDel.left = predNode.left
                # del predNode                 # delete the predecessor node
            else:
                self.delete(nodeToDel.left, predNode.value) 
            
        else:                # node to be deleted has at most 1 child
            
            # set the parent left/right pointer
            if nodeToDel.left == None:          
                if nodeParent.left == nodeToDel:
                    nodeParent.left = nodeToDel.right
                else:
                    nodeParent.right = nodeToDel.right
            else:
                if nodeParent.left == nodeToDel:
                    nodeParent.left = nodeToDel.left
                else:
                    nodeParent.right = nodeToDel.left
            # del nodeToDel                        # delete the node
                
    #----------------------------------------------------------------------------      
    # Gets the size of the tree, i.e. number of nodes
    def size(self, tree):
        if tree == None:
            return 0
        else:
            return self.size(tree.left) + 1 + self.size(tree.right)

    #-----------------------------------------------------------------------------
    # Gets the height of the tree
    def maxDepth(self, tree):
        if tree == None:
            return -1
        else:
            # computes the two depths
            lDepth = self.maxDepth(tree.left)
            rDepth = self.maxDepth(tree.right)
            # returns the appropriate depth
            return max(lDepth, rDepth) + 1

    #-----------------------------------------------------------------------------
    # Returns True if binary tree is height-balanced
    def isBalanced (self, tree):
        if tree == None:
            return True

        lh = self.maxDepth(tree.left)    # height of left subtree
        rh = self.maxDepth(tree.right)   # height of right subtree

        if abs(lh-rh) <= 1 and \
           self.isBalanced(tree.left) and \
           self.isBalanced(tree.right):
            return True
        else:
            return False

    #-----------------------------------------------------------------------------
    # Gets the minimum value
    def minValue(self, tree):
        # goes down into the left arm and returns the last value
        curNode = tree
        while curNode.left != None: 
            curNode = curNode.left
        return curNode.value

    #-----------------------------------------------------------------------------
    # Gets the maximum value
    def maxValue(self, tree):
        # goes down into the right arm and returns the last value
        curNode = tree
        while curNode.right != None:  
            curNode = curNode.right
        return curNode.value
       
    #-----------------------------------------------------------------------------
    # Prints the tree in inOrder  -- ascending order
    def printTree(self, tree):
        if tree != None:
            self.printTree(tree.left)
            print (tree.value, end = ' ')
            self.printTree(tree.right)

    #-----------------------------------------------------------------------------
    # Prints the tree in preOrder 
    def printTree_preOrder(self, tree):
        if tree != None:
            print (tree.value, end = ' ')
            self.printTree_preOrder(tree.left)
            self.printTree_preOrder(tree.right)

    #-----------------------------------------------------------------------------
    # Prints the tree in postOrder 
    def printTree_postOrder(self, tree):
        if tree != None:
            self.printTree_postOrder(tree.left)
            self.printTree_postOrder(tree.right)
            print (tree.value, end = ' ')

    #-----------------------------------------------------------------------------
    # Prints the tree in reverseOrder  --  descending order
    def printTree_reverseOrder(self, tree):
        if tree != None:
            self.printTree_reverseOrder(tree.right)
            print (tree.value, end = ' ')
            self.printTree_reverseOrder(tree.left)
            
#===============================================================================
def main():
    # Instantiate the binary search tree
    tree = BSTree()
        
    # Insert tree nodes to binary search tree
    numNodes = int(input("\nEnter number of tree nodes: "))
    print ()
    for i in range(1, numNodes+1):
        value = int(input("Enter value of node %d: " % (i)))  
        tree.insert(tree.getRoot(), value)
    print ()

    # Delete a child
    value = int(input("Enter the value to be deleted: "))
    tree.delete(tree.getRoot(),value)
    print ()
    
    # Print the tree in inOrder
    print ('InOrder:\t', end = ' ')
    tree.printTree(tree.getRoot())
    print ()
    
    # Print the tree in preOrder
    print ('PreOrder:\t', end = ' ')
    tree.printTree_preOrder(tree.getRoot())
    print ()
  
    # Print the tree in postOrder
    print ('PostOrder:\t', end = ' ')
    tree.printTree_postOrder(tree.getRoot())
    print ()

    # Print the tree in reverseOrder
    print ('ReverseOrder:\t', end = ' ')
    tree.printTree_reverseOrder(tree.getRoot())
    print ()
    
    # Looks for a value in the tree
    value = int(input("\nEnter a value to find: "))
    if tree.search(tree.getRoot(), value) != None:
        print (value,'is found in the tree')
    else:
        print (value,'is not found in the tree')

    # Print maxDepth, maxValue, minValue and the size of the tree
    print ('\nMax depth:',tree.maxDepth(tree.getRoot()))
    print ('Max value:',tree.maxValue(tree.getRoot()))
    print ('Min value:',tree.minValue(tree.getRoot()))
    print ('Size:', tree.size(tree.getRoot()))
    print ()

    # Print whether the tree is balanced
    if tree.isBalanced(tree.getRoot()):
        print ('Tree is balanced')
    else:
        print ('Tree is not balanced')
    
main()
    




    

           
