import random
number = random.randint(1, 10)
number_of_guesses = 0
user_name = input("Hello, What's your name?")
print('okay! '+ user_name+  " You're am Guessing a number between 1 and 10:")

while number_of_guesses < 5:
    guess = int(input())
    number_of_guesses +=1
    if guess < number:
        print('Too Low')
    if guess  > number:
        print('Too High')

    if guess == number:
        break
if guess == number:
    print('You guessed the number in ' + str(number_of_guesses) + ' tries!')
else:
    print("You did'nt guess the number, The number was " + str(number))