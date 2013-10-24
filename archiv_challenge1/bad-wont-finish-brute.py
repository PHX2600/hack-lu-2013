#!/usr/bin/python

import subprocess
import os

def RotChar(inChar):
    outChar = chr(ord(inChar) + 1)
    if(outChar == ':'):
        return "A"
    if(outChar == '['):
        return "0"
    return outChar

def isCorrectGuess(guessString):
    p = subprocess.Popen(["./archiv -l FluxArchiv.arc " + ''.join(guessString)], stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    if "not correct" in output:
        return False
    return True

i = 0.0

queryString = list("100000")

while queryString != list("000000"):
    if(isCorrectGuess(queryString)):
        print "****************************"
        print queryString
        print "****************************"
        exit(0)

    keepGoing = True
    j = 0
    while keepGoing:
        newChar = RotChar(queryString[j]) 
        queryString[j] = newChar
        if(newChar != '0'):
            keepGoing = False
        if(j == 5):
            keepGoing = False
        j = j + 1    

    i = i + 1
    if((i % 100) == 0):
        print "i = " + str(i)
        print str((i / 2176782336.0) * 100) + "% complete"
        print ''.join(queryString)

