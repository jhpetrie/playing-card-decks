# Created by John Petrie
# This is an example of how you can utilize the carddeck module
# In this case we have a simple game of 1 player blackjack
# The game runs in the console, but the logic could be used in other applications like a chat bot
# Simply create a new game object and call the play method to start a new game
# The play method will return the winner of the game

import carddeck
import time

class BlackJackGame: # This class is the game itself
    def __init__(self): # This is the constructor for a game object
        self.deck = carddeck.CardDeck() # This creates a new deck of cards (imported from carddeck module)
        self.player_hand = []
        self.dealer_hand = []
        self.player_score = 0
        self.dealer_score = 0
        carddeck.shuffle_deck(self.deck) # This shuffles the deck of cards
        
    def dealcard(self, hand): # This method deals a card to a hand
        hand.append(self.deck.cards.pop())
    
    def display_hand(self, hand): # This method displays the cards in a hand
        for card in hand:
            print(card.suit, card.value, card.image)
            
    def evaluate_hand(self, hand): # This method evaluates the score of a hand
        score = 0
        for card in hand:
            if card.value == 'J' or card.value == 'Q' or card.value == 'K':
                score += 10
            elif card.value == 'A':
                score += 11
            else:
                score += card.value
        if score > 21:
            for card in hand: # This loop checks for aces and changes their value to 1 if the hand is over 21
                if card.value == 'A':
                    score -= 10
                if score <= 21:
                    break
        return score

    def soft_seventeen(self): # This method checks if the dealer has a soft 17
        if self.dealer_score == 17:
            for card in self.dealer_hand: 
                if card.value == 'A': # If the dealer has an ace, they have a soft 17
                    return True
        return False

    def dealer_turn(self): # This method is the dealer's turn
        print(f'\nDealer hand:')
        self.display_hand(self.dealer_hand)
        print(f'Dealer score: {self.dealer_score}')
        time.sleep(2.5) # This is a delay to give the player time to see the dealer's hand and build suspense
        while self.dealer_score < 17 or self.soft_seventeen(): # The dealer hits on 16 or lower and soft 17
            self.dealcard(self.dealer_hand)
            print(f'\nDealer hand:')
            self.display_hand(self.dealer_hand)
            self.dealer_score = self.evaluate_hand(self.dealer_hand)
            print(f'Dealer score: {self.dealer_score}')
            time.sleep(2) # This is a delay to give the player time to see the dealer's hand and build suspense
            if self.dealer_score > 21:
                print(f'Dealer busts! Player wins!')
                winner = 'player'
                return winner
            
    def player_turn(self): # This method is the player's turn
        
        while self.player_score < 21:
            action = input('Do you want to hit or stand? ')
            if action == 'hit':
                self.dealcard(self.player_hand)
                print(f'\nPlayer hand:')
                self.display_hand(self.player_hand)
                self.player_score = self.evaluate_hand(self.player_hand)
                print(f'Player score: {self.player_score}')
                if self.player_score > 21:
                    print(f'Player busts! Dealer wins!')
                    winner = 'dealer'
                    return winner
            elif action == 'stand':
                break
            else:
                print('Invalid input. Please try again.')
    
    def play(self):
        winner = None
        
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
        
        # Check for Blackjack
        if self.player_score == 21 and self.dealer_score == 21: 
            print(f'Both players have Blackjack! Tie!')
            return winner
        elif self.player_score == 21:
            print(f'Blackjack! Player wins!')
            winner = 'player'
            return winner
        elif self.dealer_score == 21:
            print(f'Dealer Blackjack! Dealer wins!')
            winner = 'dealer'
            return winner
        
        winner = self.player_turn() # The player's turn if the player busts, returns dealer as winner
        if winner != None: # If the player busts, the game is over
            return winner
        
        winner = self.dealer_turn() # The dealer's turn
        if winner != None: # If the dealer busts, the game is over
            return winner
        
        
        if self.player_score > self.dealer_score:
            print(f'Player wins!')
            winner = 'player'
        elif self.player_score < self.dealer_score:
            print(f'Dealer wins!')
            winner = 'dealer'
        else:
            print(f'Tie!')
            winner = None
            
        return winner
   
# Main game loop for demonstration         
newgame = BlackJackGame()
winner = newgame.play()
print(f'\nWinner: {winner}')
