#!/usr/bin/python3
"""
author: Steven Paredes
abc123: obr635
class: cs3723-003
assignment: assignment 7 part 1
date: 11/25/2020

"""
import sys
import os

# These two lines take the input and turn it into an array of ints. They are global vars cause I am a tad bit lazy.
input = sys.argv[1:]
intInput = [int(x) for x in input]

# I know you said to use a dict in the hints but I was born into the jank so I revel in it!
# Also thanks for the hint to go from largest to smallest I was having some issues going smallest to largest.
val = [3000, 2000, 1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
rnum = ["MMM", "MM", "M", "CM", "DCCC", "DCC", "DC", "D", "CD", "CCC", "CC", "C", "XC", "LXXX", "LXX", "LX", "L", "XL", "XXX", "XX", "X", "IX", "VIII", "VII", "VI", "V", "IV", "III", "II", "I"]

# While I could've made this as one big ugly block I thought it looked neater separated like this.
# This does most of the work, value testing, and data processing.
def romanNum(x):
    before = x
    number = ''
    if x <= 0 or x > 3999:
        return(str(x) + " is Error")
    elif isinstance(x, int) != True:
        return(str(x) + " is Error")
        
    while x > 0:
        for y in range(len(val)):
            if x // val[y] > 0:
                x -= val[y]
                number += rnum[y]
    return(str(before) + " is " + number)

# This cuts up the input into managable pieces and slowly feeds it to romanNum(), it also returns and prints the data in the correct format.
def main():
    answer = []
    for x in range(len(intInput)):
        answer.append(romanNum(intInput[x]))
    #For these last two lines I was confused if I was supposed to print the results or return them so I did both the be safe :)
    print(answer)
    return answer

#This bad boi tells the program to start    
main()
    
