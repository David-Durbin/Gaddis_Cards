def main():
    # create the deck by calling the create_deck function
    deck = create_deck()

    # get the number of cards to deal (52 cards per deck)
    num_cards = int(input('How many cards should I deal? '))

    # deal the cards
    deal_cards(deck, num_cards)



# create_deck function returns a dictionary that represents the deck of cards
def create_deck():
    # create a dictionary with each card and its value stored as key-value pairs
    deck = { 'Ace of Spades':1, 'Two of Spades':2, 'Three of Spades':3, 'Four of Spades':4, 'Five of Spades':5,
             'Six of Spades':6, 'Seven of Spades':7, 'Eight of Spades':8, 'Nine of Spades':9, 'Ten of Spades':10,
             'Jack of Spades':10, 'Queen of Spades':10, 'King of Spades':10,

             'Ace of Hearts':1, 'Two of Hearts':2, 'Three of Hearts':3, 'Four of Hearts':4, 'Five of Hearts':5,
             'Six of Hearts':6, 'Seven of Hearts':7, 'Eight of Hearts':8, 'Nine of Hearts':9, 'Ten of Hearts':10,
             'Jack of Hearts':10, 'Queen of Hearts':10, 'King of Hearts':10,

             'Ace of Clubs':1, 'Two of Clubs':2, 'Three of Clubs':3, 'Four of Clubs':4, 'Five of Clubs':5,
             'Six of Clubs':6, 'Seven of Clubs':7, 'Eight of Clubs':8, 'Nine of Clubs':9, 'Ten of Clubs':10,
             'Jack of Clubs':10, 'Queen of Clubs':10, 'King of Clubs':10,

             'Ace of Diamonds':1, 'Two of Diamonds':2, 'Three of Diamonds':3, 'Four of Diamonds':4, 'Five of Diamonds':5,
             'Six of Diamonds':6, 'Seven of Diamonds':7, 'Eight of Diamonds':8, 'Nine of Diamonds':9,
             'Ten of Diamonds':10, 'Jack of Diamonds':10, 'Queen of Diamonds':10, 'King of Diamonds':10}

    # return the deck
    return deck


def deal_cards(deck, number):
    # create an accumulator for the hand value
    hand_value_player = 0
    hand_value_dealer = 0

    # make sure the number of cards to be delt is not greater than the number of cards in the deck
    if number > len(deck):
        number = len(deck)

    # TEST create a hand based on the cards
    hand_player = {}
    hand_dealer = {}

    # deal the cards and total their value
    for count in range(number):
        # card is the key, value is the value assigned to that key
        card, value = deck.popitem()
        card_D, value_D = deck.popitem()
        # print(card)
        # hand_value += value

        # push cards into the hand
        hand_player[card] = value
        hand_dealer[card_D] = value_D

    # print the contents of the new hand and its value
    for key in hand_player:
        print(key)
        hand_value_player += hand_player[key]

    # display the hand value
    print('The value of your hand is', hand_value_player)

    print()
    print()

    # print contents of dealer's hand and total value
    for key1 in hand_dealer:
        print(key1)
        hand_value_dealer += hand_dealer[key1]

    # print the value of the dealer's hand
    print('The value of the dealer\'s hand is', hand_value_dealer)

    print()

    if hand_value_dealer > hand_value_player:
        print("Dealer Wins.")
    else:
        print("Player wins.")

# call main()
main()
