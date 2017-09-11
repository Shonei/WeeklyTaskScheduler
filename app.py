from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror
from time import sleep
from readFile import getTimeSchedule 
import csv
from multiprocessing import Process, freeze_support
from job import job
from generateSchedule import addToSchedule
import schedule
import shutil
from functools import partial

def runScheduler(timetable):
    addToSchedule(schedule, partial(job, showerror), timetable)
    while True:
        sleep(1)
        schedule.run_pending()

class UI:
    def __init__(self):
        # needed because windows doesn't implament fork()
        freeze_support()

        self.timetable = getTimeSchedule(showerror)
        self.root = Tk()
        self.mainframe = ttk.Frame(self.root, padding="3 3 12 12")
        self.column = len(self.timetable)
        self.row = len(self.timetable[0])
        self.entry = [[0 for x in range(0, self.column)] for y in range(0, self.row)] 
        self.process = Process(target=runScheduler,  args=(self.timetable,))
        self.button1 = ttk.Button(self.mainframe, text="Update table", command=self.updateTable)
        self.button2 = ttk.Button(self.mainframe, text="Add row", command=self.addRow)
        self.button3 = ttk.Button(self.mainframe, text="Ring bell", command=partial(job, showerror))
        self.button4 = ttk.Button(self.mainframe, text="Remove row", command=self.deleteRow)
        self.button5 = ttk.Button(self.mainframe, text="Browse", command=self.loadFile)

    def onClosing(self):
        self.root.destroy()
        self.process.terminate()
        self.process.join()

    def addRow(self):
        m = [0 for x in range(0, self.column)]
        for i in range(0, self.column):
            m[i] = ttk.Entry(self.mainframe, width=10)
            m[i].insert(i, '')
            m[i].grid(column=i, row=self.row+1, sticky=(W, E))
            m[i].grid_configure(padx=5, pady=5)
        
        self.row = self.row + 1
        self.entry.append(m)
        self.moveButtons()

    def updateTable(self):

        newSchedule = [[0 for x in range(0, self.column)] for y in range(0, self.row)] 
        
        for i in range(0, self.column):
            for j in range(0, self.row):
                if re.match( r'\A[0,1,2][0-9]:[0-5][0-9]\Z|^$', self.entry[j][i].get()):
                    newSchedule[j][i] = self.entry[j][i].get()
                else:
                    showerror("Wrong time format", "The format of " + self.entry[j][i].get() + " is unsupported.")
                    return

        try:
            with open("schedule.csv", "w") as f:
                writer = csv.writer(f)
                writer.writerows(newSchedule)
        except:
            showerror("File error", "Could not write to schedule.csv")

        self.process.terminate()
        self.process.join()
        self.timetable = getTimeSchedule(showerror)
        self.process = Process(target=runScheduler, args=(self.timetable,))
        self.process.start()

    def deleteRow(self):
        for i in range(0, self.column):
            self.entry[self.row-1][i].grid_forget()
        
        self.entry.remove(self.entry[self.row-1])
        self.row = self.row - 1

    def loadFile(self):
        fname = askopenfilename(filetypes=(("Mp3 Files", "*.mp3"),))
        if fname:
            try:
                shutil.copy(fname, "ringTone.mp3")
            except:
                showerror("File error", "Could not overwrite the old ringtone.")

    def setUpUI(self):
        self.root.title("Week schedule")

        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=1)

        Label(self.mainframe, text='ponedelnik').grid(row=0, column=0)
        Label(self.mainframe, text='vtornik').grid(row=0, column=1)
        Label(self.mainframe, text='srqda').grid(row=0, column=2)
        Label(self.mainframe, text='chetvartak').grid(row=0, column=3)
        Label(self.mainframe, text='petak').grid(row=0, column=4)
        Label(self.mainframe, text='sabota').grid(row=0, column=5)

        for i in range(0, self.column):
            for j in range(0, self.row):
                string = str(self.timetable[i][j])
                if string == 'nan':
                    string = ''
                self.entry[j][i] = ttk.Entry(self.mainframe, width=10)
                self.entry[j][i].insert(i, string)
                self.entry[j][i].grid(column=i, row=j+1, sticky=(W, E))
                        
        self.moveButtons()

        for child in self.mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

        self.root.bind('<Return>', self.updateTable)
        self.root.bind('<Return>', self.addRow) 
        self.root.protocol("WM_DELETE_WINDOW", self.onClosing)   
            
        # self.process = multiprocessing.Process(target=self.runScheduler)

    def moveButtons(self):
        self.button1.grid(column=0, row=self.row+1, sticky=W)
        self.button2.grid(column=1, row=self.row+1, sticky=W)
        self.button4.grid(column=2, row=self.row+1, sticky=W)
        self.button5.grid(column=4, row=self.row+1, sticky=W)
        self.button3.grid(column=5, row=self.row+1, sticky=W)

    def run(self):
        self.process.start()
        self.root.mainloop()


if __name__ == '__main__':
    ui = UI()
    ui.setUpUI()
    ui.run()