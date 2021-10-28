"""
Session 10B: List comprehension and sets
"""

from functools import cmp_to_key

FACE_CARDS = ["Jack", "Queen", "King", "Ace"]
SUITS = ["Spades", "Hearts", "Clubs", "Diamonds"]

def create_card(suit, value):
    """
    Return a card of suit and value as a list of the name. Example: create_card("Hearts", 12) -> "Queen of Hearts"

    parameters:
    :param string suit: The suit
    :param int value: The value of the card
    """

    if value == 11 or value == 1:
        value = "Ace"
    elif value > 10:
        if value == 11:
            value = "Jack"
        elif value == 12:
            value = "Queen"
        elif value == 13:
            value = "King"

    name = "%s of %s"%(value, suit)

    return name

def fill_deck_set():
    """
    Create a full deck of cards using list comprehension. Return this list as a set.
    """

    deck = list()

    [deck := deck + [create_card(suit, j) for j in range(1,14)] for suit in SUITS]

    return set(deck)

def fill_deck_list():
    """
    Create a full deck of cards using list comprehension. Return this list as a set.
    """

    deck = list()

    [deck := deck + [create_card(suit, j) for j in range(1,14)] for suit in SUITS]

    return deck

def sort_deck(deck):
    """
    Sort a deck of cards. Can you sort a set?

    parameters:
    :param set deck: a deck of cards
    """
    return sorted(deck, key=cmp_to_key(card_comparator))

def card_comparator(a, b):

    return a[0] > b[0]

def split_deck(deck, n):
    """
    Split a deck into n sections.

    parameters:
    :param list deck: list of cards
    :param int n: The number of sections the deck will be split into
    """

    section_length = len(deck) // n
    sections = list()

    start = 0
    for i in range(n):
        stop = start + section_length
        if n % 2 == 1 and i==0:
            stop += 1
        sections.append(deck[start:stop:1])
        start = stop

    return sections

def find_card_in_list(card, deck):
    """
    Find a card in the deck.

    parameters:
    :param list card: A card with name and value
    :param list deck: A deck of cards
    """
    return deck.index(card) != 0

def find_card_in_set(card, deck):
    """
    Find a card in the deck.

    parameters:
    :param list card: A card with name and value
    :param set deck: A deck of cards
    """

    return card in deck

def main():
    print(create_card("Hearts", 5))
    print()

    deck_set = fill_deck_set()
    deck_list = fill_deck_list()

    print(deck_set)
    print(sort_deck(deck_set))
    print(find_card_in_set("Queen of Hearts", deck_set))
    print(find_card_in_list("Queen of Hearts", deck_list))
    print(split_deck(deck_list, 3))


if __name__ == "__main__":
    main()