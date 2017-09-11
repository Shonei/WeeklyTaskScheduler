import time
from readFile import getTimeSchedule

def monday(schedule, time, job):
	schedule.every().monday.at(time).do(job)

def tuesday(schedule, time, job):
	schedule.every().tuesday.at(time).do(job)

def wednesday(schedule, time, job):
	schedule.every().wednesday.at(time).do(job)

def thursday(schedule, time, job):
	schedule.every().thursday.at(time).do(job)

def friday(schedule, time, job):
	schedule.every().friday.at(time).do(job)

def saturday(schedule, time, job):
	schedule.every().saturday.at(time).do(job)

def addToSchedule(sched, job, timetable):
	times = [
		monday,
		tuesday,
		wednesday,
		thursday,
		friday,
		saturday]

	for i in range(0, len(timetable)):
		for j in range(0, len(timetable[i])):
			# skip nan values
			if timetable[i][j] == timetable[i][j]:
				times[i](sched, timetable[i][j], job)