#!/usr/bin/python3

import requests

# https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=10
r = requests.get("https://cn.bing.com/HPImageArchive.aspx", params={
    "format":"js",
    "idx":0,
    "n":10
})
# this is the images array (array<dict>)
images = r.json()['images']

# this is the string of hash of images 
images = [img['hsh'] for img in images]

# i need to prepend the url 
images = ["http://www.bing.com/hpwp/"+img for img in images]

[print(img) for img in images]