from tkinter import *
from tkinter import ttk
from time import sleep
from readFile import getTimeSchedule 
import csv
import multiprocessing
from job import job
from generateSchedule import addToSchedule
import schedule

timetable = getTimeSchedule()

def onClosing():
    global process
    process.terminate()
    process.join()
    root.destroy()

def runScheduler():
	addToSchedule(schedule, job, timetable)
	while True:
		sleep(1)
		schedule.run_pending()

def run():
	p = multiprocessing.Process(target=runScheduler)
	return p



def addRow(*args):
	global row

	m = [0 for x in range(0, column)]
	for i in range(0, column):
		m[i] = ttk.Entry(mainframe, width=10)
		m[i].insert(i, '')
		m[i].grid(column=i, row=row+1, sticky=(W, E))
		m[i].grid_configure(padx=5, pady=5)
	
	row = row + 1
	entry.append(m)
	button1.grid(column=0, row=row+1, sticky=W)
	button2.grid(column=1, row=row+1, sticky=W)
	button3.grid(column=2, row=row+1, sticky=W)

def readData(*args):
	global row
	global timetable
	global process

	process.terminate()
	process.join()

	con = False
	newSchedule = [[0 for x in range(0, column)] for y in range(0, row)] 
	
	for i in range(0, column):
		for j in range(0, row):
			newSchedule[j][i] = entry[j][i].get()
	
	with open("schedule.csv", "w") as f:
		writer = csv.writer(f)
		writer.writerows(newSchedule)

	timetable = getTimeSchedule()
	process = run()
	process.start()


if __name__ == '__main__':
	global root
	global mainframe
	global column
	global row
	global entry
	global process
	global button1
	global button2 
	global button3

	multiprocessing.freeze_support()

	root = Tk()
	root.title("Week schedule")

	mainframe = ttk.Frame(root, padding="3 3 12 12")
	mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
	mainframe.columnconfigure(0, weight=1)
	mainframe.rowconfigure(0, weight=1)

	column = len(timetable)
	row = len(timetable[0])
	entry = [[0 for x in range(0, column)] for y in range(0, row)] 

	process = multiprocessing.Process(target=runScheduler)

	button1 = ttk.Button(mainframe, text="Update table", command=readData)
	button2 = ttk.Button(mainframe, text="Add row", command=addRow)
	button3 = ttk.Button(mainframe, text="Ring bell", command=job)

	Label(mainframe, text='ponedelnik').grid(row=0, column=0)
	Label(mainframe, text='vtornik').grid(row=0, column=1)
	Label(mainframe, text='srqda').grid(row=0, column=2)
	Label(mainframe, text='chetvartak').grid(row=0, column=3)
	Label(mainframe, text='petak').grid(row=0, column=4)
	Label(mainframe, text='sabota').grid(row=0, column=5)

	for i in range(0, column):
		for j in range(0, row):
			string = str(timetable[i][j])
			if string == 'nan':
				string = ''
			entry[j][i] = ttk.Entry(mainframe, width=10)
			entry[j][i].insert(i, string)
			entry[j][i].grid(column=i, row=j+1, sticky=(W, E))
					
	button1.grid(column=0, row=row+1, sticky=W)
	button2.grid(column=1, row=row+1, sticky=W)
	button3.grid(column=2, row=row+1, sticky=W)

	for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

	root.bind('<Return>', readData)
	root.bind('<Return>', addRow) 
	root.protocol("WM_DELETE_WINDOW", onClosing)   
		
	process.start()
	root.mainloop()