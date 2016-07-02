# mesh_160524b

# enviornment settings
width = 400
height = 400
boids =[]

# physics settings
maxSpeed = 4
maxForce = .05
neighborRadius = 50
desiredSeperation = 30
meshRad = 30
cohesionWeight = 1
alignmentWeight = 1
seperatioWeight = 3

 
def setup():
    colorMode(RGB,255)
    smooth()
    stroke(255,255,255)
    size(width,height)
    start = PVector(width/2,height/2)
    b = boid(start)
    boids.append(b)
    seedBoids(150)
    
def draw():
    saveFrame()
    background(127,252,191)
    for boid in boids:
        boid.step(boids)
        boid.render(boids)

def seedBoids(count):
    for i in range(count):
        rv = PVector(random(width-1),random(height-1))
        b = boid(rv)
        boids.append(b)
    
# objects that flock
class boid():
    # creates a boid with the given x, y location and a randomly
    # generated velocity vector
    def __init__(self,loc):
        self.loc = loc
        self.velocity = PVector(random(1)*maxSpeed-maxSpeed/2,random(1)*maxSpeed-maxSpeed/2)

    # fuction to be called every frame will recalculate the velocity
    # vector and update the location
    def step(self, neighbors):
        # TODO: calculate acceleration and add it to velocity
        accl = self.flock(neighbors)
        self.velocity.add(accl)
        self.velocity.limit(maxSpeed)
        self.loc.add(self.velocity)
        self.wrapCheck()
    
    # Calculates acceleration on this boid based on flock around it
    def flock(self, neighbors):
        cohere = self.cohere(neighbors)
        sep = self.seperate(neighbors)
        align = self.align(neighbors)
        cohere.mult(cohesionWeight)
        align.mult(alignmentWeight)
        sep.mult(alignmentWeight)
        sep.add(align)
        return PVector.add(cohere,sep)
    
    # Calculates the cohesion of this boid. Cohesion is the force
    # that attracts this boid to the boids near it.
    def cohere(self, neighbors):
        sum = PVector(0,0)
        count = 0
        for boid in neighbors:
            d = self.loc.dist(boid.loc)
            if d > 0 and d < neighborRadius:
                sum.add(boid.loc)
                count += 1
        if count > 0:
            return self.steerTo(PVector.div(sum,count))
        else:
            return sum
    
    # calculated the seration component of this boids acceleration.
    # Seperation is what prevents boids from getting to close
    def seperate(self, neighbors):
        mean = PVector(0,0)
        count = 0
        for boid in neighbors:
            d = self.loc.dist(boid.loc)
            if d > 0 and d < desiredSeperation:
                c = PVector.sub(self.loc,boid.loc)
                c.normalize()
                c.div(d)
                mean = PVector.add(mean,c)
                count += 1
        if count > 0:
            mean = PVector.div(mean,count)
        return mean
    
    # Calculates the alignment component of the boids acceleration.
    # Alignment is what keeps the boids moving in the same direction
    def align(self, neighbors):
        mean = PVector(0,0)
        count = 0
        for boid in neighbors:
            d = self.loc.dist(boid.loc)
            if d > 0 and d < neighborRadius:
                mean.add(boid.velocity)
                count += 1
        if count > 0:
            mean.div(count)
        mean.limit(maxForce)
        return mean
    
    # Helps the boids turn gracefully
    def steerTo(self, target):
        desired = PVector.sub(target,self.loc)
        d = desired.mag()
        if d>0:
            desired.normalize()
            if d < 100:
                desired.mult(maxSpeed*(d/100))
            else:
                desired.mult(maxSpeed)    
            steer = PVector.sub(desired,self.velocity)
            steer.limit(maxForce)
        else:
            steer = PVector(0,0)
        
        return steer
    
    # draws the boid
    def render(self,neighbors):
        # 'radius' of triangle
        self.r = 2
        theta = self.velocity.heading() + radians(90)
        pushMatrix()
        beginShape(LINES)
        for boid in neighbors:
            d = self.loc.dist(boid.loc)
            if d > 0 and d < meshRad:
                vertex(self.loc.x,self.loc.y)
                vertex(boid.loc.x,boid.loc.y)
        endShape()
        #translate(self.loc.x,self.loc.y)
        #rotate(theta)
        #beginShape(TRIANGLES)
        #vertex(0,-1*self.r*2)
        #vertex(-1*self.r,self.r*2)
        #vertex(self.r,self.r*2)
        #endShape()
        popMatrix()
    
    # fix me    
    def wrapCheck(self):
        if self.loc.x >= width:
            self.loc.x = 0
        elif self.loc.x < 0:
            self.loc.x = width - 1
        elif self.loc.y >= height:
            self.loc.y = 0
        elif self.loc.y < 0:
            self.loc.y = height - 1

        
    
    
     