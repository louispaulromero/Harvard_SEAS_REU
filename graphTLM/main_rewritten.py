import csv
import functions as fns

col1 = []
col2 = []
col3 = []
col4 = []

VG = []
IDS =[]
IG = []
VDS = []

xCoordinates = []
yCoordinates = []


ranges = []
counter = []
counter.append(0)
counter.append(1)

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
	fns.calculateResistance(VG, IDS, IG, VDS, yCoordinates, ranges, counter, IDS[ranges[ix]], xCoordinates)
	ix = ix + 1
print xCoordinates
print yCoordinates

fns.makeGraph(xCoordinates, yCoordinates)