from graph import *
import math
import random as rm


#Window settings
windowSize(500, 500)
canvasSize(500, 500)
penSize(0)

#sets compleat color of your pen
def color(x):
    penColor(x)
    brushColor(x)

#Creates sectors
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

#Array that keeps tree to make it deletable
#obj = []

#Tree-fractal function
def dichotomy(x,y,N, N0, alpha,l,q,delta, obj):
    if N==0:
        return
    if N >= N0 - 3:
        color("brown")
    else:
        color("green")
    penSize(N)
    rnd_l = rm.uniform(0.97, 1.04)
    rnd_a = rm.uniform(0.95 +0.04, 1.05 - 0.04)
    alpha*=rnd_a
    rnd_d = rm.uniform(0.95 +0.05, 1.05 - 0.05)
    delta*=rnd_d
    obj.append(line(x,y,x+l*math.cos(alpha),y+l*math.sin(alpha)))
    dichotomy(x+l*math.cos(alpha),y+l*math.sin(alpha),N-1, N0, alpha+delta,q*l*rnd_l,q,delta, obj)
    dichotomy(x+l*math.cos(alpha),y+l*math.sin(alpha),N-1, N0, alpha-delta,q*l*rnd_l,q,delta, obj)
    dichotomy(x+l*math.cos(alpha),y+l*math.sin(alpha),N-1, N0, alpha,q*l*rnd_l,q,delta, obj)


#Draws a tree
def tree(x, y, l, N, q, obj):

    for i in obj:
        deleteObject(i)
    color("green")
    dichotomy(x, y ,N, N, -math.pi/2, l ,q,math.pi*0.2, obj)

#River
def river():
    p = ([])
    p.append([500*0.5, 500*(0.5)])
    p.append([500*(0.5 - 0.25), 500*(0.5 + 0.25)])
    p.append([500*(0.5 - 0.1), 500*(0.5 + 0.3)])
    p.append([500*(0.5 - 0.3), 500*(0.5 + 0.5)])
    p.append([500*(0.5 + 0.05), 500*(0.5 + 0.5)])
    p.append([500*(0.5 + 0.15), 500*(0.5 + 0.26)])
    p.append([500*(0.5 - 0), 500*(0.5 + 0.2)])

    color('blue')
    polygon(p)



def main():
    color("yellow")
    rectangle(0,0,500, 500)


    alpha=[math.pi]
    while alpha[-1]<2*math.pi:
        alpha.append(alpha[-1]+math.pi/50)

    #Sun
    sectors(250,250,alpha, 400,"yellow","red")
    color("yellow")
    circle(250, 250, 60)
    color("red")
    circle(250,250,40)

    #Dirt
    color("#FC7C0C")
    rectangle(0, 500, 500, 250)

    river()

    obj1 = []
    obj2 = []
    obj3 = []
    tree(500*(0.6), 500*(0.5 + 1/5), 45, 7, 0.7, obj2)
    tree(500*(0.3), 500*(0.5 + 1/3), 50, 7, 0.8, obj1)
    tree(500*(0.8), 500*(0.5 + 0.4), 46, 7, 0.75, obj3)



onTimer(main, 1)
run()
