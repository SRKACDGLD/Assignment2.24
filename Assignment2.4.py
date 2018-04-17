# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 17:43:21 2018

@author: krishna.i

Assignment 2.4: Write a Python Program to print the given string in the format 
specified in the sample output.
WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a
SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all
its citizens
Sample Output:
WE, THE PEOPLE OF INDIA,
having solemnly resolved to constitute India into a 
SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC
and to secure to all its citizens:

"""

myText = "WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute \
India into a SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure \
to all its citizens"
myTextsplit = myText.split()
j=1
for word in myTextsplit:
    if word == "INDIA," or word == "a" or word == "REPUBLIC":
        print (word,sep=" ",end=" ")
        print(end='\n')
        i=0
        while i<j:
            print(sep='',end='\t')
            i = i+1
        j=j+1
    else:
        print (word,sep=" ",end=" ")


