import random
from random import randint
print(" ")
print("Welcome to Aggie's Life Simulator")
print("All these events are randomly generated")
print(" ")

#Beginning
gender = (randint(1, 2))
surname = random.choice(open("Surnames.txt").readlines())

if gender == 1:
    male_name = random.choice(open("MaleNames.txt").readlines())        
    print("You are called " + male_name.strip() + " " + surname.strip())
else:
    female_name = random.choice(open("FemaleNames.txt").readlines())
    print("You are called " + female_name.strip() + " " + surname.strip())

Country = random.choice(open("Countries.txt").readlines())
print("You have been born in " + Country)

age = 0
input("Press Enter to age a year")
age +=1
print("You are now " + str(age))
passive_event = random.choice(open("Passive_Events.txt").readlines())
print (passive_event)
