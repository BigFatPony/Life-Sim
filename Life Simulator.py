import random
print(" ")
print("Welcome to Aggie's Life Simulator")
print("All these events are randomly generated")
print(" ")

Name = random.choice(open("FirstNames.txt").readlines())
Surname = random.choice(open("Surnames.txt").readlines())
print("You are called " + Name.strip() + " " + Surname.strip())
Country = random.choice(open("Countries.txt").readlines())
print("You have been born in " + Country)

