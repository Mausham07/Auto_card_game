

from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()


        
class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    def __init__(self):
        print("Creating New Ordered Deck!")
        print("\n")
        self.allCards = [(s,r) for s in SUITE for r in RANKS] 
    
    def shuffle(self):
        print("SHUFFLING THE CARDS")
        shuffle(self.allCards)

    def split_in_half(self):
        return(self.allCards[:26], self.allCards[26:])

class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        return "Contains {} cards".format(len(self.cards))

    def add(self, added_cards):
        self.cards.extend(added_cards)
    
    def remove_card(self):
        return self.cards.pop()

class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove_card()
        print("{} has placed: {}".format(self.name, drawn_card))
        print("\n")
        return drawn_card

    def remove_war_cards(self):
        if len(self.hand.cards) < 3:
            return self.hand.cards
        else:
            war_cards = []
            for x in range(3):
                war_cards.append(self.hand.cards.pop())
            return war_cards

    def still_has_card(self):
        """
        Return true if the player still has cards left
        """
        return len(self.hand.cards) != 0



######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")
print("\n")

# Create a new deck and split in half

d = Deck()
d.shuffle()
half1, half2 = d.split_in_half()

# create both players

computer = Player("computer", Hand(half1))

print("\n")
name = input("Enter your name: ")
user = Player(name, Hand(half2))

total_rounds = 0
war_count = 0

while user.still_has_card() and computer.still_has_card():
    total_rounds += 1 
    print("Time for next round")
    print("Here are the current standings")
    print("\n")
    print(user.name + " has the count: "+ str(len(user.hand.cards)))
    print(computer.name + " had the count: "+ str(len(computer.hand.cards)))
    print("\n")
    print("Play a card")
    print("\n")


    table_cards = []

    c_card = computer.play_card()
    p_card = user.play_card()

    table_cards.append(c_card)
    table_cards.append(p_card)

    if c_card[1] == p_card[1]:
        war_count += 1

        print("war has occured!")

        table_cards.extend(user.remove_war_cards())
        table_cards.extend(computer.remove_war_cards())

        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(table_cards)

        else:
            computer.hand.add(table_cards)

    else:
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(table_cards)

        else:
            computer.hand.add(table_cards)

print("game over, numbers of round: "+ str(total_rounds))
print("a war happened "+ str(war_count)+ " times")
print("does computer still have cards?")
print(str(computer.still_has_card()))
print("does user still have cards?")
print(str(user.still_has_card()))


