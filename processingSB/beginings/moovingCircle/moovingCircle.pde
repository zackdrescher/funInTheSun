float x = 201;
float y = 200;
float xAccel = 2;
float yAccel = 1;

void setup() {
  size(400,400);
  
  noStroke();
  fill(#C1FF3E);
}

void draw() {
  background(#1BB1F5);
    
  ellipse(x,y, 50,50);
  
  if( x  > (width - 25) || x < 25) {
    xAccel = -xAccel;
  }
  if( y  > (height - 25) || y < 25) {
    yAccel = -yAccel;
  }  
  x = x + xAccel;
  y = y + yAccel;
}
