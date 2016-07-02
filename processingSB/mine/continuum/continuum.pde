//continuum

size(1366, 786);
noFill();
background(#446C40);
stroke(230);

for (float i=-100; i<width+200; i+=15) {
  ellipse(i, .5*i, (500-i), 100);
}
save("continuum.png");
