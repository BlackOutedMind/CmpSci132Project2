##############################################################################################################
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



import csv

import collections

from datetime import *

import ExtraFunctions as ef

import matplotlib.pyplot as plt


### define main varibales and needs


stateDictionary = {}

countyDictionary = {}

electoral_Votes = {
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

totalPopVotes = 0

voting_counites = 'VotingCountiesFixed.csv'


total_RR = 0
total_BB = 0

electoral_RR = 0
electoral_BB = 0
totalCounties = 0

# Read the file and adress them to the right dictionary
def fileReader():

    global totalPopVotes, total_RR, total_BB, totalCounties, electoral_RR, electoral_BB
    countyquantity = 1


    with open(voting_counites, 'r') as data:

        #
        counties_file =  list(csv.reader(data))

        # remove the header
        header = counties_file.pop(0)

        for line in counties_file:
            # Appropriate what each line represents

            # Separate county information
            county = line[0].replace(",", "")
            county_FullName = line[1].replace(",", "")

            county_latitute = line[6]
            county_longitude = line[7]

            county_population = line[8]
            county_votes = line[12]

            # Count the total number of counties
            totalCounties += 1

            # Separate state information
            stateID = line[3]
            state_Name = line[4]

            # Separate votes information
            county_votes = int(line[12])
            votes_RR = int(line[13])
            votes_BB = int(line[14])

            totalPopVotes += county_votes

            # Count the total votes for each candidate
            total_RR += votes_RR
            total_BB += votes_BB


            # Merge date and time into one variable
            date_entry = line[15]
            time_entry = line[16]

            dateAndTime = ef.addTimeAndDate(date_entry, time_entry)


            # Add information to the dictionaries
            countyDictionary[county] = {'County Fullname':county_FullName, 
                                        'StateID':stateID, 
                                        'RR':votes_RR, 
                                        'BB':votes_BB, 
                                        'Date and Time': dateAndTime, 
                                        'County Votes': county_votes, 
                                        'Latitude': county_latitute, 
                                        'Longitude': county_longitude, 
                                        'Population': county_population
                                        }

            # Add the state to the state dictionary
            if stateID not in stateDictionary:
                stateDictionary[stateID] = {'RR': votes_RR, 
                                            'BB': votes_BB, 
                                            'Total': county_votes, 
                                            'County Quantity': countyquantity, 
                                            'State Last Vote': dateAndTime, 
                                            'State Name': state_Name, 
                                            'Pop Vote Winner': 0,
                                            'Electoral Votes Awards': electoral_Votes[stateID],
                                            'Electoral Votes Winner BB': 0,
                                            'Electoral Votes Winner RR': 0
                                            }
                # Adds to state last county to upload votes (This function is kinda useless, but it's here for safety measures)
                if dateAndTime > stateDictionary[stateID]['State Last Vote']:
                    stateDictionary[stateID]['State Last Vote'] = dateAndTime
            
            # Summs votes per state
            else:
                stateDictionary[stateID]['RR'] += votes_RR
                stateDictionary[stateID]['BB'] += votes_BB
                stateDictionary[stateID]['Total'] += county_votes
                stateDictionary[stateID]['County Quantity'] += countyquantity


# create a dictionary with the states that all the counties have been uploaded by the time requested
tempDict = {}

# Ask user for Time and Date and determine the winner of each state at that time
def askForTime():

    # Initialize variables
    totalStates = 0
    tempPopularWinner = 0 #Assume Road Runner is winning in the popular votes
    tempElectoralWinner = 0 #Assume Road Runner is winning in the electoral votes
    time = input("Please enter a time in the format HH:MM:SS: ")
    date = input("Please enter a date in the format MM/DD/YYYY: ")

    # Merge time and date into only one variable
    newDate = ef.addTimeAndDate(date, time)

    # After sorting all the time and date, check if the state has all the counties uploaded by the time requested
    for key, value in sortedCountyDictionary.items():
        if value['State Last Vote'] <= newDate:

            # If the state is not in the dictionary, add it and copy essential values in that list
            if key not in tempDict: 
                tempDict[key] = {'RR': value['RR'], 
                                'BB': value['BB'], 
                                'County Quantity': value['County Quantity'], 
                                'Pop Vote Winner': value['Pop Vote Winner'], 
                                'State Name': value['State Name']
                                }


            else: # Update the values if the state is repeated in the loop, and count the ammount of coutines in a state
                tempDict[key]['RR'] += value['RR']
                tempDict[key]['BB'] += value['BB']
                tempDict[key]['County Quantity'] += 1


    # Determine the winner of each state at the time requested
    for key, value in tempDict.items(): 

        # Check if the ammount of counties in the state is the same as the ammount of counties uploaded
        if value['County Quantity'] == stateDictionary[key]['County Quantity']:
            totalStates += 1

            if value['RR']: # If Road Runner is winning, add 1 to the counter and dertemine him as the Popular vote winner
                tempPopularWinner += 1 
            # if value['Electoral Votes Winner']: # If Road Runner is winning, add 1 to the counter and dertemine him as the Electoral vote winner
            #     tempElectoralWinner += 1

            # Print the winner of each state at the time requested
            print(f"""At {newDate}; {value['State Name']}'s winner is {value['Pop Vote Winner']}""")

    # Determine the overall winner in the time given, and determining the winner of the popular and electoral votes then print
    percentReported = (totalStates/len(stateDictionary)) * 100
    print("{:.2f}% of states have reported".format(percentReported))

    # Prints information on winner in both types of pools
    if tempPopularWinner > totalStates/2:
        print("The popular vote winner is Road Runner")
        if tempElectoralWinner > totalStates/2:
            print("The electoral vote winner is Road Runner")
        else:
            print("The electoral vote winner is Bugs Bunny")

    else:
        print("The popular vote winner is Bugs Bunny")
        if tempElectoralWinner > totalStates/2:
            print("The electoral vote winner is Road Runner")
        else:
            print("The electoral vote winner is Bugs Bunny")


# Extra Credit 3 depending on Task 7
def SeparateCountyState(stateIn):
    # Resets the temporary dictionary if this function is ran so it doesnt mix states or uses the previosly stored values
    global tempDict 
    tempDict = {}

    # Checks if the county is in the state, and copies the values to the tempDict
    for key, value in countyDictionary.items(): 
        if countyDictionary[key]['StateID'] == stateIn:
            # Copy the values to the dictionary
            tempDict[key] = {'RR': value['RR'], 
                             'BB': value['BB'], 
                             'County Name': value['County Fullname'],
                             'votes': value['County Votes'],
                             'Latitude': value['Latitude'],
                             'Longitude': value['Longitude']
                             }



# Task 7, Accept State ID and list all of the summary info for the state with winner, totals and electoral votes awarded
def call_a_state():
    state = input("Please enter a state ID: ").upper() # Upper so it the user input is not case sensitive
    print(f"""
    State Name: {stateDictionary[state]['State Name']}
    State Winner: {stateDictionary[state]['Pop Vote Winner']}
    Total Votes: {stateDictionary[state]['Total']}
    """)
    # Calls  the function to separate the counties by state to acomplish individual state plotting
    SeparateCountyState(state)



## PRINT INFO AS A CHART

# sortedStateDictionary = ef.sortDictByAlphabet(stateDictionary)



def printHeader():
    print(f"{'Values': >60} {'Percent of State Votes': >100}  {'Electoral Votes': >40}")
    print(f"{'---------------': >65}{'-------------------------': >97} {'---------------------': >42}")
    print(f"{'state Name': <20} | {'State ID':<5} | {'Sum of Votes':>18} | {'Sum of RR Values':>20} |"
        f" {'Sum of BB Values':>19} |{'Count of county': >22} |{'RR Percent':>17} | {'BB Percent':>20} | {'Road Runner': >20} | {'Buggs Bunny': >17}")

# Final information with sum of everything
def printGrandTotal(BB_percent, RR_percent, electoral_RR, electoral_BB): 
    # print(f"{'Grand Total':<20} {'':>8} {totalPopVotes:>20} {total_RR:>20} {total_BB:>22} {totalCounties:>20} {"{:.2f}%".format(percent_total):>23} {"{:.2f}%".format(100-percent_total):>22} {electoral_RR:>20} {electoral_BB:>20}")
    print(f"Grand Total: {'All':>16} | {totalPopVotes:>20} | {total_RR:>21} | {total_BB:>19} | {totalCounties:>8} | {electoral_BB:>17} | {electoral_RR:>20} {BB_percent:>20} {RR_percent:>20}")

def printStateInfo(electoral_RR, electoral_BB, sortedStateDictionary, totalPopVotes, total_RR, total_BB, totalCounties):  
    printHeader()
    BB_percent = 0
    RR_percent = 0
    electoral_RR = 0
    electoral_BB = 0
    for key in sortedStateDictionary:
        BB_percent = "{:.2f}%".format(100 * sortedStateDictionary[key]['BB'] / sortedStateDictionary[key]['Total'])  # Calculates percentages for BB
        RR_percent = "{:.2f}%".format(100 * sortedStateDictionary[key]['RR'] / sortedStateDictionary[key]['Total'])  # Calculates percentages for BB
        electoral_RR += sortedStateDictionary[key]['Electoral Votes Winner RR']
        electoral_BB += sortedStateDictionary[key]['Electoral Votes Winner BB']
        print(f"{sortedStateDictionary[key]['State Name']:<20} | {key:>6} | {sortedStateDictionary[key]['Total']:>20} | {sortedStateDictionary[key]['RR']:>20} | {sortedStateDictionary[key]['BB']:>19} | {sortedStateDictionary[key]['County Quantity']:>21} | {RR_percent: >16} | {BB_percent: >20} | {sortedStateDictionary[key]['Electoral Votes Winner RR']: >20} | {sortedStateDictionary[key]['Electoral Votes Winner BB']: >20} |")
    printGrandTotal(BB_percent, RR_percent, electoral_RR, electoral_BB)

# printStateInfo()


# Plot the USA map with the counties and the winner of the popular vote


#References https://stackoverflow.com/questions/34458251/plot-over-an-image-background-in-python


# Read the file and adress them to the right dictionaries
fileReader() # Tasks 1, 2 and 4

# Determine the winner of the popular vote
winner = ef.popularVotesWinner(stateDictionary) # Task 5

# Determine the winner of the electoral vote tally
winner = ef.electoralVotesWinner(stateDictionary) # Task 6

# Allocate winner of each state to the right dictionary
ef.winnerPerState(stateDictionary) 

# Sort the dictionaries by time for Task 9
sortedStateDictionary = ef.sortDictByTime(stateDictionary)
sortedCountyDictionary = ef.sortDictByTime(sortedStateDictionary)

# Accept date and time and show the winner at the moment requestes
askForTime() # Task 9

# Task 7, Accept State ID and list all of the summary info for the state with winner, totals and electoral votes awarded
call_a_state() 

# Sort the info alphabetically
sortedStateDictionary = ef.sortDictByAlphabet(stateDictionary)
# Task 8, Print a summary
printStateInfo(electoral_RR, electoral_BB, sortedStateDictionary, totalPopVotes, total_RR, total_BB, totalCounties) # GrandTotal work in progress

# Extra Credit 2
ef.plot_map(countyDictionary)

# Extra Credit 3 depending on Task 7
ef.plot_map(tempDict)
