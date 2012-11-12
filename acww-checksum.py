#!/usr/bin/python

# imports
import os, sys, zlib, socket, struct, re

# get file to be sent from argument
files = sys.argv[1]

filename = open(files).read()

count2 =0
count = 0

array = [filename[i:i+2] for i in range(0, os.path.getsize(files), 2)]

#print "Using little endian"

for i in range(0, len(array), 1):
    if len(array[i])!=0:
        string = array[i]
        count+= ord(string[0])+ord(string[1])*256
        count2+=1

if (count%65536!=0):
    print count, "\033[91m bad checksum\033[92m ", hex(65536-count%65536), "\033[0m"
else:
    print count, "\033[92m valid checksum\033[0m"