import matplotlib.pyplot as plt

def getData(reader, dID, list1, list2, list3, list4):
	#This loop grabs only the relevant header information and skips irrelevant data
		count = 0
		for row in reader:
			if count == 0:
				dID.append(row[1])
			if count == 2: 
				break
			count = count + 1
		#This loop creates lists of data
		for row in reader:
			if len(row) == 2 and row[0]=='Device ID':
				break
			else:
				list1.append(row[0])
				list2.append(row[1])
				list3.append(row[2])
				list4.append(row[3])

def calculateResistance(VG, IDS, IG, VDS, yCoords):
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
	for ix in range(len(VG)):
		if VG[ix] == '0':
			zeroCounter = zeroCounter + 1
			sumIDS_0V = sumIDS_0V + float(IDS[ix])
			sumVDS_0V = sumVDS_0V + float(VDS[ix])
		elif VG[ix] == '3': 
			threeCounter = threeCounter + 1
			sumIDS_3V = sumIDS_3V + float(IDS[ix])
			sumVDS_3V = sumVDS_3V + float(VDS[ix])
		elif VG[ix] == '6': 
			sixCounter =  sixCounter + 1
			sumIDS_6V = sumIDS_6V + float(IDS[ix])
			sumVDS_6V = sumVDS_6V + float(VDS[ix])
		elif VG[ix] == '9':
			nineCounter = nineCounter + 1
			sumIDS_9V = sumIDS_9V + float(IDS[ix])
			sumVDS_9V = sumVDS_9V + float(VDS[ix])
	resistance_0V = (sumVDS_0V/zeroCounter)/(sumIDS_0V/zeroCounter)
	resistance_3V = (sumVDS_3V/threeCounter)/(sumIDS_3V/threeCounter)
	resistance_6V = (sumVDS_6V/sixCounter)/(sumIDS_6V/sixCounter)
	resistance_9V = (sumVDS_9V/nineCounter)/(sumIDS_9V/nineCounter)
	#print resistance_0V
	#print resistance_3V
	#print resistance_6V
	#print resistance_9V
	yCoords.append(resistance_0V)
	yCoords.append(resistance_3V)
	yCoords.append(resistance_6V)
	yCoords.append(resistance_9V)
	

def getDeviceLength(devID, xCoords):
	deviceCol = int(devID[0][7])
	if deviceCol >= 1 and deviceCol <= 2: 
		length = 5
	elif deviceCol >= 3 and deviceCol <= 4: 
		length = 10
	elif deviceCol >= 5 and deviceCol <= 6: 
		length = 15
	elif deviceCol >= 7 and deviceCol <= 8: 
		length = 20

	length_0V = length
	length_3V = length
	length_6V = length
	length_9V = length
	xCoords.append(length_0V)
	xCoords.append(length_3V)
	xCoords.append(length_6V)
	xCoords.append(length_9V)

def makeGraph(xCoords, yCoords):
	print xCoords
	print yCoords
	plt.xlim([0,30])
	plt.xlabel('L, microm')
	plt.ylabel('R, ohms')
	plt.plot(xCoords,yCoords, 'ro')
	plt.show()