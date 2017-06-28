#https://www.youtube.com/watch?v=p4ezH9HUPOY
#Video used for linear regression
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 

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

def calculateResistance(VG, IDS, IG, VDS, ranges, rangeIndex, devID, xC_0V, xC_3V, xC_6V, xC_9V, yC_0V, yC_3V, yC_6V, yC_9V,w):
	#print 'ranges',ranges
	#print 'rangeIndex', rangeIndex
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
	#print 'start', start
	#print 'finish',finish
	#print 'the start', VG[start]
	#print IDS[start]
	#print 'the finish', VG[finish-1]
	while start < finish:
		if VG[start] == '0':
			zeroCounter = zeroCounter + 1
			sumIDS_0V = sumIDS_0V + float(IDS[start])
			sumVDS_0V = sumVDS_0V + float(VDS[start])
		elif VG[start] == '3': 
			#print 'at 3', IDS[start]
			#print 'at 3', VDS[start]
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
		yC_0V.append(round(resistance_0V,2))
		getDeviceLength(devID, xC_0V,w)
	
	if threeCounter != 0:
		VDS_AVG_3V = (sumVDS_3V/zeroCounter)
		IDS_AVG_3V = (sumIDS_3V/zeroCounter)
		resistance_3V = VDS_AVG_3V/IDS_AVG_3V
		yC_3V.append(round(resistance_3V, 2))
		getDeviceLength(devID, xC_3V,w)
	
	if sixCounter != 0:
		VDS_AVG_6V = (sumVDS_6V/zeroCounter)
		IDS_AVG_6V = (sumIDS_6V/zeroCounter)
		resistance_6V = VDS_AVG_6V/IDS_AVG_6V
		yC_6V.append(round(resistance_6V,2))
		getDeviceLength(devID, xC_6V,w)
	
	if nineCounter != 0:
		VDS_AVG_9V = (sumVDS_9V/zeroCounter)
		IDS_AVG_9V = (sumIDS_9V/zeroCounter)
		resistance_9V = VDS_AVG_9V/IDS_AVG_9V
		yC_9V.append(round(resistance_9V, 2))
		getDeviceLength(devID, xC_9V,w)
	
	rangeIndex[0] = rangeIndex[0] + 1
	rangeIndex[1] = rangeIndex[1] + 1
	
def getDeviceLength(devID, xCoords, width):
	deviceCol = int(devID[7])
	deviceRow = int(devID[9])

	#print 'Device', devID
	#print 'Dev Col',deviceCol
	#print 'Dev Row', deviceRow

	if deviceCol >= 1 and deviceCol <= 2: 
		length = 5
	elif deviceCol >= 3 and deviceCol <= 4: 
		length = 10
	elif deviceCol >= 5 and deviceCol <= 6: 
		length = 15
	elif deviceCol >= 7 and deviceCol <= 8: 
		length = 20

	if deviceRow >= 1 and deviceRow <=5:
		width = 100
	elif deviceRow >= 6 and deviceRow <= 10:
		width = 200

	xCoords.append(length)

def makeGraph(x0,y0,c0, x3, y3, c3, x6, y6, c6, x9, y9, c9, Rc, Rs, Lt, Pc):
	plt.title("Transfer Length Measurement (TLM) Graph")
	plt.xlabel('L, microm')	
	plt.ylabel('R, ohms')
	plt.xlim([0,25])
	plt.ylim([0,6000000])
	plt.plot(x0,y0,c0, label='0V')
	coefficients = np.polyfit(x0,y0,1)
	polynomial = np.poly1d(coefficients)
	ys=polynomial(x0)
	plt.plot(x0,ys,'r')
	#print 'INFORMATION FOR 0V'
	#print 'x-coords:', x0
	#print 'y-coords:', y0
	slope, intercept = np.polyfit(x0, y0, 1)
	#print '0v slope is', slope
	#print '0v intercept is ', intercept	
	plt.plot(x3,y3,c3, label='3V')
	coefficients = np.polyfit(x3,y3,1)
	polynomial= np.poly1d(coefficients)
	ys=polynomial(x3)
	plt.plot(x3,ys,'b')
	print 'INFORMATION FOR 3V'
	print 'x-coords:', x3
	print 'y-coords:', y3
	slope, intercept = np.polyfit(x3, y3, 1)
	calculateParameters(slope, intercept, Rc, Rs, Lt, Pc)
	
	print '3V slope is', slope
	print '3V intercept is ', intercept
	
	plt.plot(x6,y6,c6, label='6V')
	coefficients = np.polyfit(x6,y6,1)
	polynomial= np.poly1d(coefficients)
	ys=polynomial(x6)
	plt.plot(x6,ys,'y')
	print 'INFORMATION FOR 6V'
	print 'x-coords:', x6
	print 'y-coords:', y6
	slope, intercept = np.polyfit(x6, y6, 1)
	calculateParameters(slope, intercept, Rc, Rs, Lt, Pc)
	print '6V slope is', slope
	print '6V intercept is ', intercept
	plt.plot(x9,y9,c9, label='9V')
	coefficients = np.polyfit(x9,y9,1)
	polynomial= np.poly1d(coefficients)
	ys=polynomial(x9)
	plt.plot(x9,ys,'g')
	print 'INFORMATION FOR 9V'
	print 'x-coords:', x9
	print 'y-coords:', y9
	slope, intercept = np.polyfit(x9, y9, 1)
	calculateParameters(slope, intercept, Rc, Rs, Lt, Pc)
	print '9V slope is', slope
	print '9V intercept is ', intercept
	plt.legend(numpoints=1)

def calculateParameters(a, b, Rc, Rs, Lt, Pc):
	W = 100 #W is hard coded...need to fix this later
	contactResistance = b/2
	Rc.append(round(contactResistance,2))
	sheetResistance = a * W
	Rs.append(round(sheetResistance,2))
	transferLength = b/(2*a)
	Lt.append(round(transferLength,2))
	contactResistivity = contactResistance * transferLength * W
	Pc.append(round(contactResistivity,2))

def printTable(Rc, Rs, Lt, Pc):
	val = 3
	print '   Rc \t\tRs\t\tLt\tPc'
	for ix in range(len(Rc)):
		print str(val)+'V', Rc[ix], '\t',Rs[ix], '\t', Lt[ix],'\t',Pc[ix]
		val = val + 3
def showGraph():
	plt.show()