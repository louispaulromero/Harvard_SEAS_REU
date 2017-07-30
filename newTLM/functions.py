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
import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 

def getVoltages(v):
# Summary: Counts the number of devices tested using their 
# Device ID
# Precondition: A list containing the Device IDs my 
# be passed through the function
# Postcondition: The count of devices is returned
# ********************************************************
	#This loop collects from user the amount of voltages to analyze and their value
	loopController = int(raw_input("How many voltages would will you be analzying (MAXIMUM OF 4)?  "))
	ix = 0
	while ix < loopController:
		v.append(int(raw_input("Please enter Voltage "+ str(ix+1) + ": ")))
		ix = ix + 1
	print "Voltages entered:",v


#*********************************************************
def getCSVData(l1,l2,l3,l4,v1, i1, i2, v2, r):
# Summary: 
# Precondition:
# Postcondition:
# ********************************************************

#Enables entering file name, so any CSV can be opened
#FILENAME = str(raw_input('Please enter file name: '))+'.csv'
#Separates each column in CSV into own list
#with open(FILENAME, 'rb') as dataInCSV:
	with open('EDOPE3_NOEDOPE.csv', 'rb') as dataInCSV:
		dataAsReader = csv.reader(dataInCSV)
		for row in dataAsReader:
			if len(row) == 2:
				l1.append(row[0])
				l2.append(row[1])
				l3.append('')
				l4.append('')
			else:
				l1.append(row[0])
				l2.append(row[1])
				l3.append(row[2])
				l4.append(row[3])
	ix = 0
	while(ix < len(l1)):
		v1.append(l1[ix])
		i1.append(l2[ix])
		i2.append(l3[ix])
		v2.append(l4[ix])
		if str(v1[ix]) == 'Device ID':
			#print 'Device ID found', ix
			r.append(ix)
		ix = ix + 1
	r.append(len(v1))

#*********************************************************
def getDeviceWidhtsAndLengths(col, w,l):
# Summary: Counts the number of devices tested using their 
# Device ID
# Precondition: A list containing the Device IDs my 
# be passed through the function
# Postcondition: The count of devices is returned
# ********************************************************
	count = 0
	for ix in range(len(col)):
		if(str(col[ix][0:5]) == 'EDOP3'):
				count = count + 1
				
				deviceID = col[ix]
				#Determine Row
				deviceRow = int(deviceID[len(deviceID)-1 : len(deviceID)])
				#Get Device Widths
				if deviceRow == 1 or deviceRow == 2:
					w.append(int(20))
				elif deviceRow == 3 or deviceRow == 4:
					w.append(int(50))
				elif deviceRow == 5 or deviceRow == 6:
					w.append(int(100))
				elif deviceRow == 7 or deviceRow == 8:
					w.append(int(150))
				#Determine Column
				if deviceID[7:9] == '10':
					deviceColumn = int(deviceID[7:9])
				else:
					deviceColumn = int(deviceID[7:8])
				#print 'ROW:',str(deviceRow),'COLUMN:',str(deviceColumn)
				#Get Device Length

				#look at white paper for actual lengths
				if deviceColumn == 1 or deviceColumn == 2:
					l.append(int(5))
				elif deviceColumn == 3 or deviceColumn == 4:
					l.append(int(7))
				elif deviceColumn == 5 or deviceColumn == 6:
					l.append(int(9))
				elif deviceColumn == 7 or deviceColumn == 8:
					l.append(int(13))
				elif deviceColumn == 9 or deviceColumn == 10:
					l.append(int(18))
	
	print 'widths', w
	print 'lengths',l


#*********************************************************
#v1 = vg i1 = ids i2 = ig v2 = vds

def calculateResistance(voltages,r, w, l, v1, i1, i2, v2, yCV1, yCV2, yCV3, yCV4, iT):
# Summary: 
# Precondition:
# Postcondition:
# ********************************************************
	print 'the voltages',voltages
	print 'the ranges',r
	print 'current w'
	print 'current l', l
	start = r[iT[0]]
	finish = r[iT[1]]

	if(len(voltages) == 1):
		while start < finish:
			if v1[start] == str(voltages[0]):
				resistance1 = float(v2[start])/float(i1[start])
				yCV1.append(round(resistance1, 2)*w)
			start = start + 1					
	elif(len(voltages) == 2):
		while start < finish:
			if v1[start] == str(voltages[0]):
				resistance1 = float(v2[start])/float(i1[start])
				yCV1.append(round(resistance1, 2)*w)
			elif v1[start] == str(voltages[1]): 
				resistance2 = float(v2[start])/float(i1[start])
				yCV2.append(round(resistance2, 2)*w)
			start = start + 1
	elif(len(voltages) == 3):
		while start < finish:
			if v1[start] == str(voltages[0]):
				resistance1 = float(v2[start])/float(i1[start])
				yCV1.append(round(resistance1, 2)*w)
			elif v1[start] == str(voltages[1]): 
				resistance2 = float(v2[start])/float(i1[start])
				yCV2.append(round(resistance2, 2)*w)
			elif v1[start] == str(voltages[2]): 
				resistance3 = float(v2[start])/float(i1[start])
				yCV3.append(round(resistance3, 2) * w)
			start = start + 1
	elif(len(voltages) == 4):
		while start < finish:
			if v1[start] == str(voltages[0]):
				resistance1 = float(v2[start])/float(i1[start])
				yCV1.append(round(resistance1, 2)*w)
			elif v1[start] == str(voltages[1]): 
				resistance2 = float(v2[start])/float(i1[start])
				yCV2.append(round(resistance2, 2)*w)
			elif v1[start] == str(voltages[2]): 
				resistance3 = float(v2[start])/float(i1[start])
				yCV3.append(round(resistance3, 2) * w)
			elif v1[start] == str(voltages[3]):
				resistance4 = float(v2[start])/float(i1[start])
				yCV4.append(round(resistance4, 2) *w)
			start = start + 1
	iT[0] = iT[0] + 1
	iT[1] = iT[1] + 1

#*********************************************************
def makeGraph(xV1,yV1,c1, xV2, yV2, c2, xV3, yV3, c3, xV4, yV4, c4, Rc, Rs, Lt, Pc, w,v):
# Summary: 
# Precondition:
# Postcondition:
# ********************************************************
	#Style Graph
	plt.title("Transfer Length Measurement (TLM)")
	plt.xlabel('L, microm')	
	plt.ylabel('R, ohms')
	plt.xlim([0,20])
	#plt.ylim([0,400000])
	plt.legend(numpoints=1, loc='best')
	if len(v) == 1:
		#VOLTAGE 1
		plt.plot(xV1,yV1,c1, label=str(v[0]))
		coefficients = np.polyfit(xV1,yV1,1)
		polynomial = np.poly1d(coefficients)
		ys=polynomial(xV1)
		plt.plot(xV1,ys,'r')
		slope, intercept = np.polyfit(xV1, yV1, 1)
		calculateParameters(slope, intercept, Rc, Rs, Lt, Pc,w)
		print 'INFORMATION FOR ' + str(v[0]) + 'V'
		print 'x-coords:', xV1
		print 'y-coords:', yV1
		print str(v[0]) + 'V' + ' slope is', slope
		print str(v[0]) + 'V' + ' intercept is ', intercept	

	elif len(v) == 2:
		#VOLTAGE 1
		plt.plot(xV1,yV1,c1, label=str(v[0]))
		coefficients = np.polyfit(xV1,yV1,1)
		polynomial = np.poly1d(coefficients)
		ys=polynomial(xV1)
		plt.plot(xV1,ys,'r')
		slope, intercept = np.polyfit(xV1, yV1, 1)
		calculateParameters(slope, intercept, Rc, Rs, Lt, Pc,w)
		print 'INFORMATION FOR ' + str(v[0]) + 'V'
		print 'x-coords:', xV1
		print 'y-coords:', yV1
		print str(v[0]) + 'V' + ' slope is', slope
		print str(v[0]) + 'V' + ' intercept is ', intercept	

		#VOLTAGE 2
		plt.plot(xV2,yV2,c2, label=str(v[1]))
		coefficients = np.polyfit(xV2,yV2,1)
		polynomial= np.poly1d(coefficients)
		ys=polynomial(xV2)
		plt.plot(xV2,ys,'b')	
		slope, intercept = np.polyfit(xV2, yV2, 1)
		calculateParameters(slope, intercept, Rc, Rs, Lt, Pc,w)
		print 'INFORMATION FOR ' + str(v[1]) + 'V'
		print 'x-coords:', xV2
		print 'y-coords:', yV2
		print str(v[1]) + 'V' + ' slope is', slope
		print str(v[1]) + 'V' + ' intercept is ', intercept

	elif len(v) == 3:
		#VOLTAGE 1
		plt.plot(xV1,yV1,c1, label=str(v[0]))
		coefficients = np.polyfit(xV1,yV1,1)
		polynomial = np.poly1d(coefficients)
		ys=polynomial(xV1)
		plt.plot(xV1,ys,'r')
		slope, intercept = np.polyfit(xV1, yV1, 1)
		calculateParameters(slope, intercept, Rc, Rs, Lt, Pc,w)
		print 'INFORMATION FOR ' + str(v[0]) + 'V'
		print 'x-coords:', xV1
		print 'y-coords:', yV1
		print str(v[0]) + 'V' + ' slope is', slope
		print str(v[0]) + 'V' + ' intercept is ', intercept	

		#VOLTAGE 2
		plt.plot(xV2,yV2,c2, label=str(v[1]))
		coefficients = np.polyfit(xV2,yV2,1)
		polynomial= np.poly1d(coefficients)
		ys=polynomial(xV2)
		plt.plot(xV2,ys,'b')	
		slope, intercept = np.polyfit(xV2, yV2, 1)
		calculateParameters(slope, intercept, Rc, Rs, Lt, Pc,w)
		print 'INFORMATION FOR ' + str(v[1]) + 'V'
		print 'x-coords:', xV2
		print 'y-coords:', yV2
		print str(v[1]) + 'V' + ' slope is', slope
		print str(v[1]) + 'V' + ' intercept is ', intercept
		
		#VOLTAGE 3
		plt.plot(xV3,yV3,c3, label=str(v[2]))
		coefficients = np.polyfit(xV3,yV3,1)
		polynomial= np.poly1d(coefficients)
		ys=polynomial(xV3)
		plt.plot(xV3,ys,'y')
		slope, intercept = np.polyfit(xV3, yV3, 1)
		calculateParameters(slope, intercept, Rc, Rs, Lt, Pc,w)
		print 'INFORMATION FOR ' + str(v[2]) + 'V'
		print 'x-coords:', xV3
		print 'y-coords:', yV3
		print str(v[2]) + 'V' + ' slope is', slope
		print str(v[2]) + 'V' + ' intercept is ', intercept

	elif len(v) == 4:
		#VOLTAGE 1
		plt.plot(xV1,yV1,c1, label=str(v[0]))
		coefficients = np.polyfit(xV1,yV1,1)
		polynomial = np.poly1d(coefficients)
		ys=polynomial(xV1)
		plt.plot(xV1,ys,'r')
		slope, intercept = np.polyfit(xV1, yV1, 1)
		calculateParameters(slope, intercept, Rc, Rs, Lt, Pc,w)
		print 'INFORMATION FOR ' + str(v[0]) + 'V'
		print 'x-coords:', xV1
		print 'y-coords:', yV1
		print str(v[0]) + 'V' + ' slope is', slope
		print str(v[0]) + 'V' + ' intercept is ', intercept	

		#VOLTAGE 2
		plt.plot(xV2,yV2,c2, label=str(v[1]))
		coefficients = np.polyfit(xV2,yV2,1)
		polynomial= np.poly1d(coefficients)
		ys=polynomial(xV2)
		plt.plot(xV2,ys,'b')	
		slope, intercept = np.polyfit(xV2, yV2, 1)
		calculateParameters(slope, intercept, Rc, Rs, Lt, Pc,w)
		print 'INFORMATION FOR ' + str(v[1]) + 'V'
		print 'x-coords:', xV2
		print 'y-coords:', yV2
		print str(v[1]) + 'V' + ' slope is', slope
		print str(v[1]) + 'V' + ' intercept is ', intercept
		
		#VOLTAGE 3
		plt.plot(xV3,yV3,c3, label=str(v[2]))
		coefficients = np.polyfit(xV3,yV3,1)
		polynomial= np.poly1d(coefficients)
		ys=polynomial(xV3)
		plt.plot(xV3,ys,'y')
		slope, intercept = np.polyfit(xV3, yV3, 1)
		calculateParameters(slope, intercept, Rc, Rs, Lt, Pc,w)
		print 'INFORMATION FOR ' + str(v[2]) + 'V'
		print 'x-coords:', xV3
		print 'y-coords:', yV3
		print str(v[2]) + 'V' + ' slope is', slope
		print str(v[2]) + 'V' + ' intercept is ', intercept
		
		#VOLTAGE 4
		plt.plot(xV4,yV4,c4, label=str(v[3]))
		coefficients = np.polyfit(xV4,yV4,1)
		polynomial= np.poly1d(coefficients)
		ys=polynomial(xV4)
		plt.plot(xV4,ys,'g')
		print 'INFORMATION FOR ' + str(v[3]) + 'V'
		print 'x-coords:', xV4
		print 'y-coords:', yV4
		print str(v[3]) + 'V' + ' slope is', slope
		print str(v[3]) + 'V' + '  intercept is ', intercept
		slope, intercept = np.polyfit(xV4, yV4, 1)
		calculateParameters(slope, intercept, Rc, Rs, Lt, Pc,w)
	
	#plt.figure(1)
	#plt.show()
	plt.savefig(str(raw_input('Please enter name for file:'))+'.png')


#*********************************************************
def calculateParameters(a, b, Rc, Rs, Lt, Pc,w):
# Summary: 
# Precondition:
# Postcondition:
# ********************************************************
	ix = 0
	#need to change
	W = w[0]
	contactResistance = b/2
	Rc.append(round(contactResistance,2))
	sheetResistance = a * W
	Rs.append(round(sheetResistance,2))
	transferLength = b/(2*a)
	Lt.append(round(transferLength,2))
	contactResistivity = contactResistance * transferLength * W
	Pc.append(round(contactResistivity,2))


#*********************************************************
def printTable(Rc, Rs, Lt, Pc, v):
# Summary: 
# Precondition:
# Postcondition:
# ********************************************************
	ix = 0
	print '   Rc,ohms\tRs,ohms\t\tLt,microm\tPc,ohmscm^2'
	for ix in range(len(v)):
		print str(v[ix])+'V', Rc[ix], '\t',Rs[ix], '\t', Lt[ix],'\t\t',Pc[ix]


# ********************************************************
#
#
# REFERENCES
#
#
#  *******************************************************

#Linear Regression: https://www.youtube.com/watch?v=p4ezH9HUPOY