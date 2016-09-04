# Permeir League ELO

## TODO
- Create a basis module to run results between multiple seasons

## Programs
### reader.py
contains function to read in game data from CSV files from [football-data.co.uk](http://www.football-data.co.uk/englandm.php). Each observation will be stored in a game object.

### Game.py
 Contains the class that stores infromation for a single game.
Each game has:
- Division - The leage the game was played in.
- Date - The date of the match.
- Home Team
- Away Team
- FTHG- Full Time Home Goals
- FTAG- Full TIme Away Goals
- FTR- Full Time Result (H= Home win, D= Draw, A= Away win)

#### Todo
1. Initialization
  - Reference team object

2. convertDate
  - Find basis for converting  digit years into 4 digit years

### Season.py
A season contains a list of games and a list of teams those games match up.
The season is the link between the game and the team. Season generates the teams. Season iterates though its game list and add the games to the teams list providing the team object with the information of its schedule. The season object will simulate a season. it will go through very game and calculate the resluts and update the given team objects.Eventually as season will be passed a dictionary of teams from a previous season.

#### Todo

1. initialize season with a given set of teams from a previous season.
3. simulateGame
  - Generate and update teams ELO and rank

### team.py
Contains the class for storing information on a team. Each team has a name, a list of games and lists containing the elo, points and rank. The teams will have methods to adjust all these values based on the result the season determines.
