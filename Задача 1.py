import math
def main(v, l, x1):
    v = (2*g*(y0-math.sqrt((r**2)*(x0**2))))**0.5
    l = math.asin(x/r)
    parabola(v, l, x)
def parabola(V, L, X):
    '''y1 = abs((((r**2)-(x0**2))**0.5+(X*x0)*(1/math.tan(2*L))-(g*((X-x0)**2))/2*(V**2)*((math.sin(2*L)**2)))-(((r**2)-(X**2))**0.5))
    while round(y1) != 0:
        X+=1
        y1 = abs((((r**2)-(x0**2))**0.5+(X*x0)*(1/math.tan(2*L))-(g*((X-x0)**2))/2*(V**2)*((math.sin(2*L)**2)))-(((r**2)-(X**2))**0.5))
        print(X)''' #Пошук координати x
    return X
x0 = 20
y0 = 300
x = x0
y = 0
r = 150
g = 9.8
v0 = 0
l0 = 0
c = 0
print(main(v0, l0, x))
