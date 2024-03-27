# Created by John Petrie

import carddeck
import time

class BlackJackGame:
    def __init__(self):
        self.deck = carddeck.CardDeck()
        self.player_hand = []
        self.dealer_hand = []
        self.player_score = 0
        self.dealer_score = 0
        carddeck.shuffle_deck(self.deck)
        
    def dealcard(self, hand):
        hand.append(self.deck.cards.pop())
    
    def display_hand(self, hand):
        for card in hand:
            print(card.suit, card.value, card.image)
            
    def evaluate_hand(self, hand):
        score = 0
        for card in hand:
            if card.value == 'J' or card.value == 'Q' or card.value == 'K':
                score += 10
            elif card.value == 'A':
                score += 11
            else:
                score += card.value
        if score > 21:
            for card in hand:
                if card.value == 'A':
                    score -= 10
                if score <= 21:
                    break
        return score

    def soft_seventeen(self):
        if self.dealer_score == 17:
            for card in self.dealer_hand:
                if card.value == 'A':
                    return True
        return False

    def dealer_turn(self):
        print(f'\nDealer hand:')
        self.display_hand(self.dealer_hand)
        print(f'Dealer score: {self.dealer_score}')
        time.sleep(1.5)
        while self.dealer_score < 17 or self.soft_seventeen():
            self.dealcard(self.dealer_hand)
            print(f'\nDealer hand:')
            self.display_hand(self.dealer_hand)
            self.dealer_score = self.evaluate_hand(self.dealer_hand)
            print(f'Dealer score: {self.dealer_score}')
            time.sleep(2)
            if self.dealer_score > 21:
                print(f'Dealer busts! Player wins!')
                return
            
    def player_turn(self):
        while self.player_score < 21:
            action = input('Do you want to hit or stay? ')
            if action == 'hit':
                self.dealcard(self.player_hand)
                print(f'\nPlayer hand:')
                self.display_hand(self.player_hand)
                self.player_score = self.evaluate_hand(self.player_hand)
                print(f'Player score: {self.player_score}')
                if self.player_score > 21:
                    print(f'Player busts! Dealer wins!')
                    return
            elif action == 'stay':
                break
            else:
                print('Invalid input. Please try again.')
    
    def play(self):
        self.dealcard(self.player_hand)
        self.dealcard(self.dealer_hand)
        self.dealcard(self.player_hand)
        self.dealcard(self.dealer_hand)
        
        print(f'\nPlayer hand:')
        self.display_hand(self.player_hand)
        self.player_score = self.evaluate_hand(self.player_hand)
        print(f'Player score: {self.player_score}')
        
        print(f'\nDealer hand:')
        print(self.dealer_hand[0].suit, self.dealer_hand[0].value, self.dealer_hand[0].image)
        print('Face down card')
        self.dealer_score = self.evaluate_hand(self.dealer_hand)
        
        if self.player_score == 21 and self.dealer_score == 21:
            print(f'Both players have Blackjack! Tie!')
            return
        elif self.player_score == 21:
            print(f'Blackjack! Player wins!')
            return
        elif self.dealer_score == 21:
            print(f'Dealer Blackjack! Dealer wins!')
            return
        
        self.player_turn()
        
        time.sleep(2.5)
        print(f'\nDealer hand:')
        self.display_hand(self.dealer_hand)
        print(f'Dealer score: {self.dealer_score}')
        
        self.dealer_turn()
        
        if self.player_score > self.dealer_score:
            print(f'Player wins!')
        elif self.player_score < self.dealer_score:
            print(f'Dealer wins!')
        else:
            print(f'Tie!')
            
newgame = BlackJackGame()
newgame.play()