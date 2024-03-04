############### Blackjack Game #####################

"""The deck is unlimited, the Jack/Queen/King all count as 10, the ace can count as 11 or 1 depend on situation
The cards have equal probability of existing
If score is over 21 then it's immediately over"""


import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    random_card=random.choice(cards)
    return random_card

def calculate_score(list_of_cards):
    total_score=sum(list_of_cards)
    #print(total_score)
    if sum(list_of_cards) == 21 and len(list_of_cards)== 2:
        return 0
    if 11 in list_of_cards and sum(list_of_cards) > 21:
        list_of_cards.remove(11)
        list_of_cards.append(1)
    return total_score

new=True

while(new):

    user_cards = []
    computer_cards = []

    user_cards.append(deal_card())
    user_cards.append(deal_card())


    computer_cards.append(deal_card())
    computer_cards.append(deal_card())
    is_game_over=False

    while not is_game_over:

        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)
        print(f"User cards are {user_cards} and your current score is {user_score}")
        print(f"Computer first card is {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over=True
            print("Game over")
        else:
            has_ended = input("Do you want to draw another card? Type 'y' or 'n':")
            if has_ended == "y":
                user_cards.append(deal_card())
                user_score = calculate_score(user_cards)
            else:
                is_game_over = True



    while computer_score != 0  and computer_score <17:
        computer_cards.append(deal_card())
        computer_score=calculate_score(computer_cards)



    def compare(user,computer):
        if user == computer:
            print("It's a draw")
        elif computer == 0:
            print(f"Computer score is {computer} has a blackjack, you lost")
        elif user == 0:
            print(f"Your score is {user}, you have a blackjack , you won")
        elif user > 21:
            print(f"Your score {user} is higher than 21, you lost")
        elif computer > 21:
            print(f"Computer score is {computer}. It's higher than 21, you won")
        elif user > computer:
            print(f"Your score {user} is higher than computer score {computer}, you won")
        else:
            print(f"Your score {user} is lower than computer score {computer}, you lost")




    print(f"Your final hand is: {user_cards}, final score: {user_score}\n ")
    print(f"Computer final hand is: {computer_cards}, final score: {computer_score} \n")
    compare(user=user_score,computer=computer_score)


    again=input("Do you want to restart the game? Type 'y' or 'n':\n")
    if again == "y":
        new=True
    else:
        print("Thank you for the game. See you next time!\n")
        new=False




