#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Import the necessary packages
import os
import re
import shutil

# Getting the list of people
personList = [f for f in os.listdir('.') if re.match(r'e.*\D\.jpg', f)]
personNames = [f.split("_") for f in personList]

# Getting the list of all jpg images
files = [f for f in os.listdir('.') if re.match(r'e.*\.jpg', f)]

# Getting existing subdirectories
# they start with ./01/
existing_dirs = next(os.walk('.'))[1]
N = len(existing_dirs)

# Iterate over all images to sort them per person
# and create a new folder if it does not already exist
for r in personNames:
    N+=1
    for f in files:
        if r[1] in f:
            NewDir = "{:2d}-{}/".format(N,r[1].replace (" ", "_"))
            if not os.path.exists(NewDir): 
                os.mkdir(NewDir, 0o777)
            try:
                shutil.move(f, NewDir+f)
            except:
                print("The file does not exist.")
