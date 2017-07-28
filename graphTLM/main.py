import csv
import functions as fns
import matplotlib.pyplot as plt

voltages = []

col1 = []
col2 = []
col3 = []
col4 = []

VG = []
IDS =[]
IG = []
VDS = []

voltages = []

xCoords_V1 = []
xCoords_V2 = []
xCoords_V3 = []
xCoords_V4 = []

yCoords_V1 = []
yCoords_V2 = []
yCoords_V3 = []
yCoords_V4 = []

xCoordinates = []
yCoordinates = []

width = []

ranges = []
counter = []
counter.append(0)
counter.append(1)

contactResistance = []
sheetResistance = []
transferLength = []
contactResistivity = []

#Enables entering file name, so any CSV can be opened
#FILENAME = str(raw_input('Please enter file name: '))+'.csv'

#Separates each column in CSV into own list
#with open(FILENAME, 'rb') as dataInCSV:
with open('EDOPE3_NOEDOPE.csv', 'rb') as dataInCSV:
	dataAsReader = csv.reader(dataInCSV)
	for row in dataAsReader:
		if len(row) == 2:
			col1.append(row[0])
			col2.append(row[1])
			col3.append('')
			col4.append('')
		else:
			col1.append(row[0])
			col2.append(row[1])
			col3.append(row[2])
			col4.append(row[3])

#Function call to determine number of transistors for loop control
numberOfDevices = fns.countDeviceIDs(col1)

#Function call to 
fns.organizeData(col1, col2, col3, col4, VG, IDS, IG, VDS, ranges)

#Collect what voltages that will be used for the TLM method
'''loopController = True
while loopController:
	userInput = str(raw_input("Please a voltage: "))
	voltages.append(userInput)
	userInput = int(raw_input("Would you like to enter another voltage?\n[0=no|1=yes]"))
	if userInput == 0:
		loopController = False'''
	#ADD ERROR CHECKING


ix = 0
while ix < numberOfDevices:
	
	fns.calculateResistance(VG, IDS, IG, VDS, ranges, counter, IDS[ranges[ix]], xCoords_V1, xCoords_V2, xCoords_V3, xCoords_V4, yCoords_V1, yCoords_V2, yCoords_V3, yCoords_V4, width)
	ix = ix + 1

fns.makeGraph(xCoords_V1,yCoords_V1,'ro', xCoords_V2, yCoords_V2, 'bo', xCoords_V3, yCoords_V3,'yo', xCoords_V4, yCoords_V4, 'go', contactResistance, sheetResistance, transferLength, contactResistivity)

fns.printTable(contactResistance, sheetResistance, transferLength, contactResistivity)

fns.showGraph()