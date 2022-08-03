# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 22:54:51 2022

@author: basel
"""


#On va d'abord demander à python de choisir un nombre entre 1 et 100

import random 

random_number = random.randint(0,100)

print(random_number)

#Let's create the code to determine this random value

a= 0

while a != random_number:
    a=int(input("Enter the guessed value: "))
        
    if a>100 or a<0:
            print("the random value is only between 0 and 100, please put a value in this interval")
            
    elif random_number - 2 < a < random_number+2:
        if a<random_number:
                print("the random number is higher than the value you entered but you are close")
        elif a>random_number:
               print("the random number is lower than the value you entered but you are close")
    
    elif a<random_number:
                print("the random number is higher than the value you entered")
        
    elif a>random_number:
               print("the random number is lower than the value you entered")

    else:
        print("Well done you found the exact value!")





        

        
        

        
