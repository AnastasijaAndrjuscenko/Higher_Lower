from art import logo, vs
from game_data import data
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


print(logo)
i = 0
k = 1
score = 0


def correct_answer(a, b):
    a_followers = a
    b_followers = b
    if a_followers > b_followers:
        # 1 - A
        return "A"
    else:
        # 2 - B
        return "B"


def sel_ab():
    global i, k, score
    # TYPO: create an array to collect info for a
    info_1 = []
    # writes all info about A
    for key in data[i]:
        info_1.append(data[i].get(key))
    print(f"Compare A: {info_1[0]}, a {info_1[2]}, from {info_1[3]}")
    # create an array to collect info for a B
    info_2 = []
    # print out VS picture
    print(vs)
    # writes all info about A
    for key in data[k]:
        info_2.append(data[k].get(key))
    print(f"Compare B: {info_2[0]}, a {info_2[2]}, from {info_2[3]}")

    answer = (input("Who has more followers? Type 'A' or 'B:'")).upper()
    if answer != correct_answer(info_1, info_2):
        cls()
        print(logo)
        print(f"Sorry, that's wrong. Final score is: {score}")
        return
    else:
        if correct_answer(info_1, info_2) == "A":
            k += 1
        else:
            i = k
            k += 1
        cls()
        print(logo)
        score += 1
        print(f"You are right. Current score is {score}")
        sel_ab()


sel_ab()
