// Created by John Petrie

import java.util.ArrayList;
import java.util.List;
import java.util.Collections;
 


// Deck object (must get the deck list if you want to treat it like a list, otherwise use class methods)
public class CardDeck {
    private List<PlayingCard> deck;
    
    public CardDeck() {
        String[] suits = {"♠", "♥", "♦", "♣"};
        String[] values = {"A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"};
        String[] cardEmojis = {
            "\uD83C\uDCA1", "\uD83C\uDCA2", "\uD83C\uDCA3", "\uD83C\uDCA4", "\uD83C\uDCA5", "\uD83C\uDCA6", "\uD83C\uDCA7", "\uD83C\uDCA8", "\uD83C\uDCA9", "\uD83C\uDCAA", "\uD83C\uDCAB", "\uD83C\uDCAD", "\uD83C\uDCAE",  // Spades A-K
            "\uD83C\uDCB1", "\uD83C\uDCB2", "\uD83C\uDCB3", "\uD83C\uDCB4", "\uD83C\uDCB5", "\uD83C\uDCB6", "\uD83C\uDCB7", "\uD83C\uDCB8", "\uD83C\uDCB9", "\uD83C\uDCBA", "\uD83C\uDCBB", "\uD83C\uDCBD", "\uD83C\uDCBE",  // Hearts A-K
            "\uD83C\uDCC1", "\uD83C\uDCC2", "\uD83C\uDCC3", "\uD83C\uDCC4", "\uD83C\uDCC5", "\uD83C\uDCC6", "\uD83C\uDCC7", "\uD83C\uDCC8", "\uD83C\uDCC9", "\uD83C\uDCCA", "\uD83C\uDCCB", "\uD83C\uDCCD", "\uD83C\uDCCE",  // Diamonds A-K
            "\uD83C\uDCD1", "\uD83C\uDCD2", "\uD83C\uDCD3", "\uD83C\uDCD4", "\uD83C\uDCD5", "\uD83C\uDCD6", "\uD83C\uDCD7", "\uD83C\uDCD8", "\uD83C\uDCD9", "\uD83C\uDCDA", "\uD83C\uDCDB", "\uD83C\uDCDD", "\uD83C\uDCDE"};   // Clubs A-K
 
 
        List<PlayingCard> newDeck = new ArrayList<>();
        int emojiIndex = 0;
        for (String suit : suits) {
            for (String value : values) {
                PlayingCard card = new PlayingCard(suit, value, cardEmojis[emojiIndex]);
                newDeck.add(card);
                emojiIndex++;
            }
        }
        this.deck = newDeck;
    }

    public List<PlayingCard> getDeckList() {
        return deck;
    }

    public void shuffleDeck() {
        Collections.shuffle(deck);
    }

    public void displayDeck() {
        for (PlayingCard card : deck) {
            System.out.println(String.format("%s %s %s", card.getSuit(), card.getValue(), card.getImage()));
        }
    }
}

// Card object
class PlayingCard {
    private String suit;
    private String value;
    private String image;
 
 
    public PlayingCard(String suit, String value, String image) {
        this.suit = suit;
        this.value = value;
        this.image = image;
    }
 
 
    public String getSuit() {
        return suit;
    }
 
 
    public String getValue() {
        return value;
    }
 
 
    public String getImage() {
        return image;
    }
}

class Demo {
    public static void main(String[] args) {
        CardDeck deck = new CardDeck();
        System.out.println("\nOrdered deck of cards: ");
        deck.displayDeck();
        System.out.println("\nShuffled deck of cards: ");
        deck.shuffleDeck();
        deck.displayDeck();
    }
}