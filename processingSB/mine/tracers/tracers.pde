//tracers

ArrayList<Tracer> tracers = new ArrayList();

void setup() {
  size(640, 1136);
  noFill();
  background(#2E7B8E);
  stroke(255);
  seedTracers(100);
}

void draw() {
  for ( Tracer t : tracers) {
    int preX = t.x;
    int preY = t.y;

    t.move();
    stroke(255);
    line(preX, preY, t.x, t.y);
    stroke(100);
    line(preX+1, preY+1, t.x+1, t.y+1);
  }
  
  if(millis() > 5000) { save("tracers.png");}
}

void seedTracers(int count) {
  for (int i=0; i <count; i++) {
    Tracer t = new Tracer();
    t.x=(int)map(i, 0, count, 0, width);
    t.y=height-1;
    //t.threshold=(int)random(50, 200);
    //t.threshold=(int)(-10*pow((map(i,0,count,0,8)-4),2)+150);
    t.threshold=(int)(randomGaussian()*50+100);
    tracers.add(t);
  }
}


class Tracer {
  int x, y, threshold;

  void move() {
    if ( threshold > 0) {
      float r =  random(10);
      if ( r > 5) {
        up();
      } else if (r > 2.5) {
        left();
      } else {
        right();
      }

      threshold--;
    }
  }

  void left() {
    if (x-10 < 0) {
      move();
    } else { 
      x-=10;
    }
  }
  void right() {
    if (x+10 > width) {
      move();
    } else { 
      x+=10;
    }
  } 
  void up() {
    if (y-10 < 0) {
      threshold=0;
    } else { 
      y-=10;
    }
  }
}

