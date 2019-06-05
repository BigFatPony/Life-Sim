import random
print("Welcome to Aggie's Life Simulator")
print("All these events are randomly generated")


namelist=['John','Richard','Kevin'] #Add more names (maybe make a seperate list for male and female and randomly pick between that)
surnamelist=[['filler']] #Work on surnames after
#add year but make it pick a random number I guess

namechoice = random.choice(namelist)
print("Your name is",namechoice) #Later add surnames to name
snamechoice = random.choice(surnamelist)

#Large sh*thole filled with random events
randomevents=['You read a book','You saw a cute dog','You saw a clown in the park']


event = random.choice(randomevents)
print(event)





