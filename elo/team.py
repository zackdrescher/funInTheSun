# The class for storing information on a specific team. The team will have
# a name and a chronologcal list of games. The games are where the teams elo
# will be stored.
class team(object):

    # Initializes the team with the given name and an empty game list
    def __init__(self, name):
        self.name = name
        self.games = [0]
        self.points = [0]
        self.rank = [0]
        self.elo = [0]

    # Adds a game to the teams game list. and updates all the statistics.
    # Result is outcome of the match in this teams favor. rank will be some form
    # of data that will help modify the teams rank. eElo is the enemy teams elo
    # that will be used to calculate the new elo.
    def addGame(self, game, result, rank, eElo):
        self.games.append(game)
        if result == "W":
            point = self.points.pop()
            self.points.append(point)
            self.points.append(point + 3)
            # TODO: Calculate rank and elo based on win.
        elif result == "D":
            point = self.points.pop()
            self.points.append(point)
            self.points.append(point + 1)
        else:
            point = self.points.pop()
            self.points.append(point)
            self.points.append(point)

    # To string
    def __str__(self):
        st = [self.name, "- Points: ",str(self.points[len(self.points)-1]), "- games: "
            , str(len(self.games))]
        return "".join(st)
