import random

target = random.randint(1,100)

while True:
    user_Guess = input("Guess the target or Quit(Q): ")
    if (user_Guess == "Q"):
        break

    user_Guess = int(user_Guess)
    if user_Guess == target:
        print("Success: Correct Guess!!")
        break
    elif user_Guess > target:
        print("Your number was too high!! Guess Smaller number...")

    else:
        print("Your number was too low!! Guess higher number...")

print("--Game Over--")