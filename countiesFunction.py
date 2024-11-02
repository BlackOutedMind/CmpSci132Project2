countiesFunction


#Print what dir the program is located and reading from
print("Location is:", os.getcwd())



#Set Variable Names from the file:
county = 0
county_full = 1
county_fips = 2
state_id = 3
state_name = 4
Return_Time = 5
lat = 6
lng = 7
population = 8 
percentage_State_Population = 9
factor = 10
VoteCast = 11
Votes = 12
RR_Votes = 13
BB_Votes = 14
Return_Date = 15
Return_Time = 16
LastVar = 17
##This variable is weird, but it exists.
# 0.000277778

#Open the File so it can be imported
# countiesFile = open('Voting-Counties.csv')
countiesFile = open('Projects/CmpSci132Project2/Voting-Counties.csv', 'r')
line = countiesFile.readline()
lineList = line.split(",")

print(line)
print(lineList)

CountiesDict = {}
pos = 0
#Create a list with the desired informations
while lineList[county] != "END":
    line = countiesFile.readline()
    lineList = line.split(",")
    if lineList[county] != "END":
        lineList[Return_Time] = lineList[Return_Time].split('\n')[0]

        county = lineList[county]
        county_full = lineList[county_full]
        county_fips = int(lineList[county_fips])
        state_id = lineList[state_id]
        state_name = lineList[state_name]
        Return_Time = lineList[Return_Time]
        lat = float(lineList[lat])
        lng = float(lineList[lng])
        population = int(lineList[population])
        percentage_State_Population = lineList[percentage_State_Population]
        factor = lineList[factor]
        VoteCast = float(lineList[VoteCast])
        votes = lineList[Votes]
        RR_Votes = int(lineList[RR_Votes])
        BB_Votes = int(lineList[BB_Votes])
        Return_Date = str(lineList[Return_Date])
        Return_Time = str(lineList[Return_Time])
        CountiesDict[pos] = [lineList[county], lineList[county_full], lineList[county_fips], lineList[state_id], lineList[state_name], lineList[Return_Time], lineList[lat], lineList[lng], lineList[population], lineList[percentage_State_Population], lineList[factor], lineList[VoteCast], lineList[Votes], lineList[RR_Votes], lineList[BB_Votes], lineList[Return_Date], lineList[Return_Time], lineList[LastVar]] 
        pos += 1
    else:
        pos = 0
        break

def countVotes():
    totalVotes = 0
    for i in range(len(CountiesDict)):
        totalVotes += int(CountiesDict[i][Votes])
    return totalVotes

print(countVotes())