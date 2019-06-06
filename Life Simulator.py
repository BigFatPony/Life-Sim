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
male_name = random.choice(open("MaleNames.txt").readlines())
female_name = random.choice(open("FemaleNames.txt").readlines())
male_name1 = random.choice(open("MaleNames.txt").readlines())
female_name1 = random.choice(open("FemaleNames.txt").readlines())

def actor():
    choice = (randint(1,4))

    if choice == 1:
        print("The famous , " + male_name.strip() + " " + ", has died")
    if choice == 2:
        print("The famous, " + female_name.strip() + " " +  ", has been imprisoned")
    if choice == 3:
        print("The famous , " + female_name1.strip() + " " +  ", has died")    
    else:
        print("The famous , " + male_name1.strip() + " " +  ", has been imprisoned")

actor()

    
#Main thing happening
age = 0
def life():
    
    global age
    politics = random.choice(open("Politics.txt").readlines())
    print("You are now", +age ,"years old")
    
    if age < 6:
        baby = random.choice(open("Baby_Passive.txt").readlines())
        print(baby.strip())
        print(politics)
        age += 1
        input("*Press Enter to age a year*")
        life()
    elif age > 5 and age < 12:
        child = random.choice(open("Child_Passive.txt").readlines())
        print(child.strip())
        actor()
        age += 1
        input("*Press Enter to age a year*")
        life()
    elif age > 11 and age < 18:
        teen = random.choice(open("Teen_Passive.txt").readlines())
        print(teen.strip())
        print(politics)        
        age += 1
        input("*Press Enter to age a year*")
        life()
    elif age > 17 and age < 35:
        middle = random.choice(open("Middle_Passive.txt").readlines())
        print(middle.strip())
        print(politics)        
        age += 1
        input("*Press Enter to age a year*")
        life()    
    elif age > 34 and age < 90:
        old = random.choice(open("Old_Passive.txt").readlines())
        print(old.strip())
        print(politics)         
        age += 1
        input("*Press Enter to age a year*")
        life()
    else:
        print("You died at the age of ", + age)

life()
