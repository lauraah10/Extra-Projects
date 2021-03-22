#  File: playpoker.py
#  Description: Plays a simple version of poker. Generating the hands, classifying them and telling who the winner is
#  Course Name: CS 313E 
#  Date Created: September 18, 2015
#  Date Last Modified: September 25, 2015

# import the random number generator
# this is needed to shuffle the cards into a random order

import random

class Card (object):
  RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

  SUITS = ('C', 'D', 'H', 'S')

  def __init__ (self, rank, suit):
    # each Card object consists of two attributes: a rank
    #    and a suit
    self.rank = rank
    self.suit = suit

  def getitem (self,index):
    return self.item[index]
    
  def __str__ (self):
    # print J, Q, K, A instead of 11, 12, 13, 14
    if self.rank == 14:
      rank = 'A'
    elif self.rank == 13:
      rank = 'K'
    elif self.rank == 12:
      rank = 'Q'
    elif self.rank == 11:
      rank = 'J'
    else:
      rank = self.rank
    return str(rank) + self.suit

  # you'll find the following methods to be useful:  they 
  #    allow you to compare Card objects

  def __eq__ (self, other):
    return (self.rank == other.rank)

  def __ne__ (self, other):
    return (self.rank != other.rank)

  def __lt__ (self, other):
    return (self.rank < other.rank)

  def __le__ (self, other):
    return (self.rank <= other.rank)

  def __gt__ (self, other):
    return (self.rank > other.rank)

  def __ge__ (self, other):
    return (self.rank >= other.rank)


class Deck (object):

  def __init__ (self):
    # self.deck is the actual deck of cards
    # create it by looping through all SUITS and RANKS
    #    and appending them to a list
    self.deck = []
    for suit in Card.SUITS:
      for rank in Card.RANKS:
        card = Card (rank, suit)
        self.deck.append (card)      

  def shuffle (self):
    # the shuffle method in the random package reorders
    #    the contents of a list into random order
    random.shuffle (self.deck)

  def deal (self):
    # if the deck is empty, fail:  otherwise pop one
    #    card off and return it
    if len(self.deck) == 0:
      return None
    else:
      return self.deck.pop(0)

#Function that checks the hand is that certain type of rank 
def test (valueCards, typeCard):
  #Since the tupple is a string and can't be converted into an int because of "J Q K A"
  # we first need to change it to number strings
  #for each list in the tupple
  print("\n")
  for i in range(len(valueCards)):
    #for each str in the list change value to number strings
    for j in range(5):
      if valueCards[i][j]=="K":
        valueCards[i][j]="13"
      elif valueCards[i][j]=="Q":
        valueCards[i][j]="12"
      elif valueCards[i][j]=="J":
        valueCards[i][j]="11"
      elif valueCards[i][j]=="A":
        valueCards[i][j]="14"
      else:
        pass

  #now that we have to make the valueCards actual intergers to compare
  #for each list in the tupple
  for i in range(len(valueCards)):
    #for each string num in the tupple change to the actual number
    for j in range (5):
      valueCards[i][j]=int(valueCards[i][j])
    valueCards[i].sort()


  #now that we have the value of the cards as intergers we can start to check
  flag=True
  count=0
  pointsinitial=0
  tielist=[]
  
  #going through each list in the tupple
  for list_n in range (len(valueCards)):

    
    #will check if the hand is in order (if its straight)
    straight=checkStraight(valueCards[list_n])

    #if it is straight then we can check for either straight flush or royal flush
    if straight!=0:
      #checking if if has the same type card now to see if its a straight flush
      straightflush=checkStraightFlush(typeCard[list_n])
  
      #we know its in order that it has the same type of card now lets check if it starts with 10 
      if straightflush!=0:
        royalflush=checkRoyalFlush(valueCards[list_n])
        
        if royalflush!=0:
          print ("Hand ", list_n+1, ": Royal Flush")
          h=royalflush
          #we change the flag so we can print the highest category of the hand
          flag=False
        else:
          print ("Hand ", list_n+1, ": Sraight Flush")
          h=straightflush
          flag=False
       
    #a function that will check how many of a certain kind  it has
    #count being the times it appears and card_repeated being the card that appears that many times
    (count, card_repeated)=countCardRepeated(valueCards[list_n])

    #we will do the categories that involve a repetition of a  single card  in the hand having
    # already foundamount of times a card is repeated
    four_kind=checkFourKind(count)
    three_kind=checkThreeKind(count)
    one_pair=checkOnePair(count)

    #get the re-organized list
    #we know that for some categories the list will need to be in ascending order when checkingf for total points
    descendingvalues=valueCards[list_n]
    descendingvalues.reverse()
    check_pointlist=descendingvalues
    
    # we have to only print the one that has the highest points and when it comes to repetion four of a kind is the highest
    #therefore we start with it and change the flag so that one can know that this is the one that wins
    if four_kind!=0:
      print ("Hand ", list_n+1, ": Four of a Kind")
      h=four_kind
      #getting the new list for the total points
      check_pointtlist=fourkindlist(card_repeated, descendingvalues)
      flag=False
      
    
    #we will check how many of another certain kind it has
    (count2, card_repeated2)=countCardRepeated2(valueCards[list_n], count, card_repeated)
      
    #we know that full house and pairs involve two pairs 
    two_pair=checkTwoPair(count, count2)
    fullhouse=checkFullHouse(count, count2)

    #full house is higher in rank than 3 of a kind which could be sub category of a full house
    # therefore we want to get only the highest 
    if fullhouse!=0:
      print ("Hand ", list_n+1, ": Full House")
      h=fullhouse 
      flag=False
      #getting the new list for the total points
      check_pointtlist=fullhouselist(card_repeated, card_repeated, card_repeated2)
        
     
    #knowing it isn't a ful house we can check and print if its three of a kind
    elif three_kind!=0 and four_kind==0:
      print ("Hand ", list_n+1, ": Three of a Kind")
      h=three_kind

      check_pointlist=threekindlist(count, card_repeated, descendingvalues)
      flag=False
    #the only one left when it comes to 2 cards being repeated x times is two_pairs so we check
    elif two_pair!=0 and flag!=False:
      print ("Hand ", list_n+1, ": Two pair")
      h=two_pair
      check_pointlist=twopairlist(count, count2, card_repeated, card_repeated2, descendingvalues)
      flag=False
    elif (one_pair!=0 and flag!=False):
      print ("Hand ", list_n+1, ": One Pair")
      h=one_pair
      check_pointlist=pair_list(count, card_repeated, descendingvalues)
      flag=False


    #straight flush is higher so we need to makes sure that isn't straight flush to print, 
        #and that it is straight
    flush=checkFlush(typeCard[list_n])
    

    if flush!=0 and straightflush==0:
      print ("Hand ", list_n+1, ": Flush")
      h=flush
      flag=False
        
    if straight!=0 and straightflush==0:
      print ("Hand ", list_n+1, ": Straight")
      h=straight
      
    #the flag was set to see if it didn't go through the rest of the ranking
      #therefore if it is still true our last option to categorize it is High Card
    if flag==True:
      print ("Hand ", list_n+1, ": High Card")
      h=1

    #so it can go checking again through the new hand
    flag=True
      
    #formula to check the total point of the hands to compare later for the winner
    totalpoints=h * 13**5 + check_pointlist[0] * 13**4 + check_pointlist[1] * 13**3 + check_pointlist[2] * 13**2 + check_pointlist[3] *13 + check_pointlist[4]

    #keeping track who has the highest total points
    #saving the winner
    if pointsinitial<totalpoints:
      tielist=[]
      pointsinitial=totalpoints
      #since list_n starts at 0 the player has to be list_n +1
      winner=list_n+1
      #in case there are two players with the same total points we start adding to a list
      tielist.append(list_n+1)
    elif totalpoints==pointsinitial:
      #it is the same total points lets actually add to the formula so length of it is greater to 1
      # list of the players  with same total points
      tielist.append(list_n+1)
      
  print("\n")
  if (len(tielist)==1): 
    print("Hand ", winner, "wins" )
  else:
    print("Tie between players: ", tielist)
  #it will return the winner to main program
  return winner
     
   
def countCardRepeated (values_list):
  card_repeated=values_list[0]
  count=1
  index=[]
  for i in range (1,len(values_list)):
    if card_repeated==values_list[i]:
      count=count+1
    elif count==1:
      card_repeated=values_list[i]
    else:
      pass
  return (count, card_repeated)
  

def countCardRepeated2(valueCard, count, card_repeated):
  #if count is 0 then we don't need to check for other pair there is none
  if count==0:
    return 0

  #setting the first value of the card as the repeated one
  card_repeated2=valueCard[0]
  count2=1
  for i in range (1,len(valueCard)):
    #we already have the card_repeated however in order to check that it was actually repeated we need
    #so we go through the hand ignoring the card_that has been repeated checking if there is another card
    # that has been repeated and how many times it does
    if (card_repeated2==valueCard[i]) & (card_repeated2!=card_repeated):
      count2=count2+1
    elif (count2==1):
      card_repeated2=valueCard[i]
  return (count2, card_repeated2)

def checkStraight(value):
  point=5
  count_num=value[0]
  #check if the numbers are in order
  for i in range (len(value)):
    if count_num!=value[i]:
      return 0
    else:
      count_num=count_num+1
  return point


def checkStraightFlush(cardtype):
  point=9
  c_type=cardtype[0]
  #we know that it is in order now lets check if has the same card type
  for i in range (len(cardtype)):
    if (c_type!=cardtype[i]):
      return 0
  return point

def checkRoyalFlush(valueCard):
  #we know that it has the same kind and its in order lets check if its royal
  point=10
  if valueCard[0]!=10:
    return 0
  else:
    return point
  
def checkFourKind(count):
  point=8
  if count==4:
    return point
  else:
    return 0
  
#the list of numbers have to be rearanged for the formula
def fourkindlist(card_repeated, valuecards):
  fourlist=[card_repeated,card_repeated,card_repeated,card_repeated]
  for i in range(len(valuecards)):
    if valuecards[i]!=card_repeated:
      fourlist.append(valuecards[i])
  return fourlist

def checkThreeKind(count):
  point=4
  if count!=3:
    return 0
  else:
    return point
  
#the list of numbers arrnged for the formula of total points
def threekindlist(count, card_repeated, valuecards):
  threekind=[card_repeated,card_repeated,card_repeated]
  for i in range(len(valuecards)):
    if valuecards[i]!=card_repeated:
      threekind.append(valuecards[i])
  return threekind

def checkOnePair(count):
  point=2
  if count!=2:
    return 0
  else:
    return point
  
#the list of numbers have to be rearanged for the formula  
def pair_list(count, card_repeated, valuecards):
  #first two are the cards repeated
  pairList=[card_repeated, card_repeated]
  #rest add since its already in order skiping the repeated ones 
  for i in range(len(valuecards)):
    if valuecards[i]!=card_repeated:
      pairList.append(valuecards[i])
  return pairList

def checkTwoPair(times_a_repeated, times_b_repeated):
  #the count of how many times two diferent cards are repeated is given so now let check its two pairs
  point=3
  if (times_a_repeated==2 and times_b_repeated==2):
    return point
  else:
    return 0
  
#the list of numbers have to be re-aranged for the formula
def twopairlist(count, count2, card_repeated, card_repeated2, valuecards):
  #check which pair is higher so it can go first in the list
  if card_repeated>card_repeated2:
    twopairlist=[card_repeated, card_repeated,card_repeated2,card_repeated2]
  else:
    twopairlist=[card_repeated2,card_repeated2,card_repeated,card_repeated]
  for i in range(len(valuecards)):
    if valuecards[i]!=card_repeated and valuecards[i]!=card_repeated2:
      twopairlist.append(valuecards[i])  
  return twopairlist   

def checkFullHouse(times_a_repeated, times_b_repeated):
  #the count of how many times two diferent cards are repeated is given so now let check its two pairs
  point=7
  if ((times_a_repeated==3 and times_b_repeated==2) or (times_a_repeated==2 and times_b_repeated==3)):
    return point    
  else:
    return 0
  
#the arranged list of the full house so we can get the toal points
def fullhouselist(count, card_repeated, card_repeated2):
  #make the first 3 entries the one that is reapeated 3 times
  # and make the one that is repeated twice the following two entries of the fixed list
  # count is the amount of times the word is repeated which is connected with car_repeated so we use it
  if count==3:
    listfullhouse=[card_repeated, card_repeated, card_repeated,card_repeated2,card_repeated2]
  else:
    listfullhouse=[card_repeated2, card_repeated2, card_repeated2,card_repeated,card_repeated]
  return listfullhouse

def checkFlush(type_card):
  point=6
  c_type=type_card[0]
  #going through all the card types and checking if they are the same
  for i in range (len(type_card)):
    if (c_type!=type_card[i]):
      return 0
  return point  
   
class Poker (object):
  # when you create an object of class Poker, you
  #    create a deck, shuffle it, and deal cards
  #    out to the players.
  #
  def __init__ (self, numHands):
    self.deck = Deck()              # create a deck
    self.deck.shuffle()             # shuffle it
    self.hands = []
    numCards_in_Hand = 5

    for i in range (numHands):
      # deal out 5-card hands to numHands players
      # you'd actually get shot if you dealt this
      #    way in a real poker game (5 cards to
      #    the first player, 5 to the next, etc.)
      hand = []
      for j in range (numCards_in_Hand):
        hand.append (self.deck.deal()) 
      self.hands.append (hand)


  def play (self):

    #creating a tupple of all the values per player to later on compare and rank
    valuesCard=[]
    #creating a tupple of all the types of cards per player to later on compare and rank 
    typeCard=[]
    print("\n")
    for i in range (len(self.hands)):
      # the method "sorted" returns a sorted list without
      #   altering the original list.  reverse = True
      #   makes it sort in decreasing order
      sortedHand = sorted (self.hands[i], reverse = True)

      #printing the hands
      #at the same time getting a tupple of the values and card type to test ranking
      hand = ''
      
      eachIndiValue=[]
      eachInditype=[]
      for card in sortedHand:
        hand = hand + str(card) + ' '
        #we know the second value is the type so use [1]
        eachInditype.append(str(card)[1])

        #we kmow the first value is the actual number so we use [0]
        eachIndiValue.append(str(card)[0])
      #Adding the list of the player's values to the tupple  
      valuesCard.append(eachIndiValue)
      #Adding the list of the player's types to thetupple 
      typeCard.append(eachInditype)
      print ('Hand ' + str(i + 1) + ': ' + hand)
    winner=test(valuesCard, typeCard)



   
        
        
        

def main():

  numHands = int (input ('Enter number of hands to play (needs to be greater than 1): '))

  # need at least 2 players but no more than 6
  while (numHands < 2 or numHands > 6):
    numHands = int (input ('Enter number of hands to play: '))

  # create a Poker object:  create a deck, shuffle it, and
  # deal out the cards
  game = Poker (numHands)

  # play the game
  game=game.play()



  

main()
