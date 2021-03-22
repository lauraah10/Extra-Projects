#  File: linkedLists.py
#  Description: The program does different functions for linked lists 
#  Student's Name: Laura Ahumada
#  Student's UT EID: laa2336
#  Course Name: CS 313E 
#  Unique Number: 50597
#
#  Date Created: November 10, 2015
#  Date Last Modified: Novembe 13, 2015

#creating the Node
class Node(object):
    def __init__(self,initData):
        self.data=initData
        self.next=None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self,newData):
        self.data=newData
    def setNext(self, newNext):
        self.next=newNext

class LinkedList(object):
    #initializing the list
    def __init__(self):
        self.head=None

        
    def getLength (self):
         current=self.head
         count=0
         #counting until it hits the end which is (NONE)
         while current!=None:
             count=count + 1
             #changing to the next node
             current=current.getNext()
         return count
        
    # Add an item to the beginning of the list      
    def addFirst (self, item): 
         #creating the node
         temp=Node(item)
         #adding it to the begining of th list
         temp.setNext(self.head)
         self.head=temp

    def addLast (self, item):
        current = self.head
        # to keep track of where you are
        previous = None

        # goes through the nodes in the list until it point to the end
        while current != None :
            previous = current
            current = current.getNext()
            
        #create the node
        temp = Node(item)

        #it is now pointing at the end so 
        #   if there is a previous it at the end
        if previous != None:
            temp.setNext(current)
            previous.setNext(temp)
        #if there is no previous make the head the node
        else:
            temp.setNext(current)
            self.head = temp


    def __str__(self):
     # Return a string representation of data suitable for printing.
     #    Long lists (more than 10 elements long) should be neatly
     #    printed with 10 elements to a line, two spaces between
     #    elements
        current=self.head
        #the new string 
        save=""
        while(current!=None):
            #saving each data into the string
            save=save+" " +(str(current.getData()))
            #if it hits 10 elements then go to the next line
            if len(save.split())%10==0:
                save=save + " " + "\n"
            #change pointer
            current=current.getNext()
        #return the string of the elements
        return((save))

    def addInOrder (self, item):
     # Insert an item into the proper place of an ordered list.
     # This assumes that the original list is already properly
     #    ordered.
        #tracks where the pointer should stop
        flag=True

        #keeps track
        current=self.head
        previous=None
        #while it doesn't hits the end and hasn't found the location to enter the item
        while current!=None and flag:
            #once it gets to the first item that is larger we have found our spot to add
             if current.getData()>item:
                 #change flag to get out of loop
                 flag=False
             else:
                 #change pointers
                 previous=current
                 current=current.getNext()
                 
        #create the node
        temp = Node(item)
        #if there is a previous change pointers adding the new node
        if previous != None:
            temp.setNext(current)
            previous.setNext(temp)
        #if there is no previous make the node the head
        else:
            temp.setNext(current)
            self.head = temp
        

    def findUnordered (self, item): 
     # Search in an unordered list
     #    Return True if the item is in the list, False
     #    otherwise.
        current=self.head
        #gets data for each of the nodes
        while(current!=None):
            #if data is equal to the item
            #it is in the list! so it found it we return true and leave the loop
            if (current.getData())==item:
                return True
            else:
                #we move to the next
                current=current.getNext()
        #it didn't find it so return False
        return False
    
    def findOrdered (self, item): 
     # Search in an ordered list
     #    Return True if the item is in the list, False
     #    otherwise.
     # This method MUST take advantage of the fact that the
     #    list is ordered to return quicker if the item is not
     #    in the list
        current=self.head
        #goes through the list
        while(current!=None):
            #if the data equals the item we found it in the list
            #we leave by returning True
            if current.getData()==item:
                return True
            else:
                #since its in order if it hit a point where data is larger than item
                # there is no point of continuing so we return False 
                if(current.getData())>item:
                    return False
                else:
                    #change pointer
                    current=current.getNext()
        #it didn't find it 
        return False
    
    def delete (self, item):
     # Delete an item from an unordered list
     #    if found, return True; otherwise, return False
        #keeps track
        current=self.head
        previous=None
        found=False
        #throught the list
        while current!=None:
            #item found! we are where we want to be so we get out 
            if current.getData()==item:
                found=True
                break
            else:
                #move pointer
                previous=current
                current=current.getNext()
        #didn't find it if found is false
        if found==False:
            return False
        #if there is no previous set self head
        elif previous==None:
            self.head=current.getNext()
            return True
        #else just change the pointer leaving out(removing) the one we want to delete
        else:
            previous.setNext(current.getNext())
            return True
            

    def copyList (self):
     # Return a new linked list that's a copy of the original,
     #    made up of copies of the original elements
        current=self.head
        #create the new list
        new=LinkedList()
        previous=None
        #going through the list
        while(current!=None):
            #add the current at  last
            new.addLast(current.getData())
            #change pointers
            previous=current
            current=current.getNext()
        return new


    def reverseList (self): 
     # Return a new linked list that contains the elements of the
     #    original list in the reverse order.
     
          current=self.head
          #new list
          new=LinkedList()
          #keep track of location
          previous=None

          while current != None:
            # add the current item at the begining of the new list
            new.addFirst(current.getData())
         
            # change pointers
            previous=current
            current = current.getNext()
         #return the new reverse list
          return new

    def sortList (self): 
     # Return a new linked list that contains the elements of the
     #    original list, sorted into ascending (alphabetical) order.
     #    Do NOT use a sort function:  do this by iteratively
     #    traversing the first list and then inserting copies of
     #    each item into the correct place in the new list.
         #track of location
          current=self.head
          #new list
          new=LinkedList()
          previous=None

          while current != None:
            #add in order each of the current data into our new list
            new.addInOrder(current.getData())
            #change pointers
            previous=current
            current = current.getNext()
            
        
          return new

    def isEmpty(self):
        #if self.head is None then its empty
        return self.head==None
    
    def isSorted (self):
     # Return True if a list is sorted in ascending (alphabetical)
     #    order, or False otherwise
         #new sorted list to compare and see if the current one is sorted
          newSorted=self.sortList()
          #pointers of self and of the new
          currentNew=newSorted.head
          current=self.head
          previous=None
          previousNew=None
         #going through the list
          while current != None:
            #the sorted one and the self shoul be equal if not then it isn't sorted
            if currentNew.getData()!=current.getData():
                return False
            # change pointers of both self and new
            previous=current
            current = current.getNext()
            previousNew=currentNew
            currentNew=currentNew.getNext()
         
          return True

    
                    
    def mergeList (self, b): 
     # Return an ordered list whose elements consist of the 
     #    elements of two ordered lists combined.
             #new list that already consist of self's items
             new=self.copyList()
             #pointers
             currentB=b.head
             previousB=None
            #append each of the items in b in orderd in the already copy made list of self
             while currentB!=None:
                new.addInOrder(currentB.getData())
                #change pointer
                previous=currentB
                currentB = currentB.getNext()
            #retirm merge list
             return new

    def isEqual (self, b):
     # Test if two lists are equal, item by item, and return True.
         #to keep track of both self and b
          currentB=b.head
          current=self.head
          previous=None
          previousB=None

          while current != None and currentB!=None:
            #print(currentB.getData(),current.getData())
            #if both data are not equal then they are not equal
            if currentB.getData()!=current.getData():
                return False
            # change pointer of both self and b
            previous=current
            current = current.getNext()
            previousB=currentB
            currentB=currentB.getNext()
          if self.getLength()!=b.getLength():
              return False
          else:
              return True


    def removeDuplicates (self):
     # Modify a list, keeping only the first occurrence of an element
     #    and removing all duplicates.  Do not change the order of
     #    the remaining elements.
         #keeps a list of the items already mentioned to find duplicates
         elements=[]
         #to keep track
         current=self.head
         previous=None

         
         while current!=None:
             #if the data is already in the list we remove it
             if current.getData() in elements:
                #changing pointer of previous skipping/removing the one we want to remove 
                if previous==None:
                    self.head=current.getNext()
                else:
                    previous.setNext(current.getNext())
                 
             else:
                 #else we just make previous the current
                 previous=current
            #we add the data to our list of elements that keeps track of the ones already in it
             elements.append(current.getData())
             #change pointer
             current=current.getNext()
         return self
         
                 

         
             


    
        
def main():

   print ("\n\n***************************************************************")
   print ("Test of addFirst:  should see 'node34...node0'")
   print ("***************************************************************")
   myList1 = LinkedList()
   for i in range(35):
      myList1.addFirst("node"+str(i))

   print (myList1)

   print ("\n")
   
   print ("LENGTH")
   print (myList1.getLength())


   print ("\n\n***************************************************************")
   print ("Test of addLast:  should see 'node0...node34'")
   print ("***************************************************************")
   myList2 = LinkedList()
   for i in range(35):
      myList2.addLast("node"+str(i))

   print (myList2)

   print ("\n\n***************************************************************")
   print ("Test of addInOrder:  should see 'alpha delta epsilon gamma omega'")
   print ("***************************************************************")
   greekList = LinkedList()
   greekList.addInOrder("gamma")
   greekList.addInOrder("delta")
   greekList.addInOrder("alpha")
   greekList.addInOrder("epsilon")
   greekList.addInOrder("omega")
   print (greekList)

   print ("\n\n***************************************************************")
   print ("Test of getLength:  should see 35, 5, 0")
   print ("***************************************************************")
   emptyList = LinkedList()
   print ("   Length of myList1:  ", myList1.getLength())
   print ("   Length of greekList:  ", greekList.getLength())
   print ("   Length of emptyList:  ", emptyList.getLength())

   
   print ("\n\n***************************************************************")
   print ("Test of findUnordered:  should see True, False")
   print ("***************************************************************")
   print ("   Searching for 'node25' in myList2: ",myList2.findUnordered("node25"))
   print ("   Searching for 'node35' in myList2: ",myList2.findUnordered("node35"))

   print ("\n\n***************************************************************")
   print ("Test of findOrdered:  should see True, False")
   print ("***************************************************************")
   print ("   Searching for 'epsilon' in greekList: ",greekList.findOrdered("epsilon"))
   print ("   Searching for 'omicron' in greekList: ",greekList.findOrdered("omicron"))

   print ("\n\n***************************************************************")
   print ("Test of delete:  should see 'node25 found', 'node34 found',")
   print ("   'node0 found', 'node40 not found'")
   print ("***************************************************************")
   print ("   Deleting 'node25' (random node) from myList1: ")
   if myList1.delete("node25"):
      print ("      node25 found")
   else:
      print ("      node25 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("   Deleting 'node34' (first node) from myList1: ")
   if myList1.delete("node34"):
      print ("      node34 found")
   else:
      print ("      node34 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("   Deleting 'node0'  (last node) from myList1: ")
   if myList1.delete("node0"):
      print ("      node0 found")
   else:
      print ("      node0 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("   Deleting 'node40' (node not in list) from myList1: ")
   if myList1.delete("node40"):
      print ("      node40 found")
   else:
      print ("   node40 not found")
   print ("   myList1:  ")
   print (myList1)

   
   print ("\n\n***************************************************************")
   print ("Test of copyList:")
   print ("***************************************************************")
   greekList2 = greekList.copyList()
   print("\n\n")
   print ("   These should look the same:")
   print ("      greekList before delete:")
   print (greekList)
   print ("      greekList2 before delete:")
   print (greekList2)
   print("\n\n")
   greekList2.delete("alpha")
   print("\n\n")
   print ("   This should only change greekList2:")
   print ("      greekList after deleting 'alpha' from second list:")
   print (greekList)
   print ("      greekList2 after deleting 'alpha' from second list:(THIS ONE IS CHANGED)")
   print (greekList2)
   print("\n\n")
   greekList.delete("omega")
   print ("   This should only change greekList1:")
   print ("      greekList after deleting 'omega' from first list:")
   print (greekList)
   print ("      greekList2 after deleting 'omega' from first list:")
   print (greekList2)

   print ("\n\n***************************************************************")
   print ("Test of reverseList:  the second one should be the reverse")
   print ("***************************************************************")
   print ("   Original list:")
   print (myList1)
   print ("   Reversed list:")
   myList1Rev = myList1.reverseList()
   print (myList1Rev)

   print ("\n\n***************************************************************")
   print ("Test of sortList:  the second list should be the first one sorted")
   print ("***************************************************************")
   planets = LinkedList()
   planets.addFirst("Mercury")
   planets.addFirst("Venus")
   planets.addFirst("Earth")
   planets.addFirst("Mars")
   planets.addFirst("Jupiter")
   planets.addFirst("Saturn")
   planets.addFirst("Uranus")
   planets.addFirst("Neptune")
   planets.addFirst("Pluto!")

   print ("   Original list:")
   print (planets)
   print ("   Sorted list:")
   sortedPlanets = planets.sortList()
   print (sortedPlanets)

   print ("\n\n***************************************************************")
   print ("Test of isSorted:  should see False, True")
   print ("***************************************************************")
   print ("   Original list:")
   print (planets)
   print ("   Sorted: ", planets.isSorted())
   sortedPlanets = planets.sortList()
   print ("   After sort:")
   print (sortedPlanets)
   print ("   Sorted: ", sortedPlanets.isSorted())

   print ("\n\n***************************************************************")
   print ("Test of isEmpty:  should see True, False")
   print ("***************************************************************")
   newList = LinkedList()
   print ("New list (currently empty):", newList.isEmpty())
   newList.addFirst("hello")
   print ("After adding one element:",newList.isEmpty())

   print ("\n\n***************************************************************")
   print ("Test of mergeList")
   print ("***************************************************************")
   list1 = LinkedList()
   list1.addLast("aardvark")
   list1.addLast("cat")
   list1.addLast("elephant")
   list1.addLast("fox")
   list1.addLast("lynx")
   print ("   first list:")
   print (list1)
   list2 = LinkedList()
   list2.addLast("bacon")
   list2.addLast("dog")
   list2.addLast("giraffe")
   list2.addLast("hippo")
   list2.addLast("wolf")
   print ("   second list:")
   print (list2)
   print ("   merged list:")
   list3 = list1.mergeList(list2)
   print (list3)

   print ("\n\n***************************************************************")
   print ("Test of isEqual:  should see True, False, True")
   print ("***************************************************************")
   print ("   First list:")
   print (planets)
   planets2 = planets.copyList()
   print ("   Second list:")
   print (planets2)
   print ("      Equal:  ",planets.isEqual(planets2))
   print (planets)
   planets2.delete("Mercury")
   print ("   Second list:")
   print (planets2)
   print ("      Equal:  ",planets.isEqual(planets2))
   print ("   Compare two empty lists:")
   emptyList1 = LinkedList()
   emptyList2 = LinkedList()
   print ("      Equal:  ",emptyList1.isEqual(emptyList2))

   print ("\n\n***************************************************************")
   print ("Test of removeDuplicates:  original list has 14 elements, new list has 10")
   print ("***************************************************************")
   dupList = LinkedList()
   print ("   removeDuplicates from an empty list shouldn't fail")
   newList = dupList.removeDuplicates()
   print ("   printing what should still be an empty list:")
   print (newList)
   dupList.addLast("giraffe")
   dupList.addLast("wolf")
   dupList.addLast("cat")
   dupList.addLast("elephant")
   dupList.addLast("bacon")
   dupList.addLast("fox")
   dupList.addLast("elephant")
   dupList.addLast("wolf")
   dupList.addLast("lynx")
   dupList.addLast("elephant")
   dupList.addLast("dog")
   dupList.addLast("hippo")
   dupList.addLast("aardvark")
   dupList.addLast("bacon")
   print ("   original list:")
   print (dupList)
   print ("   without duplicates:")
   newList = dupList.removeDuplicates()
   print (newList)
main()
