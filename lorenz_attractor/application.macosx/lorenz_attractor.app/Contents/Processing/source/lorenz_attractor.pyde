# REFERENCES
# http://paulbourke.net/fractals/lorenz/

x = 0.01
y = 0
z = 0
shades = 10


# contants sigma=a, ro=b, and beta=c
A = 10
B = 28
C = 8 / 3

points = PVector(x, y, z)


def setup():
    size(700, 700, P3D)
    background(0)

def draw():

    # for handlling time
    dt = 0.01

    # formulas
    global x, y, z, shades
    dx = (A * (y - x)) * dt
    dy = (x * (B - z) - y) * dt
    dz = (x * y - C * z) * dt
    x += dx
    y += dy
    z += dz
    # print(x, y, z)

    points.add(x, y, z)
    print(points)
    
    translate(width / 2, height / 2)
    scale(5)
    stroke(255)
    
    for v in points:    # for (PVector v : points)
        stroke(150, 0, shades)
        point(x,y,z)     # point(v.x, v.y, v.z)
        shades += .5
        if shades > 255:
            shades=0
        print(shades)
    
