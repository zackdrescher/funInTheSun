# importData.py
# Author: Zack Drescher
# Date Created: 9/4/16
# Rev 2.0
# Feilds #######################################################################
import os
import pandas as pd

# Desired rows in output csv
ROWS = ['Div','Date','HomeTeam','AwayTeam','FTHG','FTAG','FTR']
###############################################################################
# Read season from csv. Accecpts string with as div## where div is the division
# header and ## is the year.
# Returns a pandas dataframe
def importSeason(s):

    # configures file path
    cwd = os.getcwd()
    path = cwd + '/data/'+ s[:2] + '/' + s + '.csv'

    # Reads csv into pandas data frame
    df = pd.read_csv(path)

    # Selects rows from original dataframe
    df = df[ROWS]

    return df
