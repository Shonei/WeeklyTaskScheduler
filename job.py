import datetime 
from pygame import mixer

def job():
	f = open('work.txt', 'a+')
	f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+"\n")
	f.close()
	mixer.init()
	mixer.music.load("bell-ringing-01.mp3")
	mixer.music.play()