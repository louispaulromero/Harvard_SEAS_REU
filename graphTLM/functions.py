import matplotlib.pyplot as plt

def countDeviceIDs(col):
	count = 0
	for ix in range(len(col)):
		if(str(col[ix]) == 'Device ID'):
			count = count + 1
	return count

def getData(c1,c2,c3,c4,VG, IDS, IG, VDS, ranges):
	ix = 0
	while(ix < len(c1)):
		VG.append(c1[ix])
		IDS.append(c2[ix])
		IG.append(c3[ix])
		VDS.append(c4[ix])
		if str(VG[ix]) == 'Device ID':
			#print 'Device ID found', ix
			ranges.append(ix)
		ix = ix + 1
	ranges.append(len(VG))
	

def calculateResistance(VG, IDS, IG, VDS, yCoords, ranges, rangeIndex, devID, xCoords):
	print 'ranges',ranges
	print 'rangeIndex', rangeIndex
	
	xCounter = 0
	zeroCounter = 0
	threeCounter = 0
	sixCounter = 0
	nineCounter = 0
	sumIDS_0V = 0
	sumVDS_0V = 0
	sumIDS_3V = 0
	sumVDS_3V = 0
	sumIDS_6V = 0
	sumVDS_6V = 0
	sumIDS_9V = 0
	sumVDS_9V = 0

	start = ranges[rangeIndex[0]]
	finish = ranges[rangeIndex[1]]

	print 'start', start
	print 'finish',finish
	print 'the start', VG[start]
	print IDS[start]
	print 'the finish', VG[finish-1]
	while start < finish:
		if VG[start] == '0':
			zeroCounter = zeroCounter + 1
			sumIDS_0V = sumIDS_0V + float(IDS[start])
			sumVDS_0V = sumVDS_0V + float(VDS[start])
		elif VG[start] == '3': 
			print 'at 3', IDS[start]
			print 'at 3', VDS[start]
			threeCounter = threeCounter + 1
			sumIDS_3V = sumIDS_3V + float(IDS[start])
			sumVDS_3V = sumVDS_3V + float(VDS[start])
		elif VG[start] == '6': 
			sixCounter =  sixCounter + 1
			sumIDS_6V = sumIDS_6V + float(IDS[start])
			sumVDS_6V = sumVDS_6V + float(VDS[start])
		elif VG[start] == '9':
			nineCounter = nineCounter + 1
			sumIDS_9V = sumIDS_9V + float(IDS[start])
			sumVDS_9V = sumVDS_9V + float(VDS[start])
		start = start + 1

	if zeroCounter != 0:
		VDS_AVG_0V = (sumVDS_0V/zeroCounter)
		IDS_AVG_0V = (sumIDS_0V/zeroCounter)
		resistance_0V = VDS_AVG_0V/IDS_AVG_0V
		yCoords.append(resistance_0V)
		xCounter = xCounter + 1
	
	if threeCounter != 0:
		VDS_AVG_3V = (sumVDS_3V/zeroCounter)
		IDS_AVG_3V = (sumIDS_3V/zeroCounter)
		resistance_3V = VDS_AVG_3V/IDS_AVG_3V
		yCoords.append(resistance_3V)
		xCounter = xCounter + 1
	
	if sixCounter != 0:
		VDS_AVG_6V = (sumVDS_6V/zeroCounter)
		IDS_AVG_6V = (sumIDS_6V/zeroCounter)
		resistance_6V = VDS_AVG_6V/IDS_AVG_6V
		yCoords.append(resistance_6V)
		xCounter = xCounter + 1
	
	if nineCounter != 0:
		VDS_AVG_9V = (sumVDS_9V/zeroCounter)
		IDS_AVG_9V = (sumIDS_9V/zeroCounter)
		resistance_9V = VDS_AVG_9V/IDS_AVG_9V
		yCoords.append(resistance_9V)
		xCounter = xCounter + 1
	
	rangeIndex[0] = rangeIndex[0] + 1
	rangeIndex[1] = rangeIndex[1] + 1
	getDeviceLength(devID, xCoords, xCounter)

def getDeviceLength(devID, xCoords, num):
	deviceCol = int(devID[7])
	if deviceCol >= 1 and deviceCol <= 2: 
		length = 5
	elif deviceCol >= 3 and deviceCol <= 4: 
		length = 10
	elif deviceCol >= 5 and deviceCol <= 6: 
		length = 15
	elif deviceCol >= 7 and deviceCol <= 8: 
		length = 20

	if num == 1:
		xCoords.append(length)
	elif num == 2:
		xCoords.append(length)
		xCoords.append(length)
	elif num == 3:
		xCoords.append(length)
		xCoords.append(length)
		xCoords.append(length)
	elif num == 4:
		xCoords.append(length)
		xCoords.append(length)
		xCoords.append(length)
		xCoords.append(length)

def makeGraph(xCoords, yCoords):
	plt.xlim([0,25])
	plt.xlabel('L, microm')
	plt.ylim([0,4500000])
	plt.ylabel('R, ohms')
	plt.plot(xCoords,yCoords, 'ro')
	plt.show()