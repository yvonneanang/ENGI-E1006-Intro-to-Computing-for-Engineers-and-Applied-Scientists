#Completed by Yvonne Naa Ardua Anang UNI: yna2103, with Joseph Duodu UNI: jd3519

import random

class Card(object):  
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return "The suit of this card is {}, and its rank is {}.".format(self.suit, self.rank)

    def value(self, total):
        self.total = total
        if self.rank.isdigit():
            return int(self.rank)
        if self.rank == "J" or self.rank == "Q" or self.rank == "K":
            return 10
        if self.rank == "A":
            if (self.total + 11) > 21:
                return 1
            else: 
                return 11
             


def make_deck():
    deck_of_cards = []
    suits = ['♠','♣','♦','♥']
    ranks = list(range(2, 11)) + ["J", "Q", "K", "A"]
    for suit in suits:
        for rank in ranks:
            card = suit + str(rank)
            deck_of_cards.append(card)
    random.shuffle(deck_of_cards)
    return deck_of_cards
            


def main():
    winner = " "
    loser = " "
    player_score = 0 
    dealer_score = 0
    while winner != "player" and loser != "player":
        deck = make_deck()
        player_card = deck[0]
        dealt_card = Card(deck[0][0], deck[0][1:])
        card_value = dealt_card.value(player_score)
        player_score += card_value
        print("You drew {}".format(player_card))
        print("Your current score is {}".format(player_score))
        if player_score == 21:
            print("You win.")
            winner = "player"
        elif player_score > 21:
            print("Dealer wins.")
            loser = "player"
        else:
            player_choice = input("Do you want another card? Yes(Y) / No(N):>>>")
            if player_choice == "Y":
                continue
            elif player_choice == "N":
                break
   
    while winner != "player" and loser != "player" and dealer_score < 17:
        deck = make_deck()
        dealer_card = deck[0]
        dealt_card = Card(deck[0], deck[0][1:])
        card_value = dealt_card.value(dealer_score)
        dealer_score += card_value
        print("\nDealer drew {}".format(dealer_card))
        print("Dealer's current score is {}\n".format(dealer_score))
        
    if winner != "player" and loser != "player":
        if dealer_score == 21:
            winner = "dealer"
            print("Dealer wins")
        elif dealer_score > 21:
            winner = "player"
            print("You win.")
        elif dealer_score == player_score:
            print("Game is a draw. No one wins.")
        elif dealer_score > player_score:
            print ("Dealer wins.")
        elif player_score > dealer_score:
            print("Player wins.")
    
    
if __name__ == "__main__":
    main()
