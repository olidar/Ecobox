#!/usr/bin/python
from __future__ import print_function
import Adafruit_DHT
import time
import os.path

s=int(input("Entrez le temps entre chaque acquisition en secondes. (Attention aux valeurs inferieures a 5!) : "))
t=int(input("Entrez le nombre de jours mis en tampon : "))
reponse = input("Voulez vous conserver les fichiers logs existants? O/n : ")
if reponse == 'N' or 'n' or 'Non' or 'non':
	for n in range (0,30):
		nomTxt= "/home/pi/Ecobox/Nichoir/Demo/source/python"+str(n)+".txt"
		try:
			os.remove(nomTxt)
		except:
			pass
	n=0

n=0
nomTxt= "/home/pi/Ecobox/Nichoir/Demo/source/python"+str(n)+".txt"

sensor = Adafruit_DHT.DHT22
pin = 23
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

compteur=time.time()
compteurjour=time.time()

while 1:
    if compteur+s<time.time():
        if humidity is not None and temperature is not None:
            try:
                with open(nomTxt,"r+") as f:
                    old = f.read()
                    f.seek(0)
                    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
                    f.write(old+str(time.asctime(time.localtime(time.time())))+" "+str('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))+"\n")
                    print(str(time.asctime(time.localtime(time.time())))+" "+str('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity)))					
            except IOError:
                open(nomTxt,"w")    
        else:
            print('Failed to get reading. Try again!')
        compteur=time.time()
    if compteurjour+ 86400 < time.time():
        n+=1
        if n == t:
            n=0
        nomTxt="/home/pi/Ecobox/Nichoir/Demo/source/python"+str(n)+".txt"
        print("Passage au ficher log",n," .")
        compteurjour=time.time()
        if os.path.isfile(nomTxt) == True:
            os.remove(nomTxt)
		
