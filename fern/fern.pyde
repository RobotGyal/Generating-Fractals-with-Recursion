size(640, 640)
background(0)
 
x = 0
y = 0
 
for _ in range(100000):
    xt = 0
    yt = 0
    r = random(100)
 
    if r <= 1:
        xt = 0
        yt = 0.16 * y
    elif r <= 8:
        xt = 0.20 * x - 0.26 * y
        yt = 0.23 * x + 0.22 * y + 1.60
    elif r <= 15:
        xt = -0.15 * x + 0.28 * y
        yt = +0.26 * x + 0.24 * y + 0.44
    else:
        xt = +0.85 * x + 0.04 * y
        yt = -0.04 * x + 0.85 * y + 1.60
size(640, 640)
background(0)
 
x = 0
y = 0
 
for _ in range(100000):
    xt = 0
    yt = 0
    r = random(100)
 
    if r <= 1:
        xt = 0
        yt = 0.16*y
    elif r <= 8:
        xt = 0.20*x - 0.26*y
        yt = 0.23*x + 0.22*y + 1.60
    elif r <= 15:
        xt = -0.15*x + 0.28*y
        yt =    0.26*x + 0.24*y + 0.44
    else:
        xt =    0.85*x + 0.04*y
        yt = -0.04*x + 0.85*y + 1.60
 
    x = xt
    y = yt
 
    m = round(width/2 + 60*x)
    n = height-round(60*y)
 
    set(m, n, "#00ff00")
    x = xt
    y = yt
 
    m = round(width / 2 + 60 * x)
    n = height - round(60 * y)
 
    set(m, n, "#00ff00")
