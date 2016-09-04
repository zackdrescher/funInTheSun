import datetime

# Class for storing the values of games.
class Game(object):

    # Initializes the game to have a division, date, home team, away team, home
    # score, away score and result.
    def __init__(self, data):
        self.div = data[0]
        self.date = self.convertDate(data[1])
        # TODO: Create reference to teams
        self.home = data[2]
        self.away = data[3]
        self.hg = int(data[4])
        self.ag = int(data[5])
        self.result = data[6]

    # Converts a string in "dd/mm/yy" format to a pyhton datetime object
    def convertDate(self, sDate):
        day = int(sDate[:2])
        sDate = sDate[3:]
        month = int(sDate[:2])
        year = int(sDate[3:])
        # TODO: Find basis for converting 2 digit years to 4 digit years
        if year < 50:
            year += 2000
        else:
            year += 1900
        date = datetime.date(year, month, day)
        return date

    # Converts this games information into a string
    def __str__(self):
        st =["Div: ", self.div,"\n",
        "Date: ", str(self.date),"\n",
        "Home: ", self.home,"\n",
        "Away: ", self.away,"\n",
        "Home Goals: ", str(self.hg),"\n",
        "Away Goals: ", str(self.ag),"\n",
        "result: ", self.result,"\n"]
        return "".join(st)
