import json

file = open("/home/kmk/HashCode2022/input_data/a_an_example.in.txt","r")

# print(file.readlines())

d = {}
data = file.readlines()
C, P = map( int, data[0].split())
totalN = len( data)

print( C, P)
d["noOfContibutors"] =  C
d["noOfProjects"] = P
d["contributors"] = {}

totalLinesTillNow = 1

for x in range (1,C+1):
    # d["contributors"]
    thecontributordict = {}
    
    eachContributorInfo = data[totalLinesTillNow].split()
    
    thecontributordict[eachContributorInfo[0]] = {}
    thecontributordict[eachContributorInfo[0]]["noOfSkills"] = int(eachContributorInfo[1])
    thecontributordict[eachContributorInfo[0]]["skills"] = {}
    print( thecontributordict)
    totalLinesTillNow += 1
    print( totalLinesTillNow)
    noOfSkills = thecontributordict[eachContributorInfo[0]]["noOfSkills"]
    for eachSkillInfo in range( noOfSkills):
        # print( totalLinesTillNow)
        temp = data[eachSkillInfo+totalLinesTillNow].split()
        thecontributordict[eachContributorInfo[0]]["skills"][temp[0]] = temp[1]
        # print( thecontributordict)
        
    totalLinesTillNow += noOfSkills
        
    
    d["contributors"].update( thecontributordict)

    
# print( d)
totalLinesTillNowPART2 = totalLinesTillNow
d["projects"] = {}

# for x in range ( totalLinesTillNow,totalN):
while totalLinesTillNowPART2 < totalN:
    print(totalLinesTillNowPART2)
    temp = data[totalLinesTillNowPART2].split()
    projName = temp[0]
    noOfDays = int( temp[1])
    scoreAwarded = int( temp[2])
    bestBefore = int( temp[3])
    noOfRoles = int( temp[4])
    
    d["projects"][projName] = {}
    d["projects"][projName]["noOfDays"] = noOfDays
    d["projects"][projName]["scoreAwarded"] = scoreAwarded
    d["projects"][projName]["bestBefore"] = bestBefore
    d["projects"][projName]["noOfRoles"] = noOfRoles
    d["projects"][projName]["skills"] = {}
    totalLinesTillNowPART2 += 1
    
    for each in range ( noOfRoles):
        if totalLinesTillNowPART2+each < totalN:
            temp2 = data[totalLinesTillNowPART2+each].split()
            d["projects"][projName]["skills"][temp2[0]] = int( temp2[1])
    totalLinesTillNowPART2 += noOfRoles
        
print( d)


    
with open("dataexample.json", "w") as outfile:
    json.dump(d, outfile)