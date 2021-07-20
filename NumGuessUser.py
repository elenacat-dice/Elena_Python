print("Think of a number between 1 and 100.")
print()
print("Is your number 50?")
print("If your number is greater type high. If your number is lower type low. If this is your number type correct.")
UserAnswer = int(input())
YourAnswer = int(50 / 2)
h = "high"
l = "low"
c = "correct"

while UserAnswer != c:
    if UserAnswer == h:
        YourAnswer = YourAnswer / 2
        print("Is you number: ", YourAnswer, "? If your number is greater type high. If your number is lower type low. If this is your number type correct.")

    elif UserAnswer == l:
        YourAnswer = YourAnswer / 2 + YourAnswer
        print("Is you number: ", YourAnswer, "? If your number is greater type high. If your number is lower type low. If this is your number type correct.")
    else:
        break

print("I guessed your number!!!")
