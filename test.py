import random
#create global value for VALUE and SUIT
VALUE = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
SUIT = ["clubs", "diamonds", "hearts", "spades"]


class Card:
    #initial instance variables for value, suit and id
    def __init__(self, value, suit, id):
        self.suit = suit
        self.id = id
        self.value = value

        if self.value == 11:
            self.rank = "J"
        elif self.value == 12:
            self.rank = "Q"
        elif self.value == 13:
            self.rank = "K"
        elif self.value == 14:
            self.rank = "A"
        else:
            self.rank = str(self.value)



class Deck:
    def __init__(self):
        self.cards = self.init_deck()

    def init_deck(self):
        """create a 52 cards deck"""
        cards_dict = []
        id = 0
        for s in SUIT:
            for v in VALUE:
                cards_dict.append(Card(v, s, id))
                id += 1
        random.shuffle(cards_dict)
        return cards_dict

    def draw(self):
        return self.cards.pop()

    def shuffles(self):
        random.shuffle(self.cards)

    def reset(self):
        self.cards = self.init_deck()

    def is_empty(self):
        if len(self.cards) == 0:
            return True
        return False


class WarCardGame:
    def __init__(self):
        self.deck = Deck()
        self.hand = 1
        self.winner = None
        self.player1_score = 0
        self.player2_score = 0

    def play(self):
        while not self.deck.is_empty() and self.hand <= 5:
            print("Hand {}".format(self.hand))
            #return the value after a card drawn from cards
            player1_card = self.deal_and_get_win_status(1)
            player2_card = self.deal_and_get_win_status(2)
            if player1_card > player2_card:
                print("Player 1 Wins!")
                self.player1_score += (player1_card + player2_card)
            elif player1_card == player2_card:
                print("It is a Tie!")
                self.player1_score += 0
                self.player1_score += 0

            else:
                print("Player 2 Wins!")
                self.player2_score += (player1_card + player2_card)
            print("Player 1 Score: {}".format(self.player1_score))
            print("Player 2 Score: {}".format(self.player2_score))
            print("\n\n")
            self.hand += 1
        self.final_winner()

    def final_winner(self):
        print("Game Over!\nFinal Score:")
        print("Player 1 Score: {}".format(self.player1_score))
        print("Player 2 Score: {}".format(self.player2_score))
        if self.player1_score > self.player2_score:
            print("Player 1 Wins!")
        elif self.player1_score == self.player2_score:
            print("It is Tie!")
        else:
            print("Player 2 Wins!")

    def deal_and_get_win_status(self, player):
        #draw a card from list of cards
        card = self.deck.draw()
        print("Player {} plays a {} of {}".format(player, card.rank, card.suit))
        return card.value


if __name__ == "__main__":
    game = WarCardGame()
    game.play()
