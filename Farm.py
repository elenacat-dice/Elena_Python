print("How many chickens are in your farm?")
example = int(input())
ChickenLegs = example * 2
print("You have ",ChickenLegs, " Chicken Legs")

print()
print("How many horses are in your farm?")
example = int(input())
HorseLegs = example * 4
print("You have ", HorseLegs, " horse legs")

print()
print("How many cows are in your farm?")
example = int(input())
CowLegs = example * 4
print("You have ", CowLegs, " cow legs")


TotalLegs = ChickenLegs + HorseLegs + CowLegs
print("You have ", TotalLegs, "legs in your farm.")
