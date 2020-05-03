def setup():
    size(500,500)
    cantor(10, 20, width-20);

def cantor(x, y, len):
    strokeWeight(3)
    if len >=1:
        line(x, y, x+len, y)
        
        y+=20
        
        cantor(x, y, len/3)
        cantor(x+len*2/3, y, len/3)
        
        
        
        
