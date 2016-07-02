import team
import game
# a class for containing the teams and games that take place between them
# in a season.
class Season(object):

    # Initializes the season by taking in a list of games and the year the
    # season begins. from the infomation it generates a dictionary of teams and
    #  the division of the season.
    def __init__(self, data):
        self.games = data
        self.div = self.games[0].div
        self.year = self.games[0].date.year
        self.teams = self.populateTeams()

    # Creates a dictionary of all the teams playing this season.
    def populateTeams(self):
        numTeams = 20
        if self.year <= 1994:
            numTeams = 22
        games = self.games
        teams = dict()
        num = 0
        # interates though games and attempts to add both teams to the teams
        # dictionary. Breaks out of the loop when there are 20 teams.
        for i in range(len(games)):
            game = self.games[i]
            # TODO: Create refernce to team object
            if(not(game.home in teams)):
                teams[game.home] = team.team(game.home)
                num += 1
            if(game.away not in teams):
                teams[game.away] = team.team(game.away)
                num += 1
            if num >= numTeams:
                break
        return teams

    # Recevies a game object and calculates the results of the game and
    # updates the teams involved. TODO: calculate and update elo and rank.
    def simulateGame(self, game):
        homeTeam = self.teams[game.home]
        awayTeam = self.teams[game.away]
        # TODO: Generate and update ELO and rank
        if game.result == "H":
            homeTeam.addGame(game, "W", 0, 0)
            awayTeam.addGame(game, "L",0,0)
        elif game.result == "A":
            awayTeam.addGame(game, "W",0,0)
            homeTeam.addGame(game, "L",0,0)
        else:
            homeTeam.addGame(game, "D",0,0)
            awayTeam.addGame(game, "D",0,0)
        # Updates the teams in the dictionary
        self.teams[game.home] = homeTeam
        self.teams[game.away] = awayTeam

    # TODO: this goes though all the games in a season. and calculates the
    # results and up dates the respective teams.
    def simulateSeason(self):
        for i in self.games:
            self.simulateGame(i)
