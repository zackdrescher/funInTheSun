// a slower dancing line on a ranomdly generated color background

void setup() { 
  frameRate(4);
}

void draw() {
  background(random(256), random(256), random(256));
  line(random(100),random(100),random(100),random(100));
}
  

