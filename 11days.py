import random
import art11


def deal_cards():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card
def calculate_score(cards):
    if sum(cards)==21 and len(cards)>21:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score,c_score):
    if u_score==c_score:
        return "Draw🤷‍♂️"
    elif c_score==0:
        return "Lose,opponent has Blackjack😒"
    elif u_score==0:
        return "you win,with Blackjack✌️ "
    elif u_score>21:
        return "you went over.you lose😤"
    elif c_score>21:
        return "opponent went over.You Win😜"
    elif u_score>c_score:
        return "YOU Win🏆"
    else:
        return "you lose🤦‍♀️"

def play_game():
    print(art11.logo)
    user_cards=[]
    computer_cards=[]
    computer_score=-1
    user_score=-1
    is_game_over=False
    for _ in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    while not is_game_over:
        user_score=calculate_score((user_cards))
        computer_score=calculate_score((computer_cards))
        print(f"your cards:{user_cards},current score:{user_score}")
        print(f" computer cards:{computer_cards},current score:{computer_score}")

        if user_score==0 or computer_score==0 or user_score>21:
            is_game_over=True
        else:
            user_should_deal=input("Type 'y' to get anther card,type 'n' to pass:")

            if user_should_deal=='y':
                user_cards.append(deal_cards())
            else:
                is_game_over=True
    while computer_score!=0 and computer_score<17:
        computer_cards.append(deal_cards())
        computer_score=calculate_score(computer_cards)

    print(f"you final hand:{user_cards},final score:{user_score}")
    print(f"computers final hand:{computer_cards},final score:{computer_score}")
    print(compare(user_score,computer_score))




play_game()




