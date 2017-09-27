def ourMin (A, n):

#Returns the position of the minimum item in an n-element integer array A

    minPos = 0
    for cur in range(1, n):
        if A[cur] < A[minPos]:
            minPos = cur
    return minPos

#------------------------------------------------------------------------------

def linearSearch(A, n, key):

#Search the n-element integer array A for a match with key.
#Return the position of the key item if found, or -1 otherwise.

    pos=0
    found = False
    while (not found and pos<n):
        if A[pos] == key:
            found = True
        else:
            pos = pos+1
    if found:
        return pos
    else:
        return -1
    
#----------------------------------------------------------------------------    

def binSearch(list, low, high, key):   
# Search a sorted array A, A[low] . . . . . A[high],for a match with key.
# Return the index of the matching array element or -1 if the key is not found

    found = False
    while (not found) and (low <=high):
        mid = (low+high)//2
        if key ==list[mid]:
            found = True
        if key < list[mid]:
            high= mid-1
        if key > list[mid]:
            low = mid+1
    if found:
        return mid
    else:
        return -1
    
#---------------------------------------------------------------------------

def binarySearch(list, n, key):
    found = False
    low = 0
    high = n-1
    while (not found) and (low <=high):
        mid = (low+high)//2
        if key ==list[mid]:
            found = True
        if key < list[mid]:
            high= mid-1
        if key > list[mid]:
            low = mid+1
    if found:
        return mid
    else:
        return -1

#--------------------------------------------------------------------------

def rBinarySearch(A, low, high, key):   #recursive
# Search a sorted array A, A[low] . . . . . A[high],for a match with key.
# Return the index of the matching array element or -1 if the key is not found

     
    if low > high:   # key not found
        return -1

    mid = (low+high)//2
    if key == A[mid]:
        return mid
    elif key < A[mid]:
        return rBinarySearch(A, low, mid-1, key)
    else:
        return rBinarySearch(A, mid+1, high, key)        

#------------------------------------------------------------------------   

def main():
    
    print ('Linear search')

    lst =[]
    n = int(input("Number of integers in the array: "))

    for i in range(n):
        num = int(input("Enter integer " + str(i+1)+ ": "))
        lst.append(num)
    print ()
    print (lst)

    key = int(input("Enter the key: "))
    pos = linearSearch(lst,n,key)
    if pos == -1:
        print (key,"is not in the list")
    else:
        print (key ,'is found at position',pos)

    print ()

    #----------------------------------------------------------------
    print ('Minimum value')
    
    print (lst)
    pos = ourMin(lst,n)
    print ("The min value is:",lst[pos]) 
    print ()

    #----------------------------------------------------------------

    print ("Binary search (list, n, key)")

    lst =[]
    n = int(input("Number of integers in the array: "))

    print ("Enter " + str(n) +" integers in order")
    for i in range(n):
        num = int(input("Enter integer " + str(i+1) + ": "))
        lst.append(num)
    print ()
    print (lst)
    key = int(input("Enter the key: "))
    pos = binarySearch(lst,n,key)
    if pos == -1:
        print (key,"is not in the list")
    else:
        print (key ,'is found at position',pos)

    print ()

    #-------------------------------------------------------------------
    
    print ('binSearch (list, low, high, key)')
    
    pos = binSearch(lst,0,n-1,key)
    if pos == -1:
        print (key,"is not in the list")
    else:
        print (key ,'is found at position',pos)

    print ()

    #---------------------------------------------------------------------
    
    print ("Recursive Binary Search:")
    
    pos = rBinarySearch(lst, 0, n-1,key)  
    if pos == -1:
        print (key,"is not in the list")
    else:
        print (key ,'is found at position',pos)

    print ()

   

main()

