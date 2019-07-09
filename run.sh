#!/bin/sh
source venv/bin/activate 

export FLASK_APP=server.py
export FLASK_ENV=development
flask run --with-threads --no-debugger -h 0.0.0.0