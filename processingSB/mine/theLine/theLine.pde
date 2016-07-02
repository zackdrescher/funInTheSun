//The Line

int width = 540, 
height = 540, 
x1 = 200, y1 = 200, 
x2 = 300, y2 = 200, 
h = 0, sb = 0, 
speed = 5;

void setup() {
  size(width, height);
  frameRate(24);
  colorMode(HSB); 
  stroke(255);
}

void draw() {
  background(h, sb+25, sb);
  adjustHSB();

  line(x1, y1, x2, y2);

  determineDir();
  x1 += speed;
  determineDir();
  y1 += speed;
  determineDir();
  x2 += speed;
  determineDir();
  y2 += speed;
}

void adjustHSB() {

  while (sb < 175) {
    sb++;
  }

  h++;
  if (h > 255) {
    h = 0;
  }
}

/*
  void determineSpeed() {
 
 int r = random(100);
 speed = 1;
 if (  < 5) {
 speed = 5;
 } else if (
 }
 */
void determineDir() {
  if ( random(100) > 60) {
    speed = -speed;
  }
}

