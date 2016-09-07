# Manipulation.py
# Author: Zack Drescher
# Date Created: 9/4/16
# Rev 2.0
# Feilds #######################################################################
import pandas as pd
################################################################################

# Creates a dicrionary storing a data frame for each team where each
# observation is a game contaning the result and record and elo ranking.
def getTeamsDict(seasonDf):

    # Get set of teams
    teams = set()

    for index, row in seasonDf.iterrows():
        teams.add(row['HomeTeam'])
        teams.add(row['AwayTeam'])

        if len(teams) > 20:
            break

    teamsDict = {}
    for team in teams:
        teamsDict[team] = getTeamFrame(team, seasonDf)

    return teamsDict

# queries the season data frame for a certians teams matches
def getTeamFrame(team, seasonDf):

    # query home and away games
    homeGames = seasonDf[seasonDf['HomeTeam'] == team]
    awayGames = seasonDf[seasonDf['AwayTeam'] == team]

    # concatinate
    frames = [homeGames, awayGames]
    teamFrame = pd.concat(frames)

    # Sort by date
    teamFrame = teamFrame.sort_values(['Date'])
    return teamFrame
