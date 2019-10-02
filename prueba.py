import math 
import pylab

g=9.8
xmaximo=1


va=20.0
vb=40.0
nv=501
deltav=(vb-va)/float(nv-1)
print(deltav)
iv=[0.0]*nv
Aa=0
Ab=math.pi/2.0
nA=101
deltaA=(Ab-Aa)/float(nA-1)
print(deltaA)
def ft(vi,Ai):
    ti=(2*vi*math.sin(Ai)/g)
    return ti
def fx(vi,Ai,ti):
    xi=vi*math.cos(Ai)*ti
    return xi


for i in range (0,nv):
    v=va+deltav*float(i)
    print (v)
    for j in range(0,nA):
        A=Aa+deltaA*float(i)
        t=ft(v,A)
        x=fx(v,A,t)
        print(v)
        if x>xmaximo:
            xmaximo=x
print (xmaximo)




