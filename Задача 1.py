import math
import turtle
def main():
    global v0, l0, x0, x
    v0 = (2*g*(y0-math.sqrt((r**2)-(x0**2))))**0.5
    if c == 0:
        l0 = math.asin(x0/r)
    else:
        b = -x0/(((r**2)-(x0**2))**0.5)
        u = (1/math.tan(2*l0))-(g*(x0-x1)/((v0**2)*(math.sin(2*l0)**2)))
        l0 = 180 + b - 2*u
    parabola()
    print('parabola[X] =', x)
def parabola():
    global v0, l0, x, Left, Right
    x = None
    if math.sin(4*l0)>0:
        Left = (v0**2)*math.sin(4*l0)/(g*2)+x0
        Right = r
        print('Le:', Left, 'Ri:', Right)
        while Left<=Right:
            x = (Left+Right)/2
            y = ((((r**2)-(x0**2))**0.5+(x-x0)*(1/math.tan(2*l0))-(g*((x-x0)**2))/(2*(v0**2)*((math.sin(2*l0)**2))))-(((r**2)-(x**2))**0.5))
            if (int(y) == 0 or math.ceil(y) == 0):
                break
            elif y<0:
                Right = x-0.01
            else:
                Left = x+0.01
    graf_parabola()
def grafics():
    global x0, y0
    turtle.up()
    turtle.goto(x0, y0 - 1)
    turtle.down()
    turtle.circle(1)
    turtle.up()
    turtle.goto(0, -r)
    turtle.down()
    turtle.circle(r)
    turtle.up()
    turtle.right(90)
    turtle.goto(0, 0)
    turtle.down()
    turtle.circle(1)
    turtle.up()
def graf_parabola():
    global l0, v0, y
    x1 = x0
    y = ((((r ** 2) - (x0 ** 2)) ** 0.5 + (x1 - x0) * (1 / math.tan(2 * l0)) - (g * ((x1 - x0) ** 2)) / (2 * (v0 ** 2) * ((math.sin(2 * l0) ** 2)))))
    while x1 <= x and y > 0:
        y = ((((r ** 2) - (x0 ** 2)) ** 0.5 + (x1 - x0) * (1 / math.tan(2 * l0)) - (g * ((x1 - x0) ** 2)) / (2 * (v0 ** 2) * ((math.sin(2 * l0) ** 2)))))
        turtle.goto(x1, y)
        turtle.down()
        x1+=1
x0 = 1
y0 = 470
x = 0
r = 450
g = 1
v0 = 0
l0 = 0
c = 0
Left = x0
Right = r
grafics()
while x!=None and math.ceil(x)<r:
    x1 = x0
    main()
    x0 = x
turtle.mainloop()
