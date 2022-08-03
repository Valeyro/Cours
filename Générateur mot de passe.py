# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 14:09:45 2022

@author: basel
"""


import random

pw_lengt = int(input("what should the length of the password be?..."))
wanted_list=str(input("do you want a normal list? "))


list_clavier = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
list_clavier_speciaux = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"\\\{\}[]µ€'

if wanted_list == 'yes':
    pw = "".join(random.sample(list_clavier, pw_lengt))

else:
    pw = "".join(random.sample(list_clavier_speciaux, pw_lengt))

print(pw)