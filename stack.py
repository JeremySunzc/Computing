"""
File: stack.py

Stack implementations
"""

class ArrayStack(object):
    """ Array-based stack implementation."""

    DEFAULT_CAPACITY = 10  # Class variable for all array stacks
    
    def __init__(self):
        self._items = list()
        for count in range(ArrayStack.DEFAULT_CAPACITY):
            self._items.append(None)
        self._top = -1
        self._size = 0


    def push(self, newItem):
        """Inserts newItem at top of stack.
        Precondition: the stack is not full."""
        if self.isFull():
            print ("Stack is full. Abort operation!!")
            return ""
        else:
            # newItem goes at logical end of array
            self._top += 1
            self._size += 1
            self._items[self._top] = newItem


    def pop(self):
        """Removes and returns the item at top of the stack.
        Precondition: the stack is not empty."""
        if self.isEmpty():
            print ("Stack is empty. Abort operation!!")
            return ""
        else:
            oldItem = self._items[self._top]
            self._top -= 1
            self._size -= 1
            return oldItem


    def peek(self):
        """Returns the item at top of the stack.
        Precondition: the stack is not empty."""
        if self.isEmpty():
            print ("Stack is empty. Abort operation!!")
            return ""
        else:
            return self._items[self._top]


    def __len__(self):
        """Returns the number of items in the stack."""
        return self._size

    
    def isEmpty(self):
        return (len(self) == 0)


    def isFull(self):
        return (self._size == ArrayStack.DEFAULT_CAPACITY)        

    
    def __str__(self):
        """Items strung from bottom to top."""
        result = ""
        for i in range(len(self)):
            result += str(self._items[i]) + " "
        return result

#--------------------------------------------------------------------#
class Node(object):

    def __init__(self, data, next = None):
        """Instantiates a Node with default next of None"""
        self.data = data
        self.next = next


class LinkedStack(object):
    """ Link-based stack implementation."""

    def __init__(self):
        self._top = None
        self._size = 0


    def push(self, newItem):
        """Inserts newItem at top of stack."""
        newNode = Node(newItem, self._top)
        self._top = newNode
        self._size += 1


    def pop(self):
        """Removes and returns the item at top of the stack.
        Precondition: the stack is not empty."""
        if self.isEmpty():    # or if self._top == None:
            print ("Stack is empty. Abort operation!!")
            return ""
        else:
            oldItem = self._top.data
            self._top = self._top.next
            self._size -= 1
            return oldItem


    def peek(self):
        """Returns the item at top of the stack.
        Precondition: the stack is not empty."""
        if self.isEmpty():     # or if self._top == None:
            print ("Stack is empty. Abort operation!!")
            return ""
        else:
            return self._top.data


    def __len__(self):
        """Returns the number of items in the stack."""
        return self._size


    def isEmpty(self):
        return len(self) == 0


    """
    def __str__(self):
  
        # Items strung from bottom to top. 
       
        # Helper builds string from end to beginning
        def strHelper(probe):
            if probe is None:
                return ""
            else:
                return strHelper(probe.next) + str(probe.data) + " "
            
        return strHelper(self._top)
    """
    
    def __str__(self):

        # Items strung from bottom to top. 
        
        result = ''
        probe = self._top
		
        while probe != None:
            result = str(probe.data) + ' ' + result
            probe = probe.next
			
        return result
    
  
            
#---------------------------------------------------------------------#

def main():
    # Test either implementation with same code
    #s = ArrayStack()
    s = LinkedStack()
    print ("Length:", len(s))
    print ("Empty:", s.isEmpty())
    print ("Push 1-10")
    for i in range(10):
        s.push(i + 1)
    print ("Peeking:", s.peek()) 
    print ("Items (bottom to top):", s)
    print ("Length:", len(s))
    print ("Empty:", s.isEmpty())
    print ("Push 11")
    s.push(11)
    print ("Popping items (top to bottom):", end = ' ')
    while not s.isEmpty(): print (s.pop(), end = ' ')
    print ("\nLength:", len(s))
    print ("Empty:", s.isEmpty())
    input('\nPlease press Enter or Return to quit the program.')
 

if __name__ == '__main__':
    main()
