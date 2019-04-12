#!/usr/bin/python3
import sys, os, subprocess
from functools import reduce

#   Simple script to update toc in README.md
#   Example usage: ./updateToc.py README.md 3
#   This will overwrite your README.md file. 
#   Use at your caution!

#   *SUFFERS* Python version 3.4.3.......... Cannot upgrade it.
#   TODO #1: Improve usage with 
#   file = sys.argv[1]
#   as it is repetitive
#   TODO #2: automatically detect where to input toc 
#   (remove targetLineNum variable) 

def pipe(*fns):
    def sub(data):
        for fn in fns:
            data = fn(data)
        return data
    return sub
    
def raiseExceptionOnErrors():
    msg = "update.py takes 2 arguments: \n1. The name of a target file as the only argument. \n2. The line number to start pasting toc from (if you already have toc, you should input the number of the first line of the toc)\nFor example, ./updateToc.py README.md 3"
    if len(sys.argv) != 3:
        raise TypeError(msg)
    return 1
    
def getToc(file):
    toc = subprocess.Popen(['./gh-md-toc', file], 
               stdout=subprocess.PIPE, 
               stderr=subprocess.STDOUT)
    stdout,stderr = toc.communicate()
    if stderr:
        raise Exception(str(stderr, 'utf-8'))
    return str(stdout, 'utf-8')

def addToc(toc):
    file = sys.argv[1]
    old = open(file,'r')
    lines = old.readlines()
    targetLineNum = int(sys.argv[2])
    new = ''
    
    def isEndOfPrevTocReached(line):
        endOfPrevTocStr = 'Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc)'
        return endOfPrevTocStr in line
    
    reached = False
    
    for counter, line in enumerate(lines):
        # insert toc
        if targetLineNum == counter:
            new = new + toc
        elif counter < targetLineNum or reached:
            new = new + line
        elif isEndOfPrevTocReached(line):
            # do not copy the previous toc
            # just do nothing 
            reached = True
    return new 
    
def saveToFile(txt):
    file = sys.argv[1]
    with open(file, 'w') as filehandle:  
        filehandle.write(txt)
    return 1
    
if __name__ == "__main__":
    file = sys.argv[1]
    main = pipe(
        getToc,
        addToc,
        saveToFile
    )
    raiseExceptionOnErrors()
    main(file)