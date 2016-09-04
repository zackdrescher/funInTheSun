import sys
sys.path.insert(0, '/home/zack/Desktop')
import reader
import season

path = "/home/zack/Desktop/data/pm94.csv"
data = reader.read(path)
s = season.Season(data)
print s.div," ", s.year
print s.teams

s.simulateSeason()
for i in s.teams:
    print s.teams[i]
