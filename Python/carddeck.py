# Created by John Petrie

import random


class PlayingCard:
    def __init__(self, suit, value, image):
        self.suit = suit
        self.value = value
        self.image = image


class CardDeck:
    def __init__(self):

        suits = ['♠', '♥', '♦', '♣']
        values = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
        card_emojis = ['\U0001F0A1', '\U0001F0A2', '\U0001F0A3', '\U0001F0A4', '\U0001F0A5', '\U0001F0A6', '\U0001F0A7', '\U0001F0A8', '\U0001F0A9', '\U0001F0AA', '\U0001F0AB', '\U0001F0AD', '\U0001F0AE',
                       '\U0001F0B1', '\U0001F0B2', '\U0001F0B3', '\U0001F0B4', '\U0001F0B5', '\U0001F0B6', '\U0001F0B7', '\U0001F0B8', '\U0001F0B9', '\U0001F0BA', '\U0001F0BB', '\U0001F0BD', '\U0001F0BE',
                       '\U0001F0C1', '\U0001F0C2', '\U0001F0C3', '\U0001F0C4', '\U0001F0C5', '\U0001F0C6', '\U0001F0C7', '\U0001F0C8', '\U0001F0C9', '\U0001F0CA', '\U0001F0CB', '\U0001F0CD', '\U0001F0CE',
                       '\U0001F0D1', '\U0001F0D2', '\U0001F0D3', '\U0001F0D4', '\U0001F0D5', '\U0001F0D6', '\U0001F0D7', '\U0001F0D8', '\U0001F0D9', '\U0001F0DA', '\U0001F0DB', '\U0001F0DD', '\U0001F0DE']

        newdeck = [PlayingCard(suit, value, image=None)
                   for suit in suits
                   for value in values]

        '''
        The following is how this appears without list comprehension:
        newdeck = []
        for suit in suits:
            for value in values:
                newdeck.append(PlayingCard(suit, value, image=None))
        '''

        '''zip function is used to combine two lists into a single list of tuples
        which is looped over assigning emoji to the current card in the tuple'''
        for emoji, card in zip(card_emojis, newdeck):
            card.image = emoji

        self.cards = newdeck


def display_deck(deck):
    for card in deck.cards:
        print(card.suit, card.value, card.image)


def shuffle_deck(deck):
    random.shuffle(deck.cards)


def demo():
    newdeck = CardDeck()
    print(f'\nOrdered deck of cards:')
    display_deck(newdeck)
    shuffle_deck(newdeck)
    print(f'\nShuffled deck of cards:')
    display_deck(newdeck)


demo()
