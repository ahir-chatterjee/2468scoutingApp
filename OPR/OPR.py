import json
import numpy
import math

fileName = raw_input("Import what json file? (ex. 2017roe): ") + ".txt"
#fileName = "2016gal.txt"
matchesFile = open(fileName,'r')
matchesStr = ""
for line in matchesFile:
    matchesStr += line
matches = json.loads(matchesStr)
matchesFile.close()

teams = []

class teamVector(object):

    def __init__(self,number):
        self.number = number
        self.totalPoints = 0
        self.dict = {}
        for team in teams:
            self.dict[team] = 0

    def printTeam(self):
        print "Team Number is " + (str)(self.number) + ". Total Points scored are " + (str)(self.totalPoints) + "."
        count = 0
        for key in self.dict:
            print "They played with " + key + " played with " + (str)(self.dict[key]) + " times."

    def countTeam(self,team):
        self.dict[team] += 1

    def addPoints(self,points):
        self.totalPoints += points

    def returnVector(self):
        outputList = []
        for key in self.dict:
            outputList.append((int)(self.dict[key]))
        return outputList

def returnDict(d):
    returnStr = ""
    for key in d:
        returnStr += (str)(key) + ": " + (str)(d[key])
    return returnStr

def returnMatchKeys():
    returnList = []
    for match in matches:
        returnList.append(match["key"])
    return returnList

def numMatches():
    return (str)(len(matches))

def returnQMStats(targetKey): #ONLY WORKS FOR QM's
    returnList = []
    for match in matches:
        if(match["key"] == targetKey):
            returnList.append((int)(match["key"][match["key"].rfind('m')+1:])) #given any string ending with qm#, it will return #
            for team in match["alliances"]["blue"]["team_keys"]:
                returnList.append((str)(team[3:]))
            for team in match["alliances"]["red"]["team_keys"]:
                returnList.append((str)(team[3:]))
            returnList.append((int)(match["alliances"]["blue"]["score"] - match["score_breakdown"]["blue"]["foulPoints"]))
            returnList.append((int)(match["alliances"]["red"]["score"] - match["score_breakdown"]["blue"]["foulPoints"]))
    return returnList

def createQMOutput():
    outputFile = open("matchesOutput.txt",'w')
    returnList = []
    outputFile.write(fileName[:len(fileName)-4] + "\n")
    for key in returnMatchKeys():
        if(key.find("_qm") != -1):
            matchStatList = []
            for stat in returnQMStats(key):
                outputFile.write((str)(stat) + " ")
                matchStatList.append(stat)
            outputFile.write("\n")
            returnList.append(matchStatList)
    outputFile.close()
    return returnList

def initializeTeams(matchOutputs):
    for matchStats in matchOutputs:
        for num in range(1,7):
            if(matchStats[num] not in teams):
                teams.append(matchStats[num])

def initializeTeamVectors(matchOutputs):
    outputList = []
    initializeTeams(matchOutputs)
    for team in teams:
        outputList.append(teamVector(team))
    return outputList

def updateTeamVectors(matchOutputs):
    for matchStats in matchOutputs:
        for number in range(1,4):
            for team in teamVectors:
                if(team.number == matchStats[number]):
                    for num in range(1,4):
                        team.countTeam(matchStats[num])
                    team.addPoints(matchStats[7])
        for number in range(4,7):
            for team in teamVectors:
                if(team.number == matchStats[number]):
                    for num in range(4,7):
                        team.countTeam(matchStats[num])
                    team.addPoints(matchStats[8])

def calculateOPR():
    a = []
    b = []
    for team in teamVectors:
        a.append(team.returnVector())
        b.append([(int)(team.totalPoints)])
    return numpy.linalg.solve(a,b)

def returnOPR():
    outputFile = open("oprOutput.txt",'w')
    returnStr = ""
    count = 0
    outputFile.write(fileName[:len(fileName)-4] + "\n")
    for key in teamVectors[0].dict:
        returnStr += "Team " + (str)(key) + " has an OPR of " + (str)(round(OPRlist[count][0],2)) + ". \n"
        outputFile.write((str)(key) + " " + (str)(round(OPRlist[count][0],2)) + "\n")
        count += 1
    outputFile.close()
    return returnStr    
                        
QMStats = createQMOutput()
teamVectors = initializeTeamVectors(QMStats)
updateTeamVectors(QMStats)
OPRlist = calculateOPR()
print returnOPR()
    
    

        




                   
