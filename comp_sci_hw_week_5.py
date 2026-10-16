import random 

card_deck = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5 , 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, "J", "J", "J", "J", "Q", "Q", "Q", "Q", "K", "K", "K", "K", "A", "A", "A", "A"]

card_values = {"J" : 10, "Q" : 10, "K" : 10}

def menu(phrase):
    print("-"*len(phrase))
    print(phrase.upper())
    print("-"*len(phrase))
    play() 

def play():
    while True:
        choice = input("Do you want to play? yes/no  ")
        if choice == "yes":
            deal()
            break
        elif choice == "no":
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
   total = sum(hand)
   print(total)
   print(card_1)
   print(card_2)

menu("!Welcome to Blackjack!")
