#!/bin/sh
# this can be add to cron as a daily job to autmaticcally update 
./getUrls.py > daily.dat
cat  all.dat daily.dat | sort | uniq > all.dat