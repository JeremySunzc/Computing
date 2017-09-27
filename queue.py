"""
File: queue.py

Queue implementations
"""

class ArrayQueue(object):
    """ Array-based queue implementation."""

    DEFAULT_CAPACITY = 10  # Class variable applies to all queues
    
    def __init__(self):
        self._items = list()
        for count in range(ArrayQueue.DEFAULT_CAPACITY):
            self._items.append(None)
        self._rear = -1
        self._size = 0


    def enqueue(self, newItem):
        """Adds newItem to the rear of queue.
        Precondition: the queue is not full."""
        if self.isFull():
            print ("Queue is full. Abort operation!!")
            return ""
        else:
            # newItem goes at logical end of array
            self._rear += 1
            self._size += 1
            self._items[self._rear] = newItem


    def dequeue(self):
        """Removes and returns the item at front of the queue.
        Precondition: the queue is not empty."""
        if self.isEmpty():
            print ("Queue is empty. Abort operation!!")
            return ""
        else:
            oldItem = self._items[0]
            for i in range(len(self) - 1):
                self._items[i] = self._items[i + 1]
            self._rear -= 1
            self._size -= 1
        return oldItem


    def peek(self):
        """Returns the item at front of the queue.
        Precondition: the queue is not empty."""
        if self.isEmpty():
            print ("Queue is empty. Abort operation!!")
            return ""
        else:
            return self._items[0]


    def __len__(self):
        """Returns the number of items in the queue."""
        return self._size


    def isEmpty(self):
        return (len(self) == 0)


    def isFull(self):
        return (self._size == ArrayQueue.DEFAULT_CAPACITY)


    def __str__(self):
        """Items strung from front to rear."""
        result = ""
        for i in range(len(self)):
            result += str(self._items[i]) + " "
        return result


#----------------------------------------------------------------------#
 
class Node(object):

    def __init__(self, data, next = None):
        """Instantiates a Node with default next of None"""
        self.data = data
        self.next = next


class LinkedQueue(object):
    """ Link-based queue implementation."""

    def __init__(self):
        self._front = None
        self._rear = None
        self._size = 0


    def enqueue(self, newItem):
        """Adds newItem to the rear of queue."""
        newNode = Node(newItem, None)
        if self.isEmpty():
            self._front = newNode
        else:
            self._rear.next = newNode
        self._rear = newNode  
        self._size += 1


    def dequeue(self):
        """Removes and returns the item at front of the queue.
        Precondition: the queue is not empty."""
        if self.isEmpty():   
            print ("Queue is empty. Abort operation!!")
            return ""
        else:
            oldItem = self._front.data
            self._front = self._front.next
            if self._front is None:
                self._rear = None
            self._size -= 1
            return oldItem


    def peek(self):
        """Returns the item at front of the queue.
        Precondition: the queue is not empty."""
        if self.isEmpty():    
            print ("Queue is empty. Abort operation!!")
            return ""
        else:
            return self._front.data


    def __len__(self):
        """Returns the number of items in the queue."""
        return self._size


    def isEmpty(self):
        return len(self) == 0


    def __str__(self):
        """Items strung from front to rear."""
        result = ""
        probe = self._front
        while probe != None:
            result += str(probe.data) + " "
            probe = probe.next
        return result

#------------------------------------------------------------------#

def main():
    # Test either implementation with same code
    q = ArrayQueue()
    #q = LinkedQueue()
    print ("Length:", len(q))
    print ("Empty:", q.isEmpty())
    print ("Enqueue 1-10")
    for i in range(10):
        q.enqueue(i + 1)
    print ("Peeking:", q.peek())
    print ("Items (front to rear):", q)
    print ("Length:", len(q))
    print ("Empty:", q.isEmpty())
    print ("Enqueue 11")
    q.enqueue(11)
    print ("Dequeuing items (front to rear):", end = ' ')
    while not q.isEmpty(): print (q.dequeue(), end = ' ')
    print ("\nLength:", len(q))
    print ("Empty:", q.isEmpty())
    input('\nPlease press Enter or Return to quit the program.')


if __name__ == '__main__': 
    main()
