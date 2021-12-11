#!/usr/bin/python3
"""
author: Steven Paredes
abc123: obr635
class: cs3723-003
assignment: assignment 7 part 2
date: 11/28/2020

"""
import sys
import os

# This puts the input in a format I am more comfortable with
input = sys.argv[1:]

# I tried the way you said to do it but I couldn't figure it out so I went with an idea that I could get working

#This checks if there are contiuous characters and returns the max 
def quadCheck(x):
    y = 0
    top = 0
    while( y < len(x) - 1): 
        # Counting contiuous occurrences of x[y] by testing it against x[y+1] if true then y++ and count++ 
        count = 1
        while x[y] == x[y + 1]: 
            y += 1
            count += 1
            if y + 1 == len(x): 
                break
        if count > top:
            top = count
        y += 1
    return count 

# This checks all of the double character possiblities
def checker2(x):
    if x == "CM":
        return 900
    if x == "DC":
        return 600
    if x == "CD":
        return 400
    if x == "XC":
        return 90
    if x == "LX":
        return 60
    if x == "XL":
        return 40
    if x == "IX":
        return 9
    if x == "VI":
        return 6
    if x == "IV":
        return 4
    else:
        return -1

# This checks all of the single character possiblities        
def checker(x):
    if x == "M":
        return 1000
    if x == "D":
        return 500
    if x == "C":
        return 100
    if x == "L":
        return 50
    if x == "X":
        return 10
    if x == "V":
        return 5
    if x == "I":
        return 1
    else:
        return -1

# This does the majority of the heavy lifting
def base10(x):
    before = x
    # If there are more than 3 contiuous characters then the syntax is wrong and an error is returned
    if quadCheck(x) > 3:
        return(before + " is -1")
    roman = 0
    # Run through the whole list and take each charater off piece meal and add its value to roman
    for y in x:
        if y.isdigit():
            return(before + " is -1")
    
            if checker2(x[0:2]) != -1:
                roman += checker2(x[0:2])
                x = x[2:]
            else:
                roman += checker(x[0])
                x = x[1:]
        else:
            roman += checker(x[0])
            x = x[1:]
    # error checking
    if roman <= 0 or roman > 3999:
        return(before + " is -1")
    return(before + " is " + str(roman))

def main():
    answer = []
    for x in range(len(input)):
        answer.append(base10(input[x].upper()))
    #For these last two lines I was confused if I was supposed to print the results or return them so I did both the be safe :)
    print(answer)
    return answer
    
main()