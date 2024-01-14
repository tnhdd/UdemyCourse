import random


def playing_game():
    global remaining_guess
    random_number = random.randint(1, 100)
    print("Welcome to number guessing game")
    print(f"I am thinking a number between 1 and 100. The answer is {random_number}")
    difficulty = input("Choose a difficulty, type 'easy' or 'hard' ")
    game_over = False

    if difficulty == "easy":
        remaining_guess = 10
    elif difficulty == "hard":
        remaining_guess = 5

    while not game_over and remaining_guess > 0:
        user_guest = int(input("Guess a number "))
        if user_guest == random_number:
            game_over = True
            print("You got the number!")
        if user_guest > random_number:
            remaining_guess -= 1
            print(f"Too high, you have {remaining_guess} remaining guess left")
        elif user_guest < random_number:
            remaining_guess -= 1
            print(f"Too low, you have {remaining_guess} remaining guess left")
        if remaining_guess == 0:
            print("Game over")


playing_game()

"""
from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
  checks answer against guess. Returns the number of turns remaining.
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

#Make function to set difficulty.
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  print(logo)
  #Choosing a random number between 1 and 100.
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
  print(f"Pssst, the correct answer is {answer}")

  turns = set_difficulty()
  #Repeat the guessing functionality if they get it wrong.
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")

    #Let the user guess a number.
    guess = int(input("Make a guess: "))

    #Track the number of turns and reduce by 1 if they get it wrong.
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")


game()


"""
