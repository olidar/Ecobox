#!/usr/bin/python

import matplotlib.pyplot as plt
import datetime
from dateutil.parser import parse


n=input("Entrez le numero du fichier log que vous voulez grapher : ")
i=1

h=1
k=1

nomTxt="logs"+str(n)+".txt"
temperature =[]
temps= []
with open(nomTxt,"r") as file:
    while file.readlines(i) != []:
        i+=1
    
    file = open(nomTxt,"r")
    while h !=i:
        line=''.join(file.readlines(h))
        temp=line[30:34]
        temperature.append(float(temp))
        h+=1
        
        
    file = open(nomTxt,"r")
    while k != i:
        line=''.join(file.readlines(k))
        time=line[0:24]
        time=parse(time)
        temps.append(time)
        k+=1


plt.plot(temps,temperature)
plt.savefig('/home/pi/Ecobox/Nichoir/Demo/data/HiBW/foo.png',format="png")
plt.show()


