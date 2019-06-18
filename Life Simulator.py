import random
from random import randint
print(" ")
print("Welcome to Aggie's Life Simulator")
print("All these events are randomly generated")
print(" ")

#IDEA FOR RANDOM EVENTS
#PUT THE IF STATEMENTS INSIDE A FUNCTION
#AND TRY TO CALL RANDOM IF STATEMENTS AT RANDOM TIMES
#OR CRY
    
#Randomised actor names + events
def actor():
    with open("MaleNames.txt") as file:
        male_name = random.choice(file.readlines())
    with open("FemaleNames.txt") as filea:
        female_name = random.choice(filea.readlines())
    with open("Actor_Actions.txt") as fileb:
        action = random.choice(fileb.readlines())
    with open("Surnames.txt") as filec:
        surname = random.choice(filec.readlines())        
    choice = (randint(1,2))
    if choice == 1:
        print("The famous actor, " + male_name.strip() + " " + surname.strip() + ", " + action)   
    else:
        print("The famous actor, " + female_name.strip() + " " + surname.strip() + ", " + action)

#war + politics + actor calling
def event():
    choice = (randint(0,10))
    with open("War.txt") as filed:
        war = random.choice(filed.readlines())  
    if choice == 0:
        print(war.strip())
        print(" ")
    elif choice == 5:
        with open("Politics.txt") as filee:
            politics = random.choice(filee.readlines())
            print(politics)
            print(" ")
    elif choice == 10:
        actor()
    else:
     print(" ")   
 
#Marriage + kid events
def marriage():
    choice = (randint(0,5))
    with open("Marriage_Events.txt") as filef:
        relationship = random.choice(filef.readlines())    
    if choice == 0:
        print(relationship.strip())
    elif choice == 5:
       with open("Parent_Events.txt") as fileg:
            kids = random.choice(fileg.readlines())
            print(kids)
    else:
        print(" ")
        
#This selects a random number for death
global ageno
ageno = (randint(70,90))


#Randomised life
def randomlife():
    
    gender = (randint(1, 2))
    with open("Surnames.txt") as fileh:
            surname = random.choice(fileh.readlines())

    if gender == 1:
            with open("MaleNames.txt") as filei:
                male_name = random.choice(filei.readlines())       
            print("You are called " + male_name.strip() + " " + surname.strip())    
    else:
            with open("FemaleNames.txt") as filej:
                female_name = random.choice(filej.readlines())
            print("You are called " + female_name.strip() + " " + surname.strip())
    country = random.choice(open("Countries.txt").readlines())
    print("You have been born in " + country)   #Didn't work properly with closing the textfile 
    print(" ")
    
    age = 0
    day = random.randint(1,28)
    month = random.randint(1,12)
    year = random.randint(1960,2019)
    dob = str(day) + "/" + str(month) + "/" + str(year)
    print("Your date of birth is: " + dob)
    
    while age < ageno:
        print("Age: " + str(age) + " years old")
       
        if age == 0:
            input("*Press Enter to age a year*")
            age += 1
        
        elif age < 4:
            print("The year is " + str(year))
            with open("Baby_Passive.txt") as filel:
                        baby = random.choice(filel.readlines())
            print(baby.strip()) 
            event()
            age += 1
            year += 1
            input("*Press Enter to age a year*")

        
        elif age >= 4 and age < 12:
            print("The year is " + str(year))
            with open("Child_Passive.txt") as filem:
                        child = random.choice(filem.readlines())
            print(child.strip())
            event()
            age += 1
            year += 1
            input("*Press Enter to age a year*")

        
        elif age >= 12 and age < 14:
            print("The year is " + str(year))
            with open("Teen_Passive.txt") as filen:
                    teen = random.choice(filen.readlines())
            print(teen.strip())
            event()
            age += 1
            year += 1
            input("*Press Enter to age a year*")

#Sexuality
        elif age == 14:
                print("The year is " + str(year))
                sexuality = input("What sexuality do you want to be: \n"
                              "1. Straight \n"
                              "2. Gay \n")
                while sexuality != "1" and sexuality != "2":
                    sexuality = input("What sexuality do you want to be: \n"
                                  "1. Straight \n"
                                  "2. Gay \n")
                if sexuality == "1":
                    print("You have decided to be Straight.")
                    age += 1
                else:
                    print("You have come out as Gay.")
                input("*Press Enter to Age a year*")
                age += 1

                                             
        elif age >= 15 and age < 20:
            print("The year is " + str(year))
            with open("Middle_Passive.txt") as fileo:
                    middle = random.choice(fileo.readlines())
            print(middle.strip())
            event()        
            age += 1
            year += 1
            input("*Press Enter to age a year*")

#partner picking
        elif age == 20:
                print("The year is " + str(year))
                if gender == 1:
                    if sexuality == 2:
                        global partner
                        partner = random.choice(open("MaleNames.txt").readlines())
                        print("You started to date: " + partner)
                    else:
                        partner = random.choice(open("FemaleNames.txt").readlines())
                        print("You started to date: " + partner)
                else:
                    if sexuality == 2:
                        partner = random.choice(open("MaleNames.txt").readlines())
                        print("You started to date: " + partner)
                    else:
                        partner = random.choice(open("FemaleNames.txt").readlines())
                        print("You started to date: " + partner)
                input("*Press Enter to age a year*")
                age += 1
    
        elif age >= 21 and age < 25:
            print("The year is " + str(year))
            with open("Middle_Passive.txt") as fileo:
                    middle = random.choice(fileo.readlines())
            print(middle.strip())
            event()
            marriage()
            age += 1
            year += 1
            input("*Press Enter to age a year*")
            
        elif age == 25:
            print("The year is " + str(year))
            print("You have married " + partner)
            age += 1
            year += 1

        elif age >= 26 and age < 30:
            print("The year is " + str(year))
            with open("Middle_Passive.txt") as fileo:
                    middle = random.choice(fileo.readlines())
            print(middle.strip())
            event()        
            age += 1
            year += 1
            input("*Press Enter to age a year*")

#Child naming
        elif age == 30:
            print("The year is " + str(year))
            bgender = (randint(1, 2))
            if bgender == 1:
                    print("You have a daughter!")
                    child = input("What would you like to name her:")
                    print("You have a daughter named " + child)
            else:
                    print("You have a son!")
                    child = input("What would you like to name him:")
                    print("You have a son named " + child)
            age += 1
            year += 1
        
        elif age >= 30 and age < 80:
            print("The year is " + str(year))
            with open("Old_Passive.txt") as filer:
                    old = random.choice(filer.readlines())
            print(old.strip())
            event()         
            age += 1
            year += 1
            input("*Press Enter to age a year*")
            
#Partner death    
        elif age == 80:
            print("The year is " + str(year))
            with open("Death.txt") as files:
                    death = random.choice(files.readlines())
            print ("Your partner," + partner.strip() + " ,has died from" + death)
            age += 1
            year += 1
            
        elif age >= 80 and age < 90:
            print("The year is " + str(year))
            with open("Old_Passive.txt") as filer:
                    old = random.choice(filer.readlines())
            print(old.strip())
            event()         
            age += 1
            year += 1
            input("*Press Enter to age a year*")
            
    else:
        death = random.choice(open("Death.txt").readlines())
    print("You died at the age of", int(age), " because of",str(death))
    print("You will be missed")


def picking():
    global genderc
    
    genderc = input("What gender would you like to be(M/F)? ").upper()
    while genderc != "M" and gender != "F":
            genderc = input("What gender would you like to be(M/F)? ").upper()
            if genderc == "M":
                    gendernum = 1
            else:
                    gendernum = 2
    name = input("What would you like to be named: ")

    surname = input("What would you like your surname to be: ")
    yeara = input("Please specify a year: ")
    country = input("Please enter a country: ")
    print("You are called " + name + " " + surname + " in the year " + yeara + " in the country " + country)
    
#Custom version
def customlife():
    age = 0
    while age < ageno:
        print("Age: " + str(age) + " years old")
       
        if age == 0:
            input("*Press Enter to age a year*")
            age += 1
        
        elif age < 4:
            with open("Baby_Passive.txt") as filel:
                        baby = random.choice(filel.readlines())
            print(baby.strip()) 
            event()
            age += 1
            input("*Press Enter to age a year*")

        
        elif age >= 4 and age < 12:
            with open("Child_Passive.txt") as filem:
                        child = random.choice(filem.readlines())
            print(child.strip())
            event()
            age += 1
            input("*Press Enter to age a year*")

        
        elif age >= 12 and age < 14:
            with open("Teen_Passive.txt") as filen:
                    teen = random.choice(filen.readlines())
            print(teen.strip())
            event()
            age += 1
            input("*Press Enter to age a year*")

#Sexuality
        elif age == 14:
                sexuality = input("What sexuality do you want to be: \n"
                              "1. Straight \n"
                              "2. Gay \n")
                while sexuality != "1" and sexuality != "2":
                    sexuality = input("What sexuality do you want to be: \n"
                                  "1. Straight \n"
                                  "2. Gay \n")
                if sexuality == "1":
                    print("You have decided to be Straight.")
                    age += 1
                else:
                    print("You have come out as Gay.")
                input("*Press Enter to Age a year*")
                age += 1

                                             
        elif age >= 15 and age < 20:
            with open("Middle_Passive.txt") as fileo:
                    middle = random.choice(fileo.readlines())
            print(middle.strip())
            event()        
            age += 1
            input("*Press Enter to age a year*")

#partner picking
        elif age == 20:
                if genderc == 1:
                    if sexuality == 2:
                        global partner
                        partner = random.choice(open("MaleNames.txt").readlines())
                        print("You started to date: " + partner)
                    else:
                        partner = random.choice(open("FemaleNames.txt").readlines())
                        print("You started to date: " + partner)
                else:
                    if sexuality == 2:
                        partner = random.choice(open("MaleNames.txt").readlines())
                        print("You started to date: " + partner)
                    else:
                        partner = random.choice(open("FemaleNames.txt").readlines())
                        print("You started to date: " + partner)
                input("*Press Enter to age a year*")
                age += 1
    
        elif age >= 21 and age < 25:
            with open("Middle_Passive.txt") as fileo:
                    middle = random.choice(fileo.readlines())
            print(middle.strip())
            event()
            marriage()
            age += 1
            input("*Press Enter to age a year*")
            
        elif age == 25:
            print("You have married " + partner)
            age += 1

        elif age >= 26 and age < 30:
            with open("Middle_Passive.txt") as fileo:
                    middle = random.choice(fileo.readlines())
            print(middle.strip())
            event()        
            age += 1
            input("*Press Enter to age a year*")

#Child naming
        elif age == 30:
            bgender = (randint(1, 2))
            if bgender == 1:
                    print("You have a daughter!")
                    child = input("What would you like to name her:")
                    print("You have a daughter named " + child)
            else:
                    print("You have a son!")
                    child = input("What would you like to name him:")
                    print("You have a son named " + child)
            age += 1
        
        elif age >= 30 and age < 80:
            with open("Old_Passive.txt") as filer:
                    old = random.choice(filer.readlines())
            print(old.strip())
            event()         
            age += 1
            input("*Press Enter to age a year*")
            
#Partner death    
        elif age == 80:
            with open("Death.txt") as files:
                    death = random.choice(files.readlines())
            print ("Your partner," + partner.strip() + " ,has died from" + death)
            age += 1
            
        elif age >= 80 and age < 90:
            with open("Old_Passive.txt") as filer:
                    old = random.choice(filer.readlines())
            print(old.strip())
            event()         
            age += 1
            input("*Press Enter to age a year*")
            
    else:
        death = random.choice(open("Death.txt").readlines())
    print("You died at the age of", int(age), " because of",str(death))
    print("You will be missed")


choicez = input("Would you like a custom or randomised game? \n"
                              "1. Custom \n"
                              "2. Random \n")
while choicez != "1" and choicez != "2":
    choicez = input("Would you like a custom or randomised game? \n"
                              "1. Custom \n"
                              "2. Random \n")
if choicez == "1": #custom
    picking()
    customlife()

else:
    randomlife()









