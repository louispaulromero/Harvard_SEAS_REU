# ********************************************************
# functions.py
#
# Summary:  This file includes the function definitions and
# implementations for use with main.py 
# a program that helps analyze data generated by a 
# 4 point probe station.
#
# Author: Louis Paul Romero
# Created: Summer 2017
# Summary of Modifications:
#  27 JUL 2017 - LPR - Added comments
#
#  *******************************************************

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 

#*********************************************************
def countDeviceIDs(col):
# Summary: Counts the number of devices tested using their 
# Device ID
# Precondition: A list containing the Device IDs my 
# be passed through the function
# Postcondition: The count of devices is returned
# ********************************************************
	count = 0
	for ix in range(len(col)):
		if(str(col[ix]) == 'Device ID'):
			count = count + 1
	return count


#*********************************************************
def organizeData(c1,c2,c3,c4,VG, IDS, IG, VDS, ranges):
# Summary: 
# Precondition:
# Postcondition:
# ********************************************************
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


#*********************************************************
def calculateResistance(VG, IDS, IG, VDS, ranges, rangeIndex, devID, xC_0V, xC_3V, xC_6V, xC_9V, yC_0V, yC_3V, yC_6V, yC_9V,w):
# Summary: 
# Precondition:
# Postcondition:
# ********************************************************
	#print 'ranges',ranges
	#print 'rangeIndex', rangeIndex
	start = ranges[rangeIndex[0]]
	finish = ranges[rangeIndex[1]]
	#print 'start', start
	#print 'finish',finish
	#print 'the start', VG[start]
	#print IDS[start]
	#print 'the finish', VG[finish-1]

	'''datapoints = input('how many data points?')
	while :n < input
		gatevoltage = input('Please enter voltage: ')'''

	#ix = 0
	while start < finish:
		if VG[start] == '0':
			resistance_1 = float(VDS[start])/float(IDS[start])
			yC_0V.append(round(resistance_1, 2))
			getDeviceLength(devID, xC_0V,w)
		elif VG[start] == '3': 
			#print 'at 3', IDS[start]
			#print 'at 3', VDS[start]
			#print '1',IDS[start]
			#print '1',VDS[start]
			resistance_2 = float(VDS[start])/float(IDS[start])
			yC_3V.append(round(resistance_2, 2))
			getDeviceLength(devID, xC_3V,w)
		elif VG[start] == '6': 
			resistance_3 = float(VDS[start])/float(IDS[start])
			yC_6V.append(round(resistance_3, 2))
			getDeviceLength(devID, xC_6V,w)
		elif VG[start] == '9':
			resistance_4 = float(VDS[start])/float(IDS[start])
			yC_9V.append(round(resistance_4, 2))
			getDeviceLength(devID, xC_9V,w)
		start = start + 1

	rangeIndex[0] = rangeIndex[0] + 1
	rangeIndex[1] = rangeIndex[1] + 1


#*********************************************************
def getDeviceLength(devID, xCoords, width):
# Summary: 
# Precondition:
# Postcondition:
# ********************************************************
	ix = 0
	if devID[0:5] == 'EDOP3':
		deviceCol = int(devID[7])
		if deviceCol == 1:
			deviceCol = int(devID[7:9])

		if deviceCol == 2: 
			length = 5
		elif deviceCol == 4: 
			length = 7
		elif deviceCol == 6: 
			length = 9
		elif deviceCol == 8: 
			length = 12
		elif deviceCol == 10:
			length = 18
		xCoords.append(length)

	if devID[0:5] == 'NMOS3':
		deviceCol = int(devID[7])
		deviceRow = int(devID[9])
		if deviceCol >= 1 and deviceCol <= 2: 
			length = 5
		elif deviceCol >= 3 and deviceCol <= 4: 
			length = 10
		elif deviceCol >= 5 and deviceCol <= 6: 
			length = 15
		elif deviceCol >= 7 and deviceCol <= 8: 
			length = 20
		xCoords.append(length)

	if devID[0:6] == 'EDOPE6':
		deviceCol = int(devID[8])
		if deviceCol == 1:
			deviceCol = int(devID[8:10])
		if deviceCol == 2: 
			length = 5
		elif deviceCol == 4: 
			length = 7
		elif deviceCol == 6: 
			length = 9
		elif deviceCol == 8: 
			length = 13
		elif deviceCol == 10:
			length = 18
		xCoords.append(length)


#*********************************************************
def makeGraph(x0,y0,c0, x3, y3, c3, x6, y6, c6, x9, y9, c9, Rc, Rs, Lt, Pc):
# Summary: 
# Precondition:
# Postcondition:
# ********************************************************
	ix = 0
	plt.title("Transfer Length Measurement (TLM)")
	plt.xlabel('L, microm')	
	plt.ylabel('R, ohms')
	plt.plot(x0,y0,c0, label='0V')

	plt.xlim([0,20])
	#plt.ylim([0,400000])
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
	plt.legend(numpoints=1, loc='best')


#*********************************************************
def calculateParameters(a, b, Rc, Rs, Lt, Pc):
# Summary: 
# Precondition:
# Postcondition:
# ********************************************************
	ix = 0
	W = input('Please enter width: ')
	contactResistance = b/2
	Rc.append(round(contactResistance,2))
	sheetResistance = a * W
	Rs.append(round(sheetResistance,2))
	transferLength = b/(2*a)
	Lt.append(round(transferLength,2))
	contactResistivity = contactResistance * transferLength * W
	Pc.append(round(contactResistivity,2))


#*********************************************************
def printTable(Rc, Rs, Lt, Pc):
# Summary: 
# Precondition:
# Postcondition:
# ********************************************************
	ix = 0
	val = 3
	print '   Rc,ohms\tRs,ohms\t\tLt,microm\tPc,ohmscm^2'
	for ix in range(len(Rc)):
		print str(val)+'V', Rc[ix], '\t',Rs[ix], '\t', Lt[ix],'\t\t',Pc[ix]
		val = val + 3


#*********************************************************
def showGraph():
# Summary: 
# Precondition:
# Postcondition:
# ********************************************************
	ix = 0
	plt.show()

#References:
#Linear Regression: https://www.youtube.com/watch?v=p4ezH9HUPOY