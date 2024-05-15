import random

print("Welcome to blackjack")

gaming = True

ballance = 100
wager = 0

points = {
    'A+': 11,
    'A-': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10
}
yourhand = []
yourpoints = 0
dealerhand = []
dealerpoints = 0


def youdrawhand():
    global yourpoints
    drawn = deck.pop(random.randint(0,len(deck)-1))
    if drawn == 'A':
        valcheck = True
        while valcheck:
            value = input("You drew an Ace, do you want it to equal 1 or 11 (1/11) ")
            if value == '1':
                yourhand.append('A-')
                yourpoints += 1
                valcheck = False
            elif value == '11':
                yourhand.append('A+')
                yourpoints += 11
                valcheck = False
            else:
                print("invalad value")
    else:
        yourhand.append(drawn)
        yourpoints += points[drawn]
    print("Your hand: " + str(yourhand) + ". Points: " + str(yourpoints))


def dealerdraw():
    global dealerpoints
    drawn = deck.pop(random.randint(0,len(deck)-1))
    if drawn == 'A':
        if dealerpoints + 11 > 17:
            dealerpoints += 1
            dealerhand.append('A-')
        else:
            dealerhand.append('A+')
            dealerpoints += 11
    else:
        dealerhand.append(drawn)
        dealerpoints += points[drawn]
    print("Dealer hand: " + str(dealerhand) + ". Points: " + str(dealerpoints))


def gameplay():
    global ballance
    print("Dealing cards.")
    youdrawhand()
    dealerdraw()
    youdrawhand()
    dealerdraw()
    thatgame = True
    while thatgame:
        decide = input("Hit or stand? (h/s) ")
        if decide == "h":
            youdrawhand()
            if yourpoints > 21:
                print("You lose.")
                ballance -= wager
                thatgame = False
        if dealerpoints < 17 and yourpoints <= 21:
            dealerdraw()
        if dealerpoints > 21:
            print("You win!")
            thatgame = False
            ballance += wager
        elif decide != "h":
            if yourpoints > dealerpoints:
                print("You win!")
                thatgame = False
                ballance += wager
            elif yourpoints == dealerpoints:
                print("Standoff")



while gaming:
    yourhand = []
    dealerhand = []
    yourpoints = 0
    dealerpoints = 0
    deck = ['A','2','3','4','5','6','7','8','9','10','J','Q','K','A','2','3','4','5','6','7','8','9','10','J','Q','K','A','2','3','4','5','6','7','8','9','10','J','Q','K','A','2','3','4','5','6','7','8','9','10','J','Q','K']
    wagering = True
    while wagering:
        wager = int(input("Your ballance is " + str(ballance) + " chips. How many would you like to wager? "))
        if wager > ballance:
            print("Wager too high, try again")
        elif wager < 1:
            print("That isn't even a wager.")
        else:
            wagering = False
    gameplay()
    cont = input("Do you want to continue? (y/n) ")
    if cont == 'n' or ballance == 0:
        gaming = False
        print("You left with a ballance of " + str(ballance) + " chips.")