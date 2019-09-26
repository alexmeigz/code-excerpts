#sorting algorithms

def swapElements(lyst, ind1, ind2):
    '''swaps two elements of a list given two indices'''
    tempVar = lyst[ind1]
    lyst[ind1] = lyst[ind2]
    lyst[ind2] = tempVar
    return lyst


def bubbleSort(lyst):
    '''O(n^2); runs through entire list in two nested loops:
    the inner loop checks if the following element is larger, if so, swap
    the outer loop repeats the inner loop, skipping the nth beginning elements
    knowing that they are sorted after nth iterations of the inner loop'''
    for i in range(len(lyst)):
        for j in range(len(lyst))[i:len(lyst)-1]:
            if lyst[j] > lyst[j+1]:
                swapElements(lyst, j, j+1)    
    return lyst

def selectionSort(lyst):
    '''O(n^2); runs through entire list in two nested loops:
    the outer loop initializes the smallest index of each iteration,
    the inner loop checks to see if any subsequent elements after the smallest
    is smaller, if so, it replaces the indexOfSmallest; after the loop iterates
    through all unsorted elements, the nth smallest element is swapped with the
    nth element, the first unsorted element in the nth iteration of i'''
    for i in range(len(lyst)):
        indexOfSmallest = i
        for j in range(len(lyst))[i:]:
            if lyst[j] < lyst[indexOfSmallest]:
                indexOfSmallest = j
        swapElements(lyst, indexOfSmallest, i)
    return lyst

def insertionSort(lyst):
    '''O(n^2); The nth iteration of the for loop guarantees the first n elements
    of the are sorted; the next unsorted element is taken in each iteration
    and inserted to the sorted portion of the list if when it finds that it
    is larger than the preceding element (swap if smaller than precedent) '''
    for i in range(len(lyst)-1):
        tracker = i
        while tracker > -1:
            if lyst[tracker+1] < lyst[tracker]:
                swapElements(lyst, tracker+1, tracker)
            tracker -= 1
    return lyst

def mergeSort(lyst):
    '''O(nlogn) There are log (base 2) n divisions into equal partitions of two
    lysts, until they reach len = 1, and n comparisons while merging back into
    a full sorted lyst; compares the first two elements from two merging lysts,
    which are guaranteed to be the smallest, until the entire list is used'''
    if len(lyst) == 1:
        return lyst
    else:
        division = len(lyst) // 2
        return merge(mergeSort(lyst[:division]), mergeSort(lyst[division:]))
    

def merge(llyst, rlyst):
    lyst = []
    while len(llyst) != 0 or len(rlyst) != 0:
        if len(llyst) == 0:
            lyst.append(rlyst.pop(0))
        elif len(rlyst) == 0:
            lyst.append(llyst.pop(0))
        elif llyst[0] < rlyst[0]:
            lyst.append(llyst.pop(0))
        else:
            lyst.append(rlyst.pop(0))
    return lyst
    
def quickSort(lyst):
    '''O(nlogn) or O(n^2) worst case**; partition is picked and elements are
    swapped from if the elements on the left are bigger and elements on the right
    are smaller than the pivot point; the partition then sets divide for quickSort
    to call recursively on both sides; repeats until the list is length 1 in which
    case its sorted; best case is O(nlogn) due to log n splits and a linear number
    of comparisons; worst case is O(n^2) since there will be n splits and n
    linear comparisons'''
    if len(lyst) == 1:
        return lyst
    pivot = lyst[0]
    leftIndex = 0
    rightIndex = len(lyst) - 1
    while rightIndex >= leftIndex:
        if pivot < lyst[leftIndex] and pivot > lyst[rightIndex]:
            swapElements(lyst, leftIndex, rightIndex)
            leftIndex += 1
            rightIndex -= 1
        else:
            if pivot >= lyst[leftIndex]:
                leftIndex += 1
            if pivot <= lyst[rightIndex]:
                rightIndex -= 1

    #case where the pivot is the extreme
    if leftIndex == len(lyst):
        return quickSort(lyst[1:]) + [pivot]
    
    return quickSort(lyst[:leftIndex]) + quickSort(lyst[rightIndex+1:])

def heapSort(lyst):
    '''O(nlogn); logn time to trickle down where trickleDown is called n
    times after swapping elements into place n * log n since it trickles
    down log n height with 2 comparisons max each; n time to build the heap
    lowest level of heap has constant time, highest level of heap has max
    log n time, but only has constant (1) amount of elements --> O(n); builds
    heap by checking if there are both childs, if so, finds larger, and if
    parent is smaller, swaps the child and parent and parent trickles down.'''
    buildHeap(lyst)
    return sortHeap(lyst)

def buildHeap(lyst):
    for i in range(len(lyst)):
        index = len(lyst) - i - 1
        leftIndex = 2 * index + 1
        rightIndex = 2 * index + 2

        if rightIndex < len(lyst):
            if lyst[leftIndex] > lyst[rightIndex]:
                largestChildIndex = leftIndex
            else:
                largestChildIndex = rightIndex
                
            if lyst[largestChildIndex] > lyst[index]:
                swapElements(lyst, largestChildIndex, index)
                trickleDown(lyst, largestChildIndex)

def trickleDown(lyst, index):
    leftIndex = 2 * index + 1
    rightIndex = 2 * index + 2

    if not leftIndex < len(lyst):
        return
    elif not rightIndex < len(lyst):
        if lyst[leftIndex] > lyst[index]:
            swapElements(lyst, leftIndex, index)
            trickleDown(lyst, leftIndex)
        return
    else:
        if lyst[leftIndex] > lyst[rightIndex]:
            largestChildIndex = leftIndex
        else:
            largestChildIndex = rightIndex
                
        if lyst[largestChildIndex] > lyst[index]:
                swapElements(lyst, largestChildIndex, index)
                trickleDown(lyst, largestChildIndex)
    
def sortHeap(lyst):
    sortedLyst = []
    initialLen = len(lyst)
    for i in range(initialLen):
        swapElements(lyst, 0, len(lyst)-1)
        sortedLyst.insert(0, lyst.pop())
        trickleDown(lyst, 0)
    return sortedLyst



