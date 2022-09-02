# Basic guessing game inspiried by freeCodeCamp

secret_word = "water"
guess = ""
max_trials = 3
trials = 0

while guess != secret_word:
    if trials == max_trials:
        print("You lose!")
        break
    else:
        guess = input("Your guess goes here: ")
        trials += 1

if guess == secret_word:
    print("You win!")

# Guessing game inspired by Mosh

secret_word = "apple"
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = input("Guess a fruit: ")
    if guess == secret_word:
        print("You win!")
        break
    guess_count += 1
else:
    print("You lose!")