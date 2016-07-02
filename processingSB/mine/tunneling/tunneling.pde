//tunneling

size(1366, 786);
noFill();
background(#423976);
stroke(255);

for ( float i=0; i<width+20; i+=15) {
  ellipse(i, height/2, 20, (250*abs((i/540)*sin(i/45)))+100);
}

