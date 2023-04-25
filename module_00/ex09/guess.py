from random import randint
import sys

def print_end(secret, count):
    if (secret == 42):
        print("The answer to the ultimate question of life, the universe and everything is 42.")
    if (count == 1):
        print("Congratulations! You got it on your first try!")
    else:
        print("Congratulations, you've got it!")
        print(f"You won in {count} attempts!")

print("This is an interactive guessing game!")
print("You have to enter a number between 1 and 99 to find out the secret number.")
print("Type 'exit' to end the game.")
print("Good luck!")
secret = randint(1, 99)
nb = 0
count = 0
while (nb != secret):
    print("What's your guess between 1 and 99?")
    number = input()
    count += 1
    if (number == 'exit'):
        sys.exit('Goodbye !')
    try :
        nb = int(number)
    except:
        print("That is not a number")
        continue
    
    if (nb > secret):
        print("Too hight!")
    elif (nb < secret):
        print("Too low!")
    else:
        print_end(secret, count)
        sys.exit('')                                                                                                                                                                                                                                                                                                                                        