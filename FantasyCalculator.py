####### Names and Spire ID ###########
# 1. Mikail Usman 34432374
# 2. Yusuf Yildirim 34446441

""" Implement the main program and functions below """
from Player import *

def initialize(): #Initializing list of players (Hardcoding all 10 players' information)
    p1 = Player('Erling Haaland', 'EPL', 18, 5, 270)
    p2 = Player('Robert Lewandowski', 'La Liga', 12, 6, 414)
    p3 = Player('Harry Kane', 'Bundesliga', 30, 6, 472)
    p4 = Player('Son Heung-Min', 'EPL', 14, 8, 660)
    p5 = Player('Julian Alvarez', 'EPL', 8, 8, 915)
    p6 = Player('Leroy Sane', 'Bundesliga', 8, 11, 903)
    p7 = Player('Mohamed Salah', 'EPL', 15, 9, 686)
    p8 = Player('Jude Bellingham', 'La Liga', 16, 3, 1164)
    p9 = Player('Toni Kroos', 'La Liga', 1, 7, 1908)
    p10 = Player('Sehrou Guirassy', 'Bundesliga', 21, 1, 494)
    players = [p1, p2, p3, p4, p5, p6, p7, p9, p10]
    return players

def display_players(players):
    #Creates a table for all 10 players and appropriate fields.
    #Prints all players and their attributes in formatted columns, rows.
    print("{:<10} {:>19} {:>10} {:>10} {:>10}".format("Name","League","Goals","Assists","Passes")) #Table header
    for player in players:
        player.print_player()

def display_goals(players, numGoals):
    #Searches through player list, adds results to new list which is then output
    queryList = [] 
    for i in range(len(players)):
        if players[i].goals == int(numGoals):
            queryList.append(players[i])
    if len(queryList) == 0:
        print("No players found")
    else:
        #Printing and formatting output list after query
        print("{:<10} {:>19} {:>10} {:>10} {:>10}".format("Name","League","Goals","Assists","Passes"))
        for player in queryList:
            player.print_player()
    
def display_league(players, league):
    #Searches through player list, adds results to new list which is then output
    queryList = []
    for i in range(len(players)):
        if players[i].league.lower() == str(league).lower(): 
            queryList.append(players[i])
    if len(queryList) == 0:
        print("No players found")
    else:
        #Printing and formatting output list after query
        print("{:<10} {:>19} {:>10} {:>10} {:>10}".format("Name","League","Goals","Assists","Passes"))
        for player in queryList:
            player.print_player()

def display_player(players, playerName):
    #Searches through player list, adds results to new list which is then output
    queryList = []
    for i in range(len(players)):
        if players[i].name == str(playerName):
            queryList.append(players[i])
    if len(queryList) == 0:
        print("No players found")
    else:
        #Printing and formatting output list after query
        print("{:<10} {:>19} {:>10} {:>10} {:>10}".format("Name","League","Goals","Assists","Passes"))
        for player in queryList:
            player.print_player()

def display_most_goals(players):
    #Searches through the list of players. Compares the no. of goals of each player to find the player with most goals
    mostGoals = int(players[0].goals)
    mostGoalsPlayer = players[0]
    for i in range(len(players)):
        if int(players[i].goals) > mostGoals:
            mostGoalsPlayer = players[i]
            mostGoals = int(players[i].goals)
    #Outputting query and included formatting
    print("{:<10} {:>19} {:>10} {:>10} {:>10}".format("Name","League","Goals","Assists","Passes"))
    mostGoalsPlayer.print_player()

def calculate_total_points(players):
    playerPoints = 0
    #Iteration through whole player list to calculate each player's points.
    for i in range(len(players)):
        #Formula with custom weights for calculating total player points for each player
        playerPoints = (0.5 * players[i].goals) + (0.1 * players[i].assists) + (0.1 * players[i].passes)
        #Outputs formatted message with player points rounded to 2 decimal places. 
        print(f'{players[i].name} has {round(playerPoints, 2)} points.')

def display_menu(): #Menu display function (Uses while loop to repetitively print 7 options)
    menuActive = True #Used to control while loop (If false, while loop ends)
    while menuActive == True:
        print()
        print("Menu")
        print("1-List all players \n2-List all players with at least a specific number of goals \n3-List all players in a specific league \n4-Find a specific player \n5-Determine the player with the most goals \n6-Determine the total points for all players and print out the values \n7-Exit")
        print()
        userOption = input("Enter Command: ")
        if userOption == '1':
            display_players(players)
        elif userOption == '2':
            numGoals = input("Please indicate number of goals: ")
            display_goals(players, numGoals)
        elif userOption == '3':
            league = input("Please indicate the league: ")
            display_league(players, league)
        elif userOption == '4':
            playerName = input("Please indicate name of player: ")
            display_player(players, playerName)
        elif userOption == '5':
            display_most_goals(players)
        elif userOption == '6':
            calculate_total_points(players)
        elif userOption == '7':
            print("Exiting")
            menuActive = False

#Execute welcome screen and start options for the program:
players  = initialize()
print("Welcome to your Fantasy Team Database!")
print("====================")
display_menu()