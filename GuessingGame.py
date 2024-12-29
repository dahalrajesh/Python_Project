import random
jackpot = random.randint(1,100)
# print(jackpot)
print("Welcome to the Guessing Game!")
print("Try to guess the number between 1 and 100.")
counter = 0
guess = None
while guess != jackpot:
    try:
        guess = int(input("Enter the  Guessing number:"))
        counter +=1
        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
        elif guess < jackpot:
            print("Too low! Try a higher number.")
        elif guess > jackpot:
            print("Too high! Try a lower number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
print("You Are correct, you won the Lottery")
print(f"You get corrected at  {counter}  attempts. ")