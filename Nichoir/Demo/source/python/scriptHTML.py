#!/usr/bin/python

import os

nomFichier="/home/pi/Ecobox/Nichoir/Demo/data/index.html"
nomImage="foo.png"
pathVideo="foo.mp4"
#pathVideo="/home/pi/Ecobox/Nichoir/Demo/data/HiBW/foo.mp4"
nomSon="themea.wav"
pathFichier="/home/pi/Ecobox/Nichoir/Demo/data/HiBW/"
Header="<html><body>"
Footer="</html>"

try:
	os.remove(nomFichier)
except:
	pass
try:
	with open(nomFichier,"r+") as f:
		f.write(Header)
		f.write("<img src=foo.png>")
#		f.write("<img src="+pathFichier+nomImage+">")
		f.write("<br><a href="+pathVideo+">This is a video</a>")
		f.write(Footer)
except IOError:
	with open(nomFichier,"w") as f:
		f.write(Header)
		f.write("<img src=foo.png>")
#		f.write("<img src="+pathFichier+nomImage+">")
		f.write("<br><a href="+pathVideo+">This is a video</a>")
		f.write(Footer)
	
