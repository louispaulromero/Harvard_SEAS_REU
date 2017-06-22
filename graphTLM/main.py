import csv
import functions as fns 
import matplotlib.pyplot as plt

deviceID = []
VG = []
IDS =[]
IG = []
VDS = []
xCoordinates = []
yCoordinates = []


#This loads CSV into memory
with open('NMOS345_AsFab.csv', 'rb') as dataInCSV: 
		dataAsReader = csv.reader(dataInCSV)
		#Function call to get data into lists
		fns.getData(dataAsReader, deviceID, VG, IDS,IG, VDS)
		#Function call to determine device location and x coordinates
		fns.getDeviceLength(deviceID, xCoordinates)
		#Fucnction call to get make makes columns in CSV into lists and and calculate resistance
		fns.calculateResistance(VG, IDS, IG, VDS, yCoordinates)

#This function takes graph and builds it
fns.makeGraph(xCoordinates, yCoordinates)