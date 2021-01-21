from math import *
from time import sleep, time

def line(screen, brush, thickness, color, startPoint, angle, length):
    brush.pu()
    brush.goto(startPoint)
    brush.color(color, color)
    brush.pensize(thickness)

    brush.pd()
    brush.goto([startPoint[0] + cos(angle) * length, startPoint[1] + sin(angle) * length])
    screen.update()
    
def lineWindmill(screen, brush, thickness, color, centerPoint, startAngle, \
                 endAngle, length, angleSpeed, angleAccel, update=0.01):
    theta = startAngle
    while theta < endAngle:
        line(screen, brush, thickness, color, [centerPoint[0] - cos(theta) * (length/2), \
                                               centerPoint[1] - sin(theta) * (length/2)], \
             theta, length)
        sleep(update)
        brush.clear()
        theta += angleSpeed
        angleSpeed += angleAccel
    line(screen, brush, thickness, color, [centerPoint[0] - cos(theta) * (length/2), \
                                           centerPoint[1] - sin(theta) * (length/2)], \
         theta, length)
    screen.update()

def lineWindmillTime(screen, brush, thickness, color, centerPoint, startAngle, \
                     terminalTime, length, angleSpeed, angleAccel, update=0.01):
    t = 0
    while t < terminalTime:
        theta = startAngle + angleSpeed * t + (1/2) * angleAccel * pow(t, 2)
        line(screen, brush, thickness, color, [centerPoint[0] - cos(theta) * (length/2), \
                                               centerPoint[1] - sin(theta) * (length/2)], \
             theta, length)
        sleep(update)
        brush.clear()
        t += 1
    line(screen, brush, thickness, color, [centerPoint[0] - cos(theta) * (length/2), \
                                           centerPoint[1] - sin(theta) * (length/2)], \
        theta, length)
    return theta

def oscillLine(screen, brush, height, amplitude, period, terminalTime, gamma, additionalFunction, \
               update = 0.01, partition = 100):
    width = screen.window_width()
    t = 0
    w = (2 * pi) / period
    X = [x * (width/partition) for x in range(partition + 1)]
    while t <= terminalTime:
        centerY = -exp(-gamma * t) * amplitude * sin(w * t)
        brush.pu()
        brush.goto([0, height])
        brush.pd()
        amp = (2/width) * acosh(1+abs(centerY))
        for x in X:
            if centerY > 0:
                brush.goto([x, -cosh(amp * (x - width/2)) + height + centerY + 1])
            if centerY < 0:
                brush.goto([x, cosh(amp * (x - width/2)) + height + centerY - 1])
        brush.pu()
        additionalFunction()
        brush.pu()
        sleep(update)
        screen.update()
        brush.clear()
        t += 1

def fallingCircle(screen, brush, height, accel, radius, terminalTime, additionalFunction, update = 0.01):
    width = screen.window_width()
    t = 0
    startY = height + (1/2) * accel * pow(terminalTime, 2)
    while t < terminalTime:
        brush.pu()
        brush.goto([width/2, startY - (1/2) * accel * pow(t, 2)])
        brush.pd()
        brush.begin_fill()
        brush.circle(30)
        brush.end_fill()
        brush.pu()
        additionalFunction()
        brush.pu()
        screen.update()
        sleep(update)
        brush.clear()
        t += 1

if __name__ == "__main__":
    import turtle as t
    brush = t.Turtle()
    screen = t.Screen()
    screen.setup(1024, 600, 100, 100)
    screen.setworldcoordinates(0, 0, 1024, 600)
    screen.tracer(0, 0)
    brush.ht()
    brush.pu()
    f = time()
    lineWindmillTime(screen, brush, 3, "#000000", [512, 300], pi/4, 200, 100, 0, 0.01, update = 0.01)
    print(time() - f)
    #: utf-16 필요한데 utf-8로 열음
