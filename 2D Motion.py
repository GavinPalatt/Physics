Web VPython 3.2
a = vec (0,-9.81,0)
p0 = vec (0,0,0) # initial position 
v = vec (2,10,0) 
dt = 0.01
Xaxis = curve (pos = [vec(-10,0,0), vec(10,0,0)])
Yaxis = curve (pos = [vec (0,-10,0), vec(0,10,0)])
ball = sphere (radius = .5, color = color.red, pos = p0)
while True:
    # Find Velocity
    v = v + a * dt
    # Find new position
    ball.pos += v * dt
    sleep(dt)
    if (ball.pos.y <=0):
        v.y = -0.8 * v.y
