# Project - Blackjack
# project-url - http://www.codeskulptor.org/#user44_zO4zuFQx4qO7VQT_3.py

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
score = 0
message = ["", ""]
stand = False

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand = []	# create Hand object

    def __str__(self):
        string = "Hand contains: "
        for card in self.hand:
            string += card.get_suit() + card.get_rank()
        return string	# return a string representation of a hand

    def add_card(self, card):
        self.hand.append(card)	# add a card object to a hand

    def get_value(self):
        # compute the value of the hand
        value = 0
        for card in self.hand:
            value += VALUES[card.get_rank()]
            if card.get_rank() == 'A' and (value+10) <= 21:
                value += 10# count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        return value					
   
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        for card in self.hand:
            card.draw(canvas, pos)
            pos[0] += 72
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.deck = []	# create a Deck object
        for suit in SUITS:
            for rank in RANKS:
                card = Card(suit, rank)
                self.deck.append(card)
            

    def shuffle(self):
        random.shuffle(self.deck)# shuffle the deck 
        return self.deck# use random.shuffle()

    def deal_card(self):
        return self.deck.pop()	# deal a card object from the deck
    
    def __str__(self):
        string = "Deck Contains "
        for card in self.deck:
            string += str(card.get_suit())+str(card.get_rank())
        return string	# return a string representing the deck



#define event handlers for buttons
def deal():
    global in_play, dealer_hand, player_hand, deck,  message, stand, score
    stand = False
    
    message[0] = 'Hit or Stand?'
    message[1] = ""
    deck = Deck()
    deck.shuffle()
    
    dealer_hand = Hand()
    player_hand = Hand()
    
    player_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    
    dealer_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    
    if in_play:
        message[0] = "Player loses!"
        score -= 1
        
    in_play = True
    return player_hand, dealer_hand

def hit():
    # replace with your code below
    global player_hand, deck, score, in_play, message, stand
    if in_play:  # if the hand is in play, hit the player
        player_hand.add_card(deck.deal_card())
          
        if player_hand.get_value() > 21: # if busted, assign a message to outcome, update in_play and score
            stand = False
            in_play = False
            message[1] = 'Player busted!'
            message[0] = 'New Deal?'
            score -= 1
    
       
def stand():
    # replace with your code below
    global dealer_hand, in_play, score, message, deck, player_hand, stand

    stand = True
    if in_play:# if hand is in play, repeatedly hit dealer until his hand has value 17 or more
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(deck.deal_card())
        if dealer_hand.get_value() > 21: # assign a message to outcome, update in_play and score
            message[1] = 'Dealer busted!!'
            score += 1
        else:
            if dealer_hand.get_value() >= player_hand.get_value():
                message[1] = 'Dealer wins!'
                score -= 1
            else:
                message[1] = 'Player wins!'
                score += 1
    message[0] = 'New deal?'
    in_play = False
    

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_polyline([(340, 500), (340, 610), (590, 610), (590, 500), (340, 500)], 3, 'Maroon')
    canvas.draw_text("Rules", (445, 520), 21, 'aqua')
    canvas.draw_text("1. Highest hand of 21 or less wins.", (345, 535), 14, 'Yellow')
    canvas.draw_text("2. Tie goes to the dealer.", (345, 552), 14, 'Yellow')
    canvas.draw_text("3. Dealer hits until cards total at least 17.", (345, 569), 14, 'Yellow')
    canvas.draw_text("4. Card totals over 21 are bust.", (345, 586), 14, 'Yellow')
    canvas.draw_text("5. Card total of 21 is 'blackjack.'", 
   
    canvas.draw_text(message[0], (400, 350), 30, "yellow")
    canvas.draw_text(message[1], (400, 420), 30, "yellow")
    canvas.draw_text(("SCORE: " + str(score)), (400, 50), 30, "yellow")
    canvas.draw_text("BLACKJACK", (50, 50), 40, "yellow")    
    
    player_pos = [60, 440]
    dealer_pos = [60, 70]
    
    player_hand.draw(canvas, player_pos)
    dealer_hand.draw(canvas, dealer_pos)
    if not stand:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_SIZE,
                          [60 + CARD_BACK_CENTER[0], 70 + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 620)
frame.set_canvas_background("Green")

# create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()

