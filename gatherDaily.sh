#!/bin/sh
# this can be add to cron as a daily job to autmaticcally update 
./getUrls.py > daily.dat
cat daily.dat  >> all.dat 
cat all.dat | sort | uniq > all.new
mv all.new all.dat