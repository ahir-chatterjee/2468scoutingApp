import xlwt
import json

def makeSpreadsheet():
    writebook = xlwt.Workbook()
    matchFile = open("matches.txt",'r')
    teamFile = open("teams.txt",'r')
    matchStr = ""
    teamStr = ""
    matchList = []
    teamList = []
    for line in matchFile:
        matchStr += line
    matchList = json.loads(matchStr)
    for line in teamFile:
        teamStr += line
    allTeams = json.loads(teamStr)
    
    sheetDict = {}
    for teamDict in allTeams:
        teamNum = teamDict["number"]
        sheet = writebook.add_sheet(teamNum,cell_overwrite_ok=True)
        sheetDict[teamNum] = sheet
        sheet.write(0,0,teamNum)
        sheet.write(0,1,"Match")
        matches = 0
        sheet.write(0,2,"Auto Penalty")
        aPen = 0
        sheet.write(0,3,"Auto Line")
        aLine = 0
        sheet.write(0,4,"Auto Switch")
        aSwitch = 0
        sheet.write(0,5,"Auto Scale")
        aScale = 0
        sheet.write(0,6,"Starting Position")
        startPos = [0,0,0]
        sheet.write(0,7,"Tele Switch")
        switch = 0
        sheet.write(0,8,"Tele Opponent Switch")
        oppSwitch = 0
        sheet.write(0,9,"Tele Scale Info")
        scaleCubes = 0
        scaleTime = 0
        scalePer = 0
        sheet.write(0,10,"Hang Info")
        hangs = 0
        hangAttempts = 0
        hangTime = 0
        sheet.write(0,11,"Assistance")
        assists = 0
        assistAttempts = 0
        sheet.write(0,12,"Vault/Exchange")
        vault = 0
        sheet.write(0,13,"Additional Comments and Prescouting")
        r = 1
        c = 2
    
        for i in range(0,len(teamDict["matches"])):
            matches += 1
            sheet.write(r,1,teamDict["matches"][i])
            autoPenStr = ""
            autoPen = teamDict["autoPenalty"][i]
            if((int)(autoPen) == 0):
                autoPenStr = "None"
            elif((int)(autoPen) == 1):
                autoPenStr = "Received"
                aPen += 1
            else:
                autoPenStr = "???"
            sheet.write(r,2,autoPenStr)
            lineStr = ""
            line = teamDict["autoLine"][i]
            if((int)(line) == 0):
                lineStr = "Not crossed"
            elif((int)(line) == 1):
                lineStr = "Crossed"
                aLine += 1
            else:
                lineStr = "???"
            sheet.write(r,3,lineStr)
            aSwitch += (int)(teamDict["autoSwitch"][i])
            sheet.write(r,4,teamDict["autoSwitch"][i] + " cubes")
            aScale += (int)(teamDict["autoScale"][i])
            sheet.write(r,5,teamDict["autoScale"][i] + " cubes")
            startPosition = teamDict["startingPos"][i]
            if(startPosition == "left"):
                startPos[0] += 1
            elif(startPosition == "center"):
                startPos[1] += 1
            elif(startPosition == "right"):
                startPos[2] += 1
            sheet.write(r,6,startPosition)
            switch += (int)(teamDict["teleSwitch"][i])
            sheet.write(r,7,teamDict["teleSwitch"][i] + " cubes")
            oppSwitch += (int)(teamDict["teleOppSwitch"][i])
            sheet.write(r,8,teamDict["teleOppSwitch"][i] + " cubes")
            scaleStr = ""
            scaleList = teamDict["teleScale"][i]
            scaleCubes = 0
            for delivery in scaleList:
                scaleStr += (str)(delivery[0])
                scaleStr += "s, "
                if((int)(delivery[1]) == 1):
                    scaleStr += "success\n"
                    scaleTime += (int)(delivery[0])
                    scaleCubes += 1
                elif((int)(delivery[1]) == 0):
                    scaleStr += "fail\n"
                else:
                    scaleStr += "???\n"
            if(len(scaleList) != 0):
                scalePer = round((float)(scaleCubes)/(float)((len(scaleList))),3)
            else:
                scalePer = 0
            scaleStr += (str)(scaleCubes) + " cubes, " + (str)((scalePer)*100) + '%'
            sheet.write(r,9,scaleStr)
            hangStr = ""
            hang = teamDict["hang"][i]
            if((int)(hang) == -1):
                hangStr = "N/A"
            elif((int)(hang) == 0):
                hangStr = "Failed"
                hangAttempts += 1
            elif((int)(hang) >= 1):
                hangStr = "Hang took " + (str)(hang) + "s"
                hangs += 1
                hangTime += (int)(hang)
                hangAttempts += 1
            else:
                hangStr = "???"
            sheet.write(r,10,hangStr)
            assistStr = ""
            assist = teamDict["assistance"][i]
            if((int)(assist) == -1):
                assistStr = "N/A"
            elif((int)(assist) == 0):
                assistStr = "Failed"
                assistAttempts += 1
            elif((int)(assist) == 1):
                assistStr = "Success (One)"
                assists += 1
                assistAttempts += 1
            elif((int)(assist) == 2):
                assistStr = "Success (Two)"
                assists += 2
                assistAttempts += 1
            else:
                assistStr = "???"
            sheet.write(r,11,assistStr)
            vault += (int)(teamDict["vaultBlocks"][i])
            sheet.write(r,12,teamDict["vaultBlocks"][i] + " cubes")
            sheet.write(r,13,teamDict["comments"][i])
            r += 1
    
        if(matches > 0):
            sheet.write(r,1,"AVG")
            sheet.write(r,2,(str)((round((float)(aPen)/(float)(matches),2))*100) + "%")
            sheet.write(r,3,(str)((round((float)(aLine)/(float)(matches),2))*100) + "%")
            sheet.write(r,4,(str)(round((float)(aSwitch)/(float)(matches),1)) + " cubes")
            sheet.write(r,5,(str)(round((float)(aScale)/(float)(matches),1)) + " cubes")
            posStr = ""
            if(startPos[0] > startPos[1] and startPos[0] > startPos[2]):
                posStr = "left pref"
            elif(startPos[1] > startPos[0] and startPos[1] > startPos[2]):
                posStr = "center pref"
            elif(startPos[2] > startPos[0] and startPos[2] > startPos[1]):
                posStr = "right pref"
            else:
                posStr = "no pref"
            sheet.write(r,6,posStr)
            sheet.write(r,7,(str)(round((float)(switch)/(float)(matches),1)) + " cubes")
            sheet.write(r,8,(str)(round((float)(oppSwitch)/(float)(matches),1)) + " cubes")
            deliveries = 0
            scaleCubes = 0
            scaleTime = 0
            for match in teamDict["teleScale"]:
                for delivery in match:
                    deliveries += 1
                    scaleTime += (int)(delivery[0])
                    if((int)(delivery[1]) == 1):
                        scaleCubes += 1
            if(scaleCubes != 0):
                scalePer = (round((float)(scaleCubes)/(float)(deliveries),3)*100)
                scaleTime = (round((float)(scaleTime)/(float)(deliveries),2))
            else:
                scalePer = 0
            sheet.write(r,9,(str)(scaleTime) + "s, " + (str)(round((float)(scaleCubes)/(float)(matches),1)) + " cubes" +
                        ", " + (str)(scalePer) + "%")
            if(hangAttempts == 0):
                sheet.write(r,10,"N/A")
            else:
                sheet.write(r,10,(str)((round((float)(hangs)/(float)(hangAttempts),2))*100) + "%, " + (str)(round((float)(hangTime)/(float)(hangAttempts),1)) + "s")
                            
            if(assistAttempts == 0):
                sheet.write(r,11,"N/A")
            else:
                sheet.write(r,11,(str)((round((float)(assists)/(float)(assistAttempts),2))*100) + "%")
            sheet.write(r,12,(str)(round((float)(vault)/(float)(matches),1)) + " cubes")
            r += 1

        if(teamDict["wheels"] != 0):
            preScoutStr = ""
            preScoutStr += (str)(teamDict["cims"]) + " cims and " + (str)(teamDict["wheels"]) + " wheels\n"
            preScoutStr += (str)(teamDict["drivetrain"]) + " drivebase\n"
            preScoutStr += "Weighs " + (str)(teamDict["weight"]) + " lbs\n"
            preScoutStr += "Programs in " + (str)(teamDict["language"]) + '\n'
            preScoutStr += "Claimed auto: " + (str)(teamDict["preAuto"]) + '\n'
            preScoutStr += "Tele Strategy: " + (str)(teamDict["preTele"]) + '\n'
            preScoutStr += "Claimed hang: " + (str)(teamDict["preHang"]) + '\n'
            preScoutStr += "Claimed assist: " + (str)(teamDict["preAssist"]) + '\n'
            preScoutStr += (str)(teamDict["preScoutComments"])
            sheet.write(r,13,preScoutStr)

    sheet = writebook.add_sheet("best",cell_overwrite_ok=True)
    sheetDict["best"] = sheet
    sheet.write(0,0,"Best Teams")
    sheet.write(0,1,"Auto Switch Cubes")
    sheet.write(0,2,"Auto Scale Cubes")
    sheet.write(0,3,"Most Switch Cubes")
    sheet.write(0,4,"Most oppSwitch Cubes")
    sheet.write(0,5,"Most Scale Cubes")
    sheet.write(0,6,"Most Hangs")
    sheet.write(0,7,"Most Assists")
    sheet.write(0,8,"Most Vault Cubes")
    sheet.write(0,9,"Objective Rankings")
    autoSwitch = []
    autoScale = []
    teleSwitch = []
    oppSwitch = []
    scaleCubes = []
    hangs = []
    assistances = []
    vaults = []
    for teamDict in allTeams:
        teamNum = teamDict["number"]
        sw = 0
        sc = 0
        for num in teamDict["autoSwitch"]:
            sw += (int)(num)
        for num in teamDict["autoScale"]:
            sc += (int)(num)
        autoSwitch.append([teamNum,sw])
        autoScale.append([teamNum,sc])
        teleSw = 0
        oppSw = 0
        for num in teamDict["teleSwitch"]:
            teleSw += (int)(num)
        for num in teamDict["teleOppSwitch"]:
            oppSw += (int)(num)
        teleSwitch.append([teamNum,teleSw])
        oppSwitch.append([teamNum,oppSw])
        teleScale = 0
        deliveries = 0
        if(len(teamDict["teleScale"]) != 0):
            for match in teamDict["teleScale"]:
                for delivery in match:
                    if((int)(delivery[1]) == 1):
                       teleScale += 1
                    deliveries += 1
        if(deliveries == 0):
            deliveries = 1
        scaleCubes.append([teamNum,teleScale,round((float)(teleScale)/(float)(deliveries),3)*100])
        hCount = 0
        hAttempts = 0
        hTime = 0
        for hang in teamDict["hang"]:
            if((int)(hang) > 0):
                hCount += 1
                hTime += (int)(hang)
                hAttempts += 1
            elif((int)(hang) == 0):
                hAttempts += 1
        if(hCount == 0):
            hCount += 1
        if(hAttempts == 0):
            hAttempts = 1
        hangs.append([teamNum,hCount-1,round((float)(hTime)/(float)(hCount)),round((float)(hCount)/(float)(hAttempts),4)*100])
        assistance = 0
        for assist in teamDict["assistance"]:
            if((int)(assist) > 0):
                assistance += (int)(assist)
        assistances.append([teamNum,assistance])
        vaultCubes = 0
        for num in teamDict["vaultBlocks"]:
            vaultCubes += (int)(num)
        vaults.append([teamNum,vaultCubes])
        
    #autoSwitch
    ordering = []
    for i in range(0,100):
        ordering.append(["",0])
    for teamList in autoSwitch:
        done = False
        for i in range(0,len(ordering)):
            if(teamList[1] > ordering[i][1] and not done):
                done = True
                replacer = teamList
                temp = []
                for j in range(i,len(ordering)-1):
                    temp = ordering[j]
                    ordering[j] = replacer
                    replacer = temp
    for i in range(0,len(ordering)):
        if((str)(ordering[i][0]) != ""):
            sheet.write(i+1,1,ordering[i][0] + " (" + (str)(ordering[i][1]) + ")")

    #autoScale
    ordering = []
    for i in range(0,100):
        ordering.append(["",0])
    for teamList in autoScale:
        done = False
        for i in range(0,len(ordering)):
            if(teamList[1] > ordering[i][1] and not done):
                done = True
                replacer = teamList
                temp = []
                for j in range(i,len(ordering)-1):
                    temp = ordering[j]
                    ordering[j] = replacer
                    replacer = temp
    for i in range(0,len(ordering)):
        if((str)(ordering[i][0]) != ""):
            sheet.write(i+1,2,ordering[i][0] + " (" + (str)(ordering[i][1]) + ")")

    #switch
    ordering = []
    for i in range(0,100):
        ordering.append(["",0])
    for teamList in teleSwitch:
        done = False
        for i in range(0,len(ordering)):
            if(teamList[1] > ordering[i][1] and not done):
                done = True
                replacer = teamList
                temp = []
                for j in range(i,len(ordering)-1):
                    temp = ordering[j]
                    ordering[j] = replacer
                    replacer = temp
    for i in range(0,len(ordering)):
        if((str)(ordering[i][0]) != ""):
            sheet.write(i+1,3,ordering[i][0] + " (" + (str)(ordering[i][1]) + ")")

    #oppSwitch
    ordering = []
    for i in range(0,100):
        ordering.append(["",0])
    for teamList in oppSwitch:
        done = False
        for i in range(0,len(ordering)):
            if(teamList[1] > ordering[i][1] and not done):
                done = True
                replacer = teamList
                temp = []
                for j in range(i,len(ordering)-1):
                    temp = ordering[j]
                    ordering[j] = replacer
                    replacer = temp
    for i in range(0,len(ordering)):
        if((str)(ordering[i][0]) != ""):
            sheet.write(i+1,4,ordering[i][0] + " (" + (str)(ordering[i][1]) + ")")
            
    #scale
    ordering = []
    for i in range(0,100):
        ordering.append(["",0,0.0])
    for teamList in scaleCubes:
        done = False
        for i in range(0,len(ordering)):
            if((teamList[1]*teamList[2]) > (ordering[i][1]*ordering[i][2]) and not done):
                done = True
                replacer = teamList
                temp = []
                for j in range(i,len(ordering)-1):
                    temp = ordering[j]
                    ordering[j] = replacer
                    replacer = temp
    for i in range(0,len(ordering)):
        if((str)(ordering[i][0]) != ""):
            sheet.write(i+1,5,ordering[i][0] + " (" + (str)(ordering[i][1]) + ", " + (str)(ordering[i][2]) + "%)")
    
    #hangs
    ordering = []
    for i in range(0,100):
        ordering.append(["",0])
    for teamList in hangs:
        done = False
        for i in range(0,len(ordering)):
            if(teamList[1] > ordering[i][1] and not done):
                done = True
                replacer = teamList
                temp = []
                for j in range(i,len(ordering)-1):
                    temp = ordering[j]
                    ordering[j] = replacer
                    replacer = temp
    for i in range(0,len(ordering)):
        if((str)(ordering[i][0]) != ""):
            sheet.write(i+1,6,ordering[i][0] + " (" + (str)(ordering[i][1]) + ", " + (str)(ordering[i][2]) + "s, " + (str)(ordering[i][3]) + "%)")

    #assistance
    ordering = []
    for i in range(0,100):
        ordering.append(["",0])
    for teamList in assistances:
        done = False
        for i in range(0,len(ordering)):
            if(teamList[1] > ordering[i][1] and not done):
                done = True
                replacer = teamList
                temp = []
                for j in range(i,len(ordering)-1):
                    temp = ordering[j]
                    ordering[j] = replacer
                    replacer = temp
    for i in range(0,len(ordering)):
        if((str)(ordering[i][0]) != ""):
            sheet.write(i+1,7,ordering[i][0] + " (" + (str)(ordering[i][1]) + ")")

    #vaults
    ordering = []
    for i in range(0,100):
        ordering.append(["",0])
    for teamList in vaults:
        done = False
        for i in range(0,len(ordering)):
            if(teamList[1] > ordering[i][1] and not done):
                done = True
                replacer = teamList
                temp = []
                for j in range(i,len(ordering)-1):
                    temp = ordering[j]
                    ordering[j] = replacer
                    replacer = temp
    for i in range(0,len(ordering)):
        if((str)(ordering[i][0]) != ""):
            sheet.write(i+1,8,ordering[i][0] + " (" + (str)(ordering[i][1]) + ")")

    
    '''
    '''
    #rankings
    ordering = []
    for i in range(0,100):
        ordering.append(["",0])
    for teamDict in allTeams:
        teamNum = teamDict["number"]
        rank = 0.0
        #current system
        for team in autoSwitch:
            if((str)(team[0]) == (str)(teamNum)):
                rank += (float)(team[1]*2)
        for team in autoScale:
            if((str)(team[0]) == (str)(teamNum)):
                rank += (float)(team[1]*6)
        for team in teleSwitch:
            if((str)(team[0]) == (str)(teamNum)):
                rank += (float)(team[1]*1.2)
        for team in oppSwitch:
            if((str)(team[0]) == (str)(teamNum)):
                rank += (float)(team[1]*1.2)
        for team in scaleCubes:
            if((str)(team[0]) == (str)(teamNum)):
                rank += (float)(team[1]*3)
        for team in hangs:
            if((str)(team[0]) == (str)(teamNum)):
                rank += (float)(team[1]*4)
        for team in assistances:
            if((str)(team[0]) == (str)(teamNum)):
                rank += (float)(team[1]*4)
        for team in vaults:
            if((str)(team[0]) == (str)(teamNum)):
                rank += (float)(team[1]*1)
        '''
        for team in autoSwitch:
            if((str)(team[0]) == (str)(teamNum)):
                rank += (float)(team[1]*2)
        for team in autoScale:
            if((str)(team[0]) == (str)(teamNum) and len(team) > 2):
                rank += (float)(team[1]*((float)(team[2])/100.0)*8)
        for team in teleSwitch:
            if((str)(team[0]) == (str)(teamNum)):
                rank += (float)(team[1]*1)
        for team in oppSwitch:
            if((str)(team[0]) == (str)(teamNum)):
                rank += (float)(team[1]*1)
        for team in scaleCubes:
            if((str)(team[0]) == (str)(teamNum)):
                rank += (float)(team[1]*5)
        for team in hangs:
            if((str)(team[0]) == (str)(teamNum)):
                rank += (float)(team[1]*4)
        for team in assistances:
            if((str)(team[0]) == (str)(teamNum)):
                rank += (float)(team[1]*4)
        for team in vaults:
            if((str)(team[0]) == (str)(teamNum)):
                rank += (float)(team[1]*1)
        '''
        done = False
        for i in range(0,len(ordering)):
            if(rank > ordering[i][1] and not done):
                done = True
                replacer = [teamNum,rank]
                temp = []
                for j in range(i,len(ordering)-1):
                    temp = ordering[j]
                    ordering[j] = replacer
                    replacer = temp
    for i in range(0,len(ordering)):
        if((str)(ordering[i][0]) != ""):
            sheet.write(i+1,9,(str)(ordering[i][0]) + " (" + (str)(round((ordering[i][1]),1)) + ")")
    
    for key in sheetDict:
        if(key == "best"):
            sheetDict[key].col(0).width = 2750
            sheetDict[key].col(1).width = 5000
            sheetDict[key].col(2).width = 5000
            sheetDict[key].col(3).width = 5000
            sheetDict[key].col(4).width = 5000
            sheetDict[key].col(5).width = 5000
            sheetDict[key].col(6).width = 5500
            sheetDict[key].col(7).width = 5000
            sheetDict[key].col(8).width = 5000
            sheetDict[key].col(9).width = 5000
        else:
            sheetDict[key].col(0).width = 1250
            sheetDict[key].col(1).width = 1500
            sheetDict[key].col(2).width = 2750
            sheetDict[key].col(3).width = 2750
            sheetDict[key].col(4).width = 2750
            sheetDict[key].col(5).width = 2500
            sheetDict[key].col(6).width = 3500
            sheetDict[key].col(7).width = 2750
            sheetDict[key].col(8).width = 4750
            sheetDict[key].col(9).width = 5500
            sheetDict[key].col(10).width = 3250
            sheetDict[key].col(11).width = 2500
            sheetDict[key].col(12).width = 3500
            sheetDict[key].col(13).width = 13250
        
    writebook.save("utah" + ".xls")
    print "done"

if __name__== '__main__':
    makeSpreadsheet()
