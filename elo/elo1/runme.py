import reader
import season

def readSeasons():
    y1 = range(93,100)
    y2 = range(00,16)
    y = y1 + y2
    for i in y:
        print i, "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        p = getPath(1, i)
        data = reader.read(p)
        s = season.Season(data)
        s.simulateSeason()
        for i in s.teams:
            print s.teams[i]

def getPath(div, year):
    if year < 10:
        year = str(year)
        s = ["0",year]
        year = "".join(s)
    divs = {1:"pm",2:"c",3:"l1",4:"l2",5:"con"}
    path = ["/home/zack/Desktop/data/",divs[div],str(year),".csv"]
    return "".join(path)
