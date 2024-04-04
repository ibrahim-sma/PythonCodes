"""
17) Write a python program to solve Rock-Paper scisscor between user & computer.
Also, include a logic to declare the winner of 5 points. 
Between, Rock & Paper -> paper wins; Paper & Scissor -> Scissor wins; Scissor & Rock -> Rock wins.
Note: Print the output in the following format: Round-wise score details
"""

import random

inp_list = ["rock", "paper", "scissor"]

user_score = 0
comp_score = 0

while True:
    random.shuffle(inp_list)
    comp_choice = random.choice(inp_list)
    user_choice = input("\nEnter your Choice: rock, paper, scissor: ")

    if user_choice not in inp_list:
        print("\n***Enter a choice only from rock, paper, scissor***")
        continue

    if  user_choice == comp_choice:
        print(f"\nBoth User & Computer has selected {user_choice}. Hence No point")
        continue
    else:
        print("Computer's choice:", comp_choice)
        print("User's choice: ", user_choice)
        print()

        if user_choice == "rock":
            if comp_choice == "scissor":
                user_score += 1
            else:
                comp_score += 1
        elif user_choice == "paper":
            if comp_choice == "rock":
                user_score += 1
            else:
                comp_score += 1
        else:
            if comp_choice == "paper":
                user_score += 1
            else:
                comp_score += 1
    
        print("Computer's Score:", comp_score)
        print("User's Score: ", user_score)
        print()
        
    if user_score == 5:
        print("User Wins")
        break
    elif comp_score == 5:
        print("Computer Wins")
        break
