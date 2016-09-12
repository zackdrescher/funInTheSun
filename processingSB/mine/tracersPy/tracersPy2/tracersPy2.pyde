
tracers = []

def setup():
    colorMode(RGB,100)
    size(640, 1136)
    noFill()
    background(46, 123, 142)
    stroke(255)
    seedTracers(100)

def draw():
    for t in tracers:
        preX = t.x
        preY = t.y
        
        t.move()
        stroke(255)
        line(preX, preY, t.x, t.y)
        stroke(100)
        line(preX+1, preY+1, t.x+1, t.y+1)
    
def seedTracers(count):
    for i in range(count):
        x = (int)(map(i, 0, count, 0, width))
        t = Tracer(x)
        tracers.append(t)
    
class Tracer:
    def __init__(self, x):
        self.x = x
        self.y = height - 1
        self.threshold = (int)(randomGaussian()*50+100)
    
    def move(self):
        if self.threshold > 0:
            r = random(10)
            if r > 5:
                self.up()
            elif r > 2.5:
                self.left()
            else:
                self.right()
            
            self.threshold-=1 
    
    def left(self):
        if self.x-10 < 0:
            self.move()
        else:
            self.x-=10
    
    def right(self):
        if self.x+10 > width:
            self.move()
        else:
            self.x+=10
    
    def up(self):
        if self.y-10 < 0: 
            self.threshold=0
        else:
            self.y-=10