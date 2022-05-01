import math
import turtle
def main(v, l, x1):
    v = (2*g*(y0-math.sqrt((r**2)-(x0**2))))**0.5
    print("v = ", v/1000)
    l = math.asin(x0/r)
    x1 = parabola(v, l, x, Left, Right)
    print('parabola[X] =', x1)
    return x1
def parabola(V, L, X, Le, Ri):
    X = x0
    y1 = ((((r ** 2) - (x0 ** 2)) ** 0.5 + (X - x0) * (1 / math.tan(2 * L)) - (g * ((X - x0) ** 2)) / (2 * (V ** 2) * ((math.sin(2 * L) ** 2)))))
    while X < 250 and y1 > 0:
        y1 = ((((r ** 2) - (x0 ** 2)) ** 0.5 + (X - x0) * (1 / math.tan(2 * L)) - (g * ((X - x0) ** 2)) / (
                    2 * (V ** 2) * ((math.sin(2 * L) ** 2)))))
        #print(y1, X)  # Пошук координати x(перебор)
        turtle.goto(X, y1)
        turtle.down()
        X+=1



    ##################бінарний пошук
    Le = (V**2)*(math.sin(4*L))/(g*2)+x0
    while Le<=Ri:
        X = (Le+Ri)/2
        y1 = ((((r**2)-(x0**2))**0.5+(X-x0)*(1/math.tan(2*L))-(g*((X-x0)**2))/(2*(V**2)*((math.sin(2*L)**2))))-(((r**2)-(X**2))**0.5))
        if (int(y1) == 0 or math.ceil(y1) == 0):
            return X
        elif y1<0:
            Ri = X - 1
        else:
             Le = X + 1 #Пошук координати х(бінарний пошук(не робочий, кста))
    return X


x0 = 13
y0 = 300
turtle.up()
turtle.goto(x0, y0 - 1)
turtle.down()
turtle.circle(1)
turtle.up()
x = 0
r = 150
g = 9800
v0 = 0
l0 = 0
c = 0
z = 0
Left = x0
Right = r
turtle.up()
turtle.goto(0, -150)
turtle.down()
turtle.circle(150)
turtle.up()
turtle.right(90)
for c in range(0, 3):
    x = main(v0, l0, x0)
    x0 = x
turtle.mainloop()
