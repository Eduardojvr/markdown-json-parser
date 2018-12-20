# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 00:57:10 2018

@author: Maame Yaa Osei and Ariel Arman Woode
"""

import re
from specialTree import *

# Opening .txt file to read from
file = input("Paste directory of markdown file here: ")
readFile = open(file)

# Initialising variables
myDict = {}
rawLine = []
cleanLine = []
tree = Tree()


# Reading data from input file
for line in readFile:
    rawLine += line.replace('\t', "").replace(" ", "").split('\n')
cleanLine = [i for i in rawLine if i is not '']


# Making headings unique to use as keys in feeder dictionary `myDict`
currKey = None
count = 0
for line in cleanLine:
    if re.match('#+.+', line):
        currKey = line + "_" + str(count)
        myDict[currKey] = []
        count += 1
    else:
        myDict[currKey].append(line)


# Inserting key, value pairs of headings and lines into parser-tree.
for k, v in myDict.items():
    tree.insert((k, v))
tree.clean()
print(tree)
print("Kindly check directory and open the file 'myjson.json' for output")
