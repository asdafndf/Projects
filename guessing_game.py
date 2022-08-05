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