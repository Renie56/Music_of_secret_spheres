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
    #print('parabola[X] =', x)
def parabola():
    global v0, l0, x, Left, Right, q
    x = None
    if math.sin(4*l0)>0:
        Left = (v0**2)*math.sin(4*l0)/(g*2)+x0
        Right = r
        #print('Left:', Left, 'Right:', Right)
        while Left<=Right and (x==None or x<r):
            x = (Left+Right)/2
            y = ((((r**2)-(x0**2))**0.5+(x-x0)*(1/math.tan(2*l0))-(g*((x-x0)**2))/(2*(v0**2)*((math.sin(2*l0)**2))))-(((r**2)-(x**2))**0.5))
            #print(y)
            if (int(y) == 0 or math.ceil(y) == 0):
                q+=1
                '''turtle.showturtle()
                graf_parabola()
                turtle.hideturtle()'''
                break
            elif y<0:
                Right = x-0.0000001
            else:
                Left = x+0.0000001
def grafics():
    global x0, y0
    turtle.up()
    turtle.goto(r, 0)
    turtle.down()
    turtle.left(90)
    turtle.circle(r, r*1.2)
    turtle.up()
    turtle.right(180)
    turtle.goto(-(a/2), 0)
    turtle.down()
    turtle.goto(a/2, 0)
    turtle.up()
    turtle.goto(x0, y0)
    turtle.down()
    turtle.goto(x0, r)
    turtle.up()
    turtle.shape('circle')
def graf_parabola():
    global l0, v0, y
    x1 = x0
    y = ((((r ** 2) - (x0 ** 2)) ** 0.5 + (x1 - x0) * (1 / math.tan(2 * l0)) - (g * ((x1 - x0) ** 2)) / (2 * (v0 ** 2) * ((math.sin(2 * l0) ** 2)))))
    #print('Кінець параболи:', x1, round(x, 2))
    while x1 <= round(x, 2) and y >= 0:
        y = ((((r ** 2) - (x0 ** 2)) ** 0.5 + (x1 - x0) * (1 / math.tan(2 * l0)) - (g * ((x1 - x0) ** 2)) / (2 * (v0 ** 2) * ((math.sin(2 * l0) ** 2)))))
        turtle.goto(x1, y)
        turtle.down()
        x1+=0.1
def borders(a):
    global x0, y0, x, q, Left, Right
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
            Le = x00+0.0000001
        else:
            Ri = x00-0.0000001
    return Ri
q = 1
w = 0.001415
p = 1.6
x0 = 0
y0 = 300
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
while y0<=1000:
    mx = borders(0)
    mn = borders(1)
    print('Висота:', y0, 'Від:', mn, 'До:', mx)
    y0+=10
#grafics()
#turtle.mainloop()
