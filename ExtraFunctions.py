#######################################################################
# #Extra Functions file, a file to store functions that are used in the project
# by Yuri W. Dourado 
# Nov/06/2024
#
# 

from datetime import *




########################################################
# necessary Variables

electoralVotesDicts = {
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




#######################################################################
# Functions





def convertTime(time):
    return datetime.strptime(time, "%H:%M:%S")
def convertDate(date):
    return datetime.strptime(date, "%m/%d/%Y")

def addTimeAndDate(date,time):
    combined = date + " " + time
    dateTimeVar = datetime.strptime(combined, "%m/%d/%Y %H:%M:%S")
    return dateTimeVar

def sortTimeAndDate(dictIn):
    return {key: val for key, val in sorted(dictIn.items(), key = lambda ele: ele[1][2])}


def popularVotesWinner(varIn):
    BB = 0
    RR = 0
    for state, totals in varIn.items():
        BB += totals['BB']
        RR += totals['RR']
        sumVotes = totals['RR'] + totals['BB']

    # print(sumVotes)

    RR_percent = "{:.2f}%".format(100 *  RR/ sumVotes)
    BB_percent = "{:.2f}%".format(100 * BB/ sumVotes)
    if RR_percent > BB_percent:
        return 'RR'
    else:
        return 'BB'

electoralVotesDicts = {}
def electoralVotesWinner(varIn):
    RR = 0
    BB = 0
    for state, votes in varIn.items():
        # print(state)
        # print(votes)
        if popularVotesWinner(varIn) == 'RR':
            electoralVotesDicts[state] = 'RR'
            RR += votes['RR']
        else:
            electoralVotesDicts[state] = 'BB'
            BB += votes['BB']
    if RR > BB:
        return 'RR'
    else:
        return 'BB'
