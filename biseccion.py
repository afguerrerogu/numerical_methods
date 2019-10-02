import math

def fun(a):
    p=a**3+4.0*a**(2)-10
    return p
print(fun(1.3475))

xa=1.0
xb=2.0
tol=10e-5
imax=30

for i in range(imax): 
    s=(xa+xb)/2
    t=fun(s)
    v=math.fabs(xa-xb)
    print xa,xb,s,t,v
    if (fun(xb)*fun(s))<0:
        xb=s
    else:
        xa=s
        
print(float(-6)**(1/3))    
