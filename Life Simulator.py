import random
print("Welcome to Aggie's Life Simulator")
print("All these events are randomly generated")



random_lines = random.choice(open("FirstNames.txt").readlines())
print("You are called " + random_lines)

