####### Names and Spire ID ###########
# 1. Mikail Usman 34432374
# 2. Yusuf Yildirim 34446441 

""" Implement the Player class and functions below """
class Player():
    #Constuctor method to initialize all attributes of the players
    def __init__(self, name, league, goals, assists, passes):
        self.name = name 
        self.league = league
        self.goals = goals 
        self.assists = assists
        self.passes = passes

    def print_player(self):
        #Prints all players and their attributes in formatted columns, rows.
        #https://stackoverflow.com/questions/19103052/string-formatting-columns-in-line
        #Where in {:<20}, '<' indicates text alignment and '20' indicates spacing for the column.
        #Additional alignment options: (<, left align) (>, right align) (^, center align)
        print(" {:<20} {:<10} {:>6} {:>10} {:>11}".format(self.name,self.league,self.goals,self.assists,self.passes))






    
