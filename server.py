#!/usr/bin/python3
# this is a flask runnable
from flask import Flask
from random import randrange
import os 
app = Flask(__name__)


f = open("daily.dat", "r")

template = """
<!DOCTYPE html>
<html>
    <head>
        <style>
        body {
            background-size: 100%% 100%%;
            background-image: url("%s");
        }
        body,html {
            height: 100%%;
            width: 100%%;
        }
        </style>
        <title>A Bing Background Image</title>
    </head>
    <body>
    </body>
</html>
"""

@app.route("/")
@app.route("/daily/")
def hello():
    """
    this will read from Linux buffer-cache, so it will 
    automatically update by the write syscall from
    another python scripts
    """
    f.seek(0,os.SEEK_SET)
    imags = f.readlines()
    count = len(imags)

    # get random number and print a random line 
    randIndex = randrange(0,count,1)
    return template % (imags[randIndex].strip())
