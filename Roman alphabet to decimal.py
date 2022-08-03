# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 15:13:14 2022

@author: basel
"""


tallies = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}



roman_number = input("write your roman number...")

sum = 0

for i in range(len(roman_number) - 1):
    left = roman_number[i]
    right = roman_number[i + 1]
    if tallies[left] < tallies[right]:
        sum -= tallies[left]
    else:
        sum += tallies[left]
sum += tallies[roman_number[-1]]

print(sum)