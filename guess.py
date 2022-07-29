#Dependencies Here
import random

#### Begin Program ####

print("Enter the low number")
low_number = int(input())

print("Please enter the high number")
high_number = int(input())

print("High: " + str(high_number))
print("Low: " + str(low_number))

while low_number > (high_number - 10):
    print("Please try again, make sure your low number is at least 10 smaller than your high number")
    low_number = int(input("Low: "))
    high_number = int(input("High: "))

secret_number = random.randint(low_number,high_number)


print("Enter a guess")
guess = int(input())

counter = 1

while guess != secret_number:
    if guess < low_number or guess > high_number:
        print("Don't be stupid!")    
    elif guess > secret_number:
        print("Lower....")
    elif guess < secret_number:
        print("Higher")
    guess = int(input())
    counter = counter + 1
    print("Guesses left: " + str(10 - counter))

if counter >= 10:
    print("You Lose!")
elif guess == secret_number:
    print("You win!, the secret number is " + str(secret_number))