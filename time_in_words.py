#!/bin/python3

import math
import os
import random
import re
import sys
from time import time

#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#

def timeInWords(h, m):
    # Write your code here
    mins = "minutes "
    
    units = ["o' clock", "one ", "two ", "three ", "four ", "five ", "six ", "seven ", "eight ", "nine ", "ten ", 
    "eleven ", "twelve ", "thirteen ", "fourteen ", "quarter ", "sixteen ", "seventeen ", "eighteen ", "nineteen ", "twenty "]
    to = "to"
    past = "past "
    half = "half "
    space = " "
    
    dif = m - 30
    if dif <= 0: connector = "past "
    else: 
        connector = "to "
        m = 60 - m
        if h == 12: h = 1
        else: h = h + 1
    time2words = ""
    if m == 30: time2words = half + connector + units[h]
    elif m == 15: time2words = units[m] + connector + units[h]
    elif m == 1: time2words = units[m] + mins[:-2] + space + connector + units[h]
    elif 1 < m <= 20: time2words = units[m] + mins + connector + units[h]
    elif 20 < m < 30: time2words = units[20] + units[m-20] + mins + connector + units[h]
    
    else: time2words = units[h] + units[m] # o' clock case

    return time2words.strip()

print(timeInWords(12, 45))
    

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     h = int(input().strip())

#     m = int(input().strip())

#     result = timeInWords(h, m)

#     fptr.write(result + '\n')

#     fptr.close()
