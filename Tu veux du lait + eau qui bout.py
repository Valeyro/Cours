# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

#Write the pseudocode to check whether someone wants milk with their tea
#Adapt your pseudocode from Task 1 by writing the extra pseudocode to check if the water in the kettle is boiling

#definir la variable "veut lait"
#dire a l utilisateur s il veut du lait avec son thé

'''si oui, alors tea avec du lait 
si non, alors juste thé'''


lait = str(input("tu veux du lait ou quoi "))
veutlait=bool(False)
if lait == "oui":
    veutlait=True


if veutlait==True:
    print("je veux du lait dans mon thé")
else:
    print("Je ne veux pas de lait")

eau=str(input("est ce que l eau est en train de bouilir "))
eaubout=bool(False)
if eau=="oui":
    eaubout=True

if eaubout==True:
    print("l eau est en train de bouillir merci de patienter ")
else:
    print("attend que l'eau bout")