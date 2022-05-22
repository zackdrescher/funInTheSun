size(1024, 1024)
noFill()
background(152,190,100)
noSmooth()

center = 1024 / 2
sphere_w = 384 * 2
steps = 20
step_w = sphere_w / 20

for i in range(steps + 1):
    w = i * step_w
    ellipse(center, center, w, sphere_w)
    
save("orb.png") 
