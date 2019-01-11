# 1:14 1:28 14

import random

def main():
    options = ["Rock", "Paper", "Scissors"]
    random_choice = random.choice(options)
    your_choice = int(input("1 for Rock, 2 for Paper, 3 for Scissors: "))
    print("Computer:", random_choice)
    print("User:", options[your_choice-1])

main()
