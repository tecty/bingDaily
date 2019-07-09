#!/usr/bin/python3

import requests
import json 

# https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=10
r = requests.get("https://cn.bing.com/HPImageArchive.aspx", params={
    "format":"js",
    "idx":0,
    "n":10
})
# this is the images array (array<dict>)
images = r.json()['images']
# print(images)
# store the parsed data 
new_images = []
for img in images:
    new_img = {
        "url":"http://www.bing.com/hpwp/"+ img['hsh'],
        "copyright": img['copyright']
    }
    new_images.append(new_img)


[print(json.dumps(img)) for img in new_images]