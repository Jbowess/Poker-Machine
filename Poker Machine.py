import random

#symbols that appear on Poker Machine
pokerSymbols = ["@", "$", "%", "#", "&"]
#method of input
while True:
    credit = 100
    print("Welcome to DragonLink Slot Machine, Goodluck")
    while credit > 0:
        print("Balance: ", "$",credit)
        try:
            bet = int(input("Bet Total: "))
        except:
            print("Do not include Cent bets")
            continue
        if bet > credit:
            print("Invalid amount")
# Value of each box within poker machine
        else:
            credit -= bet
            box1Horizontal = random.choice(pokerSymbols)
            box2Horizontal = random.choice(pokerSymbols)
            box3Horizontal = random.choice(pokerSymbols)
            box4Horizontal = random.choice(pokerSymbols)


            box1Vertical = random.choice(pokerSymbols)
            box2Vertical = random.choice(pokerSymbols)
            box3Vertical = random.choice(pokerSymbols)
            box4Vertical = random.choice(pokerSymbols)
            box5Vertical = random.choice(pokerSymbols)

# Creating the format of the poker machine

            print("|====================|")
            print("|", box1Vertical, "|", random.choice(pokerSymbols), "|", random.choice(pokerSymbols), "|", random.choice(pokerSymbols), "|", random.choice(pokerSymbols), " |")
            print("|====================|")
            print("|", box2Vertical, "|", random.choice(pokerSymbols), "|", random.choice(pokerSymbols), "|", random.choice(pokerSymbols), "|", random.choice(pokerSymbols), " |")
            print("|====================|")
            print("|", box3Vertical, "|", box1Horizontal, "|", box2Horizontal, "|", box3Horizontal, "|", box4Horizontal, " |")
            print("|====================|")
            print("|", box4Vertical, "|", random.choice(pokerSymbols), "|", random.choice(pokerSymbols), "|", random.choice(pokerSymbols), "|", random.choice(pokerSymbols), " |")
            print("|====================|")
            print("|", box5Vertical, "|", random.choice(pokerSymbols), "|", random.choice(pokerSymbols), "|", random.choice(pokerSymbols), "|", random.choice(pokerSymbols), " |")
            print("|====================|")
# sorting the different ways of wining
            if box3Vertical == box1Horizontal and box1Horizontal == box2Horizontal and box2Horizontal == box3Horizontal and box3Horizontal == box4Horizontal:
                winnings = bet * 10
                print("You won!: ", "$", winnings)
                credit += winnings
            elif box1Vertical == box2Vertical and box2Vertical ==  box3Vertical and box3Vertical == box4Vertical and box5Vertical == box5Vertical:
                winnings = bet * 10
                print("You won!: ", "$", winnings)
                credit += winnings
            elif box1Vertical == box2Vertical and box2Vertical == box3Vertical and box3Vertical == box4Vertical and box5Vertical == box1Horizontal and box1Horizontal == box2Horizontal and box2Horizontal == box3Horizontal and box3Horizontal == box4Horizontal:
                winnings = bet * 44
                print("JACKPOT!!!!!!!!!!!: ", "$", winnings)
                credit += winnings
            elif box2Vertical == box3Vertical and box3Vertical == box4Vertical:
                winnings = bet * 4
                print("You won!: ", "$", winnings)
                credit += winnings
            elif box1Horizontal == box2Horizontal and box2Horizontal == box3Horizontal:
                winnings = bet * 4
                print("You won!: ", "$", winnings)
                credit += winnings
            else:
                print("You lost, Keep Playing")
    print("You are out of Credit")
    print("Thank you for playing Dragon link!")
    print()