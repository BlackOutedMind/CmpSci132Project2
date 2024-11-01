#
#     Program: Voting Counties USA Buggs Bunny vs. Road Runner
#
#     By: Paige E. McCullough
#
#     Date: October 31, 2024
#
#     Program Details:  This program imports the state abbreviation and votes per county for BB and RR from 'VotingCounties!.csv'.  
#                       The program adds the votes from each county for each candidate and calculates the total number of votes
#                       and percentage of votes for BB and RR for each state. The program also calculates the number of votes and
#                       percentage for the overall winner. 
#                        
#     Note: All the commas in lines 13 and 14 for VotingCounties!.csv have been removed. If the commas are not removed the program 
#           only calculates the counites with votes <1,000 votes. 
#

import csv
from collections import defaultdict 


# Creates variable for file.
voting_counites='Voting-Counties.csv' 
voting_counties = 'VotingCountiesFixed.csv'

#Initializes a variable to hold the total votes.
state_totals = defaultdict(lambda: {'RR': 0, 'BB': 0})

# Opens the file.
with open(voting_counites,'r') as data:
    
    Counties_file = csv.reader(data)
    next(Counties_file)  # Skip the first row with titles in VotingCounties!.csv
    
    
    for line in Counties_file:
        if line[13].isdigit() and line[14].isdigit():# .isdigit() does the same thing as lines 18 & 19
            
                state = line[3]  # References state name in 4th column of 'VotingCounties!.csv file'.
                value_RR = int(line[13].replace(',', ''))
                value_BB = int(line[14].replace(',', ''))

                # Updates the total for each state.
                state_totals[state]['RR'] += value_RR
                state_totals[state]['BB'] += value_BB
                
total_RR = 0  #Initilizes varible to determine who won popular vote. 
total_BB = 0

for state, totals in state_totals.items():
    total_votes = totals['RR'] + totals['BB'] #Calculates the total votes. 
    if total_votes > 0:
        RR_percent = "{:.2f}%".format(100 * totals['RR'] / total_votes) #Calculates percentages for RR
        BB_percent = "{:.2f}%".format(100 * totals['BB'] / total_votes) #Calculates percentages for BB

    print(f"State: {state} - Total Votes for RR: {totals['RR']}, Total Votes for BB: {totals['BB']}")
    print(f"Percentages - RR: {RR_percent}, BB: {BB_percent}")
    print("-----------------")
    
    total_RR += totals['RR'] #Adds to the total for each state 
    total_BB += totals['BB']
    percent_total = (100*total_RR)/(total_RR + total_BB) #Calculates percentage for overall winner.  

if total_RR > total_BB:  #Determines winner of the popular vote. 
    overall_winner = 'RR'
    overall_votes = total_RR
elif total_BB > total_RR:
    overall_winner = 'BB'
    overall_votes = total_BB

print(f"Winner of the popluar vote: {overall_winner} with {overall_votes} votes.", "-", f"%{percent_total:.3}") #Prints results for overall winner
