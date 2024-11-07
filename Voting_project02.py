
#
#     Program: Voting Counties USA Buggs Bunny vs. Road Runner
#
#     By: Paige E. McCullough, Sabrina Abdukadirova and Yuri Dourado
#
#     Date: October 31, 2024
#
#     Work Done: Sabrina Abdukadirova- Calculated Sum of votes of each state, matched the state name with state id,
#     calculated count of county,did the Electoral Votes for Road Runner and Buggs Bunny, and Created and organized the graph
#     Paige-
#     Yuri -
# Update 2.0, changes made by Yuri Dourado. Modulirizing, and cleaning up code.


#Imports section

import csv
from collections import defaultdict

from collections import OrderedDict

from datetime import *

import ExtraFunctions as ef






#####
# Creates variable for the input file.
voting_counites = 'VotingCountiesFixed.csv'

# Initializes a variable to hold the total votes.
state_totals = defaultdict(lambda: {'RR': 0, 'BB': 0})
# Counts the total votes of each state
stateVotes = defaultdict(int)
# Counts the number of counties in each state
countyCount = defaultdict(int)
# Dictionary to match state ID to state Name
state_abbr = {}

# Geografic location
# geograficLocations = {}
masterDict = {}
    
# Innitializes the variable to add all the votes
totalPopVotes = 0

# Total Counties
totalCounties = 0
# Opens the file and read the data
with open(voting_counites, 'r') as data:
    Counties_file = list(csv.reader(data))
    header = Counties_file.pop(0) # Skip the first row with titles in VotingCounties!.csv

    # Dictionary with the state and electoral counts
    votes = {
        'AL': 9, 'AK': 3, 'AZ': 11, 'AR': 6, 'CA': 54,
        'CO': 10, 'CT': 7, 'DE': 3, 'DC': 3, 'FL': 30, 'GA': 16,
        'HI': 4, 'ID': 4, 'IL': 19, 'IN': 11, 'IA': 6,
        'KS': 6, 'KY': 8, 'LA': 8, 'ME': 4, 'MD': 10,
        'MA': 11, 'MI': 15, 'MN': 10, 'MS': 6,
        'MO': 10, 'MT': 4, 'NE': 5, 'NV': 6, 'NH': 4,
        'NJ': 14, 'NM': 5, 'NY': 28, 'NC': 16,
        'ND': 3, 'OH': 17, 'OK': 7, 'OR': 8, 'PA': 19,
        'RI': 4, 'SC': 9, 'SD': 3, 'TN': 11,
        'TX': 40, 'UT': 6, 'VT': 3, 'VA': 13, 'WA': 12,
        'WV': 4, 'WI': 10, 'WY': 3
    }
    for line in Counties_file:
        if line[13].isdigit() and line[14].isdigit():  # .isdigit() does the same thing as lines 18 & 19

            # Based on the index from line, pulls the data and assigns it to a variable for the loop
            county = line[0].replace(',', '') 
            
            state_id = line[3].replace(',', '')  
            
            value_RR = int(line[13].replace(',', '')) 
            
            value_BB = int(line[14].replace(',', '')) 
            
            county_votes = int(line[12].replace(',', ''))
            
            state_name = line[4].replace(',', '')

            lat = float(line[6].replace(',', ''))

            lng = float(line[7].replace(',', ''))


            # Updates the total for each state.
            state_totals[state_id]['RR'] += value_RR
            state_totals[state_id]['BB'] += value_BB
            # Adds all votes toghether
            totalPopVotes += value_BB
            totalPopVotes += value_RR
            # Adds the county's total votes to calculate state's total of votes
            stateVotes[state_id] += county_votes
            # Counts county per state
            countyCount[state_id] += 1
            # Counts all the counties
            totalCounties += 1

            # Finds state abbreviation to full state name
            state_abbr[state_id] = state_name


            #Combine date and time into one variable
            dateTimeIn = ef.addTimeAndDate(line[15], line[16])
        
            #Creates a dictionary for each county, and subvalues of state, state name, time, votes and geographic location
            masterDict[county] = [state_id,state_name, dateTimeIn, value_RR, value_BB, lat, lng]

# Initializes variables to keep track of the total votes for each candidate.
total_RR = 0 
total_BB = 0
# Tracks the total electoral votes for each candidate.
electoral_RR = 0
electoral_BB = 0

def determineWinner(dictIn):
    for state, totals in dictIn.items():
        state_total_votes = totals['RR'] + totals['BB']  # Calculates the total votes.
        if state_total_votes > 0:
            RR_percent = "{:.2f}%".format(100 * totals['RR'] / state_total_votes)  # Calculates percentages for RR
            BB_percent = "{:.2f}%".format(100 * totals['BB'] / state_total_votes)  # Calculates percentages for BB


            # This checks to see if value for abbreviation matches state name.
            state_name = state_abbr.get(state, state)


            # Based on percent checks to see who the winner is
            RR_win = RR_percent > BB_percent
            BB_win = BB_percent > RR_percent
            # This initializes the variables to -
            RR_electoral = '-'
            BB_electoral = '-'

        if RR_win:
            RR_electoral = votes[state] # if RR wins it gets assigned the electoral votes for that state
            total_RR += totals['RR'] # Keeps track of RR votes in the states
            electoral_RR += votes[state]  # adds the electoral votes to total
        elif BB_win:
            BB_electoral = votes[state]# Same as top information except for BB
            total_BB += totals['BB']
            electoral_BB += votes[state]

                # print(f'Total Votes in {state}: {count_votes}')
        print(f"{state_name:<20}  {state:>6}  {stateVotes[state]:>20} {totals['RR']:>20}  {totals['BB']:>21} {countyCount[state]: >20}  {RR_percent: >22} {BB_percent:>22} {RR_electoral:>20} {BB_electoral:>20}")

# determineWinner(state_totals)

temp_state_winner = defaultdict(lambda: {'RR': 0, 'BB': 0})
def askForTime():
    time = input("Please enter the time in the format \"HH:MM:SS\": ")
    date = input("Please enter the date in the format \"MM/DD/YYYY\": ")
    newDate = ef.addTimeAndDate(date, time)
    print(newDate)
    sortedMasterDict = ef.sortTimeAndDate(masterDict)
    for key, val in sortedMasterDict.items():
        if val[2] <= newDate:
            # determineWinner()
            temp_state_winner[val[0]]['RR'] += val[3]
            temp_state_winner[val[0]]['BB'] += val[4]

    
            # print(f"County: {key} State: {val[0]} Time: {val[2]} Votes RR: {val[3]} Votes BB: {val[4]}")
    # determineWinner(temp_state_winner)

askForTime()


## At the asked time, determine the winner using the temp_state_winner dictionary

print("Popular votes winner: ",ef.popularVotesWinner(temp_state_winner))

# Same, but for electoral votes
print(ef.electoralVotesWinner(temp_state_winner))



# Printing the headers for the chart
def printHeaders():
    print(f"{'Values': >60} {'Percent of State Votes': >100}  {'Electoral Votes': >40}")
    print(f"{'---------------': >65}{'-------------------------': >97} {'---------------------': >42}")
    print(f"{'state Name': <20} | {'State ID':<5} | {'Sum of Votes':>18} | {'Sum of RR Values':>20} |"
        f" {'Sum of BB Values':>19} |{'Count of county': >22} |{'RR Percent':>17} | {'BB Percent':>20} | {'Road Runner': >20} | {'Buggs Bunny': >17}")

# for state, totals in sorted(state_totals.items())


def percentTotal():
    percent_total = (100 * total_RR) / (total_RR + total_BB)  # Calculates percentage for overall winner.
    return percent_total

# Determines winner of the popular vote.
def determinePopVoteWinner():
    if total_RR > total_BB:   
        overall_winner = 'RR'
        overall_votes = total_RR
    elif total_BB > total_RR:
        overall_winner = 'BB'
        overall_votes = total_BB

# Prints the Electoral votes Grand total
def printGrandTotal():
    print(f"{'Grand Total':<20} {'':>8} {totalPopVotes:>20} {total_RR:>20} {total_BB:>22} {totalCounties:>20} {"{:.2f}%".format(percent_total):>23} {"{:.2f}%".format(100-percent_total):>22} {electoral_RR:>20} {electoral_BB:>20}")
