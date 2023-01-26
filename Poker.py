#  File: Poker.py

#  Description: This program simulates a regular Poker game, otherwise known as the 5-Card Draw.

#  Student's Name: Ankita Sumeet 

#  Student's UT EID: as96977

#  Course Name: CS 313E 

#  Unique Number: A5

#  Date Created: 9/19/21

#  Date Last Modified: 9/20/21

import sys
import random

class Card (object): 
  # The player with the highest valued hand wins

  RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)
  SUITS = ('C', 'D', 'H', 'S')

  # constructor
  def __init__ (self, rank = 12, suit = 'S'): 
    if (rank in Card.RANKS):
      self.rank = rank
    else:
      self.rank = 12

    if (suit in Card.SUITS):
      self.suit = suit
    else:
      self.suit = 'S'

  # string representation of a Card object
  def __str__ (self): 
    if (self.rank == 14):
      rank = 'A'
    elif (self.rank == 13):
      rank = 'K'
    elif (self.rank == 12):
      rank = 'Q'
    elif (self.rank == 11):
      rank = 'J'
    else:
      rank = str (self.rank)
    
    return rank + self.suit  

  # equality tests
  def __eq__ (self, other):
    return self.rank == other.rank

  def __ne__ (self, other):
    return self.rank != other.rank

  def __lt__ (self, other):
    return self.rank < other.rank

  def __le__ (self, other):
    return self.rank <= other.rank

  def __gt__ (self, other):
    return self.rank > other.rank

  def __ge__ (self, other):
    return self.rank >= other.rank

class Deck (object): 
  # constructor
  def __init__ (self, num_decks = 1):
    self.deck = []
    for i in range (num_decks):
      for suit in Card.SUITS:
        for rank in Card.RANKS:
          card = Card (rank, suit)
          self.deck.append (card)

  # shuffle the deck
  def shuffle (self):
    random.shuffle (self.deck)

  # deal a card
  def deal (self):
    if (len(self.deck) == 0):
      return None
    else:
      return self.deck.pop(0)

class Poker (object): 
  # constructor
  def __init__ (self, num_players = 2, num_cards = 5):
    self.deck = Deck()
    self.deck.shuffle()
    self.all_hands = []
    self.numCards_in_Hand = num_cards

    # deal the cards to the players
    for i in range (num_players):
      hand = []
      for j in range (self.numCards_in_Hand):
        hand.append (self.deck.deal())
      self.all_hands.append (hand)

  # simulate the play of poker
  def play (self):
    # sort the hands of each player and print
    for i in range (len(self.all_hands)):
      sorted_hand = sorted (self.all_hands[i], reverse = True)
      self.all_hands[i] = sorted_hand
      
      hand_str = ''
      for card in sorted_hand:
        hand_str = hand_str + str (card) + ' '

      print ('Player ' + str(i + 1) + ' : ' + hand_str)

    # determine the type of each hand and print
    hand_type = []	# create a list to store type of hand
    hand_points = []	# create a list to store points for hand

    for i in range (len(self.players)):
      if self.is_royal(self.players[i]) != 0:
        hand_points.append(self.is_royal(self.players[i]))
        hand_type.append(10)
        print("Player", str(i + 1)+ ": Royal Flush")
      elif self.is_straight_flush(self.players[i]) != 0:
        hand_points.append(self.is_straight_flush(self.players[i]))
        hand_type.append(9)
        print("Player", str(i + 1)+ ": Straight Flush")
      elif self.is_four_kind(self.players[i]) != 0:
        hand_points.append(self.is_four_kind(self.players[i]))
        hand_type.append(8)
        print("Player", str(i + 1)+ ": Four of a Kind")
      elif self.is_full_house(self.players[i]) != 0:
        hand_points.append(self.is_full_house(self.players[i]))
        print("Player", str(i + 1)+ ": Full House")
        hand_type.append(7)
      elif self.is_flush(self.players[i]) != 0:
        hand_points.append(self.is_flush(self.players[i]))
        print("Player", str(i + 1)+ ": Flush")
        hand_type.append(6)
      elif self.is_straight(self.players[i]) != 0:
        hand_points.append(self.is_straight(self.players[i]))
        print("Player", str(i + 1)+ ": Straight")
        hand_type.append(5)
      elif self.is_three_kind(self.players[i]) != 0:
        hand_points.append(self.is_three_kind(self.players[i]))
        print("Player", str(i + 1)+ ": Three of a Kind")
        hand_type.append(4)
      elif self.is_two_pair(self.players[i]) != 0:
        hand_points.append(self.is_two_pair(self.players[i]))
        print("Player", str(i + 1)+ ": Two Pair")
        hand_type.append(3)
      elif self.is_one_pair(self.players[i]) != 0:
        hand_points.append(self.is_one_pair(self.players[i]))
        hand_type.append(2)
        print("Player", str(i + 1)+ ": One Pair")
      else:
        hand_points.append(self.is_high_card(self.players[i]))
        hand_type.append(1)
        print("Player", str(i + 1)+ ": High Card")
    

    # determine winner and print
    max_players = []
    max_val = max(hand_type)
    for i in range (len(hand_points)):
      if hand_type[i] == max_val:
        max_players.append(i)
      else:
        continue
    j = 0
    if len(max_players) == 1:
          print("Player", str(max_players[0]+1), "wins.")
    else:
      while j < len(max_players):
        if hand_points[max_players[j]] == max(hand_points):
          print("Player", str(max_players[j] + 1) + " ties.")
          hand_points[max_players[j]] = 0
          j = 0
        elif len(max_players) == 1:
          print("Player", str(max_players[j]+1) + " ties.")
          return
        else:
          j += 1
    return


  # determine if a hand is a royal flush
  # made of 10, Jack, Queen, King, and Ace all of the same of suit
  def is_royal (self, hand):
    same_suit = True
    for i in range (len(hand) - 1):
      same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

    if (not same_suit):
      return 0, ''

    rank_order = True
    for i in range (len(hand)):
      rank_order = rank_order and (hand[i].rank == 14 - i)

    if (not rank_order):
      return 0, ''

    points = 10 * 15**5 + hand[0].rank * 15**4 + hand[1].rank * 15**3 + hand[2].rank * 15**2 + hand[3].rank * 15 + hand[4].rank

    return points, 'Royal Flush'

  # determine if a hand is a straight flush
  # cards in numerical sequence but of the same suit
  def is_straight_flush (self, hand): 

    same_suit = True
    for i in range (len(hand) - 1):
      same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

    if (not same_suit):
      return 0, ''

    rank_order = True
    for i in range (len(hand) - 1):
      rank_order = rank_order and (hand[i].rank == (hand[i + 1].rank + 1))

    for i in range (len(hand) - 1):
      if (hand[i].rank == 14):
        return 0, ''
    
    points = 9 * 15**5 + hand[0].rank * 15**4 + hand[1].rank * 15**3 + hand[2].rank * 15**2 + hand[3].rank * 15 + hand[4].rank

    
    return points, 'Straight Flush'


  # determine if a hand is a four of a kind
  # hand must have four cards of the same numerical rank
  def is_four_kind (self, hand):
    countR = 0
    for i in range (len(hand) - 1):
        if(hand[i]).rank == (hand[i+1]).rank:
            countR += 1

    if(countR == 3):
        points = 8 * 15**5 + hand[0].rank * 15**4 + hand[1].rank * 15**3 + hand[2].rank * 15**2 + hand[3].rank * 15 + hand[4].rank
        return points , 'Four of a Kind'
    else:
        return 0 , ''


  # determine if a hand is a full house
  # three of the cards must have the same numerical rank 
  # the two remaining cards have the same numerical rank, different from those of the initial three
  def is_full_house (self, hand): # LOGIC 
    points = 7 * 15**5 + hand[0].rank * 15**4 + hand[1].rank * 15**3 + hand[2].rank * 15**2 + hand[3].rank * 15 + hand[4].rank
    if (hand[0].rank == hand[1].rank) and (hand[1].rank == hand[2].rank):
        if (hand[3].rank == hand[4].rank):
            if (hand[0].rank != hand[3].rank):
                return points, 'Full House'
            else:
                return 0, ''
        else:
            return 0, ''

    elif (hand[2].rank == hand[3].rank) and (hand[3].rank == hand[4].rank):
        if (hand[0].rank == hand[1].rank):
            if (hand[2].rank == hand[0].rank):
                return 0, ''
            else:
                return points, 'Full House'
        else:
            return 0, ''
    else:
        return 0, ''


  # determine if a hand is a flush
  # 5 cards all of the same suit where numerical order does not matter
  def is_flush (self, hand): #LOGIC
    logic = 0 
    for i in range (len(hand) - 1):
      if (hand[i].suit == hand[i + 1].suit):
          logic += 1

    if logic == 4:
        points = 6 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3 + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1 + (hand[4].rank) 
        return points, 'Flush'
    else:
        return 0, ''
  

  # determine if a hand is straight
  # 5 cards are in numerical order but are not all of the same suit
  def is_straight (self, hand): 
    for i in range (len(hand) - 1):
      if (hand[i].rank == (hand[i+1].rank + 1)):
        points = 5 * 15**5 + hand[0].rank * 15**4 + hand[1].rank * 15**3 + hand[2].rank * 15**2 + hand[3].rank * 15 + hand[4].rank
        return points, 'Straight'
      else:
        return 0, ''


  # determine if a hand is a three of a kind
  # three cards are the same rank and the other two are unrelated
  def is_three_kind (self, hand):
    for i in range (len(hand) - 1):
      if hand[i].rank == hand[i+1].rank:
        if (hand[i+1].rank == hand[i+2].rank) and (i+2 < len(hand) - 1):
          points = 3 * 15**5 + hand[0].rank * 15**4 + hand[1].rank * 15**3 + hand[2].rank * 15**2 + hand[3].rank * 15 + hand[4].rank 
          return points, 'Three of a Kind'
    
    return 0, ''
        
    
  # determine if a hand is a two pair
  # two cards have a matching rank another two cards have a different matching rank
  # the fifth is random card
  def is_two_pair (self, hand):
    matching = []
    for i in range (len(hand)):
      if hand[i].rank not in matching:
        matching.append(hand[i].rank)
      else:
        continue
    if len(matching) != 3:
      return 0, ''
    else:
      points = 3 * 15**5 + hand[0].rank * 15**4 + hand[1].rank * 15**3 + hand[2].rank * 15**2 + hand[3].rank * 15 + hand[4].rank
      return points, 'Two Pair'
        
        
  # determine if a hand is one pair
  # two cards are the same rank and the other three cards are unrelated
  def is_one_pair (self, hand):
    other = []
    x = 0
    for i in range (len(hand) - 1):
      if (hand[i].rank == hand[i + 1].rank):
          x = hand[i+1].rank
    
    for card in hand:
       if x != card.rank:
           other.append(card.rank)

    other = sorted(other, reverse=True)

    if len(other) > 3:
      return 0, ''
    else:
      points = 2 * 15**5 + x * 15**4 + x * 15**3 + other[0] * 15**2 + other[1] * 15 + other[2]
      return points, 'One Pair' 


  # determine if a hand is a high card
  # if none of the categories above then the hand having the highest ranking card wins
  def is_high_card (self,hand):
    points = 15**5 + hand[0].rank * 15**4 + hand[1].rank * 15**3 + hand[2].rank * 15**2 + hand[3].rank * 15 + hand[4].rank
    return points, 'High Card'

def main(): 
  # read number of players from stdin
  line = sys.stdin.readline()
  line = line.strip()
  num_players = int (line)
  if (num_players < 2) or (num_players > 6):
    return

  # create the Poker object
  game = Poker (num_players)

  # play the game
  game.play()

if __name__ == "__main__":
  main()
