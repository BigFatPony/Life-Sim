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

#Calender
day = random.randint(1,28)
month = random.randint(1,12)
year = random.randint(1960,2019)
dob = str(day) + "/" + str(month) + "/" + str(year)
print("Your date of birth is: " + dob)

#actor crap
def actor():
    male_name = random.choice(open("MaleNames.txt").readlines())
    female_name = random.choice(open("FemaleNames.txt").readlines())
    action = random.choice(open("Actor_Actions.txt").readlines())
    surname = random.choice(open("Surnames.txt").readlines())
    choice = (randint(1,2))
    if choice == 1:
        print("The famous actor, " + male_name.strip() + " " + surname.strip() + ", " + action)   
    else:
        print("The famous actor, " + female_name.strip() + " " + surname.strip() + ", " + action)
actor()

#war + politics + actor calling
def event():
    choice = (randint(0,10))
    war = random.choice(open("War.txt").readlines())    
    if choice == 0:
        print( war.strip())
    elif choice == 5:
        politics = random.choice(open("Politics.txt").readlines())
        print(politics)
    elif choice == 10:
        actor()
    else:
     print(" ")   

#Sexuality
def sexuality():
    print("You began looking at people... and began wondering...gay... or straight")
    sexuality = input("What is your sexuality? ")
    if sexuality == "straight".upper:
        print("You have chosen to be straight")
    else:
        print("You came out as gay")

#Marriage

#Children

    
#Main thing happening
age = 0
def life():
    
    global age

    politics = random.choice(open("Politics.txt").readlines())
    print("You are", +age ,"years old")

    if age == 0:
        age += 1
        input("*Press Enter to age a year*")
        life()
    elif age < 6:
        baby = random.choice(open("Baby_Passive.txt").readlines())
        print(baby.strip()) 
        event()
        age += 1
        input("*Press Enter to age a year*")
        life()
    elif age > 5 and age < 12:
        child = random.choice(open("Child_Passive.txt").readlines())
        print(child.strip())
        event()
        age += 1
        input("*Press Enter to age a year*")
        life()
    elif age > 11 and age < 18:
        teen = random.choice(open("Teen_Passive.txt").readlines())
        print(teen.strip())
        event()
        sexuality()
        age += 1
        input("*Press Enter to age a year*")
        life()
    elif age > 17 and age < 35:
        middle = random.choice(open("Middle_Passive.txt").readlines())
        print(middle.strip())
        event()        
        age += 1
        input("*Press Enter to age a year*")
        life()    
    elif age > 34 and age < 90:
        old = random.choice(open("Old_Passive.txt").readlines())
        print(old.strip())
        event()         
        age += 1
        input("*Press Enter to age a year*")
        life()
    else:
        death = random.choice(open("Death.txt").readlines())
        print("You died at the age of", int(age), " because of",str(death))
        print("You will be missed")
life()
