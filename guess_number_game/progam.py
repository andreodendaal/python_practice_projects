
import random

print('-----------------------------------------')
print('         GUESS THAT NUMBER GAME')
print('-----------------------------------------')
print()

the_number = random.randint(0, 100)
guess = -1
input_name = input("Whats your name? ")
while guess != the_number:
    input_str_number = input("Enter any number between 0 and 100: ")
    guess = int(input_str_number)

    if guess < the_number:
        print("Your guess of {0} was too low {1}, try again! ".format(guess, input_name))

    elif guess > the_number:
        print("Your guess of {0} was too high {1}, try again !".format(guess, input_name))

    else:
        print("You win, great job {0}!".format(input_name))

print("Done")




