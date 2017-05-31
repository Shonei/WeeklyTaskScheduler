from tkinter import *
from tkinter import ttk
import thread
from time import sleep
from readFile import getTimeSchedule 

timetable = getTimeSchedule()
# timetable.next()
# print(timetable[0][3])


root = Tk()
root.title("Feet to Meters")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

column = len(timetable)
row = len(timetable[0])
entry = [[0 for x in range(0, column)] for y in range(0, row)] 

def addRow(*args):
	m = [0 for x in range(0, column)]
	for i in range(0, column):
		m[i] = ttk.Entry(mainframe, width=10)
		# entry[j][i].insert(i, str(timetable[i][j]))
		m[i].grid(column=i, row=j+2, sticky=(W, E))
	entry.append(m)

def readData(*args):
	for i in range(0, column):
		for j in range(0, row):
			print(entry[j][i].get())

Label(mainframe, text='ponedelnik').grid(row=0, column=0)
Label(mainframe, text='vtornik').grid(row=0, column=1)
Label(mainframe, text='srqda').grid(row=0, column=2)
Label(mainframe, text='chetvartak').grid(row=0, column=3)
Label(mainframe, text='petak').grid(row=0, column=4)
Label(mainframe, text='sabota').grid(row=0, column=5)

for i in range(0, column):
	for j in range(0, row):
		entry[j][i] = ttk.Entry(mainframe, width=10)
		entry[j][i].insert(i, str(timetable[i][j]))
		entry[j][i].grid(column=i, row=j+1, sticky=(W, E))
				
button1 = ttk.Button(mainframe, text="Update table", command=readData).grid(column=0, row=row+1, sticky=W)
button2 = ttk.Button(mainframe, text="Add row", command=addRow).grid(column=1, row=row+1, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

# feet_entry.focus()
root.bind('<Return>', readData)
root.bind('<Return>', addRow)    
root.mainloop()
    