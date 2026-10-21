import random 

card_deck = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5 , 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, "J", "J", "J", "J", "Q", "Q", "Q", "Q", "K", "K", "K", "K", "A", "A", "A", "A"]

card_values = {"J" : 10, "Q" : 10, "K" : 10, "A" : 11}

total = 0

def menu(phrase):
    print("-"*len(phrase))
    print(phrase.upper())
    print("-"*len(phrase))
    play() 

def play():
    while True:
        start_choice = input("Do you want to play? yes/no  ")
        if start_choice == "yes" or start_choice == "Yes" or start_choice == "Y" or start_choice == "y":
            deal()
            break
        elif start_choice == "no" or start_choice == "No" or start_choice == "N" or start_choice == "n":
            print("BORING!")
            deal()
            break
        else:
            print("yes or no")

def deal():
   card_1 = random.choice(card_deck)
   card_deck.remove(card_1)
   card_2 = random.choice(card_deck)
   card_deck.remove(card_2)
   hand = [card_1, card_2]
   print(hand)
   total = hand_total(hand)
   choice(hand)
   return hand

def hand_total(hand):
    total = 0
    for card in hand:
        if card in card_values:
            total += card_values[card]
        else:
            total += card
    return total

def choice(hand):
    answer = input("Hit or Stand? ")
    if answer == "Hit" or answer == "hit" or answer == "H" or answer == "h":
        hand, total = hit(hand)
        choice(hand)
    elif answer == "Stand" or answer == "stand" or answer == "S" or answer == "s":
        stand()
    else:
        print("Answer with 'Hit' to Hit and 'Stand' to Stand")
        choice(hand)

def hit(hand):
    new_card = random.choice(card_deck)
    card_deck.remove(new_card)
    hand.append(new_card)
    total = hand_total(hand)
    print(hand)
    return hand, total

def stand():
    pass

menu("!Welcome to Blackjack!")
