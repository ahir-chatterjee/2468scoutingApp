import json
import radarPlot
import spreadsheetMaker
import multiRadarPlot
import autoChart
import teleChart

def runScoutingApp():
    class Match(object):
    
        def __init__(self,number,red,blue,random):
            self.dict = {"number": number,"red": red,"blue": blue,"random": random}
            
        def returnMatch(self):
            returnStr = ""
            for key in self.dict:
                returnStr += key + ": " + (str)(self.dict[key]) + "\n"
            return returnStr
    
        def importDict(self,diction):
            for key in self.dict:
                self.dict[key] = diction[key]

        def compareMatch(self,other):
            same = True
            for key in self.dict:
                if(self.dict[key] != other.dict[key]):
                    same = False
            return same
    
    class Team(object):
    
        def __init__(self,teamNum):
            self.dict =  {"matches": [],"number": teamNum,"autoPenalty": [],"autoLine": [],"autoSwitch": [],"autoScale": [],
                          "startingPos": [],"teleSwitch": [],"teleOppSwitch": [],"teleScale": [],"hang": [],
                          "assistance": [],"vaultBlocks": [],"comments": [],"cims": 0,"wheels": 0,"drivetrain": "",
                          "weight": 0,"preAuto": "","preTele": "","preHang": "","preAssist": "","language": "","preScoutComments": ""}
    
        def returnTeam(self):
            returnStr = ""
            for key in self.dict:
                returnStr += key + ": " + (str)(self.dict[key]) + "\n"
            return returnStr
    
        def addMatch(self,matchNum,general,scale,comment):
            self.dict["matches"].append((int)(matchNum))
            self.dict["autoPenalty"].append(general[0])
            self.dict["autoLine"].append(general[1])
            self.dict["autoSwitch"].append(general[2])
            self.dict["autoScale"].append(general[3])
            self.dict["startingPos"].append(general[4])
            self.dict["teleSwitch"].append(general[5])
            self.dict["teleOppSwitch"].append(general[6])
            self.dict["teleScale"].append(scale)
            self.dict["hang"].append(general[7])
            self.dict["assistance"].append(general[8])
            self.dict["vaultBlocks"].append(general[9])
            self.dict["comments"].append(comment)
    
        def addPreData(self,preData):
            self.dict["cims"] = preData[1]
            self.dict["wheels"] = preData[2]
            self.dict["drivetrain"] = preData[3]
            self.dict["weight"] = preData[4]
            self.dict["language"] = preData[5]
            self.dict["preAuto"] = preData[6]
            self.dict["preTele"] = preData[7]
            self.dict["preHang"] = preData[8]
            self.dict["preAssist"] = preData[9]
            self.dict["preScoutComments"] = preData[10]
    
        def importDict(self,diction):
            for key in self.dict:
                self.dict[key] = diction[key]

        def compareTeam(self,other):
            if(self.dict["number"] == other.dict["number"]):
                return True
            return False
    
    def enterMatch():
        matchInfo = raw_input("Enter match string: ").split()
        
        number = matchInfo[0]
        red = []
        blue = []
        random = []
        for num in range(1,4):
            red.append((str)(matchInfo[num])) 
        for num in range(4,7):
            blue.append((str)(matchInfo[num])) 
        for num in range(7,9):
            random.append(matchInfo[num])
        match = Match(number,red,blue,random)
        matchList.append(match)
        return match
    
    def makeSpreadsheet():
        spreadsheetMaker.makeSpreadsheet()

    def radarPlotStats(team):
        teamNum = team.dict["number"]
        numMatches = (float)(len(team.dict["matches"]))
        if(numMatches == 0):
            numMatches = 1
        
        switch = 0
        sumSwitch = 0
        for i in range(0,len(team.dict["matches"])):
            cubes = (int)(team.dict["teleSwitch"][i]) + (int)(team.dict["teleOppSwitch"][i])
            if(cubes >= 6):
                sumSwitch += 5
            elif(cubes >= 4):
                sumSwitch += 4
            elif(cubes >= 3):
                sumSwitch += 3
            elif(cubes >= 2):
                sumSwitch += 2
            elif(cubes > 0):
                sumSwitch += 1
        switch = (float)(sumSwitch)/numMatches
        
        scale = 0
        sumScale = 0
        for i in range(0,len(team.dict["matches"])):
            cubes = 0
            acc = 0
            for delivery in team.dict["teleScale"][i]:
                if((int)(delivery[1]) == 1):
                    cubes += 1
                acc += 1
            if(acc != 0):
                acc = (float)(cubes)/(float)(acc)
            if(acc <= 0.25 and cubes > 0):
                sumScale += 1
            elif(cubes >= 7 and acc >= 0.75):
                sumScale += 5
            elif((cubes >= 4 and acc >= .75) or cubes >= 7):
                sumScale += 4
            elif((cubes >= 2 and acc >= .75) or cubes >= 4):
                sumScale += 3
            elif((cubes > 0 and acc >= .75) or cubes >= 2):
                sumScale += 2
            elif(cubes > 0):
                sumScale += 1
        scale = (float)(sumScale)/numMatches
        
        hang = 0
        sumHang = 0
        for i in range(0,len(team.dict["matches"])):
            result = (int)(team.dict["hang"][i])
            if(result == 0):
                sumHang += 1
            elif(result == -1):
                sumHang += 0
            elif(result > 30):
                sumHang += 1
            elif(result > 21):
                sumHang += 2
            elif(result > 16):
                sumHang += 3
            elif(result > 9):
                sumHang += 4
            elif(result < 9):
                sumHang += 5
        hang = (float)(sumHang)/numMatches

        vault = 0
        sumVault = 0
        for i in range(0,len(team.dict["matches"])):
            cubes = (int)(team.dict["vaultBlocks"][i])
            if(cubes >= 7):
                sumVault += 5
            elif(cubes >= 5):
                sumVault += 4
            elif(cubes >= 3):
                sumVault += 3
            elif(cubes >= 2):
                sumVault += 2
            elif(cubes > 0):
                sumVault += 1
        vault = (float)(sumVault)/numMatches

        teamStats = [teamNum,switch,scale,hang,vault]
        return teamStats
    
    def createRadarPlot(team):
        teamStats = radarPlotStats(team)
        radarPlot.createRadarPlot(teamStats[0],teamStats[1],teamStats[2],teamStats[3],teamStats[4])

    def createMultiPlot(team1,team2,team3):
        team1Stats = radarPlotStats(team1)
        team2Stats = radarPlotStats(team2)
        team3Stats = radarPlotStats(team3)
        multiRadarPlot.createMultiRadarPlot(team1Stats,team2Stats,team3Stats)

    def readPreScoutingFile(filename):
        matchFile = open(filename+".txt",'r')
        for line in matchFile:
            if(line[0:2] == "QR"):
                info = line[8:].split('|')
                info[len(info)-1] = info[len(info)-1][:len(info[8])]
                print info
                newTeam = Team(info[0])
                newTeam.addPreData(info)
                entered = False
                for team in teamList:
                    if(team.compareTeam(newTeam)):
                        team.addPreData(info)
                        entered = True
                if(not entered):
                    teamList.append(newTeam)

    def readMatchFile(filename):
        matchFile = open(filename+".txt",'r')
        number = ""
        red = []
        blue = []
        random = []
        teamStrs = []
        for line in matchFile:
            if(line[0:2] == "QR"):
                teamStrs.append(line[8:len(line)-1])
        for teamStr in teamStrs:
            matchInfo = teamStr.split('|')[0].split()[0].split(',')
            number = matchInfo[0][2:]
            if(matchInfo[1] == "R"):
                red.append(matchInfo[2])
            elif(matchInfo[1] == "B"):
                blue.append(matchInfo[2])
            else:
                print "Error: Team's color could not be found"
            if(len(random) != 2):
                random.append(matchInfo[3])
                random.append(matchInfo[4][:len(matchInfo[4])-1])
        newMatch = Match(number,red,blue,random)
        duplicate = False
        for match in matchList:
            if(match.compareMatch(newMatch)):
                duplicate = True
        if(duplicate):
            choice = raw_input("Duplicate match detected. Proceed with entering? (Y/N) ")
            if(choice[0] == "y" or choice[0] == "Y"):
                duplicate = False
        if(not duplicate):
            print (str)(filename) + ".txt imported."
            matchList.append(newMatch)
            for i in range(0,len(teamStrs)):
                teamNum = teamStrs[i].split(')')[0].split(',')[2]
                teamStrs[i] = teamStrs[i].split(')')[1]
                teamStrs[i] = teamStrs[i][1:]
                teamStrs[i] += '| ' + teamNum
            enterQRTeams(newMatch,teamStrs)
            return duplicate
        else:
            print (str)(filename) + ".txt importing aborted."
            return duplicate
            
    
    def enterPreData():
        tempList = []
        tempList.append(raw_input("Enter team number: "))
        tempList.append(raw_input("Enter " + tempList[0] + "'s #cims: "))
        tempList.append(raw_input("Enter " + tempList[0] + "'s #wheels: "))
        tempList.append(raw_input("Enter " + tempList[0] + "'s drivetrain: "))
        tempList.append(raw_input("Enter " + tempList[0] + "'s weight: "))
        tempList.append(raw_input("Enter " + tempList[0] + "'s programming language: "))
        tempList.append(raw_input("Enter " + tempList[0] + "'s auto capabilities: "))
        tempList.append(raw_input("Enter " + tempList[0] + "'s tele capabilities: "))
        tempList.append(raw_input("Enter " + tempList[0] + "'s hang capabilities: "))
        tempList.append(raw_input("Enter " + tempList[0] + "'s assist capabilities: "))
        tempList.append(raw_input("Enter " + tempList[0] + "'s additional comments. "))
        found = False
        for team in teamList:
            if(team.dict["number"] == tempList[0]):
                team.addPreData(tempList)
                found = True
        if(not found):
            newTeam = Team(tempList[0])
            newTeam.addPreData(tempList)
            teamList.append(newTeam)
        
    
    def enterTeams(match):
        for team in match.dict["red"]:
            enterTeam(match.dict["number"],team)
        for team in match.dict["blue"]:
            enterTeam(match.dict["number"],team)

    def enterQRTeams(match,teamStrs):
        for teamStr in teamStrs:
            split = teamStr.split('|')
            scaleStats = []
            for i in range(0,len(split[1].split()),2):
                scaleStats.append([split[1].split()[i],split[1].split()[i+1]])
            genStats = split[0].split()
            comment = split[2][1:]
            teamNum = split[3][1:]
            found = False
            for team in teamList:
                if(team.dict["number"] == teamNum):
                    team.addMatch(match.dict["number"],genStats,scaleStats,comment)
                    found = True
            if(not found):
                newTeam = Team(teamNum)
                newTeam.addMatch(match.dict["number"],genStats,scaleStats,comment)
                teamList.append(newTeam)
            found = False
            
    def enterTeam(matchNum,teamNum):
        scaleStats = []
        genStats = []
        userInput = []
        while(len(userInput) != 3):
            userInput = raw_input("Enter team " + (str)(teamNum) +"'s string for match #" + (str)(matchNum) + ": ").split('|')
        genStats = userInput[0].split()
        for i in range(0,len(userInput[1].split()),2):
            scaleStats.append([userInput[1].split()[i],userInput[1].split()[i+1]])
        found = False
        comment = userInput[2][1:]
        for team in teamList:
            if(team.dict["number"] == teamNum):
                team.addMatch(matchNum,genStats,scaleStats,comment)
                found = True
        if(not found):
            newTeam = Team(teamNum)
            newTeam.addMatch(matchNum,genStats,scaleStats,comment)
            teamList.append(newTeam)
        found = False
    
    def loadMatchesList(fileName):
        matchesStr = ""
        tempList = []
        returnList = []
        matchesFile = open(fileName,'r')
        for line in matchesFile:
            matchesStr += line
        if(len(matchesStr) > 0):
            tempList = json.loads(matchesStr)
        for matchDict in tempList:
            newMatch = Match(-1,[],[],[])
            newMatch.importDict(matchDict)
            returnList.append(newMatch)
        return returnList
    
    def loadTeamsList(fileName):
        teamsStr = ""
        tempList = []
        returnList = []
        teamsFile = open(fileName,'r')
        for line in teamsFile:
            teamsStr += line
        if(len(teamsStr) > 0):
            tempList = json.loads(teamsStr)
        for teamDict in tempList:
            newTeam = Team(-1)
            newTeam.importDict(teamDict)
            returnList.append(newTeam)
        return returnList

    def autoBarChart():
        teams = raw_input("Enter red robots: ").split()
        temp = raw_input("Enter blue robots: ").split()
        for team in temp:
            teams.append(team)
        autoRun = []
        switch = []
        scale = []
        matchNum = raw_input("Enter matchNum: ")
        for teamNum in teams:
            for team in teamList:
                if(team.dict["number"] == teamNum):
                    aR = 0
                    sW = 0
                    sC = 0
                    matches = 0
                    for match in team.dict["autoLine"]:
                        aR += (int)(match)
                        matches += 1
                    for match in team.dict["autoSwitch"]:
                        sW += (int)(match)
                    for match in team.dict["autoScale"]:
                        sC += (int)(match)
                    aR = round((float)(aR)/(float)(matches),3)
                    sW = round((float)(sW)/(float)(matches),3)
                    sC = round((float)(sC)/(float)(matches),3)
                    autoRun.append(aR)
                    switch.append(sW)
                    scale.append(sC)
        print autoRun
        print switch
        print scale
        autoChart.createBarChart(autoRun,switch,scale,teams,matchNum)

    def teleBarChart():
        teams = raw_input("Enter red robots: ").split()
        temp = raw_input("Enter blue robots: ").split()
        for team in temp:
            teams.append(team)
        vault = []
        switch = []
        oppSwitch = []
        scale = []
        hang = []
        assist = []
        matchNum = raw_input("Enter matchNum: ")
        for teamNum in teams:
            for team in teamList:
                if(team.dict["number"] == teamNum):
                    v = 0
                    sW = 0
                    oSW = 0
                    sC = 0
                    h = 0
                    a = 0
                    matches = 0
                    for match in team.dict["vaultBlocks"]:
                        v += (int)(match)
                        matches += 1
                    for match in team.dict["teleSwitch"]:
                        sW += (int)(match)
                    for match in team.dict["teleOppSwitch"]:
                        oSW += (int)(match)
                    for match in team.dict["teleScale"]:
                        for delivery in match:
                            if((int)(delivery[1]) == 1):
                                sC += 1
                    for match in team.dict["hang"]:
                        if((int)(match) > 0):
                            h += 1
                    for match in team.dict["assistance"]:
                        if((int)(match) > 0):
                            a += (int)(match)
                    v = round((float)(v)/(float)(matches),1)
                    sW = round((float)(sW)/(float)(matches),1)*1.2
                    oSW = round((float)(oSW)/(float)(matches),1)*1.2
                    sC = round((float)(sC)/(float)(matches),1)*3
                    h = round((float)(h)/(float)(matches),1)*4
                    a = round((float)(a)/(float)(matches),1)*4
                    vault.append(v)
                    switch.append(sW)
                    oppSwitch.append(oSW)
                    scale.append(sC)
                    hang.append(h)
                    assist.append(a)
        print vault
        print switch
        print oppSwitch
        print scale
        print hang
        print assist
        teleChart.createBarChart(vault,switch,oppSwitch,scale,hang,assist,teams,matchNum)
    
    def save():
        teamDictList = []
        matchDictList = []
        with open('teams.txt','w') as outfile:
            for team in teamList:
                teamDictList.append(team.dict)
            json.dump(teamDictList,outfile)
        with open('matches.txt','w') as outfile:
            for match in matchList:
                matchDictList.append(match.dict)
            json.dump(matchDictList,outfile)
    
    def commands(cmd):
        cmdarray = cmd.split()
        if(len(cmdarray) > 0):
            basecmd = cmdarray[0]
            if(basecmd == "matchReport"):
                print "Beginning Match Report"
                print ""
                print ""
                print ""
                enterTeams(enterMatch())
            elif(basecmd == "preScouting"):
                if(len(cmdarray) == 2):
                    if((int)(cmdarray[1]) > 0):
                        for num in range(0,(int)(cmdarray[1])):
                            enterPreData()
                    else:
                        print "Number of teams must be greater than 0."
                else:
                    print "preScouting takes exactly one parameter (numberOfTeamsEntering)"
            elif(basecmd == "help"):
                print "The available commands are:",
                for cmd in cmds:
                    print cmd,
                print ""
            elif(basecmd == "save"):
                print "matches.txt saved."
                print "teams.txt saved."
            elif(basecmd == "team"):
                if(len(cmdarray) == 2):
                    found = False
                    for team in teamList:
                        if(team.dict["number"] == cmdarray[1]):
                            found = True
                            print team.returnTeam()
                    if(cmdarray[1] == "all"):
                        for team in teamList:
                            print team.returnTeam()
                        found = True
                    if(not found):
                        print "Could not find team " + cmdarray[1] + "."
                else:
                    print "team takes exactly one parameter (teamName)"
            elif(basecmd == "match"):
                if(len(cmdarray) == 2):
                    found = False
                    for match in matchList:
                        if(match.dict["number"] == cmdarray[1]):
                            found = True
                            print match.returnMatch()
                    if(cmdarray[1] == "all"):
                        for match in matchList:
                            print match.returnMatch()
                        found = True
                    if(not found):
                        print "Could not find match #" + cmdarray[1] + "."
                else:
                    print "match takes exactly one parameter (matchNumber)"
            elif(basecmd == "editTeam"):
                for team in teamList:
                    if(team.dict["number"] == cmdarray[1]):
                        if(len(cmdarray) == 5):
                            if(len(team.dict[cmdarray[2]]) == 0):
                                team.dict[cmdarray[2]].append(cmdarray[4])
                            else:
                                team.dict[cmdarray[2]][cmdarray[3]] == cmdarray[4]
                        else:
                            team.dict[cmdarray[2]] = cmdarray[3]
            elif(basecmd == "radarPlot"):
                for team in teamList:
                    createRadarPlot(team)
                print "radar plots created"
            elif(basecmd == "makeSpreadsheet"):
                makeSpreadsheet()
            elif(basecmd == "readMatchFile"):
                if(len(cmdarray) == 2):
                    readMatchFile(cmdarray[1])
                else:
                    print "readMatchFile takes exactly one parameter (matchFile)"
            elif(basecmd == "runApp"):
                if(not readMatchFile(raw_input("Import which match file? "))):
                    save()
                    makeSpreadsheet()
                    for team in teamList:
                        createRadarPlot(team)
                    print "radar plots created"
            elif(basecmd == "multiPlot"):
                if(len(cmdarray) == 4):
                    team1 = Team("-1")
                    team2 = Team("-1")
                    team3 = Team("-1")
                    for team in teamList:
                        if(team.dict["number"] == cmdarray[1]):
                            team1 = team
                        elif(team.dict["number"] == cmdarray[2]):
                            team2 = team
                        elif(team.dict["number"] == cmdarray[3]):
                            team3 = team
                    createMultiPlot(team1,team2,team3)
                else:
                    print "multiPlot takes exactly 4 parameters (team1,team2,team3)"
            elif(basecmd == "barChart"):
                if(len(cmdarray) == 2):
                    if(cmdarray[1] == "auto"):
                        autoBarChart()
                    elif(cmdarray[1] == "tele"):
                        teleBarChart()
                    else:
                        print "barChart " + (str)(cmdarray[1]) + " is unknown."
                else:
                    print "barChart takes exactly 1 parameter (auto/tele)"
            elif(basecmd == "readPreFile"):
                if(len(cmdarray) == 2):
                    readPreScoutingFile(cmdarray[1])
                else:
                    print "readPreFile takes exactly 1 parameter (fileName)"
            else:
                print "Unknown command. Type 'help' for a list of valid commands."
            
        
    
    matchList = loadMatchesList("matches.txt")
    teamList = loadTeamsList("teams.txt")
    
    cmds = ["readPreFile","preScouting","help","save","readMatchFile","makeSpreadsheet","radarPlot","close","barChart"]
    while True:
        print "Enter a command."
        cmd = raw_input("")
        if (cmd == "devClose"):
            break
        print ""
        save()
        if (cmd == "close"):
            break
        commands(cmd)
        print ""
    
if __name__ == '__main__':
    runScoutingApp()

