import random
n = random.randint(1, 100)
print("Enter an integer from 1 to 100.")
guess = int(input())

while n != guess:
    print()
    if guess < n:
        print("Your guess is too low.")
        print("Enter another integer from 1 to 100: ")
        guess = int(input())
    elif guess > n:
        print("Your guess is too high.")
        print("Enter another integer from 1 to 100: ")
        guess = int(input())
    elif guess == n:
        break
print("Your guess is correct. Congradulations! The correct number was ", n)
