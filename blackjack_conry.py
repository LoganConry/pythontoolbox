#Logan Conry
#Blackjack project ISAN 3305
#I did not pick to do any extra rules, just enjoy the vibes of a simple game


import random
NUM_DECKS = 2
RESHUFFLE_AT = 20
DECK_SIZE = 52
DEALER_STANDS_AT = 17
BLACKJACK_PAYS = 1.5


#Builds the shoe randomly for the 2 decks
def build_shoe(num_decks):
    shoe = []
    for decks in range(num_decks):
        for cards in range(DECK_SIZE):
            shoe.append(cards)
    random.shuffle(shoe)
    return shoe

#The program guarantees that a card wont be dealt twice by using the pop function, which removes the item it selects from the list entirely.
#Because of this, that card will never be dealt again until the decks are reshuffled.
#As this loops, it will remove cards until it reacheds the reshuffle threshold and restart.
def deal_card(shoe):
    card = shoe.pop()
    return card

#Assigns a text name based on the previously established rank and suit which i reuse here
def card_name(card):
    suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
    faces = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
    rank = faces[card % 13]
    suit = suits[card // 13]
    card_pick = (f"{rank} of {suit}")
    return card_pick


#This next part is primarily from the packet as of right now sorry but it uses the different operators to see which of the 13 faces and 4 suits it is
def hand_value(hand):
    total = 0
    aces = 0
    for card in hand:
        rank = card % 13
        if rank == 12:
            total += 11
            aces += 1
        elif rank >= 8:
            total += 10
        else:
            total += rank + 2
    while total > 21 and aces > 0:
        total -= 10
        aces -= 1
    return total

#Checks the two constraints to see if it is a blackjack or not
def is_blackjack(hand):
    if len(hand) == 2 and hand_value(hand) == 21:
        blackjack = True
    else:
        blackjack = False
    return blackjack

#Shows the players hand and creates that list
def show_player(hand):
    player_hand = []
    for card in hand:
        player_hand.append(card_name(card))
    print (f"Current Player Hand: {player_hand}; Current Total {hand_value(hand)}")

#Shows the dealers hand and handles the hole rule
def show_dealer(hand, hide_hole):
    dealer_hand = []
    for card in hand:
        dealer_hand.append(card_name(card))
    if hide_hole == True:
        print(f"Current Dealer Hand: {dealer_hand[0]}, hidden")
    else:
        print(f"Current Dealer Hand: {dealer_hand}")

#Gets the bet from the user and validates the entry
def get_bet(balance):
    bet_amount = int(input(f"How much would you like to bet? Only accepting whole number bets. Current balance is ${balance:.2f}. "))
    while bet_amount < 1 or bet_amount > balance:
        print("Bet amount is invalid")
        bet_amount = int(input(f"How much would you like to bet? Only accepting whole number bets. Current balance is ${balance:.2f}. "))
    else:
        return bet_amount

#Getting the buy in and validates it
def get_buy_in():
    buy_in = int(input("What is your starting buy in? "))
    while buy_in < 1:
        print("Invalid buy in")
        buy_in = int(input("What is your starting buy in? "))
    return buy_in

#Whole bunch of stuff for the players turns, establishes rules for standing, doubling down, and hitting
def player_turn(hand, shoe, bet, balance):
    turn_over = False
    while turn_over != True:
        user_input = str(input("What would you like to do? (hit, double, stand) "))
        if user_input == "stand":
            turn_over = True
        elif user_input == "double":
            if bet*2 <= balance and len(hand) == 2:
                bet = bet*2
                hand.append(deal_card(shoe))
                show_player(hand)
                turn_over = True
            else:
                print("You are not able to double down as your balance is too low or you have too many cards" )          
        elif user_input == "hit":
            hand.append(deal_card(shoe))
            show_player(hand)
            if hand_value(hand) > 21:
                turn_over = True
            elif hand_value(hand) == 21:
                turn_over = True
        else:
            print("Invalid choice: What would you like to do? (hit, double, stand) ")
    
    return bet

#Does the dealers turn which is rather simple, he just stands at a certain number and hits otherwise
def dealer_turn(hand, shoe):
    while hand_value(hand) < DEALER_STANDS_AT:
        hand.append(deal_card(shoe))

#Settles the bet based on the outcomes. It is ordered as such that outcomes that exclude other outcomes are done first, i.e. it checks blackjacks first to as to ensure it isnt checking a blackjack for a push or something later on    
def settle(player_hand, dealer_hand, bet):
    if is_blackjack(player_hand) == True and is_blackjack(dealer_hand) == False:
        result = (bet * BLACKJACK_PAYS)
    elif is_blackjack(dealer_hand) == True and is_blackjack(player_hand) == False:
        result = bet * -1
    elif hand_value(player_hand) > 21:
        result = bet * -1
    elif hand_value(dealer_hand) > 21:
        result = bet
    elif hand_value(player_hand) > hand_value(dealer_hand):
        result = bet
    elif hand_value(dealer_hand) > hand_value(player_hand):
        result = bet * -1
    else:
        result = 0
    return result

#Does the play hand thing, largely from the packet but I did it in my preferred way of checking the boolean values and checking for the blackjacks.
def play_hand(shoe, bet, balance):
    player = []
    dealer = []
    player.append(deal_card(shoe))
    dealer.append(deal_card(shoe))
    player.append(deal_card(shoe))
    dealer.append(deal_card(shoe))
    show_player(player)
    show_dealer(dealer, True)
    if is_blackjack(dealer) == True or is_blackjack(player) == True:
        if is_blackjack(dealer) == True and is_blackjack(player) != True:
            print("Dealer Blackjack! ")
        elif is_blackjack(player) == True and is_blackjack(dealer) != True:
            print("Player Blackjack! ")
        else:
            print("Dual Blackjack whoaaa! ")
        return settle(player, dealer, bet), player, dealer, bet
    bet = player_turn(player, shoe, bet, balance)
    if hand_value(player) >21:
        show_dealer(dealer, False)
        return -bet, player, dealer, bet
    dealer_turn(dealer, shoe)
    show_dealer(dealer, False)
    return settle(player, dealer, bet), player, dealer, bet

#Simple validated loop checking if we can play again
def play_again():
    replay = input("Play again? y/n ")
    while replay != "y" and replay != "n" and replay != "Y" and replay != "N":
        print("Invalid choice")
        replay = input("Play again? y/n ")
    if replay == "y" or replay == "Y":
        replay = True
    else:
        replay = False
    return replay

#Keeps track of the biggest win
def update_biggest_win(biggest_win, result):
    if result > biggest_win:
        biggest_win = result
        return biggest_win
    else:
        return biggest_win

#Checks if we need to reshuffle and does, then reassigns to the shoe
def check_reshuffle(shoe, num_decks):
    if len(shoe) < RESHUFFLE_AT:
        shoe = build_shoe(num_decks)
        print("Reshuffling")
    return shoe
    
#Prints a summary list of all of the key metrics from your session
def cash_out(buy_in, balance, hands, biggest_win):
    net = balance - buy_in
    print(f"Buy in: ${buy_in:.2f}")
    print(f"Final Balance: ${balance:.2f}")
    print(f"Net Winnings: ${net:.2f}")
    print(f"Hands Played: {hands}")
    print(f"Biggest Win: ${biggest_win:.2f}")

def show_log(file_name):
    infile = open(file_name, 'r')
    for line in infile:
        print(line.rstrip('\n'))
    infile.close()


#I didnt want to have a bunch of stuff in main so i made this to kind of consolidate
#Sets the baselines for the games such as win, hands and buy in. Then loops while game conditions are valid and returns the values.
#Okay at this point this is a big function with various things oops
def play_session(buy_in, num_decks):
    biggest_win = 0
    hands = 0
    balance = buy_in
    keep_playing = True
    shoe = build_shoe(num_decks)
    balance_log = open('balance_log.txt', 'w')
    balance_log.write(f"Starting Balance: ${buy_in:.2f} \n")
    balance_log.close()
    hand_log = open('hand_log.txt', 'w')
    hand_log.write(f"Hand Log \n")
    hand_log.close()
    while keep_playing == True and balance >= 1:
        shoe = check_reshuffle(shoe, num_decks)
        bet = get_bet(balance)
        result, player_hand, dealer_hand, last_bet = play_hand(shoe, bet, balance)
        hand_log = open('hand_log.txt', 'a')
        hand_log.write(f"Hands: {hands+1} \n Last Bet: ${last_bet:.2f} \n")
        hand_log.write("Player \n")
        for card in player_hand:
            hand_log.write(f"{card_name(card)} \n")
        hand_log.write(f"Hand Value: {hand_value(player_hand)} \n")
        hand_log.write("Dealer \n")
        for card in dealer_hand:
            hand_log.write(f"{card_name(card)} \n")
        hand_log.write(f"Hand Value: {hand_value(dealer_hand)} \n")
        hand_log.write(f"Result: ${result:.2f} \n")
        hand_log.write("\n")
        hand_log.close()
        if result > 0:
            print(f"You won ${result:.2f}")
        elif result < 0:
            print(f"You lost ${result:.2f}")
        else:
            print("Push Bet. Money Back")
        balance = result + balance
        hands = hands + 1
        balance_log = open('balance_log.txt', 'a')
        balance_log.write(f"Hands: {hands}, Result: ${result:.2f}, Balance: ${balance:.2f} \n")
        balance_log.close()
        biggest_win = update_biggest_win(biggest_win, result)
        print(f"Balance: ${balance:.2f} ")
        if balance >= 1:
            keep_playing = play_again()
        else:
            print("Out of money, minimum bet is $1")
    return balance, hands, biggest_win
 
         

def main():
    buy_in = get_buy_in()
    balance, hands, biggest_win = play_session(buy_in, NUM_DECKS)
    cash_out(buy_in, balance, hands, biggest_win)
    view_log = input("View a log? (balance, hands, none) ")
    if view_log == "hands":
        show_log("hand_log.txt")
    elif view_log == "balance":
        show_log("balance_log.txt")
    else:
        print("goodbye")
        
main()
