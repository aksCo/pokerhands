import collections
from collections import defaultdict 
import sys

def pair(hand):
    values = [v[0] for v in hand]
    val_counter = defaultdict(int)
    for i in values:
        val_counter[i] += 1
    key_list = list(val_counter.keys()) 
    val_list = list(val_counter.values())
    if 2 in val_counter.values():
        return True, key_list[val_list.index(2)]
    else:
        return False, None
    
def two_pairs(hand): 
    pairs = []
    non_pair = 0
    values = [v[0] for v in hand]
    val_counter = defaultdict(int)
    for i in values:
        val_counter[i]+=1
    key_list = list(val_counter.keys()) 
    val_list = list(val_counter.values())

    for i in range(len(val_list)):
        if val_list[i] == 2:
            pairs.append(key_list[i])
        else:
            non_pair = key_list[i]
    if sorted(val_counter.values())==[1,2,2]:
        return True, pairs, non_pair
    else:
        return False, None, None
    
def three_of_kind(hand):
    
    values = [v[0] for v in hand]
    val_counter = defaultdict(int)
    for i in values:
        val_counter[i]+=1
    key_list = list(val_counter.keys()) 
    val_list = list(val_counter.values())
    if 3 in val_counter.values():
        return True, key_list[val_list.index(3)]
    else:
        return False, None
    
def isstraight(hand):
    
    values = [v[0] for v in hand]
    only_numbers = []
    for i in values:
        only_numbers.append(sequence[i])
    if sorted(only_numbers) == [k for k in range(min(only_numbers), max(only_numbers)+1)]:
        return True
    else:
        return False
    
def flush(hand):
    
    suits = [s[1] for s in hand]
    if len(set(suits)) == 1:
      return True
    else:
      return False
  
def full_house(hand):
    
    if pair(hand)[0] and three_of_kind(hand)[0]:
        return True
    else:
        return False
    
def four_of_kind(hand):
    
    values = [v[0] for v in hand]
    val_counter = defaultdict(int)
    for i in values:
        val_counter[i]+=1
    key_list = list(val_counter.keys()) 
    val_list = list(val_counter.values())
    if 4 in val_counter.values():
        return True, key_list[val_list.index(4)]
    else:
        return False, None
    
def straight_flush(hand):
    
    if isstraight(hand) and flush(hand):
        return True
    else:
        return False

def royal_flush(hand):
    
    values = [v[0] for v in hand]
    only_numbers = []
    for i in values:
        only_numbers.append(sequence[i])
    if isstraight(hand) and flush(hand):
        if sorted(only_numbers)[0] == 10:
            return True
        else:
            return False
        
def getranking(hand):

    if royal_flush(hand):
        return 10
    if straight_flush(hand):
        return 9
    if four_of_kind(hand)[0]:
        return 8
    if full_house(hand):
        return 7
    if flush(hand):
        return 6
    if isstraight(hand):
        return 5
    if three_of_kind(hand)[0]:
        return 4
    if two_pairs(hand)[0]:
        return 3
    if pair(hand)[0]:
        return 2
    return 1 

def comparison(a, b): 
    
    A = sorted(a, reverse=True)
    B = sorted(b, reverse=True)
    for i in range(0,len(a)):
        if A[i] != B[i]:
            if A[i] > B[i]:
                return 'Player1'
            elif A[i] < B[i]:
                return 'Player2'
            break 
        else:
            continue
        
def tie(hand1, hand2, rank):
#   Tie breaker to decide highest rank
    v1 = [v[0] for v in hand1]
    v2 = [v[0] for v in hand2]

    v1_numbers = []
    for i in v1:
        v1_numbers.append(sequence[i])
    v2_numbers = []
    for i in v2:
        v2_numbers.append(sequence[i])   
    
    if rank == 1 or rank == 5 or rank == 6 or rank == 9:
        return comparison(v1_numbers, v2_numbers)
    
    if rank == 2: # Pair
        a1,b1 = pair(hand1)
        a2,b2 = pair(hand2)
        b1 = sequence[b1]
        b2 = sequence[b2]
        # Compare values with pair
        if b1 > b2:
            return "Player1"
        elif b1 < b2:
            return "Player2"
        # Remove same values and compare next highest card 
        elif b1 == b2:
            v1_numbers.remove(b1)
            v1_numbers.remove(b1)
            v2_numbers.remove(b2)
            v2_numbers.remove(b2)
            return comparison(v1_numbers, v2_numbers)
        
    if rank == 3: # Two Pairs
        
        a1,b1,c1 = two_pairs(hand1)
        a2,b2,c2 = two_pairs(hand2)
        b1a = sequence[b1[0]]
        b1b = sequence[b1[1]]
        b2a = sequence[b2[0]]
        b2b = sequence[b2[1]]
        c1 = sequence[c1]
        c2 = sequence[c2]
        b1_numbers = sorted([b1a, b1b])
        b2_numbers = sorted([b2a, b2b])

        # Compare the corresponding pair value
        if b1_numbers[0] > b2_numbers[0]:
            return 'Player1'
        elif b1_numbers[0] < b2_numbers[0]:
            return 'Player2'
        elif b1_numbers[1] > b2_numbers[1]:
            return 'Player1'
        elif b1_numbers[1] < b2_numbers[1]:
            return 'Player2'  
        # Compare the leftover card
        elif c1 > c2:
            return 'Player1'
        elif c1 < c2:
            return 'Player2'
            
    if rank == 4: # Three of a kind
        a1,b1 = three_of_kind(hand1)
        a2,b2 = three_of_kind(hand2)
        b1 = sequence[b1]
        b2 = sequence[b2]

        if b1 > b2:
            return "Player1"
        elif b1 < b2:
            return "Player2"
            
    if rank == 7: #Full House
        a1,b1 = three_of_kind(hand1)
        a2,b2 = three_of_kind(hand2)
        c1,d1 = pair(hand1)
        c2,d2 = pair(hand2)
        b1 = sequence[b1]
        b2 = sequence[b2]
        d1 = sequence[d1]
        d2 = sequence[d2]
        # Three of a kind
        if b1 > b2:
            return "Player1"
        elif b1 < b2:
            return "Player2"
        # Card values that have a pair
        elif d1 > d2:
            return "Player1"
        elif d1 < d2:
            return "Player2"

    if rank == 8: # Four of a Kind
        a1,b1 = four_of_kind(hand1)
        a2,b2 = four_of_kind(hand2)
        b1 = sequence[b1]
        b2 = sequence[b2]

        if b1 > b2:
            return "Player1"
        elif b1 < b2:
            return "Player2"
        
if __name__ == '__main__':
    
    sequence = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10,"J":11, "Q":12, "K":13, "A":14}
    counter = {'Player1': 0, 'Player2':0}
    
    for line in sys.stdin:
        p1 = line.split()[:5]
        p2 = line.split()[5:]
        
        if getranking(p1) > getranking(p2):
            counter['Player1']+=1
        elif getranking(p1) < getranking(p2):
            counter['Player2']+=1
        
        elif getranking(p1) == getranking(p2):
            rank = getranking(p1) 
            winner = tie(p1, p2, rank)
            if winner == 'Player1':
                counter['Player1']+=1
            elif winner == 'Player2':
                counter['Player2']+=1
            
    print(counter)