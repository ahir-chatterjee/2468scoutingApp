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
    teamList = json.loads(teamStr)
    
    sheetDict = {}
    for teamDict in teamList:
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
                scalePer = round((float)(scaleCubes)/(float)((len(scaleList))),1)
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
                hangTime += hang
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
                assistStr = "Success"
                assists += 1
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
            if(scaleCubes != 0):
                scalePer = (round((float)(scalePer)/(float)(scaleCubes),2)*100)
                scaleTime = (round((float)(scaleTime)/(float)(scaleCubes),1))
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
            preScoutStr += "Claimed assist: " + (str)(teamDict["preAssist"])
            sheet.write(r,13,preScoutStr)

    sheet = writebook.add_sheet("best",cell_overwrite_ok=True)
    sheetDict["best"] = sheet
    sheet.write(0,0,"Best Teams")
    sheet.write(0,1,"Rank")
    sheet.write(1,1,"1st")
    sheet.write(2,1,"2nd")
    sheet.write(3,1,"3rd")
    sheet.write(0,2,"Auto Cubes")
    sheet.write(0,3,"Most Switch Cubes")
    sheet.write(0,4,"Most Scale Cubes")
    sheet.write(0,5,"Fastest Hang")
    sheet.write(0,6,"Best Assistance")
    sheet.write(0,7,"Most Vault Cubes")
    autoCubes = []
    switchCubes = []
    scaleCubes = []
    hangs = []
    assistances = []
    vaults = []
    for teamDict in teamList:
        teamNum = teamDict["number"]
        aCubes = 0
        for num in teamDict["autoSwitch"]:
            aCubes += (int)(num)
        for num in teamDict["autoScale"]:
            aCubes += (int)(num)
        autoCubes.append([teamNum,aCubes])
        teleSwitch = 0
        for num in teamDict["teleSwitch"]:
            teleSwitch += (int)(num)
        for num in teamDict["teleOppSwitch"]:
            teleSwitch += (int)(num)
        switchCubes.append([teamNum,teleSwitch])
        teleScale = 0
        if(len(teamDict["teleScale"]) != 0):
            for match in teamDict["teleScale"]:
                for delivery in match:
                    if((int)(delivery[1]) == 1):
                       teleScale += 1
        scaleCubes.append([teamNum,teleScale])
        hCount = 0
        for hang in teamDict["hang"]:
            if((int)(hang) > 0):
                hCount += 1
        hangs.append([teamNum,hCount])
        assistance = 0
        for assist in teamDict["assistance"]:
            if(assist == 1):
                assist += 1
        assistances.append([teamNum,assistance])
        vaultCubes = 0
        for num in teamDict["vaultBlocks"]:
            vaultCubes += (int)(num)
        vaults.append([teamNum,vaultCubes])
    first = ["",0]
    second = ["",0]
    third = ["",0]
    for teamList in autoCubes:
        if(teamList[1] > first[1]):
            third = second
            second = first
            first = teamList
        elif(teamList[1] > second[1]):
            third = second
            second = teamList[1]
        elif(teamList[1] > third[1]):
            third = teamList[1]
    sheet.write(1,2,first[0])
    sheet.write(2,2,second[0])
    sheet.write(3,2,third[0])
    first = ["",0]
    second = ["",0]
    third = ["",0]
    for teamList in switchCubes:
        if(teamList[1] > first[1]):
            third = second
            second = first
            first = teamList
        elif(teamList[1] > second[1]):
            third = second
            second = teamList
        elif(teamList[1] > third[1]):
            third = teamList
    sheet.write(1,3,first[0])
    sheet.write(2,3,second[0])
    sheet.write(3,3,third[0])
    first = ["",0]
    second = ["",0]
    third = ["",0]
    for teamList in scaleCubes:
        if(teamList[1] > first[1]):
            third = second
            second = first
            first = teamList
        elif(teamList[1] > second[1]):
            third = second
            second = teamList
        elif(teamList[1] > third[1]):
            third = teamList[1]
    sheet.write(1,4,first[0])
    sheet.write(2,4,second[0])
    sheet.write(3,4,third[0])
    first = ["",0]
    second = ["",0]
    third = ["",0]
    for teamList in hangs:
        if(teamList[1] > first[1]):
            third = second
            second = first
            first = teamList
        elif(teamList[1] > second[1]):
            third = second
            second = teamList
        elif(teamList[1] > third[1]):
            third = teamList
    sheet.write(1,5,first[0])
    sheet.write(2,5,second[0])
    sheet.write(3,5,third[0])
    first = ["",0]
    second = ["",0]
    third = ["",0]
    for teamList in assistances:
        if(teamList[1] > first[1]):
            third = second
            second = first
            first = teamList
        elif(teamList[1] > second[1]):
            third = second
            second = teamList
        elif(teamList[1] > third[1]):
            third = teamList
    sheet.write(1,6,first[0])
    sheet.write(2,6,second[0])
    sheet.write(3,6,third[0])
    first = ["",0]
    second = ["",0]
    third = ["",0]
    for teamList in vaults:
        if(teamList[1] > first[1]):
            third = second
            second = first
            first = teamList
        elif(teamList[1] > second[1]):
            third = second
            second = teamList
        elif(teamList[1] > third[1]):
            third = teamList
    sheet.write(1,7,first[0])
    sheet.write(2,7,second[0])
    sheet.write(3,7,third[0])
    
    for key in sheetDict:
        if(key == "best"):
            sheetDict[key].col(0).width = 2750
            sheetDict[key].col(1).width = 1500
            sheetDict[key].col(2).width = 3000
            sheetDict[key].col(3).width = 4500
            sheetDict[key].col(4).width = 4500
            sheetDict[key].col(5).width = 3500
            sheetDict[key].col(6).width = 4000
            sheetDict[key].col(7).width = 4500
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
            sheetDict[key].col(9).width = 5000
            sheetDict[key].col(10).width = 2250
            sheetDict[key].col(11).width = 2500
            sheetDict[key].col(12).width = 3500
            sheetDict[key].col(13).width = 13250
        
    writebook.save("test" + ".xls")

if __name__== '__main__':
    makeSpreadsheet()
