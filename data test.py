import random
from random import randint


def limit_read():   
        string = "#Child"
        file = open('All_The_Data.txt','w')
        file.write(string)
        f = file()
        for line in f:
            if line.find(string) == -1:
                print(line)
            else:
                break

limit_read()    


