#Ryan Kinsella, 10194574

#may need to use pip in python command line idle to install csv
import csv
import random

#globals for testing
maxTimeDelay = 50 #will be divided by 100
maxPlanesToChoose = 50


def listFromCSV(fileName): #str
    aList=[]
    filePath=str("C:\\Users\\R-k-l\\Documents\\Python\\"+fileName)
    with open(filePath) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            aList.append(float(row[0]))
    return aList

def gatesRequired(arrival,departure): #list, list
    #start off with 0 gates for the first elif statement to work properly
    gateCount=0
    numPlanesInGates=0
    departureTimes=[]

    for i in range(0,len(arrival)):
        departureTimes.append(departure[i]) #list of the lowest departure times
        departureTimes.sort() #O(nlogn)total
        
        #do this first so that a new plane can access the departing planes gate
        if (departureTimes[0] < arrival[i]):
            #plane["
            del departureTimes[0]
            numPlanesInGates-=1

        #add a plane to an available gate if there's room
        if (numPlanesInGates < gateCount):
            numPlanesInGates+=1

        #otherwise create a new gate and shove the new plane there 
        else:
            gateCount+=1
            numPlanesInGates+=1

    return gateCount


#takes in two lists, a number of planes , and a time that planes are allowed to be late
def alterFromInputs(sList,eList,numPlanesEffected,timeDelay): #list,list,int,int

    #loops for the number of random planes effected
    for i in range (0,numPlanesEffected):
        randList = random.sample(list(range(0,len(sList))),numPlanesEffected)
        earlyOrLate=random.randint(0,1)
        #plane arrival is late
        if (earlyOrLate==0):
            sList[randList[i]]+=timeDelay
            if (sList[randList[i]] > eList[randList[i]]):
                sList[randList[i]]-=timeDelay
            
        #plane departure is late
        else:
            eList[randList[i]]+=timeDelay
            
    return sList,eList

#creates a new list that is randomly generated for start and end times
def randomAlter(sList,eList): #list, list, float, float
    #maxTimeDelay and maxPlanesToChoose are global variables
    timeDelay=float(random.randint(0,maxTimeDelay)/100)
    randomNumPlanesEffected=random.randint(0,maxPlanesToChoose) #between 0 and 100 random planes effected
    randList = random.sample(list(range(0,len(sList))),maxPlanesToChoose)
    
    #loops for the number of random planes effected
    for i in range (0,randomNumPlanesEffected):
        
        earlyOrLate=random.randint(0,1)
        #plane arrival is late
        if (earlyOrLate==0):
            sList[randList[i]]+=timeDelay
            if (sList[randList[i]] > eList[randList[i]]):
                sList[randList[i]]-=timeDelay
            
            
        #plane departure is late
        else:
            eList[randList[i]]+=timeDelay
            
    return sList,eList,timeDelay,randomNumPlanesEffected


#Main
#takes in two lists, a number of planes , and a time that planes are allowed to be late


#Import lists from CSV files
s1=listFromCSV("start1.csv")
s2=listFromCSV("start2.csv")
f1=listFromCSV("finish1.csv")
f2=listFromCSV("finish2.csv")


# 1. regular outputs
print("1. Regular outputs without late times: ")
print("Using start1 and finish1: ",gatesRequired(s1,f1))
print("Using start2 and finish2: ",gatesRequired(s2,f2))

# 2. aircraft allowed to run late outputs, run for a specified number of
#random planes that arrive late
#start1 and finish1 csv files used
timeLate15mins=0.25
numberOfPlanesLate=40
alteredStart1,alteredFinish1 = alterFromInputs(s1,f1,numberOfPlanesLate,timeLate15mins)

print()
print("2. Altered outputs with random late planes")
print("15 mins: ",gatesRequired(alteredStart1,alteredFinish1))

# 3. aircraft allowed to run late, run for random plane start times and end times
print()
print("3. Fully Random Outputs")

#random alter creates a new list that is randomly generated for start and end times
for i in range(0,10):
    alteredStart1,alteredFinish1,timeDelayMain,randomNumPlanesEffected = randomAlter(s1,f1)
    print("Number of gates required: ",gatesRequired(alteredStart1,alteredFinish1))
    print("Time delay: ",round(timeDelayMain*60,2),"minutes")
    print("Planes Effected: ",randomNumPlanesEffected)





      


