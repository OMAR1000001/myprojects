from game_data import data
import random

loop = True
turns = 0


def game():
    global loop

    def comper(chosen, chosen1):
        chosen = int(data[chosen]['follower_count'])
        chosen1 = int(data[chosen1]['follower_count'])
        if chosen > chosen1:
            return "comare"
        else:
            return "agenst"

    def right(turn, user):
        if user == "A":
            if comper(chosen=chosen,chosen1=chosen1) == "comare":
                return turn + 1
            else:
                return turn
        elif user == "B":
            if comper(chosen=chosen,chosen1=chosen1) == "agenst":
                return turn + 1
            else:
                return turn
        else:
            return turn

    chosen1 = random.choice(range(0, 50))
    while loop:
        global turns
        T=turns
        print(f"your score is {turns}")
        chosen=chosen1
        chosen1 = random.choice(range(0, 50))
        comp1 = data[chosen]['name'], data[chosen]['description'], data[chosen]['country']
        agns = data[chosen1]['name'], data[chosen1]['description'], data[chosen1]['country']
        print(f"A-compare: {comp1}\nB-against: {agns} ")
        user = input("whitch one do you thing have more followers (A or B): ")
        comper(chosen=chosen, chosen1=chosen1)
        turns = right(turn=turns, user=user)
        if turns == T:
            print("wronge ANSWER, Try again ")
            print(f"your total score is {T}")
            loop = False




game()


