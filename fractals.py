def setup(): 
    size(60,600)
    
def draw(): 
    background(255)
    translate(300,500)
    y(100)
    
def y(sz): 
    line(0,0,0,-sz)
    translate(0,-sz)
    rotate(radians(30))
    line(0,0,0,-0.8*sz)     # right branch
    rotate(radians(-60))
    line(0,0,0,-0.8*sz)     # left branch
    rotate(radians(30))
    translate(0,sz) 