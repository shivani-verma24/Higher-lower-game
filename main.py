from game_data import data
from art import logo, vs
import random

score = 0
A = random.choice(data)
print(logo)

while (True):

    print("Compare A: ", end=" ")
    print(A['name'] + ", " + A['description'] + ", from " + A['country'])
    print(vs)

    B = random.choice(data)
    if (A == B):
        B = random.choice(data)

    print("Against B: ", end=" ")
    print(B['name'] + ", " + B['description'] + ", from " + B['country'])

    ch = input("Who has more followers? Type 'A' or 'B': ").upper()


    prev = score

    if (ch == 'A'):
        if (A['follower_count'] > B['follower_count']):
            score += 1
    elif (ch == 'B'):
        if (A['follower_count'] < B['follower_count']):
            score += 1

    if (score > prev):
        print(f"You're right! Current score: {score}")
        A = B.copy()

    else:
        print(f"Sorry, that's wrong. Final score: {prev}")
        break

# Project by Shivani Verma