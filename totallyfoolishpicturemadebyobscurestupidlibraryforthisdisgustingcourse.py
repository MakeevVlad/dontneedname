from graph import *
import math
from time import sleep

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
    myln=line(x,y,x+l*math.cos(alpha),y+l*math.sin(alpha))
    if N==1:
        return [myln]
    else:
        leftb=dichotomy(x+l*math.cos(alpha),y+l*math.sin(alpha),N-1,alpha+delta,q*l,q,delta)
        rightb=dichotomy(x+l*math.cos(alpha),y+l*math.sin(alpha),N-1,alpha-delta,q*l,q,delta)
        return [myln,[leftb,rightb]]
def dichofill(obj,x,y,N,alpha,l,q,delta):
    obj.append(line(x,y,x+l*math.cos(alpha),y+l*math.sin(alpha)))
    if N==1:
        return
    else:
        obj.append([[],[]])
        dichofill(obj[1][0],x+l*math.cos(alpha),y+l*math.sin(alpha),N-1,alpha+delta,q*l,q,delta)
        dichofill(obj[1][1],x+l*math.cos(alpha),y+l*math.sin(alpha),N-1,alpha-delta,q*l,q,delta)
def deltree(tree,N):
    if N==1:
        deleteObject(tree[0])
        del tree
    else:
        deltree(tree[1][0],N-1)
        deltree(tree[1][1],N-1)
        del tree[1]
        deleteObject(tree[0])
        del tree[0]
def depth(tree,corr): #uniform trees only, corr=0 initially
    if len(tree)==0:
        return corr
    elif len(tree)==1:
        return 1+corr
    else:
        return depth(tree[1][0],corr+1)
def levelup(tree,x,y,alpha,l,q,delta):
    if len(tree)==0:
        tree.append(line(x,y,x+l*math.cos(alpha),y+l*math.sin(alpha)))
    elif len(tree)==1:
        leftb=line(x+l*math.cos(alpha),y+l*math.sin(alpha),
                   x+l*math.cos(alpha)+q*l*math.cos(alpha+delta),y+l*math.sin(alpha)+q*l*math.sin(alpha+delta))
        rightb=line(x+l*math.cos(alpha),y+l*math.sin(alpha),
                    x+l*math.cos(alpha)+q*l*math.cos(alpha-delta),y+l*math.sin(alpha)+q*l*math.sin(alpha-delta))
        tree.append([[leftb],[rightb]])
    else:
        levelup(tree[1][0],x+l*math.cos(alpha),y+l*math.sin(alpha),alpha+delta,l*q,q,delta)
        levelup(tree[1][1],x+l*math.cos(alpha),y+l*math.sin(alpha),alpha-delta,l*q,q,delta)
def leveldown(tree):
    if len(tree)==0:
        return
    elif len(tree)==1:
        deleteObject(tree[0])
        del tree[0]
    elif len(tree[1][0])==1:
        deleteObject(tree[1][0][0])
        deleteObject(tree[1][1][0])
        del tree[1][1]
        del tree[1][0]
        del tree[1]
    else:
        leveldown(tree[1][0])
        leveldown(tree[1][1])
def blinktree():
    if grow[0]:
        levelup(tree,1600,950,-math.pi/2-math.pi/10,200,0.7,math.pi/9)
        if depth(tree,0)==8:
            grow[0]=False
    else:
        leveldown(tree)
        if depth(tree,0)==0:
            grow[0]=True
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
dichotomy(1000,900,19,-math.pi/2,300,0.6,math.pi*0.3)
dichotomy(100,900,19,-math.pi/2,100,0.8,math.pi*0.05)
color("green")
rectangle(0,900,10000,10000)
color("cyan")
dichotomy(300,920,15,-math.pi/2+math.pi/15,200,0.7,math.pi*0.1)
color("orange")
tree=[]
grow=[True] #xtremely dirty!!
onTimer(blinktree,1000)


run()
