# Module containing functions for reading in the CSV data into Game objects.
import csv
import game

# Function to be called from another file.
def read(path):
    # This reads in the CSV into a list of lists containing strings of the
    # values
    with open(path, 'rb') as f:
        reader = csv.reader(f)
        data = list(reader)
    # Pops off the label line of the CSV
    data.remove(data[0])
    # TODO: turn csv data into a list of games.
    games = []
    for i in range(len(data)):
        if data[i][0] == "":
            break
        g = toGame(data[i])
        games.append(g)
    return games

# Converts list of game information into a game object
def toGame(data):
     g = game.Game(data)
     return g
