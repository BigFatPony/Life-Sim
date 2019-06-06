import random
from random import randint
print(" ")
print("Welcome to Aggie's Life Simulator")
print("All these events are randomly generated")
print(" ")

#Beginning for the randomised version
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



#Code from Barker
day = random.randint(1,28)
month = random.randint(1,12)
year = random.randint(1960,2019)
dob = str(day) + "/" + str(month) + "/" + str(year)
print("Your date of birth is: " + dob)

#passive event system + age



age = 0
def life():
    global age
    print("You are now", +age ,"years old")  
    if age < 6:
        baby = random.choice(open("Baby_Passive.txt").readlines())
        print(baby)
        age += 1
        input("*Press Enter to age a year*")
        life()
    elif age > 5 and age < 12:
        child = random.choice(open("Child_Passive.txt").readlines())
        print(teen)
        age += 1
        input("*Press Enter to age a year*")
        life()
    elif age > 11 and age < 18:
        teen = random.choice(open("Teen_Passive.txt").readlines())
        print(teen)
        age += 1
        input("*Press Enter to age a year*")
        life()
    elif age > 17 and age < 50:
        middle = random.choice(open("Middle_Passive.txt").readlines())
        print(middle)
        age += 1
        input("*Press Enter to age a year*")
        life()
    elif age > 49 and age < 90:
        old = random.choice(open("Old_Passive.txt").readlines())
        print(old)
        age += 1
        input("*Press Enter to age a year*")
        life()
    else:
        print("You died at the age of ", + age)

life()
