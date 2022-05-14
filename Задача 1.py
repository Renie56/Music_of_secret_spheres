import decimal
import math
import turtle
from decimal import Decimal, ROUND_HALF_DOWN, ROUND_HALF_UP


def main():
    global v0, l0, x0, x, x1
    '''v00 = 5 * l/1.5708
    v0 = ((2*g*(y0-math.sqrt(((r+R)**2)-(x0**2))))**0.5)+v00
    v0 *= 0.82 ** q'''
    if q == 0:
        print("degrees(l0):", math.degrees(l0))
        v0 = 5 + math.degrees(l0) * 5 / 90
        # l0 = math.radians(90) - 2 * math.atan(x0 / (((r+R)**2 - x0**2)**0.5))
        print('Швидкість:', v0)
        print('кут:', math.degrees(l0))
        parabola1()
    else:
        if q > 1:
            tg_b = -x / ((((r + R) ** 2) - (x ** 2)) ** 0.5)
            b = math.atan(tg_b)
            if b < 0:
                b += math.pi
            print("b:", math.degrees(b))
            tg_u = (math.tan(l0)) + (g * (x - x0) / ((v0 ** 2) * (math.cos(l0) ** 2)))
            print('tg_u:', tg_u)
            print('(math.tan(l0)):', (math.tan(l0)))
            print('ll', math.degrees(l0))
            print("2:", (g * (x - x0) / ((v0 ** 2) * (math.cos(l0) ** 2))))
            print('x:', x, 'x0:', x0, 'v0:', v0, 'math.cos(l0):', math.cos(l0))
            u = math.atan(tg_u)
            if u < 0:
                u += math.pi
            u = math.pi - u
            print("u:", math.degrees(u))
            if x > 0:
                l0 = 2 * b - math.radians(180) - u
                print("м'яч впаде у додатніх іксах")
            elif x < 0:
                l0 = u - 2 * b
                l0 = math.radians(180) - l0
                print("м'яч впаде у від'ємних іксах іксах")
            print("l0:", math.degrees(l0))
        parabola()
        # print("tg_b:", tg_b, "tg_u:", tg_u)
        # print("tg_b:", b, "tg_u:", u)
        # print("tg_b:", math.degrees(b), "tg_u:", math.degrees(u))


def parabola1():
    global v0, l0, x, Left, Right, q, counter, x0, y0
    x = None
    print('v0:', v0)
    if (v0 == 0 and abs(x0) < (r + R)):
        x = x0
        q += 1
        v0 = ((2 * g * (y0 - math.sqrt(((r + R) ** 2) - (x0 ** 2)))) ** 0.5)
        turtle.up()
        turtle.goto(x0, y0)
        turtle.down()
        turtle.goto(x0, r + R)
        turtle.up()
        v0 *= 0.82
        l0 = math.radians(90)-math.asin((x)/((((r + R) ** 2) - (x ** 2)) ** 0.5))
        if x < 0:
            v0*=-1
        print("l0:", math.degrees(l0), "v:", v0)
    else:
        Left = x0
        Right = (r + R)
        y = 0
        counter = 0
        # print('Le:', Left, 'Ri:', Right)
        while Left <= Right and (x == None or x < (r + R)):
            x = (Left + Right) / 2
            y1 = y
            y = y0+ (x - x0) * (math.tan(l0)) - (g * ((x - x0) ** 2)) / (2 * (v0 * math.cos(l0)) ** 2) - ((((r + R) ** 2) - (x ** 2)) ** 0.5)
            print('y:', y, 'x:', x, 'L:', Left, 'R:',Right, "v0:", v0)
            #print('y0:', y0, 'x- x0 * (math.tan(l0)):', (x- x0)* (math.tan(l0)), '(g...:', (g * ((x - x0) ** 2)) / (2 * (v0 ** 2) * ((math.cos(l0) ** 2))), 'kolo:',((((r + R) ** 2) - (x ** 2)) ** 0.5))
            number = Decimal(y)
            if y == y1:
                counter += 1
            if counter > 5 :
                Right = x - 1e-15
            elif counter > 5 and y > 0:
                Left = x + 1e-15
            elif abs(y) < 100 and number.quantize(Decimal("1.00000000"), ROUND_HALF_DOWN) == 0:
                graf_parabola()
                q += 1
                break
            elif y < 0 and v0 > 0:
                Right = x - 1e-30
            elif y > 0 and v0 > 0:
                Left = x + 1e-30
            elif y < 0 and v0 < 0:
                Left = x + 1e-30
            else:
                Right = x - 1e-30

        '''vy1 = v0 * math.sin(l0)
        vpy =((2*g*(y0-math.sqrt(((r+R)**2)-(x0**2))))**0.5) * math.sin(l0)'''
        vx1 = v0 * math.cos(l0)
        vy1 = v0 * math.sin(l0)
        vy1*=-1
        print('vx1:', vx1,'vy1:', vy1)
        tg_b = -x / ((((r + R) ** 2) - (x ** 2)) ** 0.5)
        b = math.atan(tg_b)
        if b < 0:
            b += math.pi
        print("b:", math.degrees(b))
        tg_u = (math.tan(l0)) + (g * (x - x0) / ((v0 ** 2) * (math.cos(l0) ** 2)))
        u = math.atan(tg_u)
        if u < 0:
            u += math.pi
        u = math.pi - u
        print("u:", math.degrees(u))
        if x > 0:
            l0 = 2 * b - math.radians(180) - u
            print("м'яч впаде у додатніх іксах")
        elif x < 0:
            l0 = u - 2 * b
            l0 = math.radians(180) - l0
            print("м'яч впаде у від'ємних іксах іксах")
        #print('y0:', y0)
        vp = ((2 * g * (y0 - math.sqrt(((r + R) ** 2) - (x ** 2))))) ** 0.5
        print('l0:', math.degrees(l0))
        vx = vx1 + (vy1 + vp) * math.cos(l0)
        vy = (vy1 + vp) * math.sin(l0)
        print("v_only_x:", vx)
        if vx < 0:
            v0 = vx / -math.cos(l0)
        else:
            v0 = (vx**2+vy**2)**0.5
            l0 = math.asin(vy/v0)
        print("v_abs:", v0)
        print('l0:', math.degrees(l0))
        print("vp:", vp)
        v0 *= 0.82
        print("v:", v0)


def parabola():
    global v0, l0, x, Left, Right, q, counter
    x = None
    if v0 > 0:
        Left = (v0 ** 2) * math.sin(2 * l0) / (g * 2) + x0
        Right = (r + R)
    else:
        Left = -(r + R)
        Right = (v0 ** 2) * math.sin(2 * l0) / (g * 2) + x0

    if (abs(Left) * 2 < R+r and v0 > 0) or abs(Right)* 2 < R+r and v0 < 0:
        print("v0:", v0)
        y = 0
        counter = 0
        print('Le:', Left, 'Ri:', Right)
        print(math.degrees(l0))
        #l0 = math.radians(180) - l0
        #l0*=-1
        #print(math.degrees(l0))
        while Left <= Right and (x == None or abs(x) < abs((r + R))):
            x = (Left + Right) / 2
            y1 = y
            y = (((r+R)**2)-(x0**2))**0.5 + (x - x0) * (math.tan(l0)) - (g * ((x - x0) ** 2)) / (2 * (v0 * math.cos(l0)) ** 2) - ((((r + R) ** 2) - (x ** 2)) ** 0.5)
            print('y:', y, 'x:', x, 'L:', Left, 'R:', Right, "v0:", v0)
            number = Decimal(y)
            if y == y1:
                counter += 1
                # print(counter)
            if counter > 5:
                if y < 0 :
                    Right = x - 1e-10
                else:
                    Left = x + 1e-10
            elif y < 100 and number.quantize(Decimal("1.00000"), ROUND_HALF_DOWN) == 0:
                graf_parabola()
                q += 1
                break
            elif y > 0:
                if v0 > 0:
                    Left = x + 1e-30
                else:
                    Right = x - 1e-30
            elif y < 0:
                if v0 > 0:
                    Right = x - 1e-30
                else:
                    Left = x + 1e-30
        if x != None:
            print('priv_v0:', v0, 'x0:', x0)
            print("x:", x, "x0:", x0)
            if v0 > 0 and x0 > x :
                v0 += (abs(2 * g * (((r + R) ** 2 - (x0) ** 2) ** 0.5 - ((r + R) ** 2 - (x) ** 2) ** 0.5))) ** 0.5
            elif v0 < 0 and x0 > x:
                v0 -= (2 * g * (((r + R) ** 2 - (x0) ** 2) ** 0.5 - ((r + R) ** 2 - (x) ** 2) ** 0.5)) ** 0.5
            elif v0 > 0 and x0 < x :
                v0 -= (abs(2 * g * (((r + R) ** 2 - (x0) ** 2) ** 0.5 - ((r + R) ** 2 - (x) ** 2) ** 0.5))) ** 0.5
            elif v0 < 0 and x0 < x:
                v0 += (2 * g * (((r + R) ** 2 - (x0) ** 2) ** 0.5 - ((r + R) ** 2 - (x) ** 2) ** 0.5)) ** 0.5
            print('x', x, 'x0', x0)
            print('f:', ((r + R) ** 2 - (x0) ** 2) ** 0.5, "s:",  ((r + R) ** 2 - (x) ** 2) ** 0.5)
            print('first:', ((r + R) ** 2 - (x0) ** 2) ** 0.5 - ((r + R) ** 2 - (x) ** 2) ** 0.5, 'second:', 2 * g)
            print('n_v0:', v0)
            v0 *= 0.82 ** q
            print("у ітерацію %d швидкість " %(q), v0)


def borders(a):
    global x0, y0, x, q, Left, Right, x00, x1
    Le = w
    Ri = p
    Left = x0
    Right = (r + R)
    while Le != Ri and Le < Ri:
        x00 = (Le + Ri) / 2
        x0 = x00
        q = 1
        while x != None and x < (r + R):
            x1 = x0
            main()
            x0 = x
        x = 0
        if q >= 3 + a:
            Le = x00 + 0.000000001
        else:
            Ri = x00 - 0.000000001
    return Ri


def grafics():
    global x0, y0
    turtle.up()
    turtle.goto((r + R), 0)
    turtle.down()
    turtle.left(90)
    turtle.circle((r + R), (r) * 1.2)
    # turtle.shape('circle')


def hoh():
    turtle.up()
    turtle.goto(-10, y0)
    turtle.down()
    turtle.goto(10, y0)
    turtle.up()


def graf_parabola():
    global y, x1
    x1 = x0
    y = y0 + (x1 - x0) * (math.tan(l0)) - (g * ((x1 - x0) ** 2)) / (2 * (v0 * math.cos(l0)) ** 2)
    if q == 0:
        turtle.up()
        turtle.goto(x1, y)
    turtle.down()
    print("q:", q, "x1:", x1, "v0:", v0)
    print('Кінець параболи:', x1, x, y)
    if v0 < 0 and ((k < -70 and q == 0) or (abs(abs(x)-abs(x0)) < 0.5)):
        x1 -= 0.0001
    elif v0 > 0 and ((k < -70 and q == 0) or (abs(abs(x)-abs(x0)) < 0.5)):
        x1 += 0.0001
    elif v0 < 0:
        x1 -= 0.1
    else:
        x1 += 0.1
    while y >= (((r + R) ** 2) - (x ** 2)) ** 0.5:
        if q == 0:
            y = y0 + (x1 - x0) * (math.tan(l0)) - (g * ((x1 - x0) ** 2)) / (2 * (v0 * math.cos(l0)) ** 2)
        else:
            y = (((r + R) ** 2) - (x0 ** 2)) ** 0.5 + (x1 - x0) * (math.tan(l0)) - (g * ((x1 - x0) ** 2)) / (2 * (v0 * math.cos(l0)) ** 2)
        print("y:", y, x, x1)
        turtle.goto(x1, y)
        if v0 < 0 and ((k < -70 and q == 0) or (abs(abs(x) - abs(x0)) < 0.5)):
            x1 -= 0.001
        elif v0 > 0 and ((k < -70 and q == 0) or (abs(abs(x) - abs(x0)) < 0.5)):
            x1 += 0.001
        elif v0 < 0:
            x1 -= 0.1
        else:
            x1 += 0.1
    turtle.up()


def answer2():
    global y0
    while y0 <= 1000:
        mx = borders(0)
        # turtle.goto(x00 * 10, y0 // 10)
        # print("x правої границі :", x00*100, "y правої границі :", y0//10)
        # turtle.down()
        y0 += 10
    # turtle.up()
    y0 = 300
    while y0 <= 1000:
        mn = borders(1)
        # turtle.goto(x00 * 10, y0 // 10)
        # print("x лівої границі :", x00 * 100, "y лівої границі :", y0 // 10)
        # turtle.down()
        y0 += 10
    # border()


def answer1():
    global x1, x0
    turtle.up()
    #hoh()
    grafics()
    coordinats()
    nemb = Decimal(x)
    while x != None and nemb.quantize(Decimal("1.00"), ROUND_HALF_UP) < (r + R):
        main()
        nemb = Decimal(x)
        x1 = x0
        x0 = x
        print("x1:", x1, "x0:", x0, 'q:', q, "x", x, nemb.quantize(Decimal("1.00"), ROUND_HALF_UP), (r+R))
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj")
        if q > 7:
            print("забагато відскоків")
            break
        print(nemb.quantize(Decimal("1.00"), ROUND_HALF_UP), (r+R))
        ab = nemb.quantize(Decimal("1.00"), ROUND_HALF_UP)
        if ab >= (r+R):
            print('ccccccccccccccc')
            break
    turtle.mainloop()


def border():
    turtle.up()
    turtle.goto(182 * 10, 15 // 10)
    turtle.down()
    turtle.left(90)
    turtle.forward(80)


def coordinats ():
    turtle.up()
    turtle.goto(-500, 0)
    turtle.down()
    turtle.goto(500, 0)
    turtle.up()
    turtle.goto(0, -500)
    turtle.down()
    turtle.goto(0, 500)


q = 0
counter = 0
d = 40.3
R = d / 2
a = 400
w = 0.003
p = 7
x0 = 15
y0 = 300
k = 0
l0 = math.radians(k)
x00 = 0
x = 0
r = 150
g = 9800
v0 = 0
c = 0
mx = 0
mn = 0
Left = 0
'''turtle.up()
turtle.goto(156.51939972894036, 0)
turtle.down()
turtle.goto(156.51939972894036, 200)
turtle.up()'''
print("x0:", x0, "y0:", y0, "l0(до горизонту):", math.degrees(l0))
Right = (r + R)
answer1()
turtle.mainloop()
