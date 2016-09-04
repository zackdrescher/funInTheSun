import sys
sys.path.insert(0, '/home/zack/Desktop')
import reader

path = "/home/zack/Desktop/data/pm15.csv"
data = reader.read(path)
for i in range(len(data)):
    print data[i]
