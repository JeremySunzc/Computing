def insertionSort(A, n):
#sort an array of n integer elements using insertion sort algorithm

#insertion sort orders sublists A[0], . . .,A[i].  1 <= i <= n-1.
#for each i, insert A[i] in the correct postition A[j] 

    for i in range(1, n):              #i identifies the sublist A[0] to A[i] 

        #index j scans down list from A[i] looking for correct position to locate target.
        #assigns it to A[j]                            
        target = A[i]
        j = i

        #locate insertion point by scanning downward as long as target < A[j-1] and we have not encountered
        #the beginning of the list
        while j > 0 and target < A[j-1]:
            A[j] = A[j-1]               #shift elements up list to make room for insertion  
            j = j-1

        A[j] = target                   #the location is found; insert the target 
        
#----------------------------------------------------------------------------------------------------------------
def insertionSort1(A, n):
#sort an array of n integer elements using insertion sort algorithm

#insertion sort orders sublists A[0], . . .,A[i].  1 <= i <= n-1.
#for each i, insert A[i] in the correct postition A[j+1] 

    for i in range(1, n):              #i identifies the sublist A[0] to A[i] 

        #index j scans down list from A[i-1] looking for correct position to locate target.
        # assigns it to A[j+1]
        target = A[i]
        j = i-1
         
        #locate insertion point by scanning downward as long as target < A[j] and we have not encountered
        #the beginning of the list
        while j >= 0 and target < A[j]:
            A[j+1] = A[j]               #shift elements up list to make room for insertion  
            j = j-1

        A[j+1] = target                 #the location is found; insert target to A[j+1] 
        
#----------------------------------------------------------------------------------------------------------------
def bubbleSort(A, n):
#sort an array of n integer elements using bubble sort algorithm

    i = n-1                       #i is the index of last element in the sublist

    while i > 0:                  #continue the process until no exchagnes are made
        lastExchangeIndex = 0     #start lastExchagneIndex at 0 

        for j in range(0, i):     #scan the subliat A[0] to A[i]
            if A[j] > A[j+1]:     #exchange a pair and update lastExchangeIndex 
                swap (A, j, j+1)
                lastExchangeIndex = j

        i = lastExchangeIndex     #set i to index of the last exchange. Continue sorting the sublist A[0] to A[i]  

#----------------------------------------------------------------------------------------------------------------
def bubbleSort1(A, n):
#sort an array of n integer elements using bubble sort algorithm

    for i in range(0, n-1):
        for j in range(0, n-i-1):    
            if A[j] > A[j+1]:     
                swap (A, j, j+1)
                
#----------------------------------------------------------------------------------------------------------------
def swap(A, i, j):
#interchange the values of A[i] and A[j]
    temp = A[i]      
    A[i] = A[j]     
    A[j] = temp       

          
#-------------------------------------------------------------------------------------------------------------
def printList(A, n):
    for i in range(0, n):
        print (A[i], end = ' ')
    print ()
    print ()

#-------------------------------------------------------------------------------------------------------------
def split (A, low, high):
# split the list into two sublists
# rearranges the list so that the pivot is properly positioned at A[pos]

    middle = (low + high) // 2   # get the mid index and assign its value to pivot
    pivot = A[middle]
    swap(A, middle, low)        # exchange the pivot with the first item
     
    left = low + 1              # index for left search
    right = high                # index for right search

    while left <= right:
        # search from left for element > pivot
        while left <= right and A[left] <= pivot:
            left = left + 1

        # search from right for element <= pivot
        while A[right] > pivot:
            right = right - 1

        # interchange elements if left and right have not passed each other
        if left < right:
            swap(A, left, right)
	
	
    # end of searches; place pivot in correct position
    pos = right
    A[low] = A[right]
    A[pos] = pivot

    return pos                  # pos is the final position of pivot 
	
#-------------------------------------------------------------------------------------------------------------
def quickSort(A, low, high):
# sort array elements A[low], . . ., A[high] using quick sort algorithm
    if low < high:                   # list has more than one element
        pos = split(A, low, high)    # split into two sublists; pos is the final position of pivot
        quickSort(A, low, pos-1)     # sort left sublist
        quickSort(A, pos+1, high)    # sort right sublist
   
    # else list has 0 or 1 element and requires no sorting

#-------------------------------------------------------------------------------------------------------------
def partition (A, first, last):
# partition list into two sublists
# rearranges the list so that the pivot is properly positioned 

    # find the pivot and exchange it with the last item
    middle = (first + last) // 2
    pivot = A[middle]
    swap(A, middle, last)
    
    # set boundary point to first position
    boundary = first

    # move items less than pivot to the left
    for index in range(first, last):
        if A[index] < pivot:
            swap(A, index, boundary)
            boundary = boundary + 1

    # exchange the pivot item and the boundary item
    swap(A, last, boundary)

    return boundary          # final position of pivot
	
#-------------------------------------------------------------------------------------------------------------
def quickSort1(A, first, last):
# sort array elements A[first], . . ., A[last] using quick sort algorithm
    if first < last:                  # list has more than one element
        pivotLocation = partition(A, first, last)   # partition into two sublists
        quickSort1(A, first, pivotLocation-1)    # sort left sublist
        quickSort1(A, pivotLocation+1, last)     # sort right sublist
   
    # else list has 0 or 1 element and requires no sorting

#-------------------------------------------------------------------------------------------
def quickSort2(array):
# sort elements in array using quick sort algorithm

    if len(array) <= 1:  # list of 0 or 1 element do not require sorting
        return array
    else:
        pivot = array.pop(0)  # select and remove pivot value (1st value)
        less = []             # create empty subarrays less and greater
        greater = []

        # append each item into appropriate subarray
        for item in array:
            if item < pivot:
                less.append(item)
            else:
                greater.append(item)

        return quickSort2(less) + [pivot] + quickSort2(greater)

#-------------------------------------------------------------------------------------------

def main():
   
    A = [38, 58, 13, 15, 51, 27, 10, 19, 12, 86, 49, 67, 84, 60, 25]
    n = len(A)
    
    print ("Original List: ")
    printList(A, n)

    print ("Insertion Sort: ")
    insertionSort(A, n)

    print ("Sorted List: ")
    printList (A, n)
    print ("==============================================================")
    #--------------------------------------------------------------------
    A = [38, 58, 13, 15, 51, 27, 10, 19, 12, 86, 49, 67, 84, 60, 25]
    n = len(A)
    
    print ("Original List: ")
    printList(A, n)

    print ("Insertion Sort 1: ")
    insertionSort1(A, n)

    print ("Sorted List: ")
    printList (A, n)
    print ("==============================================================")
    #--------------------------------------------------------------------
    A = [38, 58, 13, 15, 51, 27, 10, 19, 12, 86, 49, 67, 84, 60, 25]
    n = len(A)

    print ("Original List: ")
    printList(A, n)

    print ("Bubble Sort: ")
    bubbleSort(A, n)

    print ("Sorted List: ")
    printList (A, n)
    print ("==============================================================")
    #--------------------------------------------------------------------
    A = [38, 58, 13, 15, 51, 27, 10, 19, 12, 86, 49, 67, 84, 60, 25]
    n = len(A)

    print ("Original List: ")
    printList(A, n)

    print ("Bubble Sort 1: ")
    bubbleSort1(A, n)

    print ("Sorted List: ")
    printList (A, n)
    print ("==============================================================")
    #--------------------------------------------------------------------
    A = [38, 58, 13, 15, 51, 27, 10, 19, 12, 86, 49, 67, 84, 60, 25]
    n = len(A)
    
    print ("Original List: ")
    printList(A, n)

    print ("Quick Sort: ")
    quickSort(A, 0, n-1)

    print ("Sorted List: ")
    printList (A, n)
    print ("==============================================================")
    #--------------------------------------------------------------------
    A = [38, 58, 13, 15, 51, 27, 10, 19, 12, 86, 49, 67, 84, 60, 25]
    n = len(A)
    
    print ("Original List: ")
    printList(A, n)

    print ("Quick Sort 1: ")
    quickSort1(A, 0, n-1)

    print ("Sorted List: ")
    printList (A, n)
    print ("==============================================================")
    #--------------------------------------------------------------------
    A = [38, 58, 13, 15, 51, 27, 10, 19, 12, 86, 49, 67, 84, 60, 25]
    n = len(A)
    
    print ("Original List: ")
    printList(A, n)

    print ("Quick Sort 2: ")
    sortedA = quickSort2(A)

    print ("Sorted List: ")
    printList (sortedA, n)
    print ("==============================================================")
    #--------------------------------------------------------------------

main()
                      
    
