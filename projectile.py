Web VPython 3.2

g=9.8 #gravity

mycanvas= canvas(title="Projectile Motion", x=0, y=0, height=400, width=400)

ball = sphere(canvas=mycanvas ,radius=0.5, color=color.red, make_trail= True, trail_color= color.red,pos= vector(-200,0,0))
ground = box(color=color.green, size=vector(400, 10, 0), pos=vector(0, -5, 0))
v0 = float(input("Enter Initial Velocity: "))
ang = float(input("Enter the angle of projection(in Degree): "))
ang_r = radians(ang)
speed_label = label(pos= ball.pos + vector(0, 10, 0), text="0 m/s")


time =0
dx=0.01
v0x= v0*cos(ang_r)
v0y= v0*sin(ang_r)

while(ball.pos.y>=0):
    rate(100)
    ball.pos.y = v0y*time - (1/2)*g*time**2
    ball.pos.x =-200+ v0x*time
    vx=v0x
    vy=v0y-g*time
    speed= mag(vector(vx,vy,0))
    speed_label.pos= ball.pos + vector(0,10,0)
    speed_label.text = f"{speed:.2f} m/s"
    time=time+dx

label(pos=vector(0,-100,0),text=f"The total time taken: {time:.2f} sec \nThe total distance covered in X-axis: {ball.pos.x+200:.2f} m")
