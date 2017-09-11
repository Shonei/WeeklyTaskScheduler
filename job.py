import datetime 
from pygame import mixer

def job(callback):
	f = open('work.txt', 'a+')
	f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+"\n")
	f.close()
	mixer.init()
	try:
		mixer.music.load("ringTone.mp3")
	except:
		callback("File missing", "The ringTone.mp3 file is missing from the root.")
	mixer.music.play()