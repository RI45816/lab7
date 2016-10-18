# File: milesPerWeek.py 
# Author: Uzoma Uwanamodo 
# Date: 10/18/2016
# Section: 05
# E-mail: uu3@umbc.edu
# Description: Calculate how many miles per week the user drives in highest week
# Collaboration: During lab, collaboration between students is allowed, although I understand I still must understand the material and complete the assignment myself.

def maximum(*n): # Get the activity with the highest number of votes
    highest = n[0] # The variable representing the largest number as of yet
    for i in n:
        highest = i if i > highest else highest # If the number being tested is bigger than the current max, set it as the new max
    activites = [] # Array to store all of the games that have the maximum
    for i in range(len(n)):
        if n[i] == highest:
            activites.append(i)
    return activites


def main():
    games = ["Twister", "Dodgeball", "Capture the Flag","Hide and Seek", "Croquet", "Ring Toss", "Ping Pong"] # The games the user shall choose from
    for i in range(len(games)):
        print(i+1,"-",games[i])
    print("")
    votes = [0]*len(games) # Store the nber of votes each activity gets
    vote = int(input("What game would you like to play? (0 to quit): ")) # Ask the user for their vote
    while vote != 0: # As long as the user doesn't enter the sentinel

        if vote in range(1,len(games)+1): # If the vote is for one of the options
            votes[vote-1]+=1 # Count the vote
        vote = int(input("What game would you like to play? (0 to quit): ")) # Ask the user for their vote
            
    print("")
    for i in range(len(games)):
        print(games[i],"has",votes[i],"votes")
    MOST_VOTED = [games[i] for i in maximum(*votes)] # The games that got the most votes
    print("After tallying up the votes, it seems that","%s%s%s" % (", ".join(MOST_VOTED[:-1]),", and " if len(MOST_VOTED) > 1 else "",MOST_VOTED[-1]),"got the most votes")
main()

