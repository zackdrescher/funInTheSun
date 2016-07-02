//flockPromise_150603b

ArrayList<PointPosition> pointPosition = new ArrayList();
boolean alternate = true;
int setDistance = 5;
int threshold = 135;
int width = 540,
   height = 720;
color pColor;
int[] directions = {
   (width*-1),
   width,
   -1,
   1
 };

void setup() {
 size(width,height);
 frameRate(24);
 seedColor();
 seedPoints(width);
 pColor = color(
           red(int(map(randomNormal(),0,1,0,50))),
           green(int(map(randomNormal(),0,1,0,50))),
           blue(int(map(randomNormal(),0,1,0,50)))
          );
}

void draw() {
 if (frameCount % 36 == 0) { 
   pColor = color(
             red(int(map(randomNormal(),0,1,0,50))),
             green(int(map(randomNormal(),0,1,0,50))),
             blue(int(map(randomNormal(),0,1,0,50)))
            );
 }
 fill(pColor,setDistance);
 stroke(pColor,setDistance);
 rect(-2,-2,width+2,height+2);
 alterPixels();
 updatePoints();
}

void seedColor() {
 loadPixels();
   for (int k=0; k<width*height; k++) {
     pixels[k] = color(
       int(map(random(1.0),0,1,0,255)),
       int(map(random(1.0),0,1,0,255)),
       int(map(random(1.0),0,1,0,255)),
       int(map(random(1.0),0,1,0,255))
       );
   }
 updatePixels();
}

void seedPoints(int count){
 for (int i=0; i<count; i++) {
   PointPosition p = new PointPosition();
     p.pos.x = width/2;
     p.pos.y = height/2;
     p.tpos.x = width/2 + cos(i);
     p.tpos.y = height/2 + sin(i);
   pointPosition.add(p);
 }
}

void alterPixels() {
 loadPixels();
   for (int k=width+1; k<width*height-width-1; k++){
     int pModifier = directions[int(random(directions.length))];
     if (brightness(pixels[k]) > threshold){
       pixels[k-pModifier] = color(
         int(red(pixels[k+pModifier])),
         int(green(pixels[k+pModifier])),
         int(blue(pixels[k-pModifier])),
         int(brightness(pixels[k-pModifier]))
       );
     } else if (brightness(pixels[k]) == threshold) {
       //
     } else {
       pixels[k-width] = pixels[k];
       pixels[k] = pixels[k+pModifier];
     }
   }
   threshold = setThreshold(threshold,1,255);
 updatePixels();
}

void updatePoints() {
 int i = 0;
 for(PointPosition p:pointPosition){
   threshold = setThreshold(threshold,153,255);
   p.tpos.x = p.tpos.x+cos(millis()/3)*i*TAU;
   p.tpos.y = p.tpos.y+sin(millis())*i*TAU;
   p.update();
   p.render();
   if (p.pos.x < 0 || p.pos.x > width) {
     p.pos.x = width/2;
     p.pos.y = height/2;
     p.tpos.x = width/2 + cos(i);
     p.tpos.y = height/2 + sin(i);
   }
   if (p.pos.y < 0 || p.pos.y > height) {
     p.pos.x = width/2;
     p.pos.y = height/2;
     p.tpos.x = width/2 + cos(i);
     p.tpos.y = height/2 + sin(i);
   }
   i++;
 }
}

int setThreshold(int threshold, int minThreshold, int maxThreshold) {
 if (threshold <= maxThreshold && threshold >= minThreshold && alternate) {
   threshold++;
 } else if (threshold <= maxThreshold && threshold >= minThreshold) {
   threshold--;
 } else if (alternate) {
   threshold = maxThreshold;
   alternate = !alternate;
 } else {
   threshold = minThreshold;
   alternate = !alternate;
 }
 return threshold;
}

class PointPosition {
 PVector pos = new PVector();
 PVector tpos = new PVector();
 void update(){
   pos.lerp(tpos,0.00001);
 }
 void render(){
   stroke(255);
   ellipse(pos.x,pos.y,setDistance,setDistance);
 }
};

float randomNormal() {
 float x = 1.0, y = 1.0, s = 2.0;
 while (s >= 1.0) {
   x = random(-1.0f, 1.0f);
   y = random(-1.0f, 1.0f);
   s = x*x + y*y;
 }
 return x * sqrt(-2.0f * log(s)/s);
}
