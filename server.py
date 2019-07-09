#!/usr/bin/python3
# this is a flask runnable
from flask import Flask
from random import randrange
import os 
from json import loads
app = Flask(__name__)


dailyFh = open("daily.dat", "r")
allFh = open("all.dat", "r")

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
        #copyright {
            color: white;
            font-size: 2.3em;
            text-shadow: 2px 2px grey;    
            position: absolute;
            bottom: 0;
            right: 0;
        }
        </style>
        <title>%s</title>
    </head>
    <body>
    <p id="copyright">%s</p>
    </body>
</html>
"""

def getTemplateByFh(fh):
    fh.seek(0,os.SEEK_SET)
    imags = fh.readlines()
    count = len(imags)

    # get random number and print a random line 
    randIndex = randrange(0,count,1)
    img_info = loads(imags[randIndex])
    return template % (
        img_info['url'],
        img_info['copyright'],
        img_info['copyright']
    )

@app.route("/")
@app.route("/daily/")
def dailyImage():
    """
    this will read from Linux buffer-cache, so it will 
    automatically update by the write syscall from
    another python scripts
    """
    return getTemplateByFh(dailyFh)


@app.route("/all/")
def allImage():
    """
    this will read from Linux buffer-cache, so it will 
    automatically update by the write syscall from
    another python scripts
    """
    return getTemplateByFh(allFh)