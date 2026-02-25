"""
18) Write a hangman game program where the user will predict the letters of the word.
A user has to guess the word within 7 attempts.
"""
import random

random_list = """
Quantum,computing,virtual,reality,augmented,reality,driving,drone,delivery,
gene,editing,personalized,medicine,printing,bioprinting,sustainable,technology,
renewable,energy,vertical,farming,space,exploration,artificial,general,intelligence,
social,medias,influence,ethical,digital,privacy,concerns,future,automation,
robotics,lifelong,learning,citizen,science,global,connectivity,information,overload
""".replace("\n", "").split(",")
print(random_list)

# random.shuffle(random_list)
# guess_word = random.choice(random_list).lower()
# while True:
#     print("\nCurrent Guess:")
#     print("_"*len(guess_word))
#     break

choice_count = 7

guessed_letters = []


word = "animation"
print(word.index("a"))
print(word.find("a"))

while choice_count:
    my_guess = input("Enter a letter of choice from alphabet a-z: ")





