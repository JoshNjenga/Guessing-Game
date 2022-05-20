import random
n = 33
guess = 0
to_be_guessed = int(n * random.random()) + 1

while guess != to_be_guessed:
    guess = int(input("Number: "))
    if guess < to_be_guessed:
        print("number is too small")
    elif guess > to_be_guessed:
        print("number too large")
else:
    print("Congratulations, you are correct")