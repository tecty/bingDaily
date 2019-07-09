#!/usr/bin/python3
# randomly read one url from a file 

from random import randrange
from json import loads

f = open("daily.dat", "r")
imags = f.readlines()
count = len(imags)

# get random number and print a random line 
randIndex = randrange(0,count,1)

# use the json obj to become a dictionary 
img_info = loads(imags[randIndex])
print(img_info['url'])
print(img_info['copyright'])