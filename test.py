#!/usr/bin/python3
# randomly read one url from a file 

from random import randrange

f = open("daily.dat", "r")
imags = f.readlines()
count = len(imags)

# get random number and print a random line 
randIndex = randrange(0,count,1)
print(imags[randIndex])