global theta

def setup():
    size(500,500)

def draw():
    background(255)
    theta = map(mouseX,0,width,0,PI/2);
    translate(width/2, height)
    branch(100, theta)
    
def branch(len, theta):
  line(0, 0, 0, -len);
  translate(0, -len);
 
  len *= 0.66;
 
  if (len > 2):
    pushMatrix()
    rotate(theta)
    branch(len, theta)
    popMatrix()
 
    pushMatrix()
    rotate(-theta)
    branch(len, theta)
    popMatrix()
