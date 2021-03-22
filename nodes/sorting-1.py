#  File: sorting.py
#  Description: Calculates the average execution time of each of the sorting methods in each of the 3 different length list, for each of the different orders(sorted, reversed and random)
#  Student's Name:Laura Ahumada
#  Student's UT EID: laa2336
#  Course Name: CS 313E 
#  Unique Number: 50597
#
#  Date Created: 12/01/15
#  Date Last Modified: 12/03/15

import random
import time
import sys
sys.setrecursionlimit(10000)

#sorting functions
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

def selectionSort(alist):
    for fillslot in range(len(alist)-1,0,-1):
        positionOfMax = 0
        for location in range(1,fillslot+1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location
        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp


def insertionSort(alist):
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index

        while position>0 and alist[position-1]>currentvalue:
            alist[position] = alist[position-1]
            position = position-1

        alist[position] = currentvalue

def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist,startposition,sublistcount)
        sublistcount = sublistcount // 2

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):
        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position] = alist[position-gap]
            position = position - gap

        alist[position] = currentvalue

def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0

        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1

def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
    if first < last:
        splitpoint = partition(alist,first,last)
        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):
    pivotvalue = alist[first]
    leftmark = first + 1
    rightmark = last
    done = False

    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark += 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark -= 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark
def timingBubbleSort (myList):
      sumtime=0
      for i in range (5):
          startTime = time.perf_counter()
          bubbleSort(myList)
          endTime = time.perf_counter()
          elapsedTime = endTime - startTime
          sumtime=sumtime+elapsedTime
      average=sumtime/5
      return average
        
def timingSelectionSort(myList):
      sumtime=0
      for i in range (5):
          startTime = time.perf_counter()
          selectionSort(myList)
          endTime = time.perf_counter()
          elapsedTime = endTime - startTime
          sumtime=sumtime+elapsedTime
      average=sumtime/5
      return average

def timingInsertionSort(myList):
      sumtime=0
      for i in range (5):
          startTime = time.perf_counter()
          insertionSort(myList)
          endTime = time.perf_counter()
          elapsedTime = endTime - startTime
          sumtime=sumtime+elapsedTime
      average=sumtime/5
      return average


def timingShellSort(myList):
      sumtime=0
      for i in range (5):
          startTime = time.perf_counter()
          shellSort(myList)
          endTime = time.perf_counter()
          elapsedTime = endTime - startTime
          sumtime=sumtime+elapsedTime
      average=sumtime/5
      return average

    
def timingMergeSort(myList):
      sumtime=0
      for i in range (5):
          startTime = time.perf_counter()
          mergeSort(myList)
          endTime = time.perf_counter()
          elapsedTime = endTime - startTime
          sumtime=sumtime+elapsedTime
      average=sumtime/5
      return average

    
def timingQuickSort(myList):
      sumtime=0
      for i in range (5):
          startTime = time.perf_counter()
          quickSort(myList)
          endTime = time.perf_counter()
          elapsedTime = endTime - startTime
          sumtime=sumtime+elapsedTime
      average=sumtime/5
      return average


def main():

      #initializing a list for the average of specific sorting methods
      # the results are saved here to at the end print it      
      bubbleAvr=[]
      selectionAvr=[]
      insertionAvr=[]
      shellAvr=[]
      mergeAvr=[]
      quickAvr=[]

      #Creating the sorted lists
      myList10=[i for i in range (10)]
      myList100=[i for i in range (100)]
      myList1000=[i for i in range (1000)]

      #making the different lists a tupple
      listoflist=[myList10,myList100,myList1000]

      #iterating over the tupple that has the the list of 10, the list of 100 and the list of 1000
      for i in listoflist:
          #calling each of the functions that will calculate the average
          # saving each result by appending it to their corresponding list type
          bubbleAvr.append(timingBubbleSort(i))
          selectionAvr.append(timingSelectionSort(i))
          insertionAvr.append(timingInsertionSort(i))
          shellAvr.append(timingShellSort(i))
          mergeAvr.append(timingMergeSort(i))
          quickAvr.append(timingQuickSort(i))

      #reversing each of the 10, 100, and 1000 items lists
      myList10.reverse()
      myList100.reverse()
      myList100.reverse()
      
      #iterating over the changed tupple that has the reversed lists of 10, 100 and 1000
      for i in listoflist:
          #calling each of the functions that will calculate the average
          # saving each result by appending it to their corresponding list type
          bubbleAvr.append(timingBubbleSort(i))
          selectionAvr.append(timingSelectionSort(i))
          insertionAvr.append(timingInsertionSort(i))
          shellAvr.append(timingShellSort(i))
          mergeAvr.append(timingMergeSort(i))
          quickAvr.append(timingQuickSort(i))
          
      #randomizing each of the lists
      random.shuffle(myList10)
      random.shuffle(myList100)
      random.shuffle(myList1000)

      #iterating over the changed tupple that has the reversed lists of 10, 100 and 1000
      for i in listoflist:
          #calling each of the functions that will calculate the average
          # saving each result by appending it to their corresponding list type
          bubbleAvr.append(timingBubbleSort(i))
          selectionAvr.append(timingSelectionSort(i))
          insertionAvr.append(timingInsertionSort(i))
          shellAvr.append(timingShellSort(i))
          mergeAvr.append(timingMergeSort(i))
          quickAvr.append(timingQuickSort(i))

      
    
      #initializing the location of where the results for the different types of results relie on the average list
      # we know that the first 3 elements of each of the average list contains the results for sorted, that the next three are the results
      # for reversed, and the rest are the results for Random.
      # since we are starting by printing the Random results we know that it starts at index 6 so that is why we initialize the location at 6
      l=6

      #the names of the types of list to be printed
      names=["Random", "Sorted", "Reverse"]

      #iterating over each type, to be printed in order
      for type_ in range (3):
          #printing  how we want the output to look  with the iterating names and results
          print("Input type = " + names[type_] )  
          print("                     avg time   avg time   avg time" )
          print("      Sort function      (n=10)    (n=100)    (n=1000)")
          print("-----------------------------------------------------")
          print ("       bubbleSort     {0:0.6f}    {1:0.6f}    {2:0.6f}".format(bubbleAvr[l],bubbleAvr[l+1], bubbleAvr[l+2]))
          print ("    selectionSort     {0:0.6f}    {1:0.6f}    {2:0.6f}".format(selectionAvr[l],selectionAvr[l+1], selectionAvr[l+2]))
          print ("    insertionSort     {0:0.6f}    {1:0.6f}    {2:0.6f}".format(insertionAvr[l],insertionAvr[l+1], insertionAvr[l+2]))
          print ("        shellSort     {0:0.6f}    {1:0.6f}    {2:0.6f}".format(shellAvr[l],shellAvr[l+1], shellAvr[l+2]))
          print ("        mergeSort     {0:0.6f}    {1:0.6f}    {2:0.6f}".format(mergeAvr[l],mergeAvr[l+1], mergeAvr[l+2]))
          print ("        quickSort     {0:0.6f}    {1:0.6f}    {2:0.6f}".format(quickAvr[l],quickAvr[l+1], quickAvr[l+2]))
          #the  results for the Sorted results start from index 0 and we know that if the location is 6 we just printed Random so we
          # change the location to 0 to then print the results for sorted
          if l+3==9:
              l=0
          #the results for reverse are the ones that follow therefore we just move the location to 3 more over
          else:
              l=l+3
          print("\n")

        
          
          


















      
      
main()

