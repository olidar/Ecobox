#!/usr/bin/python

nomFichier="home.html"
nomImage="foo.png"
nomVideo="videomp4.mp4"
nomSon="themea.wav"
pathFichier="/home/pi/Scripts/"
Header="<html><body>"
Footer="</html>"


with open(nomFichier,"r+") as f:
	f.write(Header)
	f.write("<img src="+pathFichier+nomImage+">")
	f.write("<br><a href="+pathFichier+nomVideo+">This is a video</a>")
	f.write("<br><a href="+pathFichier+nomSon+">This is a sound file</a>")
	f.write(Footer)
	
