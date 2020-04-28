import random
name = input("Hello there, what is your name: ")
secretNumber = random.randint(1, 20)
print('Greetings, '+name+' ,I am thinking of a number between 1 and 20.')
print('Take a guess:')
for guessTaken in range(1, 7):
    guess = int(input())
    if guess < secretNumber:
        print('No '+name+'! Your guess is too low. You have', (6 - guessTaken), 'chances left. Try again!!')
    elif guess > secretNumber:
        print('No '+name+'! Your guess is too high. You have', (6 - guessTaken), 'chances left. Try again!!')
    else:
        break
if guess == secretNumber:
    print('Good job '+name+'! You guessed my number in ' + str(guessTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))
