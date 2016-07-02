//iPhoneWall

size(640, 1136);
noFill();
background(#676CB7);
stroke(230);

for (float i=-100; i<height+200; i+=15) {
  float x = map(i, 0, 1136, 0, 2*37);
  ellipse(width/2, i, 300, 50);
  
}

