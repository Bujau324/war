from card import Card


class Deck:
    def __init__(self):
        self.deck = []

    def build_deck(self):
        
        # add numbered Hearts
        for i in range(2, 11):
            self.deck.append(Card(i, "Heart"))
        
        # add jack, Queen, King, Ace of hearts
        self.deck.append(Card("Jack", "Heart"))
        self.deck.append(Card("Queen", "Heart"))
        self.deck.append(Card("King", "Heart"))
        self.deck.append(Card("Ace", "Heart"))
        
        # add numbered Diamonds
        for i in range(2, 11):
            self.deck.append(Card(i, "Diamond"))
        
        # add jack, Queen, King, Ace of Diamonds
        self.deck.append(Card("Jack", "Diamond"))
        self.deck.append(Card("Queen", "Diamond"))
        self.deck.append(Card("King", "Diamond"))
        self.deck.append(Card("Ace", "Diamond"))

        # add numbered Spades
        for i in range(2, 11):
            self.deck.append(Card(i, "Spade"))
        
        # add jack, Queen, King, Ace of Spades
        self.deck.append(Card("Jack", "Spade"))
        self.deck.append(Card("Queen", "Spade"))
        self.deck.append(Card("King", "Spade"))
        self.deck.append(Card("Ace", "Spade"))

        # add numbered clubs
        for i in range(2, 11):
            self.deck.append(Card(i, "Club"))
        
        # add jack, Queen, King, Ace of Clubs
        self.deck.append(Card("Jack", "Club"))
        self.deck.append(Card("Queen", "Club"))
        self.deck.append(Card("King", "Club"))
        self.deck.append(Card("Ace", "Club"))
    
    def show_deck(self):
        for card in self.deck:
            print(card.rank, card.suit)