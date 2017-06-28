import csv
import functions as fns
import matplotlib.pyplot as plt

col1 = []
col2 = []
col3 = []
col4 = []

VG = []
IDS =[]
IG = []
VDS = []

xCoords_0V = []
xCoords_3V = []
xCoords_6V = []
xCoords_9V = []

yCoords_0V = []
yCoords_3V = []
yCoords_6V = []
yCoords_9V = []

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

with open('NMOS345_AsFab.csv', 'rb') as dataInCSV: 
	dataAsReader = csv.reader(dataInCSV)
	for row in dataAsReader:
		#print row
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

numberOfDevices = fns.countDeviceIDs(col1)

ix = 0
fns.getData(col1, col2, col3, col4, VG, IDS, IG, VDS, ranges)

while ix < numberOfDevices:
	fns.calculateResistance(VG, IDS, IG, VDS, ranges, counter, IDS[ranges[ix]], xCoords_0V, xCoords_3V, xCoords_6V, xCoords_9V, yCoords_0V, yCoords_3V, yCoords_6V, yCoords_9V, width)
	ix = ix + 1

fns.makeGraph(xCoords_0V,yCoords_0V,'ro', xCoords_3V, yCoords_3V, 'bo', xCoords_6V, yCoords_6V,'yo', xCoords_9V, yCoords_9V, 'go', contactResistance, sheetResistance, transferLength, contactResistivity)

fns.printTable(contactResistivity, sheetResistance, transferLength, contactResistivity)

fns.showGraph()