import pandas

def getTimeSchedule(callback):
	colnames = ['Ponedelnik', 'Vtornik', 'Srqda', 'Chetvartak', 'Petak', 'Sabota']
	try:
		data = pandas.read_csv('schedule.csv', names=colnames)
	except:
		callback("File missing", "The schedulle.csv is missing from the root directory.")

	dateList = []
	dateList.append(data.Ponedelnik)
	dateList.append(data.Vtornik)
	dateList.append(data.Srqda)
	dateList.append(data.Chetvartak)
	dateList.append(data.Petak)
	dateList.append(data.Sabota)

	# print(dateList)

	return dateList

# getTimeSchedule()