import math
import turtle
from decimal import Decimal, ROUND_HALF_DOWN
def main():
    global v0, l0, x0, x, x1
    v0 = (2*g*(y0-math.sqrt((r**2)-(x0**2))))**0.5
    if q == 1:
        l0 = math.radians(90) - 2 * math.atan(x0 / ((r**2 - x0**2)**0.5))
    else:
        tg_b = -x0/(((r**2)-(x0**2))**0.5)
        b = math.atan(tg_b)
        if b < 0:
            b += math.pi
        tg_u = (math.tan(l0))-(g*(x0-x1)/((v0**2)*(math.cos(l0)**2)))
        u = math.atan(tg_u)
        if u < 0:
            u += math.pi
        l0 = 2*b - math.radians(180) - u
    parabola()
def parabola():
    global v0, l0, x, Left, Right, q, counter
    x = None
    if math.degrees(l0)>0:
        Left = (v0**2)*math.sin(2*l0)/(g*2)+x0
        Right = r
        y=0
        counter = 0
        while Left<=Right and (x==None or x<r):
            x = (Left+Right)/2
            y1=y
            y = (((((r**2)-(x0**2))**0.5+(x-x0)*(math.tan(l0))-(g*((x-x0)**2))/(2*(v0**2)*((math.cos(l0)**2)))))-(((r**2)-(x**2))**0.5))
            number = Decimal(y)
            if y == y1:
                counter += 1
            if counter > 4 and y < 0:
                Right = x - 1e-10
            elif counter > 4 and y > 0:
                Left = x + 1e-10
            elif number.quantize(Decimal("1.0000"), ROUND_HALF_DOWN) == 0 :
                q+=1
                break
            elif y<0:
                Right = x-1e-30
            else:
                Left = x+1e-30
def borders(a):
    global x0, y0, x, q, Left, Right, x00, x1
    Le = w
    Ri = p
    Left = x0
    Right = r
    while Le!=Ri and Le<Ri:
        x00 = (Le+Ri)/2
        x0 = x00
        q = 1
        while x!=None and x<r:
            x1 = x0
            main()
            x0 = x
        x = 0
        if q>=3+a:
            Le = x00+0.000000001
        else:
            Ri = x00-0.000000001
    return Ri
def grafics():
    global x0, y0
    turtle.up()
    turtle.goto(r, 0)
    turtle.down()
    turtle.left(90)
    turtle.circle(r, (r*1.2))
    turtle.up()
    turtle.right(180)
    turtle.goto(-(a/2), 0)
    turtle.down()
    turtle.goto((a/2), 0)
    turtle.up()
    turtle.goto(0, 500)
    turtle.down()
    turtle.goto(0, 0)
    turtle.up()
    #turtle.shape('circle')
def graf_parabola():
    global l0, v0, y
    x1 = x0
    y = ((((r ** 2) - (x0 ** 2)) ** 0.5 + (x1 - x0) * ( math.tan( l0)) - (g * ((x1 - x0) ** 2)) / (2 * (v0 ** 2) * ((math.cos( l0) ** 2)))))
    print('Кінець параболи:', x1, x)
    while x1 <= x and y >= 0:
        y = ((((r ** 2) - (x0 ** 2)) ** 0.5 + (x1 - x0) *  (math.tan( l0)) - (g * ((x1 - x0) ** 2)) / (2 * (v0 ** 2) * ((math.cos( l0) ** 2)))))
        turtle.goto(x1, y)
        turtle.down()
        x1+=0.1
q = 1
counter=0
a = 400
w = 0.0001415
p = 1.5
x0 = 0
y0 = 300
x00 = 0
x = 0
r = 150
g = 9.8
v0 = 0
l0 = 0
c = 0
mx = 0
mn = 0
Left = x0
Right = r
#turtle.up()
#grafics()
while y0<=1000:
    mx = borders(0)
    mn = borders(1)
    print('Висота:', y0, 'Від:', mn, 'До:', mx)
    y0+=10
'''turtle.up()
turtle.forward(100)
turtle.mainloop()'''
