from graph import *
import math

def color(x):
    penColor(x)
    brushColor(x)
def sectors(x,y,phi,r, bg, fg):
    color(fg)
    circle(x,y,r)
    color(bg)
    epsilon=math.pi/500
    chi=phi[1]
    i=1
    while chi<phi[0]+2*math.pi:
        polygon([[x,y],[x+r*math.cos(chi),y+r*math.sin(chi)],[x+r*math.cos(chi+epsilon),y+r*math.sin(chi+epsilon)]])
        chi=chi+epsilon
        if not len(phi)==i+1 and chi>phi[i+1]:
            chi=phi[i+2]
            i=i+2
def dichotomy(x,y,N,alpha,l,q,delta):
    if N==0:
        return
    line(x,y,x+l*math.cos(alpha),y+l*math.sin(alpha))
    dichotomy(x+l*math.cos(alpha),y+l*math.sin(alpha),N-1,alpha+delta,q*l,q,delta)
    dichotomy(x+l*math.cos(alpha),y+l*math.sin(alpha),N-1,alpha-delta,q*l,q,delta)
windowSize(10000,10000)
canvasSize(10000,10000)
penSize(0)
color("white")
color("yellow")
rectangle(0,0,10000,900)
alpha=[math.pi]
while alpha[-1]<2*math.pi:
    alpha.append(alpha[-1]+math.pi/200)
#del alpha[-1] #needed if n=20
sectors(1000,900,alpha,1000,"yellow","red")
color("yellow")
circle(1000,900,630)
color("red")
circle(1000,900,600)
color("purple")
penSize(12)
dichotomy(1000,900,15,-math.pi/2,300,0.6,math.pi*0.3)
dichotomy(100,900,15,-math.pi/2,100,0.8,math.pi*0.05)
color("green")
rectangle(0,900,10000,10000)
color("cyan")
dichotomy(300,920,15,-math.pi/2+math.pi/15,200,0.7,math.pi*0.1)
color("orange")
dichotomy(1500,1000,19,-math.pi/2-math.pi/10,100,0.8,math.pi*0.2)

run()
