import functions as fns
import matplotlib.pyplot as plt

#Necessary lists
col1 = []
col2 = []
col3 = []
col4 = []
VG = []
IDS =[]
IG = []
VDS = []
deviceRanges = []
voltages = []
widths = []
#X-Coordinates
lengths = []
#Y-Coordinates
yCoordsV1 = []
yCoordsV2 = []
yCoordsV3 = []
yCoordsV4 = []
#Index Tracker
indexTracker = []
indexTracker.append(0)
indexTracker.append(1)
#Parameters to be calculated
contactResistance = []
sheetResistance = []
transferLength = []
contactResistivity = []

fns.getVoltages(voltages)
fns.getCSVData(col1,col2, col3, col4, VG, IDS, IG, VDS, deviceRanges)

print 'Device Ranges:',deviceRanges
#Function call to determine number of transistors for loop control and their width
fns.getDeviceWidhtsAndLengths(col2, widths, lengths)
numberOfDevices = len(widths)

ix = 0
while ix < numberOfDevices:
	currentWidth = widths[0]
	currentLength = lengths[0]
	fns.calculateResistance(voltages,deviceRanges, currentWidth, currentLength, VG, IDS, IG, VDS, yCoordsV1, yCoordsV2, yCoordsV3, yCoordsV4, indexTracker)
	ix = ix + 1

fns.makeGraph(lengths,yCoordsV1,'ro', lengths, yCoordsV2, 'bo', lengths, yCoordsV3,'yo', lengths, yCoordsV4, 'go', contactResistance, sheetResistance, transferLength, contactResistivity, widths, voltages)

fns.printTable(contactResistance, sheetResistance, transferLength, contactResistivity, voltages)