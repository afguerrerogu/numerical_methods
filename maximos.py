import math

pi=math.pi

N=101
nx=(2*pi)/(N-1)
ny=(pi)/(N-1)
print((nx,ny))
 
fmax=-1000
fmin=1000

def funcion(a,b):
    v=math.sin(a)*math.cos(a)-math.cos((b/2)+(pi/3))
    return v
print(funcion(pi,pi))

for i in range (0,N):
    x=(-pi)+nx*float(i)
    for j in range (0,N):
        y=(-pi/2)+ny*float(j)
        fun=funcion(x,y)
        if fun>fmax:
            fmax=fun
        if  fun<fmin:
            fmin=fun

print(fmax,fmin)

