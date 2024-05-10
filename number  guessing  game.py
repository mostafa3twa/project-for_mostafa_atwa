from random import randint

answer=randint(1,100)
attemps_hard=5
attemps_easy=10
#creat a function for the hard game
def H_game():
    """ if you choise the hard game"""
    global attemps_hard
    global answer
    while attemps_hard !=0:
        guess_user=int(input("make a guess:"))
        if guess_user!= answer and guess_user>answer:
            print("Too high.\n guess again.")
            attemps_hard-=1
            print(f"You have {attemps_hard} attemps remaining to guess the number")
        elif guess_user!=answer and guess_user<answer:
              print("Too low.\n guess again.")
              attemps_hard-=1
              print(f"You have {attemps_hard} attemps remaining to guess the number")
        elif guess_user==answer:
              print(f"You got it! The answer was {answer}.")
              attemps_hard=0


# creat a function for the easy game
def E_game():
     """ if you choise the easy game"""
     global attemps_easy
     global answer
     while attemps_easy !=0:
            guess_user=int(input("make a guess:"))
            if guess_user!= answer and guess_user>answer:
                print("Too high.\n guess again.")
                attemps_easy-=1
                print(f"You have {attemps_easy} attemps remaining to guess the number")
            elif guess_user!=answer and guess_user<answer:
                print("Too low.\n guess again.")
                attemps_easy-=1
                print(f"You have {attemps_easy} attemps remaining to guess the number")
            elif guess_user==answer:
                print(f"You got it! The answer was {answer}.")
                attemps_easy=0



print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard': ")
if level=="hard":
     print(f"You have {attemps_hard} attemps remaining to guess the number ")
     H_game()
     if H_game==0:
          print("You lose")

elif level=="easy":
     print(f"You have {attemps_easy} attemps remaining to guess the number ")
     E_game()
     if E_game==0:
          print("You lose")
     


