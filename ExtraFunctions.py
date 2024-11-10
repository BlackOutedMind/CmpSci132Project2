#######################################################################
# #Extra Functions file, a file to store functions that are used in the project
# by Yuri W. Dourado 
# Nov/06/2024
#
# 

from datetime import *
import matplotlib.pyplot as plt

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

def sortDictByTime(dictIn):
    return dict(sorted(dictIn.items(), key=lambda item: item[1]['State Last Vote']))

def sortDictByAlphabet(dictIn):
    return dict(sorted(dictIn.items(), key=lambda item: item[0]))


def popularVotesWinner(varIn):
    BB = 0
    RR = 0
    sumVotes = 0
    for state, totals in varIn.items():
        BB += totals['BB']
        RR += totals['RR']
        sumVotes = totals['RR'] + totals['BB']

    # print(sumVotes)

    RR_percent = "{:.2f}%".format(100 *  RR/ sumVotes)
    BB_percent = "{:.2f}%".format(100 * BB/ sumVotes)
    if RR_percent > BB_percent:
        return 'Road Runner'
    else:
        return 'Bugs Bunny'

def winnerPerState(varIn):
    RR = 0
    BB = 0
    for state, votes in varIn.items():
        if votes['RR'] > votes['BB']:
            # print(f'{state} winner is Road Runner')
            varIn[state]['Pop Vote Winner'] = 'Road Runner'
            RR += 1
        else:
            # print(f'{state} winner is Bugs Bunny')
            varIn[state]['Pop Vote Winner'] = 'Bugs Bunny'
            BB += 1
    if RR > BB:
        return 'Road Runner'
    else:
        return 'Bugs Bunny'


# electoralVotesDicts = {}
def electoralVotesWinner(varIn):
    RR = 0
    BB = 0
    for state, votes in varIn.items():
        # print(state)
        # print(votes)
        if varIn[state]['RR'] > varIn[state]['BB']:
            # electoralVotesDicts[state] = 'RR'
            varIn[state]['Electoral Votes Winner RR'] = varIn[state]['Electoral Votes Awards']
            RR += votes['RR']
        else:
            varIn[state]['Electoral Votes Winner BB'] = varIn[state]['Electoral Votes Awards']

            BB += votes['BB']

    if RR > BB:
        return 'Road Runner'
    else:
        return 'Bugs Bunny'

def plot_map(dictIn):
    # Plot the map of the USA
    fig, ax = plt.subplots()
    # img = plt.imread("USA-Map.jpg")
    ax.set_aspect('equal')
    ax.set_axis_off()
    ax.set_title('USA Counties Winner of Popular Vote')
    # ax.imshow(img, extent=[-180, -65, 20, 75])

    # From countyDictionary, pull latitudes and longitudes and plot them on the map
    for key, value in dictIn.items():
        if dictIn[key]['RR'] > dictIn[key]['BB']:
            color = 'Green'
        else:
            color = 'Magenta'
        ax.plot(float(dictIn[key]['Longitude']), float(dictIn[key]['Latitude']), 'o', color=color, markersize=3)
    plt.show()
