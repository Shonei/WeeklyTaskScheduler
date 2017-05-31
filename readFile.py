import pandas

def getTimeSchedule():
	colnames = ['Ponedelnik', 'Vtornik', 'Srqda', 'Chetvartak', 'Petak', 'Sabota']
	data = pandas.read_csv('schedule.csv', names=colnames)

	dateList = []
	dateList.append(data.Ponedelnik)
	dateList.append(data.Vtornik)
	dateList.append(data.Srqda)
	dateList.append(data.Chetvartak)
	dateList.append(data.Petak)
	dateList.append(data.Sabota)

	return dateList

# print(getTimeSchedule())