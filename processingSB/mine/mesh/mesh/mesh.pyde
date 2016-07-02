#mesh
width = 720
height = 540
mesh = [[]]

def setup():
    size(width, height)
    noFill()
    stroke(255)
    seedNodes(100)
    d()

def d():
    for i in mesh:
        for j in i:
            j.drawPoint()
                        
# Populates the mesh array. Count is how many nodes you want to span
# the width of the frame
def seedNodes(count):
    hNum = (int)(540.0/720*count)
    for i in range(hNum):
        for j in range(count):
            x = (int)(map(i,0,count,0,width))
            y = (int)(map(j,0,hNum,0,height))
            n = node(x,y)
            print(len(mesh))
            print(len(mesh[i-1]))
            mesh[i-1].append(n)
            if j == count:
                mesh.append([])

class node():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def drawPoint():
        point(self.x,self.y)

    