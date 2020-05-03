i = di = dj = 0 # deriviatives?
fn1, fn2, fn3 = random(20), random(20), random(20) # for colors
f = 10
 
def setup():
    global zmx1, zmx2, zmy1, zmy2
    size(500, 500)
    zmx1 = int(width / 4)
    zmx2 = 2
    zmy1 = int(height / 4)
    zmy2 = 2
 
def draw():
    global i
 
    if i <= width:
        i += 1
    x = float(i + di) / zmx1 - zmx2
    for j in range(height + 1):
        y = zmy2 - float(j + dj) / zmy1
        a = b = aa = bb = 0
        cr, ci = x, y
        n = 1
        while n < 200 and (aa + bb) < 4:
            aa = a * a
            bb = b * b
            a = 2 * a * b + ci
            b = bb - aa + cr
            n += 1
 
        # COLOR
        re = (n * fn1) % 255
        gr = (n * fn2) % 255
        bl = (n * fn3) % 255
        stroke(re, gr, bl)
        point(i, j)

def mousePressed():
    global zmx1, zmx2, zmy1, zmy2, di, dj
    global i, j
    background(200)
    xt, yt = mouseX, mouseY
    di = di + xt - width / 2.
    dj = dj + yt - height / 2.
    zmx1 = zmx1 * f
    zmx2 = zmx2 * (1. / f)
    zmy1 = zmy1 * f
    zmy2 = zmy2 * (1. / f)
    di, dj = di * f, dj * f
    i = j = 0
